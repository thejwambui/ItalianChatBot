from flask import Flask, render_template, request
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

italian_bot = ChatBot("chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

italian_bot.set_trainer(ChatterBotCorpusTrainer)

italian_bot.train("chatterbot.corpus.italian")

@app.route('/')
def home():
	return render_template("index.html")

@app.route("/get")
def get_bot_response():
	userText = request.args.get('msg')
	return str(italian_bot.get_response(userText))


if __name__ == "__main__":
	app.run(debug=True)
