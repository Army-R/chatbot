#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:40:29 2022

@author: Army-R
"""
# Creacion de un Chatbot[https://youtu.be/L2JomWubedE] 

# chatbot.storage.drop() limpia el historial del chatbot

# Importamos las librerias chattboter
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
# ChatterBotCorpusTrainer viene prediseñado

# ESte es el nombre de nuestro chatbot
chatbot = ChatBot("Mylo")

conversation = open("chatbot_wrdlst.txt", "r").readlines()

# Entrenamos al chatbot
triner = ListTrainer(chatbot) 

# Aquí se entrenan las respuestas del chatbot
# El chatterbot.corpuse.spanish, viene con respuestas en español
triner.train(conversation)

# Flujo de comunicacion
while True:
   request = input('Me: ') 
   aswr = chatbot.get_response("request")
   print("Mylo: ", aswr)
   
   
