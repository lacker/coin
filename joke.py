#!/usr/bin/env python3
import os

from flask import Flask, request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)


total = 0

@app.route('/joke')
@payment.required(1)
def tell_joke():
  total += 1
  sness = ''
  if total > 1:
    sness = 's'
  joke = ('Why did the programmer code a whole road? To earn %d satoshi%s.'
          % (total, sness))
  return joke

  
# set up and run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
