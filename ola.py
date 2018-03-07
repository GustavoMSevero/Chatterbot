# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Jarvis_dialog')

dialogIntro = ['Ola', 'Ola', 'Quem e voce?', 'Sou Jarvis chatbot criado pelo Sr. Gustavo']
di = str(dialogIntro)

bot.set_trainer(ListTrainer)
bot.train(dialogIntro)

while True:
    question = input('You: ')
    answer = bot.get_response(question)
    print('Jarvis: ', answer)
