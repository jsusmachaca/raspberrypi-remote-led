from flask import Flask, render_template, jsonify
from gpiod import Chip, LINE_REQ_DIR_OUT


app = Flask(__name__)

chip = Chip("gpiochip4")
line = chip.get_line(17)
line.request(consumer="app", type=LINE_REQ_DIR_OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led-on', methods=['POST'])
def led_on():
    line.set_value(1)
    return jsonify({'message': 'led is on'})

@app.route('/led-off', methods=['POST'])
def led_off():
    line.set_value(0)
    return jsonify({'message': 'led is off'})
