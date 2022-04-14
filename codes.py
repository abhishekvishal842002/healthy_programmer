
# lets make the function which creates the respective file once and logs the data
def log(a,b):
    with open(b,"a") as f:
        f.write(str(a)+"\n")

# now lets make the function for playing music
def playsong(a):
        mixer.init()
        mixer.music.load(a)
        mixer.music.play()


import time
from pygame import mixer

while True:
    a=time.localtime()
    h=a.tm_hour
    m=a.tm_min
    s=a.tm_sec

    if h==9 and m==0 and s==0 :
        playsong("water.mp3")
        user=input("LETS START WORKING!\nSTART WITH DRINKING A CUP OF WATER\nwhen you complete drinking , PLEASE TYPE DRANK BELOW\n")
        if user=="drank":
            mixer.music.pause()
            log(time.asctime(),"water.txt")
        else:
            print("invalid input!")

    elif (h==10 or h==11 or h==12 or h==13 or h==14 or h==15 or h==16 or h==17) and m==0 and s==0 :
        playsong("water.mp3")
        user=input("its been an hour now its time to drink water\nwhen you complete drinking , PLEASE TYPE drank BELOW\n")

        if user=="drank":
            mixer.music.pause()
            log(time.asctime(),"water.txt")
        else:
            print("invalid input!")

    elif ( h==9 or h==10 or h==11 or h==12 or h==13 or h==14 or h==15 or h==16 ) and (m==25 or m==55) and s==0 :
        playsong("eye.mp3")
        user=input("you are continuously seeing the screen. please close your eyes once\nwhen you complete , PLEASE TYPE eye BELOW\n")

        if user=="eye":
            mixer.music.pause()
            log(time.asctime(),"eye.txt")
        else:
            print("invalid input!")
            
    elif ( h==10 or h==12 or h==14 or h==16 ) and m==40 and s==0 :
        playsong("exercise.mp3")
        user=input("you are continuously sitting on the chair. please do some exercise\nwhen you complete , PLEASE TYPE exercise BELOW\n")

        if user=="exercise":
            mixer.music.pause()
            log(time.asctime(),"exercise.txt")
        else:
            print("invalid input!")
    


