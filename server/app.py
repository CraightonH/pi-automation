from flask import Flask, request
#from functions import *

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'
OFF = 'off'
ON = 'on'
STATUS = ''

app = Flask(__name__)

def setLight(color, state):
  global STATUS
  STATUS = color
  return (color, state)

@app.route('/stoplight/red')
def enableRed():
  return setLight(RED, ON)

@app.route('/stoplight/yellow')
def enableYellow():
  return setLight(YELLOW, ON)

@app.route('/stoplight/green')
def enableGreen():
  return setLight(GREEN, ON)

@app.route('/stoplight/status')
def status():
  global STATUS
  return STATUS

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
