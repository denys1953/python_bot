from bs4 import BeautifulSoup
import requests
import time
import telebot

bot = telebot.TeleBot('1224839753:AAGNY5vzELd-Ibp4-pED4S8Lm85eKaM4L1A')
URL = 'https://index.minfin.com.ua/reference/coronavirus/ukraine/'
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
def coronavirus_uk_all():
   full_page_all = requests.get(URL, head)
   soup_all = BeautifulSoup(full_page_all.content, 'html.parser')
   convert_all = soup_all.findAll("strong", {"class": "black"})
   return convert_all[0].text  
def coronavirus_uk_death():
   full_page_death = requests.get(URL, head)
   soup_death = BeautifulSoup(full_page_death.content, 'html.parser')
   convert_death = soup_death.findAll("strong", {"class": "red"})
   return convert_death[0].text
def coronavirus_uk_health():
   full_page_health = requests.get(URL, head)
   soup_health = BeautifulSoup(full_page_health.content, 'html.parser')
   convert_health = soup_health.findAll("strong", {"class": "green"})
   return convert_health[0].text 
@bot.message_handler(commands=['start'])
def start_message(message):
   keyboard = telebot.types.ReplyKeyboardMarkup(True)
   keyboard.row('coronavirus 🇺🇦')
   bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def echo_msg(message):
   if message.text == 'coronavirus 🇺🇦':
      bot.send_message(message.chat.id, "🇺🇦 Всього захворівших в Україні: " + coronavirus_uk_all())
      bot.send_message(message.chat.id, "🇺🇦 Померло: " + coronavirus_uk_death())
      bot.send_message(message.chat.id, "🇺🇦 Виздоровіли: " + coronavirus_uk_health())
if __name__ == '__main__':
   bot.polling(none_stop=True)