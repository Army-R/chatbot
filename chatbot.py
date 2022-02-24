#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 18:40:29 2022

@author: Army-R
"""
from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# ChatBot name
chatbot = ChatBot("Pal")

conversation = open("chatbot_training.txt", "r").readlines()

trainer = ListTrainer(chatbot)
#trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(conversation)
#trainer.train("chatterbot.corpus.spanish")

# Flujo de comunicacion
while True:
    try:
       request = input('Me: ')
       aswr = chatbot.get_response(request)
       print("Andrea", aswr)

    except(KeyboardInterrupt, EOFError, SystemExit):
       break
