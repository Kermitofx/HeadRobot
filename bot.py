#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("956323132:AAEH1-KFy6IHd7b9oE0ukmMzwtMtcVxIS1I")

##
def gen_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('💞 | Channel Official',
                                          url='https://telegram.me/HeadChannelBr'))
    return markup


@bot.message_handler(commands=['start'])
def canal_command(me):
    bot.reply_to(m,
                    '👨‍💻 | Este Bot Foi Criado com o objetivo de ajuda a melhorar a moderação do grupo\n\n😋 ME Adiciona no seu grupo como adm e deixa eu faze meu trabalho hehe',
                    reply_markup=gen_markup())
                    
                    #####
@bot.message_handler(commands=["ban"])
def ban_user(m):
	if not bot.get_chat_member(chat_id=m.chat.id, user_id=m.from_user.id).status == "member":
		bot.send_message(m.chat.id, "Nao Posso bani um administrador.")
	else: 
			if m.reply_to_message: 
				get = bot.get_chat(m.reply_to_message.from_user.id) 
				user_name = get.first_name
				user_id = get.id
				bot.ban_chat_member(chat_id=m.chat.id, user_id=user_id)
				bot.send_message(m.chat.id, "Usuario Banido✅")

   ######Unban####
@bot.message_handler(commands=["unban"])
def unban_user(m):
    if m.reply_to_message:
        get = bot.get_chat(m.reply_to_message.from_user.id)
        user_name = get.first_name
        user_id = get.id
        bot.unkick_chat_member(chat_id=m.chat.id, user_id=user_id)
        bot.send_message(m.chat.id,"Usuário Desbani Do Grupo!!")
