import telebot
from telebot import types
from cryptography.fernet import Fernet
import os
import shutil
from setuptools import setup
from Cython.Build import cythonize

API_TOKEN = '7193240931:AAHiuPDv_kmUmFGN3u68SYa5CDf6PEHuKk0' 
ADMIN_ID = 5099564264 

bot = telebot.TeleBot(API_TOKEN)

is_bot_locked = False
send_new_user_notifications = True
banned_users = set()
required_channels = []

key = Fernet.generate_key()
cipher = Fernet(key)

with open('key.key', 'wb') as key_file:
    key_file.write(key)

with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipher = Fernet(key)

def save_settings():
    with open('settings.txt', 'w') as settings_file:
        settings_file.write(f'{is_bot_locked}\n')
        settings_file.write(f'{send_new_user_notifications}\n')
        settings_file.write('\n'.join(required_channels) + '\n')

def load_settings():
    global is_bot_locked, send_new_user_notifications, required_channels
    if os.path.exists('settings.txt'):
        with open('settings.txt', 'r') as settings_file:
            lines = settings_file.readlines()
            is_bot_locked = lines[0].strip() == 'True'
            send_new_user_notifications = lines[1].strip() == 'True'
            required_channels = [line.strip() for line in lines[2:] if line.strip()]

load_settings()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if is_bot_locked and message.from_user.id not in banned_users:
        bot.send_message(message.chat.id, "تم تعطيل البوت من قبل مطور البوت.")
        return

    for channel in required_channels:
        member = bot.get_chat_member(channel, message.from_user.id)
        if member.status not in ['member', 'administrator', 'creator']:
            bot.send_message(message.chat.id, f"عذراً ⚠️\n- لا يمكنك استخدام البوت الا بعد الاشتراك في قناة البوت \n اشترك ثم ارسل /start \n• القناة : {channel}")
            return

    markup = types.InlineKeyboardMarkup()
    button_encrypt = types.InlineKeyboardButton("تشفير ملف", callback_data="encrypt_file")
    button_decrypt = types.InlineKeyboardButton("فك تشفير ملف Cython", callback_data="decrypt_file")
    markup.add(button_encrypt, button_decrypt)
    bot.send_message(message.chat.id, "مرحبًا! اختر عملية:", reply_markup=markup)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if message.from_user.id != ADMIN_ID:
        return

    markup = types.InlineKeyboardMarkup()
    button_lock = types.InlineKeyboardButton("قفل البوت", callback_data="lock_bot")
    button_unlock = types.InlineKeyboardButton("فتح البوت", callback_data="unlock_bot")
    button_ban = types.InlineKeyboardButton("حظر مستخدم", callback_data="ban_user")
    button_unban = types.InlineKeyboardButton("فك حظر مستخدم", callback_data="unban_user")
    button_stats = types.InlineKeyboardButton("إحصائيات المستخدمين", callback_data="user_stats")
    button_toggle_notifications = types.InlineKeyboardButton(
        "تفعيل/تعطيل إشعارات المستخدمين الجدد", callback_data="toggle_notifications")
    button_add_channel = types.InlineKeyboardButton("إضافة قناة اشتراك", callback_data="add_channel")
    button_remove_channel = types.InlineKeyboardButton("حذف قناة اشتراك", callback_data="remove_channel")
    button_list_channels = types.InlineKeyboardButton("عرض قنوات الاشتراك", callback_data="list_channels")
    
    markup.add(button_lock, button_unlock)
    markup.add(button_ban, button_unban)
    markup.add(button_stats)
    markup.add(button_toggle_notifications)
    markup.add(button_add_channel, button_remove_channel)
    markup.add(button_list_channels)

    bot.send_message(message.chat.id, "مرحباً بك عزيزي المطور في لوحة التحكم 🚀", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "encrypt_file")
def ask_for_file(call):
    msg = bot.send_message(call.message.chat.id, "أرسل الملف الذي تريد تشفيره 🈹")
    bot.register_next_step_handler(msg, handle_encrypt_file)

@bot.callback_query_handler(func=lambda call: call.data == "decrypt_file")
def ask_for_cython_file(call):
    msg = bot.send_message(call.message.chat.id, "أرسل الملف الذي تريد فك تشفيره 🔡")
    bot.register_next_step_handler(msg, handle_decrypt_file)

@bot.callback_query_handler(func=lambda call: call.data == "lock_bot")
def lock_bot(call):
    global is_bot_locked
    is_bot_locked = True
    save_settings()
    bot.send_message(call.message.chat.id, "تم قفل البوت.")

@bot.callback_query_handler(func=lambda call: call.data == "unlock_bot")
def unlock_bot(call):
    global is_bot_locked
    is_bot_locked = False
    save_settings()
    bot.send_message(call.message.chat.id, "تم فتح البوت.")

@bot.callback_query_handler(func=lambda call: call.data == "ban_user")
def ask_for_ban_user(call):
    msg = bot.send_message(call.message.chat.id, "أرسل ايدي المستخدم الذي تريد حظره:")
    bot.register_next_step_handler(msg, handle_ban_user)

@bot.callback_query_handler(func=lambda call: call.data == "unban_user")
def ask_for_unban_user(call):
    msg = bot.send_message(call.message.chat.id, "أرسل ايدي المستخدم الذي تريد فك حظره:")
    bot.register_next_step_handler(msg, handle_unban_user)

@bot.callback_query_handler(func=lambda call: call.data == "user_stats")
def user_stats(call):
    users_count = len(bot.get_updates())
    bot.send_message(call.message.chat.id, f"• اجمالي المستخدمين: {users_count}")

@bot.callback_query_handler(func=lambda call: call.data == "toggle_notifications")
def toggle_notifications(call):
    global send_new_user_notifications
    send_new_user_notifications = not send_new_user_notifications
    save_settings()
    status = "مفعلة" if send_new_user_notifications else "معطلة"
    bot.send_message(call.message.chat.id, f"إشعارات المستخدمين الجدد {status}.")

@bot.callback_query_handler(func=lambda call: call.data == "add_channel")
def ask_for_add_channel(call):
    if len(required_channels) >= 5:
        bot.send_message(call.message.chat.id, "يمكنك إضافة 5 قنوات كحد أقصى.")
    else:
        msg = bot.send_message(call.message.chat.id, "أرسل رابط القناة التي تريد إضافتها 🔗")
        bot.register_next_step_handler(msg, handle_add_channel)

@bot.callback_query_handler(func=lambda call: call.data == "remove_channel")
def ask_for_remove_channel(call):
    if not required_channels:
        bot.send_message(call.message.chat.id, "لا توجد قنوات في القائمة.")
    else:
        msg = bot.send_message(call.message.chat.id, "أرسل رابط القناة التي تريد حذفها 🔗")
        bot.register_next_step_handler(msg, handle_remove_channel)

@bot.callback_query_handler(func=lambda call: call.data == "list_channels")
def list_channels(call):
    if not required_channels:
        bot.send_message(call.message.chat.id, "لا توجد قنوات في القائمة.")
    else:
        channels_list = "\n".join(required_channels)
        bot.send_message(call.message.chat.id, f"قنوات الاشتراك:\n• {channels_list}")

def handle_ban_user(message):
    try:
        user_id = int(message.text)
        banned_users.add(user_id)
        bot.send_message(message.chat.id, f"تم حظر المستخدم {user_id}.")
    except ValueError:
        bot.send_message(message.chat.id, "الرجاء إرسال ايدي مستخدم صحيح.")

def handle_unban_user(message):
    try:
        user_id = int(message.text)
        banned_users.discard(user_id)
        bot.send_message(message.chat.id, f"تم فك حظر المستخدم {user_id}.")
    except ValueError:
        bot.send_message(message.chat.id, "الرجاء إرسال ايدي مستخدم صحيح.")

def handle_add_channel(message):
    channel_link = message.text.strip()
    if channel_link not in required_channels:
        required_channels.append(channel_link)
        save_settings()
        bot.send_message(message.chat.id, f"تم إضافة القناة {channel_link}.")
    else:
        bot.send_message(message.chat.id, "القناة موجودة بالفعل في القائمة.")

def handle_remove_channel(message):
    channel_link = message.text.strip()
    if channel_link in required_channels:
        required_channels.remove(channel_link)
        save_settings()
        bot.send_message(message.chat.id, f"تم حذف القناة {channel_link}.")
    else:
        bot.send_message(message.chat.id, "القناة غير موجودة في القائمة.")

def handle_encrypt_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open(message.document.file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        with open(message.document.file_name, 'rb') as file:
            file_data = file.read()
        
        encrypted_data = cipher.encrypt(file_data)
        
        encrypted_file_name = 'encrypted_' + message.document.file_name
        with open(encrypted_file_name, 'wb') as file:
            file.write(encrypted_data)
        
        with open(encrypted_file_name, 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(message.document.file_name)
        os.remove(encrypted_file_name)
    else:
        bot.send_message(message.chat.id, "لم يتم إرسال ملف. يرجى المحاولة مرة أخرى.")

def handle_decrypt_file(message):
    if message.document:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        
        with open(message.document.file_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        
        with open(message.document.file_name, 'rb') as file:
            encrypted_data = file.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        
        decrypted_file_name = 'decrypted_' + message.document.file_name
        with open(decrypted_file_name, 'wb') as file:
            file.write(decrypted_data)
        
        setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("{decrypted_file_name}")
)
"""
        with open('setup.py', 'w') as setup_file:
            setup_file.write(setup_code)
        
        os.system('python setup.py build_ext --inplace')
        
        cython_output = decrypted_file_name.replace('.pyx', '.so') if '.pyx' in decrypted_file_name else decrypted_file_name.replace('.pyx', '.pyd')
        with open(cython_output, 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        os.remove(message.document.file_name)
        os.remove(decrypted_file_name)
        shutil.rmtree('build')
        os.remove('setup.py')
        os.remove(cython_output)
    else:
        bot.send_message(message.chat.id, "لم يتم إرسال ملف. يرجى المحاولة مرة أخرى.")

bot.polling()