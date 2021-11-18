
from webbot import Browser
import random
import time

web = Browser()

tab = 1
add = 1

print ("Made By Hamster")
print ("I'm not responsible for your actions")
print ("Instagram: @hamster.py")
print ("Thanks For Use")
web.go_to('https://kahoot.it')
code = input("Enter The Game Code: ")

while True:

  text_areas = web.find_elements(xpath='//input')
  web.type(web.Key.TAB,into=text_areas[0].text)
  web.type(code)
  web.type(web.Key.ENTER,into=text_areas[0].text)


  text_areas2 = web.find_elements(xpath='//input')
  web.type(web.Key.TAB,into=text_areas2[0].text)
  web.type(code)
  web.type(web.Key.ENTER,into=text_areas2[0].text)


  time.sleep(2)


  text_areas3 = web.find_elements(xpath='//input')
  web.type(web.Key.TAB,into=text_areas3[0].text)
  web.type(code)
  web.type(web.Key.ENTER,into=text_areas3[0].text)


  adj1 = ['nuked', 'SPAMMED', 'pig', 'meme', 'kids', 'pog', 'saucy', 'mommy', 'fortnite', 'earth', 'old','cosmic', 'neat', 'supa', 'rough', 'killer', 'spooky', 'retro', 'astro', 'baren', 'burned', 'chared', 'dead', 'daring', 'drunk', 'droopy', 'dank', 'angry', 'good', 'happy', 'hopeful', 'gentle', 'hairy', 'kind', 'limp', 'blind', 'lumpy', 'insane', 'meek', 'petty', 'rocky', 'sad', 'useless', 'sickly', 'zesty', 'burpy', 'thicc', 'sus']
  bot_username = random.choice(adj1) + "boi"

      
  text_areas4 = web.find_elements(xpath='//input')
  web.type(web.Key.TAB,into=text_areas4[0].text)
  web.type(bot_username)
  web.type(web.Key.ENTER,into=text_areas4[0].text)


  web.execute_script("window.open(' kahoot.it');")
  tab = tab + add
  web.switch_to_tab(tab)