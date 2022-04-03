from numpy import rint
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import json

bot_username = 'new_acc_fortest'
bot_password = 'qsef2468'

profiles = []

for user in json.load(open('./Result.json')):
		profiles.append({'username': user['username'], 'isPrivate': user['isPrivate']})
amount = 300

print(len(profiles))

# 'usernames' or 'links'
result = 'usernames'

us = ''


class Instagram():
	def __init__(self, username, password):
		self.username = username
		self.password = password
		options = Options()
		options.add_experimental_option("excludeSwitches", ["enable-logging"])
		self.browser = web.Chrome("chromedriver",options=options)
		self.browser.set_window_size(900, 900)

	def close_browser(self):
		self.browser.close()
		self.browser.quit()

	def login(self):
		browser = self.browser
		try:
			browser.get('https://www.instagram.com')
			time.sleep(random.randrange(3, 5))
			# Enter username:
			username_input = browser.find_element_by_name('username')
			username_input.clear()
			username_input.send_keys(self.username)
			time.sleep(random.randrange(2, 4))
			# Enter password:
			password_input = browser.find_element_by_name('password')
			password_input.clear()
			password_input.send_keys(self.password)
			time.sleep(random.randrange(1, 3))
			password_input.send_keys(Keys.ENTER)
			time.sleep(random.randrange(3, 5))
			print(f'[{self.username}] Successfully logged on!')
		except Exception as ex:
			print(f'[{self.username}] Authorization fail')
			self.close_browser()

	def xpath_exists(self, url):
		browser = self.browser
		try:
			browser.find_element_by_xpath(url)
			exist = True
		except NoSuchElementException:
			exist = False
		return exist

	def send_message(self, users, amount):
		counter = 0
		browser = self.browser
		browser.get('https://www.instagram.com/direct/inbox/')
		for user in users:
			# write_message_btn = browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
			if counter == 0:
				browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
				counter = 1
			time.sleep(random.randrange(1, 3))
			write_message_btn = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button')
			write_message_btn.click()
			time.sleep(random.randrange(1, 3))
			find_user_text_area = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input")
			find_user_text_area.send_keys(user['username'])
			time.sleep(random.randrange(1, 3))
			select_user_btn = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div")
			# /div/div[3]/button
			select_user_btn.click()
			time.sleep(random.randrange(3, 6))
			next_btn = browser.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div[3]/div/button")
			next_btn.click()
			time.sleep(random.randrange(3, 6))
			text_area = browser.find_element_by_tag_name('textarea')
			text_area.send_keys(f"""Proiect NFT Românesc!
Salut și scuze pentru mesaj privat, dar am un mic info poate te interesează: 
se face un joc pe blockchain inspirat din istoria și mitologia româneasca cu Ștefan cel Mare ca erou dar și Baba Dochia și Statu-Palmă-Barbă-Cot și mulți alții.

Acesta e username-ul și pe Twitter și pe IG și pe TikTok: @PuzzlesCrusade

Cel mai activ se promovează pe Twitter. Nu-ți dau link să nu crezi că e scam. 
Vezi despre ce e vorba și poate dai un follow, proiectul are potențial!!""")
			time.sleep(random.randrange(3, 4))
			browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()



bot = Instagram(bot_username, bot_password)
bot.login()
bot.send_message(profiles, amount)
