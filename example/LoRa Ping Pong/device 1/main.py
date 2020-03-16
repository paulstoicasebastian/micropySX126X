from sx1262 import SX1262
import time

def cb(arg):
    events = lora.events()
    if events & SX1262.RX_DONE:
        msg, err = lora.recv()
        error = SX1262.ERROR[err]
        print('Receive: {}, {}'.format(msg, error))
    elif events & SX1262.TX_DONE:
        print('TX done.')
    lora.startReceive()

lora = SX1262('P5','P6','P7','P8')

lora.begin()

lora.setBlocking(False)
lora.setCallback(cb)
lora.startReceive()

while True:
    lora.send(b'Ping')
    time.sleep(10)
