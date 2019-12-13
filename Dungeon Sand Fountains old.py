print("Loading... please wait. This may take a while.")
print("Please do not click on this window while the game is loading.")
import time
import random
import math
#import numpy
#import panda
import pygame
import ctypes
import _pickle
import os.path
import os
pygame.init()
Images = [f for f in os.listdir("Images") if os.path.isfile(os.path.join("Images", f))]
class DisplayManager:
    def __init__(self):
        ctypes.windll.user32.SetProcessDPIAware()
        self.ScreenRes=(1920,1080)
        self.Window=pygame.display.set_mode(self.ScreenRes,pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)
        self.GameRes=(480,270)
        self.ResRatio=(self.ScreenRes[0]//self.GameRes[0],self.ScreenRes[1]//self.GameRes[1])

    def LoadImages(self):
        self.Images={}
        for Image in os.listdir("Images"):
            self.Images[Image[:-4]]=pygame.image.load("Images\{0}".format(Image)).convert_alpha()
            self.Images[Image[:-4]]=pygame.transform.scale(self.Images[Image[:-4]],
                                                           (self.Images[Image[:-4]].get_size()[0]*self.ResRatio[0],self.Images[Image[:-4]].get_size()[1]*self.ResRatio[1]))
        
    def PlaceImage(self,ImageID,x,y):
        x=round(x)
        y=round(y)
        if ImageID in self.Images.keys():
            y=self.GameRes[1]-y-(self.Images[ImageID].get_size()[1]/self.ResRatio[1])
            self.Window.blit(self.Images[ImageID], (x*self.ResRatio[0],y*self.ResRatio[1]))
        else:
            print("ERROR: Image "+ImageID+" has not been loaded. Make sure you have placed the image in the images folder and spelt the file name correctly.")

    def PlaceText(self, Text, x, y):
        x=round(x)
        y=round(y)
        x2=x
        for Letter in Text:
            if Letter in self.Images.keys():
                y2=self.GameRes[1]-y-(self.Images[Letter].get_size()[1]/self.ResRatio[1])
                self.Window.blit(self.Images[Letter], (x2*self.ResRatio[0],y2*self.ResRatio[1]))
                x2+=(self.Images[Letter].get_size()[0]/self.ResRatio[0])+1
            elif Letter=="\n":
                y+=-6
                x2=x
            elif Letter==" ":
                x2+=6
            else:
                print("ERROR: Character "+Letter+" has not been loaded. Make sure the character is present in the images folder.")

    def Update(self):
        pygame.event.get()
        pygame.display.update()
        self.PlaceImage("Blank",0,0)

class SoundManager:
    def __init__(self):
        pygame.mixer.set_num_channels(4)

    def LoadSounds(self):
        self.Sounds={}
        for Sound in os.listdir("Sounds"):
            self.Sounds[Sound[:-4]]=pygame.mixer.Sound("Sounds\{0}".format(Sound))

    def PlaySound(self,SoundID,Loops):
        if SoundID in self.Sounds.keys():
            self.Sounds[SoundID].play(loops=Loops)
        else:
            print("ERROR: Sound "+SoundID+" has not been loaded. Make sure you have placed the sound in the sounds folder and spelt the file name correctly.")

    def StopSounds(self):
        pygame.mixer.stop()

def Save(SaveData):
    _pickle.dump(SaveData, open("Saves\SaveFile.sav","wb"))
    
def Load():
    for SaveFile in os.listdir("Saves"):
        SaveData = _pickle.load(open("Saves\{0}".format(SaveFile),"rb"))
        return SaveData
    if SaveData==None:
        print("ERROR: Save file not present")
        return "ERROR"

def Overworld(Screen, Mixer, SaveData, TempData):
    TempData["ActiveEncounter"]=False
    TempData["EncounterData"]=None
    Screen.PlaceImage("Map",0,0)
    if not TempData["Moving"][0]:
        Screen.PlaceImage("Flag2",TempData["PositionData"][SaveData["Position"]][0][0],TempData["PositionData"][SaveData["Position"]][0][1])
        InputKeys=pygame.key.get_pressed()
        if InputKeys[pygame.K_w] and not (TempData["PositionData"][SaveData["Position"]][1][0]==-1):
            TempData["Moving"][0]=True
            TempData["Moving"][1]=TempData["PositionData"][SaveData["Position"]][1][0]
        elif InputKeys[pygame.K_d] and not (TempData["PositionData"][SaveData["Position"]][1][1]==-1):
            TempData["Moving"][0]=True
            TempData["Moving"][1]=TempData["PositionData"][SaveData["Position"]][1][1]
        elif InputKeys[pygame.K_s] and not (TempData["PositionData"][SaveData["Position"]][1][2]==-1):
            TempData["Moving"][0]=True
            TempData["Moving"][1]=TempData["PositionData"][SaveData["Position"]][1][2]
        elif InputKeys[pygame.K_a] and not (TempData["PositionData"][SaveData["Position"]][1][3]==-1):
            TempData["Moving"][0]=True
            TempData["Moving"][1]=TempData["PositionData"][SaveData["Position"]][1][3]
    else:
        if TempData["Moving"][2]>=30:
            SaveData["Position"]=TempData["Moving"][1]
            TempData["Moving"]=[False,0,0]
        else:
            TempData["Moving"][2]+=1
            Screen.PlaceImage("Flag2",(TempData["PositionData"][TempData["Moving"][1]][0][0]*(TempData["Moving"][2])+
                                          TempData["PositionData"][SaveData["Position"]][0][0]*(30-TempData["Moving"][2]))/30,
                                          (TempData["PositionData"][TempData["Moving"][1]][0][1]*(TempData["Moving"][2])+
                                          TempData["PositionData"][SaveData["Position"]][0][1]*(30-TempData["Moving"][2]))/30)
    for Encounter in TempData["Encounters"]:
        Screen.PlaceImage("Alert1",(TempData["PositionData"][Encounter[0]][0][0]+
                                          TempData["PositionData"][Encounter[1]][0][0])/2,
                                          (TempData["PositionData"][Encounter[0]][0][1]+
                                          TempData["PositionData"][Encounter[1]][0][1])/2+5+math.sin(TempData["AnimateTick"]/35)*-0.75)
        Screen.PlaceImage("Alert2",(TempData["PositionData"][Encounter[0]][0][0]+
                                          TempData["PositionData"][Encounter[1]][0][0])/2+1,
                                          (TempData["PositionData"][Encounter[0]][0][1]+
                                          TempData["PositionData"][Encounter[1]][0][1])/2-1)
    if random.randint(0,2500)==0:
        TempData["Airships"].append([-20,random.randint(0,270)])
    ToDelete=[]
    for AirshipNum in range(0,len(TempData["Airships"])):
        Screen.PlaceImage("Airship",TempData["Airships"][AirshipNum][0],TempData["Airships"][AirshipNum][1])
        TempData["Airships"][AirshipNum][0]+=0.2
        if TempData["Airships"][AirshipNum][0]>500:
            ToDelete.append(AirshipNum)
    for i in ToDelete:
        TempData["Airships"].pop(i)
    if False:
        TempData["EncounterData"]={}
        TempData["EncounterData"]["Type"]="Battle"
        TempData["EncounterData"]["Enemies"]=["Goblin","Orc"]
        SaveData=Encounter(SaveData,TempData["EncounterData"])
    return SaveData, TempData

def Encounter(Screen, Mixer, SaveData,TempData):
    TempData["ActiveEncounter"]=True
    if TempData["EncounterData"]["Type"]=="Battle":
        Screen.PlaceImage("EncounterBack",0,0)
    elif TempData["EncounterData"]["Type"]=="Dialogue":
        Screen.PlaceImage(TempData["EncounterData"]["Background"],0,0)
        if not TempData["PageNumber"]==-1:
            Screen.PlaceText(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][0],10,80)
            for OptionNum in range(0,len(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]])-1):
                Screen.PlaceText(str(OptionNum+1)+"; "+TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][OptionNum+1][0],10,60-OptionNum*10)
        else:
            TempData["ActiveEncounter"]=False
            return(SaveData,TempData)
        InputKeys=pygame.key.get_pressed()
        if InputKeys[pygame.K_1] and len(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]])>0:
            TempData["PageNumber"]=TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][1][1]
            Mixer.PlaySound("ExampleSound",0)
        elif InputKeys[pygame.K_2] and len(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]])>1:
            TempData["PageNumber"]=TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][2][1]
            Mixer.PlaySound("ExampleSound",0)
        elif InputKeys[pygame.K_3] and len(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]])>2:
            TempData["PageNumber"]=TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][3][1]
            Mixer.PlaySound("ExampleSound",0)
        elif InputKeys[pygame.K_4] and len(TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]])>3:
            TempData["PageNumber"]=TempData["EncounterData"]["Dialogue"][TempData["PageNumber"]][4][1]
            Mixer.PlaySound("ExampleSound",0)
        while InputKeys[pygame.K_1] or InputKeys[pygame.K_2] or InputKeys[pygame.K_3] or InputKeys[pygame.K_4]:
                InputKeys=pygame.key.get_pressed()
                pygame.event.get()
    return SaveData,TempData

def NewGame():
    SaveData={}
    SaveData["Position"]=4
    SaveData["Party"]=[]
    TempData={}
    TempData["ActiveEncounter"]=True
    TempData["EncounterData"]={}
    TempData["EncounterData"]["Type"]="Dialogue"
    TempData["EncounterData"]["Background"]="BlankWhite"
    TempData["EncounterData"]["Dialogue"]=[]
    TempData["EncounterData"]["Dialogue"].append(["WAKE UP ADVENTURER!",["AGREE AND GET OUT OF BED",1],["STAY SLEEPING",2]])
    TempData["EncounterData"]["Dialogue"].append(["OK YOU CAN GO NOW",["EXIT",-1]])
    TempData["EncounterData"]["Dialogue"].append(["BRUH",["FINE I'LL GET UP THEN",1],["STAY SLEEPING",2]])
    TempData["PageNumber"]=0
    TempData["PositionData"]=[]
    TempData["PositionData"].append([[43,125],[-1,2,3,-1]]) #Links are done up down left right -1 means no link
    TempData["PositionData"].append([[122,229],[-1,-1,2,-1]])
    TempData["PositionData"].append([[144,152],[1,4,3,0]])
    TempData["PositionData"].append([[173,40],[2,-1,-1,0]])
    TempData["PositionData"].append([[224,229],[-1,5,-1,2]])
    TempData["PositionData"].append([[319,184],[-1,8,7,4]])
    TempData["PositionData"].append([[321,22],[7,-1,-1,-1]])
    TempData["PositionData"].append([[365,104],[5,8,6,-1]])
    TempData["PositionData"].append([[394,162],[-1,-1,7,5]])
    TempData["AnimateTick"]=0
    TempData["Moving"]=[False,0,0]
    TempData["Encounters"]=[]
    TempData["Airships"]=[]
    ToDelete=[]
    for i in range(0,5):
        TempData["Encounters"].append([random.randint(0,len(TempData["PositionData"])-1),-1])
        while TempData["Encounters"][i][1]==-1:
            TempData["Encounters"][i][1]=random.choice(TempData["PositionData"][TempData["Encounters"][i][0]][1])
        for i2 in range(0,i):
            if TempData["Encounters"][i2][0] in TempData["Encounters"][i] and TempData["Encounters"][i2][1] in TempData["Encounters"][i]:
                ToDelete.append(i)
    for i in range(0,len(ToDelete)):
        TempData["Encounters"].pop(ToDelete[i]-i)
    return SaveData,TempData
    
def Main():
    Screen=DisplayManager()
    Screen.LoadImages()
    Mixer=SoundManager()
    Mixer.LoadSounds()
    Mixer.PlaySound("DesertTheme1",-1)
    SaveData,TempData=NewGame()
    while True:
        FrameTime=time.time()
        if TempData["ActiveEncounter"]:
            SaveData,TempData = Encounter(Screen, Mixer, SaveData,TempData)
        else:
            SaveData,TempData=Overworld(Screen, Mixer, SaveData,TempData)
        TempData["AnimateTick"]+=1
        Screen.Update()
        if FrameTime+0.016>time.time():
            time.sleep(0.017-(time.time()-FrameTime))

Main()

