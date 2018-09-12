#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import random
import telebot
from telebot import types
from config import *


bot = telebot.TeleBot(BOT_APIKEY)
import os
with open('ides.txt', 'r') as f:
    myNames = f.readlines()
    
for n in myNames:
    bot.delete_message(CANAL,n)