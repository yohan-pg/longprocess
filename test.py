import os 
import longprocess
import time

print(os.getpid())
longprocess.linger()

while True:
    time.sleep(1)
    print(".")