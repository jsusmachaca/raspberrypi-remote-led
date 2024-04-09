from flask import Flask, render_template, jsonify
from rpi.raspberry import Raspberry

app = Flask(__name__)

raspberry = Raspberry(7)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led-on', methods=['POST'])
def led_on():
    raspberry.on()
    return jsonify({'message': 'led is on'})

def coco():
    print('loco')

@app.route('/led-off', methods=['POST'])
def led_off():
    raspberry.off()
    return jsonify({'message': 'led is off'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')