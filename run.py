import os

from flask import Flask, redirect

app = Flask(__name__)
messages = []


def add_message(username, message):
    """ Add messages to messages list"""
    messages.append("{} : {}".format(username, message))


def get_all_messages():
    """ Get all messages and separate using br"""
    return "<br>".join(messages)


@app.route("/")
def index():
    """Main Page with instructions"""
    return "To send a message use /USERNAME/MESSAGE"


@app.route("/<username>")
def user(username):
    """ Display chat messages """
    return "<h1>Welcome {0} </h1>  {1}".format(username, get_all_messages())


@app.route("/<username>/<message>")
def send_message(username, message):
    """ Create a new message and redirect to chat page """
    add_message(username, message)
    return redirect("/" + username)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)