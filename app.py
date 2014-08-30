import os

from mandrill import Mandrill
from flask import Flask, request, redirect, abort

app = Flask(__name__)
mandrill_client = Mandrill(os.environ['MANDRILL_API_KEY'])


@app.route('/')
def index():
    return redirect(os.environ['USER_SITE'])


@app.route('/send', methods=['POST'])
def forward():
    message = {
               'to': [{'email': os.environ['USER_EMAIL']}],
               'from_email': request.form['email'],
               'subject': 'Message from {}, Subject:{}'.format(request.form['name'], request.form['subject']),
               'text': request.form['message'],
              }
    result = mandrill_client.messages.send(message=message)
    if result[0]['status'] != 'sent':
        abort(500)
    return redirect(os.environ['SUCCESS_PAGE'])


@app.errorhandler(500)
def error(e):
    return ('Sorry, something went wrong! %s - %s' % (e.__class__, e), 500)

