# import time
import random
import math
# import numpy
# import panda
import pygame
import ctypes
import _pickle
import os.path
import os

print("Loading... please wait. This may take a while.")
print("Please do not click on this window while the game is loading.")
pygame.init()
Images = [f for f in os.listdir("Images") if os.path.isfile(os.path.join("Images", f))]


class DisplayManager:
    def __init__(self):
        self.Images = {}
        ctypes.windll.user32.SetProcessDPIAware()
        self.ScreenRes = (1920, 1080)
        self.Window = pygame.display.set_mode(self.ScreenRes, pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE)
        self.GameRes = (480, 270)
        self.ResRatio = (self.ScreenRes[0] // self.GameRes[0], self.ScreenRes[1] // self.GameRes[1])

    def load_images(self):
        for Image in os.listdir("Images"):
            self.Images[Image[:-4]] = pygame.image.load("Images\{0}".format(Image)).convert_alpha()
            self.Images[Image[:-4]] = pygame.transform.scale(self.Images[Image[:-4]],
                                                             (self.Images[Image[:-4]].get_size()[0] * self.ResRatio[0],
                                                              self.Images[Image[:-4]].get_size()[1] * self.ResRatio[1]))

    def place_image(self, image_id, x, y):
        x = round(x)
        y = round(y)
        if image_id in self.Images.keys():
            y = self.GameRes[1] - y - (self.Images[image_id].get_size()[1] / self.ResRatio[1])
            self.Window.blit(self.Images[image_id], (x * self.ResRatio[0], y * self.ResRatio[1]))
        else:
            print(
                "ERROR: Image " + image_id + " has not been loaded. Make sure you have placed the image in the images "
                                             "folder and spelt the file name correctly.")

    def place_text(self, text, x, y):
        x = round(x)
        y = round(y)
        x2 = x
        for Letter in text:
            if Letter in self.Images.keys():
                y2 = self.GameRes[1] - y - (self.Images[Letter].get_size()[1] / self.ResRatio[1])
                self.Window.blit(self.Images[Letter], (x2 * self.ResRatio[0], y2 * self.ResRatio[1]))
                x2 += (self.Images[Letter].get_size()[0] / self.ResRatio[0]) + 1
            elif Letter == "\n":
                y += -6
                x2 = x
            elif Letter == " ":
                x2 += 6
            else:
                print(
                    "ERROR: Character " + Letter + " has not been loaded. Make sure the character is "
                                                   "present in the images folder.")

    def update(self):
        pygame.event.get()
        pygame.display.update()
        self.place_image("Blank", 0, 0)


class SoundManager:
    def __init__(self):
        self.Sounds = {}
        pygame.mixer.set_num_channels(4)

    def load_sounds(self):
        for Sound in os.listdir("Sounds"):
            self.Sounds[Sound[:-4]] = pygame.mixer.Sound("Sounds\{0}".format(Sound))

    def play_sound(self, sound_id, loops):
        if sound_id in self.Sounds.keys():
            self.Sounds[sound_id].play(loops=loops)
        else:
            print(
                "ERROR: Sound " + sound_id + " has not been loaded. Make sure you have placed the sound in "
                                             "the sounds folder and spelt the file name correctly.")

    @staticmethod
    def stop_sounds():
        pygame.mixer.stop()


def save(data):
    _pickle.dump(data, open("Saves\SaveFile.sav", "wb"))


def load():
    for SaveFile in os.listdir("Saves"):
        save_data = _pickle.load(open("Saves\{0}".format(SaveFile), "rb"))
        return save_data
    print("ERROR: save file not present")
    return "ERROR"


def over_world(screen, mixer, save_data, temp_data):
    temp_data["ActiveEncounter"] = False
    temp_data["EncounterData"] = None
    screen.place_image("Map", 0, 0)
    if not temp_data["Moving"][0]:
        screen.place_image("Flag2", temp_data["PositionData"][save_data["Position"]][0][0],
                           temp_data["PositionData"][save_data["Position"]][0][1])
        input_keys = pygame.key.get_pressed()
        if input_keys[pygame.K_w] and not (temp_data["PositionData"][save_data["Position"]][1][0] == -1):
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][0]
            while input_keys[pygame.K_w]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif input_keys[pygame.K_d] and not (temp_data["PositionData"][save_data["Position"]][1][1] == -1):
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][1]
            while input_keys[pygame.K_d]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif input_keys[pygame.K_s] and not (temp_data["PositionData"][save_data["Position"]][1][2] == -1):
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][2]
            while input_keys[pygame.K_s]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif input_keys[pygame.K_a] and not (temp_data["PositionData"][save_data["Position"]][1][3] == -1):
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][3]
            while input_keys[pygame.K_a]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
    else:
        if temp_data["Moving"][2] >= 30:
            save_data["Position"] = temp_data["Moving"][1]
            temp_data["Moving"] = [False, 0, 0]
        else:
            temp_data["Moving"][2] += 1
            screen.place_image("Flag2",
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][0] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][0] * (
                                        30 - temp_data["Moving"][2])) / 30,
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][1] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][1] * (
                                        30 - temp_data["Moving"][2])) / 30)
    for encounter in temp_data["Encounters"]:
        screen.place_image("Alert1", (temp_data["PositionData"][encounter[0]][0][0] +
                                      temp_data["PositionData"][encounter[1]][0][0]) / 2,
                           (temp_data["PositionData"][encounter[0]][0][1] +
                            temp_data["PositionData"][encounter[1]][0][1]) / 2 + 5 + math.sin(
                               temp_data["AnimateTick"] / 35) * -0.75)
        screen.place_image("Alert2", (temp_data["PositionData"][encounter[0]][0][0] +
                                      temp_data["PositionData"][encounter[1]][0][0]) / 2 + 1,
                           (temp_data["PositionData"][encounter[0]][0][1] +
                            temp_data["PositionData"][encounter[1]][0][1]) / 2 - 1)
    if random.randint(0, 2500) == 0:
        temp_data["Airships"].append([-20, random.randint(0, 270)])
    to_delete = []
    for AirshipNum in range(0, len(temp_data["Airships"])):
        screen.place_image("Airship", temp_data["Airships"][AirshipNum][0], temp_data["Airships"][AirshipNum][1])
        temp_data["Airships"][AirshipNum][0] += 0.2
        if temp_data["Airships"][AirshipNum][0] > 500:
            to_delete.append(AirshipNum)
    for i in to_delete:
        temp_data["Airships"].pop(i)
# temp_data["EncounterData"] = {}
# temp_data["EncounterData"]["Type"] = "Battle"
# temp_data["EncounterData"]["Enemies"] = ["Goblin", "Orc"]
# save_data = random_encounter(save_data, temp_data["EncounterData"])
    return save_data, temp_data


def random_encounter(screen, mixer, save_data, temp_data):
    temp_data["ActiveEncounter"] = True
    if temp_data["EncounterData"]["Type"] == "Battle":
        screen.place_image("EncounterBack", 0, 0)
    elif temp_data["EncounterData"]["Type"] == "Dialogue":
        screen.place_image(temp_data["EncounterData"]["Background"], 0, 0)
        if not temp_data["PageNumber"] == -1:
            screen.place_text(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][0], 10, 80)
            for OptionNum in range(0, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) - 1):
                screen.place_text(str(OptionNum + 1) + "; " +
                                  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][OptionNum + 1][0], 10,
                                  60 - OptionNum * 10)
        else:
            temp_data["ActiveEncounter"] = False
            return save_data, temp_data
        input_keys = pygame.key.get_pressed()
        if input_keys[pygame.K_1] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 0:
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_2] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 1:
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_3] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 2:
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][1]
            mixer.play_sound("ExampleSound", 0)
        elif input_keys[pygame.K_4] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 3:
            temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][1]
            mixer.play_sound("ExampleSound", 0)
        while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3] or input_keys[pygame.K_4]:
            input_keys = pygame.key.get_pressed()
            pygame.event.get()
    return save_data, temp_data


def new_game():
    save_data = {"Position": 4}
    temp_data = {"ActiveEncounter": True, "EncounterData": {}}
    temp_data["EncounterData"]["Type"] = "Dialogue"
    temp_data["EncounterData"]["Background"] = "BlankWhite"
    temp_data["EncounterData"]["Dialogue"] = []
    temp_data["EncounterData"]["Dialogue"].append(
        ["WAKE UP ADVENTURER!", ["AGREE AND GET OUT OF BED", 1], ["STAY SLEEPING", 2]])
    temp_data["EncounterData"]["Dialogue"].append(["OK YOU CAN GO NOW", ["EXIT", -1]])
    temp_data["EncounterData"]["Dialogue"].append(["BRUH", ["FINE I'LL GET UP THEN", 1], ["STAY SLEEPING", 2]])
    temp_data["PageNumber"] = 0
    temp_data["PositionData"] = []
    temp_data["PositionData"].append([[43, 125], [-1, 2, 3, -1]])  # Links are done up down left right -1 means no link
    temp_data["PositionData"].append([[122, 229], [-1, -1, 2, -1]])
    temp_data["PositionData"].append([[144, 152], [1, 4, 3, 0]])
    temp_data["PositionData"].append([[173, 40], [2, -1, -1, 0]])
    temp_data["PositionData"].append([[224, 229], [-1, 5, -1, 2]])
    temp_data["PositionData"].append([[319, 184], [-1, 8, 7, 4]])
    temp_data["PositionData"].append([[321, 22], [7, -1, -1, -1]])
    temp_data["PositionData"].append([[365, 104], [5, 8, 6, -1]])
    temp_data["PositionData"].append([[394, 162], [-1, -1, 7, 5]])
    temp_data["AnimateTick"] = 0
    temp_data["Moving"] = [False, 0, 0]
    temp_data["Encounters"] = []
    temp_data["Airships"] = []
    for i in range(0, 5):
        temp_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
        while temp_data["Encounters"][i][1] == -1:
            temp_data["Encounters"][i][1] = random.choice(temp_data["PositionData"][temp_data["Encounters"][i][0]][1])
        for i2 in range(0, i):
            if temp_data["Encounters"][i2] == temp_data["Encounters"][i]:
                temp_data["Encounters"].pop(i)
    print(len(temp_data["Encounters"]))
    return save_data, temp_data


def main():
    screen = DisplayManager()
    screen.load_images()
    mixer = SoundManager()
    mixer.load_sounds()
    mixer.play_sound("DesertTheme1", -1)
    save_data, temp_data = new_game()
    while True:
        if temp_data["ActiveEncounter"]:
            save_data, temp_data = random_encounter(screen, mixer, save_data, temp_data)
        else:
            save_data, temp_data = over_world(screen, mixer, save_data, temp_data)
        temp_data["AnimateTick"] += 1
        screen.update()


main()
