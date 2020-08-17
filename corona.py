from bs4 import BeautifulSoup
import requests
import time
import telebot
bot = telebot.TeleBot('1224839753:AAGNY5vzELd-Ibp4-pED4S8Lm85eKaM4L1A')
# TOKEN = '1224839753:AAGNY5vzELd-Ibp4-pED4S8Lm85eKaM4L1A'

def coronavirus_uk():
   URL = 'https://index.minfin.com.ua/reference/coronavirus/ukraine/'
   head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}

   full_page = requests.get(URL, head)
   soup = BeautifulSoup(full_page.content, 'html.parser')
   convert = soup.findAll("strong", {"class": "black"})
   return convert[0].text  
@bot.message_handler(commands=['start'])
def start_message(message):
   keyboard = telebot.types.ReplyKeyboardMarkup(True)
   keyboard.row('coronavirus 🇺🇦')
   bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def echo_msg(message):
   if message.text == 'coronavirus 🇺🇦':
      bot.send_message(message.chat.id, "🇺🇦 Всього захворівших в Україні: " + coronavirus_uk())
if __name__ == '__main__':
   bot.polling(none_stop=True)

