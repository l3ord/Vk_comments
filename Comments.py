# -*- coding: utf-8 -*-
import os, sys, vk_api, colorama, time
from colorama import Fore, Back, Style
from time import sleep

colorama.init()

token = input('Введите токен от страницы вк: ') # получить токен можно здесь https://vkhost.github.io/
post_id = input('Введите айди поста: ') # https://vk.com/wall234202173_6 в данном случае айди будет 6
owner_id = input('Введите айди пользователя: ') # https://vk.com/wall234202173_6 в данном случае айди пользователя это 234202173
message = input('Введите текст комментария: ') 
caption = ' || By FL1NEE'
banner = """
			╔═══╗──────────────╔╗╔╗──╔╦╗
			║╔═╗║─────────────╔╝╚╣╚╗╔╝║║
			║║─╚╬══╦╗╔╦╗╔╦══╦═╬╗╔╩╗║║╔╣║╔╗
			║║─╔╣╔╗║╚╝║╚╝║║═╣╔╗╣║─║╚╝║║╚╝╝
			║╚═╝║╚╝║║║║║║║║═╣║║║╚╗╚╗╔╝║╔╗╗
			╚═══╩══╩╩╩╩╩╩╩══╩╝╚╩═╝─╚╝─╚╝╚╝"""
info = ('                         Software creating by FL1NE\n                         Supported by Dimf-174_YT')
caps = ('              			 TG-@FL1NEE\n              			 YT-FL1NE\n              			 VK-@fl1nee')

print(Fore.GREEN + info)
print(Fore.YELLOW + banner)
print(Fore.MAGENTA + caps)

a = input('1-Быстрая накрутка\n2-Медленная накрутка\n: ')# При медленной накрутке шанс появлении каптчи меньше

def main():
	count = 0
	vk_session = vk_api.VkApi(token=token)
	vk = vk_session.get_api()
	os.system('cls||clear')
	print(Fore.GREEN + info)
	print(Fore.YELLOW + banner)
	print(Fore.MAGENTA + caps)
	while True:
		try:
			vk.wall.createComment(owner_id=owner_id, post_id=post_id, message=message + caption) 
			vk.wall.createComment(owner_id=owner_id, post_id=post_id, message=message + caption) 
			count += 2
			time.sleep(2)
			print(Fore.GREEN + 'Накручено комментариев: ' + str(count), end='\r')
		except Exception as er:
			print(Fore.RED + 'Возникла ошибка: ', er)
			time.sleep(5) 
def min():
	count = 0
	vk_session = vk_api.VkApi(token=token)
	vk = vk_session.get_api()
	os.system('cls||clear')
	print(Fore.GREEN + info)
	print(Fore.YELLOW + banner)
	print(Fore.MAGENTA + caps)
	while True:
		try:
			vk.wall.createComment(owner_id=owner_id, post_id=post_id, message=message)
			count += 1
			time.sleep(2)
			print(Fore.GREEN + 'Накручено комментариев: ' + str(count), end='\r')
		except Exception as er:
			print(Fore.RED + 'Возникла ошибка: ', er)
			time.sleep(5)
if a == '1':
    main() 
if a == '2':
    min() 
else:
    print('Возникла ошибка: неправильно введëное значение') 
