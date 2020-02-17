import threading
import time
import random

from client import client
from server import server

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")
