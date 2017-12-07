from serial import Serial
from time import sleep
from datetime import datetime
import requests


URL = 'http://127.0.0.1:8080/postLog'

def post(id, state):
    data = {'id': id, 'success': state, 'time': datetime.utcnow()}
    req = requests.post(URL, data)
    print req.status_code

serial_connection = Serial('/dev/ttyACM0', 9600)

while True:
    id = str(serial_connection.readline())
    id = id.strip('\n')
    state = str(serial_connection.readline())
    state = state.strip('\n')
    if id and state:
        print id
        print state
        post(id, state)
    sleep(0.01)

