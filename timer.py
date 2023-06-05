import time
seconds=input("enter the time in second")
def countdown_timer(seconds):
    while seconds>0:
        min=int(seconds/60)
        sec=int(seconds%60)
        timer=f'{min}:{sec}'
        seconds-=1
        time.sleep(5)
        print(timer)
countdown_timer(int(seconds))





























