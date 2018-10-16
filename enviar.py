#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import requests
import random
import telebot
from telebot import types
import os
from config import *
import filetype
import urllib
from future.utils import iteritems

nuevos = 'log'+CANAL.replace('@','')+'.txt'   
try:
    with open(nuevos, 'r') as f:
        old = f.read().split('\n')
except:
    old = []



new = {}
nov = []
fich = []
ides = []
asigs = {}
subcat = {}
bot = telebot.TeleBot(BOT_APIKEY)
os.chdir(CARPETA)

def envia(kind, n):
    name = n.split('/')
    nombre = name[-1]
    cat = n[2:].replace('/',' ')
    abcd = kind.mime.split("/")
    if kind is not None:
        
        if abcd[0] == "video":
            s = bot.send_video(CANAL,open(n,'rb'))
            ides.append(s.message_id)
            if nombre not in old and old: new[cat]=s.message_id
        elif abcd[0] == "audio":
            s = bot.send_audio(CANAL,open(n,'rb'))
            ides.append(s.message_id)
            if nombre not in old and old: new[cat]=s.message_id
        elif abcd[0] == "image":
            s = bot.send_photo(CANAL,open(n,'rb'))
            ides.append(s.message_id)
            if nombre not in old and old: new[cat]=s.message_id
        else:
            s = bot.send_document(CANAL,open(n,'rb'))
            ides.append(s.message_id)
            if nombre not in old and old: new[cat]=s.message_id
    else:
            s = bot.send_document(CANAL,open(n,'rb'))
            ides.append(s.message_id)
            if n not in old and old: new[cat] = s.message_id


for root, dirs, files in os.walk("./"):
    
    for dir in dirs:
        
        for root1,dirs1,files1 in os.walk(dir):
        
            if len(files1) is not 0 or len(dirs1) is not 0:
               
                s = bot.send_message(CANAL,(root1.replace("\\"," ")))
                ides.append(s.message_id)
                
                if '\\' not in root1:  
                    asigs[root1.replace("\\"," ")]= s.message_id
                else:
                    subcat[''.join(root1.split('\\'))] = s.message_id
            for f3 in files1: 
                root1 = '/'.join(root1.split('\\'))
                a =("./"+ root1+"/"+f3)
                kind = filetype.guess(a)
                fich.append(f3)
                envia(kind, a)
                
    if root == './' and len(files) is not 0 :
        s = bot.send_message(CANAL,"Archivos sueltos")
        ides.append(s.message_id)
        asigs["Archivos sueltos"]= s.message_id
        for n in files:
            kind = filetype.guess(root+n)
            fich.append(n)
            envia(kind,root+n)
            
a=[]


markup = types.InlineKeyboardMarkup()
for key,value in iteritems(asigs):
    markup.row(types.InlineKeyboardButton(str(key) ,url=LINK_CANAL+"/"+str(value)))
    b = []
    for n in subcat.keys():
        if key in n:
            b.append(types.InlineKeyboardButton(str(n.replace(key,'')) ,url=LINK_CANAL+"/"+str(subcat[n])))
    if len(b)>0:
        markup.row(*b)
a = bot.send_message(CANAL,"MENU", reply_markup=markup,parse_mode='Markdown')
ides.append(a.message_id)

if new:
    mensaje = '*Nuevos archivos*\n\n'

    for archivo, mid in iteritems(new):
        mensaje += u"[{}]({}/{})".format(archivo,LINK_CANAL,mid)+"\n"
        
        
    bot.send_message(CANAL,mensaje,parse_mode='Markdown',disable_web_page_preview=True)


os.chdir('..')
a = 'ides'+CANAL.replace('@','')+'.txt'
with open(a, 'w') as f:
    for item in ides:
        f.write("%s\n" % item)

with open(nuevos, 'w') as f:
    for item in fich:
        f.write("%s\n" % item)
