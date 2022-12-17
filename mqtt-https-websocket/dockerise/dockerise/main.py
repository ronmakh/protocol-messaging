import time
import random
import publish as hakase

while True:
    hakase.call_publish(
        "staging/raw",
        random.randint(20,50)
    )
    print("Publishing...")
    time.sleep(2.5)