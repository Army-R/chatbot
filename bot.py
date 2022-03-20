from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

# ChatBot name
bot = ChatBot("Pal")

conversation = open("chatbot_training.txt", "r").readlines()

trainer = ListTrainer(bot)
#trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(conversation)
#trainer.train("chatterbot.corpus.spanish")

# Flujo de comunicacion
while True:
    try:
       request = input('Me: ')
       aswr = bot.get_response(request)
       print("Andrea", aswr)

    except(KeyboardInterrupt, EOFError, SystemExit):
       break
