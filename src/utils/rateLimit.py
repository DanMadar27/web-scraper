from time import sleep
from threading import Lock

requests_lock = Lock()

requests = 0 # counter
limit = 60 # 60 requests
interval = 60  # 60 seconds

def is_rate_limited():
    global requests

    if requests >= limit:
        return True
    
    with requests_lock:
        requests += 1
        return requests >= limit

def reset_rate_limit():
    global requests

    while True:
        sleep(interval)
        with requests_lock:
            requests = 0
