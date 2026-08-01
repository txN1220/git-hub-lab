import time
seconds = 5
while seconds > 0:
    print(seconds, end='\r', flush=True)
    time.sleep(1)
    seconds -= 1
print('we did it!')