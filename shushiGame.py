from PIL import ImageGrab
import os
import time
import webbrowser
from pip import main
from win32 import win32api
import win32.lib.win32con as win32con

#req numpy .The Python Imaging Library.PyWin
#src tutoreal link ="https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117"
#####################################
#intrctions how to set game play  
# get Image from the fearst view window
# open in painter 
# get pixsls from top Left corner 
# then get pixsels bottom Right corner 
# laft top = 21,153
# bottom right = 791,715
# left top corner - 1 add pad_X and pad
#

x_pad =20 #laft top corner
y_pad =152 #right top corner
    
def get_cords():
    x,y = win32api.GetCursorPos()#create 2 vars x and y and set it to mouse position!!!
    x = x - x_pad
    y = y - y_pad
    print(x, y)####>>>>>>>> chinge <<<<<<<< here >>>>>>>>

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def screenGrab():   
    # laft top = 21,153
    #<<<<<<<<<<<<20 - 791>>>>>>>>>>>>pad_x
    #<<<<<<<<<<<<152 - 715>>>>>>>>>>>pad_y
# bottom right = 791,715
    box = (x_pad+1,y_pad+1,x_pad+771,y_pad+562)#set Limits of image frame
    im = ImageGrab.grab(box)#mack shore you put box in grab >>> grab(box) <<<
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
    '.png', 'PNG')

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')

 #on relese button   
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
  #  print ("Click.") #completely optional. But nice for debugging purposes.

def openBrowser():
    srcUrl1 ="https://www.silvergames.com/en/youda-sushi-chef"
    google=webbrowser.open(srcUrl1)

def LogInGame():# >>>>>>>>>>> need to work on thet befor use 
    time.sleep(3)
    mousePos((392,336))#start window (play button pos)
    #prass on Play btn
    leftClick()
    #skip the add 
    skipAdds()
    #skip adds second screen
    time.sleep(10)#<<<<< Adds >>>>>
    mousePos((387,378))#<<<<<< inter game button >>>>>>>
    leftClick()
    time.sleep(2)
    mousePos((557, 183))#<<<<<<< star button >>>>>>>
    leftClick()
    time.sleep(2)
    mousePos((375 ,298))#continue button 
    leftClick()
    print("end inter game ")

def skipAdds():
    mousePos((731, 510))#skip button pos
    time.sleep(8)#delay 8 seconds
    leftClick()#click on left mouse button 
# <<<<<<<<< pic gold from sell shushi (1-6)  cstomers >>>>>>>>
def picCoin():
    mousePos((112,233))
    time.sleep(0.1)
    leftClick()
    print("coin 1 pickd")
    mousePos((221,226))
    time.sleep(0.1)
    leftClick()
    print("<<<<<<<< pic coin 2 >>>>>>> ")
    mousePos((331,228))
    time.sleep(0.1)
    leftClick()
    print("<< pic coin 3>>")
    mousePos((442,218))
    time.sleep(0.1)
    leftClick()
    print("pic coin 4")
    mousePos((547,227))
    time.sleep(0.1)
    leftClick()
    print("pic coin 5")
    mousePos((659, 214))
    time.sleep(0.1)
    leftClick()
    print("pic coin 6")
    print("pic coin task finish")

#<<<<<<<<< Food making >>>>>> (1-9) >>>>>
#<<< food level 1
def onigiri():
    #1,1,2
    mousePos((220,329)) #pic food 1
    time.sleep(0.1)
    leftClick()
    time.sleep(0.1)
    leftClick()
    print("pic food 1")
    
    mousePos((220,387))
    time.sleep(0.1)
    leftClick()
    leftUp()
    print("pic food 2")
    CreateFood()
#
def roe_maki():
    #1,3 
    mousePos((220,329)) #pic food 1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")
    mousePos((218,440))#pic food 3 
    time.sleep(0.1)
    leftClick()
    print("pic food3")
    CreateFood() 
#leve 2 food 
def gunkan_maki():
    #1,2,3,3
    mousePos((220,329)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")
    mousePos((220,387))#pos food2 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 2")
    mousePos((217,443))#pos food 3 =x2
    time.sleep(0.1)
    leftClick()
    time.sleep(0.1)
    leftClick()
    print("make = food 3")
    CreateFood()
#level 3 food
def sake_roll():
    #1,1,2,4
    mousePos((220,329)) #pic food 1 =x2
    time.sleep(0.1)
    leftClick() 
    time.sleep(0.1)
    leftClick()
    print("pic food 1")
    mousePos((220,387))#pos food2 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 2")
    mousePos((162,324))#pos food4 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 4")
    CreateFood()
#
def unagi_nigiri():
    #1 2 4 4 
    mousePos((220,329)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")
    mousePos((220,387))#pos food2 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 2")
    mousePos((150, 392))#pos food5 =x2
    time.sleep(0.1)
    leftClick()
    time.sleep(0.1)
    leftClick()
    print("pic food 5")
    CreateFood()
#
def california_Roll():
    #1 , 3 ,4 ,7
    mousePos((220,329)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")
    mousePos((217,443))#pos food 3 =x1
    time.sleep(0.1)
    leftClick()
    print("make = food 3")
    mousePos((162,324))#pos food4 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 4")
    mousePos((98,327))#pos food7 =x1
    time.sleep(0.1)
    leftClick()
    CreateFood()
    print("pic food 7")
def Ebi_nigiri():
    mousePos((220,329)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")
    mousePos((162,442)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    time.sleep(0.1)### chack if need x2 clicks
    leftClick()
    print("pic food 6")
    CreateFood()
def ringu_maki():
    #1,4,4,7,8
    mousePos((220,329)) #pic food 1 =x1
    time.sleep(0.1)
    leftClick() 
    print("pic food 1")

    mousePos((162,324))#pos food4 =x1
    time.sleep(0.1)
    leftClick()
    time.sleep(0.1)
    leftClick()#cheack if need x2 Clicks
    print("pic food 4")

    mousePos((98,327))#pos food7 =x1
    time.sleep(0.1)
    leftClick()
    print("pic food 7")
    mousePos((112 ,385))#food 8 
    time.sleep(0.1)
    leftClick()
    print("food 8")
    CreateFood()





def CreateFood():
    mousePos((344,440))# create food button
    time.sleep(0.1)
    leftClick()
    leftUp()
    mousePos((303,406))
    time.sleep(0.1)
    leftClick()
    leftUp()
    print("food create")
#>>>>>>>>>> bay metereals to make shushi
#>>> Metereal 1 <<<
def met1():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((427,88))#met pos
    leftClick()
    leftUp()
#>>> Metereal 2 <<<
def met2():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((433,188))
    leftClick()
    leftUp()
#>>> Metereal 3 <<<
def met3():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((407,312))
    leftClick()
    leftUp()
#>>> Metereal 4 <<<
def met4():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((334,100))
    leftClick()
    leftUp()
#>>> Metereal 5 <<<
def met5():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((332,199))
    leftClick()
    leftUp()
#>>> Metereal 6 <<<
def met6():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((339, 293))
    leftClick()
    leftUp()
#>>> Metereal 7 <<<
def met7():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((258, 116))
    leftClick()
    leftUp()
#>>> Metereal 8 <<<
def met8():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((265 ,209))
    leftClick()
    leftUp()
#>>> Metereal 9 <<<
def met9():
    mousePos((652,354))#open bay menu
    leftClick()
    leftUp()
    mousePos((270 ,317))
    leftClick()
    leftUp()


def Start_bot():  
    openBrowser()
    time.sleep(3)
   ## LogInGame()# go till game start !!! need set solotion for adds its random aperss 
    
if __name__ == '__main__':
    Start_bot()

