from flask import Flask, render_template, jsonify
from gpiozero import LED


app = Flask(__name__)
led = LED(4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led-on', methods=['POST'])
def led_on():
    led.on()
    return jsonify({'message': 'led is on'})

@app.route('/led-off', methods=['POST'])
def led_off():
    led.off()
    return jsonify({'message': 'led is off'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')