from flask import Flask, request
from app_gpio import *
import time

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'
STATUS = ''
CYCLE_SECONDS = 3
stoplight = StopLight()

app = Flask(__name__)

def setLight(color):
  # hook into GPIO here
  global STATUS
  STATUS = color
  stoplight.enable_light(color)
  return color

@app.route('/stoplight/cycle')
def enableCycle():
  setLight(RED)
  time.sleep(CYCLE_SECONDS)
  setLight(YELLOW)
  time.sleep(CYCLE_SECONDS)
  setLight(GREEN)
  time.sleep(CYCLE_SECONDS)
  return enableCycle()

@app.route('/stoplight/red')
def enableRed():
  return setLight(RED)

@app.route('/stoplight/yellow')
def enableYellow():
  return setLight(YELLOW)

@app.route('/stoplight/green')
def enableGreen():
  return setLight(GREEN)

@app.route('/stoplight/status')
def status():
  global STATUS
  return STATUS

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
