#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

   TICTACTOE
   AUTHOR: JULIANFUN123 - INTERAAPPS
   WEBSITE: INTERAAPPS.DE


"""


print("\n"*100)

####  Imports
try:
    import sys
    from time import gmtime, strftime
except:
    print('Couldn\'t import the base Libs.')
    exit()
## #  Changind Directory
sys.path.insert(0, 'ttc')

logFile = open("ttc_logfile.txt","w+")
def gameLog(l):
    global logFile
    logFile.write(logFile.read()+"\n"+str( strftime("%Y-%m-%d %H:%M:%S", gmtime()) )+' | '+l)

try:
    import normal
    import ttc_init
    import bot
except:
    print("Couldn't load the Gamefiles")
    gameLog("Couldn't load the Gamefiles")


# Intro
print(ttc_init.intro_step_1)
ttc_init.time.sleep(0.5)
print("\n"*100)
print(ttc_init.intro_step_2)
ttc_init.time.sleep(0.5)
print("\n"*100)
print(ttc_init.intro_step_3)
ttc_init.time.sleep(0.5)


h = 50
while h != 0:
    ttc_init.time.sleep(0.05)
    print("\n")
    h-=1

ttc_init.flyingMatchfield()

# Gameoptions

while True:
    print("""
     GAMEOPTIONS:

      1  : NORMAL
      2  : BOT (RANDOM)

      __

      99 : EXIT
    """)

    try:
        option = raw_input('Enter Gametype: ')
    except:
        option = input('Enter Gametype: ')

    if option=="1":
        normal.start()
    elif option=="2":
        bot.start()
    elif option=="99":
        print('Bye!')
        exit()
    else:
        print('Not found :(')

logFile.close()
