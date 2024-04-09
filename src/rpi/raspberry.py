import RPi.GPIO as rpi



class Raspberry:
    def __init__(self, pin: int) -> None:
        self.pin = pin
        rpi.setmode(rpi.BOARD)
        rpi.setup(pin, rpi.OUT)

    def on(self) -> bool:
        try:
            rpi.output(self.pin, rpi.HIGH)
            print('led is on')
            return True
        except Exception as e:
            print(f'Error {e}')
            return False
            

    def off(self) -> bool:
        try:
            rpi.output(self.pin, rpi.LOW)
            print('led is offf')
            return True
        except Exception as e:
            print(f'Error {e}')
            return False