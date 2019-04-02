#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

s1 = "Player1"
s2 = "Player2"
b = ["","","","","","","","",""]

def winned():
    global b
    b = ["","","","","","","","",""]

def full():
    global b
    return (b[0]!="" and b[1]!="" and b[2]!="" and b[3]!="" and b[4]!="" and b[5]!="" and b[6]!="" and b[7]!="" and b[8]!="")


# 012
# 345
# 678

def win(v):
    return ((b[0]==v and b[1]==v and b[2]==v) or
    (b[3]==v and b[4]==v and b[5]==v) or
    (b[6]==v and b[7]==v and b[8]==v) or
    (b[0]==v and b[3]==v and b[6]==v) or
    (b[1]==v and b[4]==v and b[7]==v) or
    (b[2]==v and b[5]==v and b[8]==v) or
    (b[0]==v and b[4]==v and b[8]==v) or
    (b[2]==v and b[4]==v and b[6]==v))

def showgame():
    global b
    print("\n"*100)
    print(b[0] +"|"+ b[1] +"|"+ b[2])
    time.sleep(0.05)
    print(b[3] +"|"+ b[4] +"|"+ b[5])
    time.sleep(0.05)
    print(b[6] +"|"+ b[7] +"|"+ b[8])

    if win("o"):
        print(s2+" won!")
        winned()
    if win("x"):
        print(s1+" won!")
        winned()
    if full():
        print("Done")
        b = ["","","","","","","","",""]


playsnow = 1

def play():
    global playsnow
    global b
    global s1
    global s2


    n2 = ""

    if playsnow==1:
        sa = s1
    if playsnow==2:
        sa = s2

    try:
        try:
            inp = raw_input(sa+": ")
        except:
            inp = input(sa+": ")
        if inp=="exit":
            exit()
        n = int(inp)
        if (n < 10) and (n > 0):
            n2 = n-1

    except:
        print("Error")


    if n2 != "":
        if b[n2] == "":

            if playsnow == 1:
                b[n2] = "x"
                playsnow = 2
            elif playsnow == 2:
                b[n2] = "o"

                playsnow = 1
        else:
            print("This field is already in use!")
            #play()
        showgame()
    else:
        print("You have to type a number from 1-9!")
        #play()
    play()

def start():
    global s1, s2
    try:
        s1 = str(raw_input("Spieler1 o: "))
        s2 = str(raw_input("Spieler2 x: "))
    except:
        s1 = str(input("Spieler1 o: "))
        s2 = str(input("Spieler2 x: "))
    play()
