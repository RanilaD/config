#!/usr/bin/python

import vk
#print("PLACEHOLDER")

enabled = False

if enabled:
	try: 
		session = vk.AuthSession('6434888', 'sersh008@mail.ru', 'wesarqq', scope='messages')
		vk_api = vk.API(session)

		messages = vk_api.messages.getDialogs(count=20, unread=1)

		if messages['count'] > 0:
			print('\uf0e0')
		else:
			print('\uf2b6')
	except Exception as ex:
		print('\uf2b6')
else:
	print("DISABLED")
