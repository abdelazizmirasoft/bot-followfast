import pyautogui,time, datetime
from pynput.keyboard import Key, Controller
from random import randint

def closeTab():
    keyboard1.press(Key.ctrl_l)
    keyboard1.press("w")
    keyboard1.release("w")
    keyboard1.release(Key.ctrl_l)
def prevTab():
    keyboard1.press(Key.ctrl_l)
    keyboard1.press(Key.shift)
    keyboard1.press(Key.tab)
    keyboard1.release(Key.tab)
    keyboard1.release(Key.shift)
    keyboard1.release(Key.ctrl_l)
def nextTab():
    keyboard1.press(Key.ctrl_l)
    keyboard1.press(Key.tab)
    keyboard1.release(Key.tab)
    keyboard1.release(Key.ctrl_l)
def pageDown():
    keyboard1.press(Key.page_down)
    keyboard1.release(Key.page_down)
def typeChar(char):
    keyboard1.press(char)
    keyboard1.release(char)
def switchWindow():
    keyboard1.press(Key.alt)
    keyboard1.press(Key.tab)
    time.sleep(2)
    keyboard1.release(Key.tab)
    keyboard1.release(Key.alt)
def hitEnter():
    keyboard1.press(Key.enter)
    time.sleep(2)
    keyboard1.release(Key.enter)
def hitDown():
    keyboard1.press(Key.down)
    time.sleep(2)
    keyboard1.release(Key.down)
def likePost(pathFFStep1,pathFFStep2, pathLikeWebsite, postName):    
    pyautogui.click(pos[0],pos[1])
    time.sleep(randint(15,20))
    pos49 = pyautogui.locateCenterOnScreen(pathFFStep1)
    posLike = pyautogui.locateCenterOnScreen(pathFFStep2)
    index = 0
    while pos49 != None and posLike != None and index < 20:
          index += 1
          pyautogui.click(posLike[0],posLike[1])
          prevTab()
          time.sleep(randint(1,4))
          pyautogui.click(posLike[0],posLike[1])
          time.sleep(2)
          posStopTabBrave = pyautogui.locateCenterOnScreen('buttons/stopTab.PNG')
          pyautogui.click(posStopTabBrave[0],posStopTabBrave[1])
          nextTab()
          print (postName+" Yes!")
          time.sleep(randint(13,18))
          counterPressDown = 0
          posLikeWebsite = pyautogui.locateCenterOnScreen(pathLikeWebsite)
          while counterPressDown<20 and posLikeWebsite == None:
                  hitDown()
                  counterPressDown+=1
                  posLikeWebsite = pyautogui.locateCenterOnScreen(pathLikeWebsite)
          if posLikeWebsite != None:
              pyautogui.click(posLikeWebsite[0],posLikeWebsite[1])
              time.sleep(randint(3,6))
          closeTab()
          time.sleep(2)
          closeTab()
          prevTab()
          time.sleep(randint(10,16))
          pos49 = pyautogui.locateCenterOnScreen(pathFFStep1)
          posLike = pyautogui.locateCenterOnScreen(pathFFStep2)
pyautogui.FAILSAFE = False
keyboard1 = Controller()


## Listing my clickable pictures
buttonsList = ['FbSubsList.PNG', 'InstaLikeList.PNG', 'TweetList.PNG', 'LikeTweetList.PNG'] #,'RetweetList.PNG']
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0"]

loop = 0
while True:
    time.sleep(1)
    pyautogui.click(470,10)
    time.sleep(1)
    pyautogui.click(470,10)
    time.sleep(1)
    pyautogui.click(470,10)
    if loop == 2:
        loop = 0
    else:
        loop += 1 
    for b in buttonsList:
        ## Locate the picture center  
        pos = pyautogui.locateCenterOnScreen('buttons/'+b)#If the file is not a png file it will not work
        ##pyautogui.moveTo(start)#Moves the mouse to the coordinates of the image
        print(pos)
        if pos != None:
            if b == 'FbSubsList.PNG':
                pyautogui.click(pos[0],pos[1])
                time.sleep(randint(15,20))
                ## Loop clicking on the follow button
                posFollowFb = pyautogui.locateCenterOnScreen('buttons/FollowFbFollowFast.PNG')
                while posFollowFb != None:
                    print ("Follow Yes!")
                    pyautogui.click(posFollowFb[0],posFollowFb[1])
                    time.sleep(randint(1,4))
                    closeTab()
                    time.sleep(randint(10,15))
                    posFollowFb = pyautogui.locateCenterOnScreen('buttons/FollowFbFollowFast.PNG')
            if b == 'InstaLikeList.PNG':
                likePost('buttons/49LikeInsta.PNG', 'buttons/LikeInstaFollowFast.PNG', 'buttons/LikeInsta.PNG', "LikeInsta")
            if b == 'TweetList.PNG':
                pyautogui.click(pos[0],pos[1])
                time.sleep(15)
                ## Loop clicking on the follow button
                posTweet = pyautogui.locateCenterOnScreen('buttons/49Tweet.PNG')
                while posTweet != None:
                    print ("Tweet Yes!")
                    #posTweetClick = pyautogui.locateCenterOnScreen('buttons/TweetFollowFast.PNG')
                    #pyautogui.click(posTweetClick[0],posTweetClick[1])
                    pyautogui.click(posTweet[0],posTweet[1]+15)
                    prevTab()
                    time.sleep(randint(1,4))
                    #pyautogui.click(posTweetClick[0],posTweetClick[1])
                    pyautogui.click(posTweet[0],posTweet[1]+15)
                    time.sleep(1)
                    posStopTabBrave = pyautogui.locateCenterOnScreen('buttons/stopTab.PNG')
                    pyautogui.click(posStopTabBrave[0],posStopTabBrave[1])
                    #nextTab()
                    nextTab()
                    time.sleep(randint(9,15))
                    pageDown()
                    pageDown()
                    posTweetTweeter = pyautogui.locateCenterOnScreen('buttons/TweetTweeter.PNG')
                    if posTweetTweeter != None:
                        #Type 4 times random chars to avoid looping
                        typeChar(alphabet[randint(0,26)])
                        typeChar(alphabet[randint(0,26)])
                        typeChar(alphabet[randint(0,26)])
                        typeChar(alphabet[randint(0,26)])
                        pyautogui.click(posTweetTweeter[0],posTweetTweeter[1])
                        time.sleep(randint(9,15))
                    closeTab()
                    time.sleep(2)
                    #closeTab()
                    closeTab()
                    prevTab()
                    time.sleep(randint(12,16))
                    posTweet = pyautogui.locateCenterOnScreen('buttons/49Tweet.PNG')
            if b == 'LikeTweetList.PNG':
                likePost('buttons/49LikeTweet.PNG','buttons/LikeTweetFollowFast.PNG', 'buttons/LikeTweeter.PNG', "LikeTweeter")
                time.sleep(15)
            if b == 'RetweetList.PNG':
                pyautogui.click(pos[0],pos[1])
                time.sleep(15)
    #switchWindow()
    #print ("switch window")
    if loop == 2:
        timeSleep = randint(1100,1500)
        print("Sleep time:"+str(timeSleep/60)+"min Since: "+str(datetime.datetime.now().time()))
        keyboard1.press(Key.f5)
        keyboard1.release(Key.f5)
        time.sleep(timeSleep)
             


