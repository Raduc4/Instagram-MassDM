from numpy import rint
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import json

bot_username = 'starkebeb111'
bot_password = 'qsef2468'

profiles = []

for user in json.load(open('./result.json')):
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
		for user in users:
			print(user)
			if user['isPrivate'] == True:
				continue
			browser.get('https://instagram.com/' + user['username'])
			followButton_text = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div')
			followers_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
			if followButton_text.text == 'Follow': 
				followers_button.click()
				time.sleep(random.randrange(3, 4))
				message_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/header/section/div[1]/div[1]/div/div[1]/button')
				time.sleep(random.randrange(3, 4))
				message_button.click()
				time.sleep(random.randrange(3, 4))
				if counter == 0:
					browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
					counter = 1
				text_area = browser.find_element_by_tag_name('textarea')
				text_area.send_keys(f"""Hello""")
				time.sleep(random.randrange(3, 4))
				browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
				continue
			else:
				print('No followers')
				continue





bot = Instagram(bot_username, bot_password)
bot.login()
bot.send_message(profiles, amount)
