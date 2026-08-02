import time
seconds = 5
while seconds > 0:
    print(seconds)
    print(flush=True, end='\r')
    time.sleep(1)
    seconds = seconds - 1
print('we did it!')
