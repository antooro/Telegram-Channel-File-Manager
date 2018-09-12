import requests
import random
import telebot
from telebot import types
import os
from config import *
import filetype

ides = []
asigs = {}

bot = telebot.TeleBot(BOT_APIKEY)
os.chdir(CARPETA)

for root, dirs, files in os.walk("./"):  
    for dir in dirs:
        if root == './' and files is not None:
            s = bot.send_message(CANAL,"Archivos sueltos")
            ides.append(s.message_id)
            asigs["Archivos sueltos"]= s.message_id
            for n in files:
                kind = filetype.guess(root+n)
                if kind is not None:
                    abcd = kind.mime.split("/")
                    print abcd[0]
                    if abcd[0] == "video":
                        s = bot.send_video(CANAL,open(n,'rb'))
                        ides.append(s.message_id)
                    elif abcd[0] == "audio":
                        s = bot.send_audio(CANAL,open(n,'rb'))
                        ides.append(s.message_id)
                    elif abcd[0] == "image":
                        s = bot.send_photo(CANAL,open(n,'rb'))
                        ides.append(s.message_id)
                    else:
                        s = bot.send_document(CANAL,open(n,'rb'))
                        ides.append(s.message_id)
                else:
                        s = bot.send_document(CANAL,open(n,'rb'))
                        ides.append(s.message_id)
                
        for root1,dirs1,files1 in os.walk(dir):
            s = bot.send_message(CANAL,root1)
            ides.append(s.message_id)
            asigs[root1]= s.message_id
            for f3 in files1: 
                root1 = '/'.join(root1.split('\\'))
                a =("./"+ root1+"/"+f3)
                kind = filetype.guess(a)
                if kind is not None:
                    abcd = kind.mime.split("/")
                    if abcd[0] == "video":
                        s = bot.send_video(CANAL,open(a,'rb'))
                        ides.append(s.message_id)
                    elif abcd[0] == "audio":
                        s = bot.send_audio(CANAL,open(a,'rb'))
                        ides.append(s.message_id)
                    elif abcd[0] == "image":
                        s = bot.send_photo(CANAL,open(a,'rb'))
                        ides.append(s.message_id)
                    else:
                        s = bot.send_document(CANAL,open(a,'rb'))
                        ides.append(s.message_id)
                else:
                        s = bot.send_document(CANAL,open(a,'rb'))
                        ides.append(s.message_id)

a=[]
markup = types.InlineKeyboardMarkup()

for key,value in asigs.iteritems():
    a.append(types.InlineKeyboardButton(str(key) ,url=LINK_CANAL+"/"+str(value)))

markup.row(*a)
a = bot.send_message(CANAL," selecciona la asignatura", reply_markup=markup,parse_mode='Markdown')
ides.append(a.message_id)

os.chdir('..')
with open('ides.txt', 'w') as f:
    for item in ides:
        f.write("%s\n" % item)
