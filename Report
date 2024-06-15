import requests,random,re,time

######L7N#####
R = '\033[1;31;40m'
X = '\033[1;33;40m' 
F = '\033[1;32;40m' 
C = "\033[1;97;40m" 
B = '\033[1;36;40m'
C1 = '\033[1;35;40m'
######L7N#####

link_message = input(f"{C}• {B}Link {C1}♪{B} Message : {C}")
print('\r')
link_channel = input(f"{C}• {B}Link {C1}♪{B} Channel : {C}")
def Email():
	rand = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	email = str(''.join(random.choice(rand) for i in range(int(random.randint(6,9)))))+random.choice(["@gmail.com","@hotmail.com","@yahoo.com","@live.com"])
	return email

def Phone():
	rand = ["1","2","3","4","5","6","7","8","9","0"]
	rand_num = str(''.join(random.choice(rand) for i in range(int((10)))))
	phone_1 = "+1"+rand_num
	phone_2 = "+7"+rand_num
	phone_3 = "+44"+rand_num
	phonse = phone_1,phone_2,phone_3
	phone = random.choice(phonse)
	return phone

def Country():	 
	Countries = "English","Español","Français","Italiano","Українська"
	country = random.choice(Countries)
	return country

def report():
	while True:
		cookies = {
    'stel_ssid': 'cb79591986f65f4f2c_5194073663299526481',
}
		headers = {
    'authority': 'telegram.org',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-IQ,ar;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'stel_ssid=cb79591986f65f4f2c_5194073663299526481',
    'origin': 'https://telegram.org',
    'referer': 'https://telegram.org/support',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

		data = {
    'message': '''
Hello, I am a user of the Telegram platform, but there is a problem There is a channel that publishes Pornography !
This Message {} 
And This is the channel link {} 
I hope to deal with the report so that I can have a good experience without revealing this nonsense 
    '''.format(link_message,link_channel),
    'email': '{}'.format(Email()),
    'phone': '{}'.format(Phone()),
    'setln': '{}'.format(Country()),
}
		response = requests.post('https://telegram.org/support', cookies=cookies, headers=headers, data=data).text
		res_get = re.compile(r'<div class="alert alert-success"><b>(.*?)</b><br/>(.*?)</div>', re.DOTALL)
		match = res_get.search(response)
		if match:
		  responses = match.group(1) + " " + match.group(2)
		  if "شكرًا على بلاغك&#33; سنحاول الرّد بأسرع ما يمكن." in responses :
		  	print(F+"Done Send Report")
		  else:
		  	print(R+"Erorr Send Report")
		else:
			print(X+"There is an error in the information ")
		time.sleep(1)

#BY ~ L7N
report()				
