from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot("Wall-E", storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='postgres://nfoholeyagpbvf:b3401f36c9deefc98176b786196e6148e310de4ffa53c59138ba20e616196e8c@ec2-44-206-89-185.compute-1.amazonaws.com:5432/dfgso923ne7qc3')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


trainer.train('application/data/data.yml')


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get")
def getBotResponse():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))
