from flask import Flask
from flask import request
from flask_mailman import Mail
from flask_mailman import Message

import sys

app = Flask(__name__)
app.config['MAIL_BACKEND'] = 'console'
mail = Mail(app)

@app.route('/form-handle', methods=['POST'])
def hello_world():
    body = ''
    for key, val in request.form.items():
        body += '{0}: {1}\n'.format(key, val)

    msg = Message("Hello",
                  sender="from@example.com",
                  recipients=["tom@toms-projekte.de"],
                  body=body)

    mail.send(msg)
    return "Mail sent!"
