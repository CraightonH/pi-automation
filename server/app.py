from flask import Flask, request
from app_gpio import *
import time, threading

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'
STATUS = ''
CYCLE_SECONDS = 3
CYCLE = False
stoplight = StopLight()

app = Flask(__name__)

def setLight(color):
  # hook into GPIO here
  global STATUS
  STATUS = color
  stoplight.enable_light(color)
  return color

def cycle():
  global CYCLE
  CYCLE = True
  while CYCLE:
    if CYCLE: # short-circuit the loop
      setLight(RED)
      time.sleep(CYCLE_SECONDS)
    if CYCLE: # short-circuit the loop
      setLight(YELLOW)
      time.sleep(CYCLE_SECONDS)
    if CYCLE: # short-circuit the loop
      setLight(GREEN)
      time.sleep(CYCLE_SECONDS)

@app.route('/stoplight/cycle')
def enableCycle():
  threading.Thread(target=cycle, daemon=True).start()
  # while CYCLE:
  #   if CYCLE: # short-circuit the loop
  #     setLight(RED)
  #     time.sleep(CYCLE_SECONDS)
  #   if CYCLE: # short-circuit the loop
  #     setLight(YELLOW)
  #     time.sleep(CYCLE_SECONDS)
  #   if CYCLE: # short-circuit the loop
  #     setLight(GREEN)
  #     time.sleep(CYCLE_SECONDS)
  return ''

@app.route('/stoplight/red')
def enableRed():
  global CYCLE
  CYCLE = False
  return setLight(RED)

@app.route('/stoplight/yellow')
def enableYellow():
  global CYCLE
  CYCLE = False
  return setLight(YELLOW)

@app.route('/stoplight/green')
def enableGreen():
  global CYCLE
  CYCLE = False
  return setLight(GREEN)

@app.route('/stoplight/off')
def off():
  global CYCLE
  CYCLE = False
  stoplight.disable_all()
  return ''

@app.route('/stoplight/status')
def status():
  global STATUS
  return STATUS

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80, debug=True)
