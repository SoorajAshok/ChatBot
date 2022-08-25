from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot("Wall-E", storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')
trainer = ChatterBotCorpusTrainer(bot)
#trainer.train(conversation)
trainer.train("chatterbot.corpus.english")

#import os
#conversation = open('application/data/data.yml').read()
#trainer.train(conversation)
trainer.train('application/data/data.yml')


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get")
def getBotResponse():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
