import time
import random
import math
import copy
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


def new_game():
    save_data = {"Position": 4, "Party": [], "Name": "You"}
    save_data["Party"].append(
        Character(save_data["Name"], 1, 8, 8, 8, 8, 8, 8, [["Physical", "Melee", 4], ["Magical", "Ranged", 4]]))
    save_data["GuildHall"]=[]
    save_data["StoryProgress"] = {"JigsawPieces": 0}
    save_data["Tutorial"]=True
    save_data["Inventory"] = {}
    save_data["Inventory"]["Gold"] = 10
    save_data["Inventory"]["Jigsaw Pieces"] = 0
    temp_data = {"EncounterData": {}, "ActiveScreen": "Encounter"}
    temp_data["EncounterData"]["Type"] = "Dialogue"
    temp_data["EncounterData"]["Background"] = "House"
    temp_data["EncounterData"]["Character"] = "None"
    temp_data["EncounterData"]["Dialogue"] = []
    temp_data["EncounterData"]["Dialogue"].append(
        ["A LOUD, FRANTIC KNOCK ON THE DOOR SUDDENLY WAKES YOU UP", ["GET OUT OF BED AND ANSWER IT", 2, ["Character","Quin"]], ["COVER YOUR EARS WITH A PILLOW AND TRY TO GO BACK TO SLEEP", 1]])
    temp_data["EncounterData"]["Dialogue"].append(["THE KNOCKING INCREASES, IT'S NO USE", ["GIVE IN AND GET UP", 2, ["Character","Quin"]], ["KEEP TRYING TO GO BACK TO SLEEP", 1]])
    temp_data["EncounterData"]["Dialogue"].append(["YOU OPEN THE DOOR TO SEE YOUR OLD FRIEND QUIN THE WATER MAGE.\nHE HAS BEEN MISSING FOR WEEKS", ["SAY HELLO", 3],["ASK HIM WHERE ON EARTH HE HAS BEEN! THE WHOLE VILLAGE HAS BEEN LOOKING FOR HIM!",4]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["QUIN GREETS YOU CORDIALLY AND BEGINS HIS TALE", ["CONTINUE", 5]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["QUIN SHUSHES YOU AND BEGINS HIS TALE", ["CONTINUE", 5]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["'A MONTH AGO WHEN THE GREAT FOUNTAIN BROKE AND THE FLOW OF WATER STOPPED,\nI STARTED RESEARCHING EVERYTHING ABOUT THE ANCIENT OBJECT'", ["CONTINUE", 6]])
    temp_data["EncounterData"]["Dialogue"].append(
        ["'AS YOU HAVE NO DOUBT REALISED BY NOW, THIS TRAGEDY IS NO SIMPLE TRIFLE.\nSPEED WAS OF THE UTMOST IMPORTANCE, PEOPLE WERE ALREADY BEGINNING TO GO THIRSTY'",
            ["CONTINUE", 7]])
    temp_data["EncounterData"]["Dialogue"].append([
            "'SO, AS TIME WAS OF THE ESSENCE, I RAN TO THE GREAT LIBRARY\nAND SPENT A MONTH THERE RESEARCHING THIS PHENOMENON WHEN I FOUND THIS;'",
            ["LOOK CLOSER AT THE OBJECT HE IS HOLDING", 8],["ASK HIM TO GET TO THE POINT ALREADY",9]])
    temp_data["EncounterData"]["Dialogue"].append([
        "YOU SEE A BOOK WITH THE TITLE 'AQA REVISION GUIDE TO FOUNTAIN REPAIR' BRANDED ACROSS THE FRONT",
        ["ASK HIM TO CONTINUE WITH HIS TALE", 10], ["ASK HIM TO GET TO THE POINT ALREADY", 9]])
    temp_data["EncounterData"]["Dialogue"].append([
        "HE LOOKS AT YOU WITH A SLIGHTLY HURT EXPRESSION, AND THEN PROCEEDS TO GET TO THE POINT",
        ["PHEW", 10]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'ANYWAY, IN THIS BOOK IT STATES THAT TO REPAIR THE GREAT FOUNTAIN INSIDE THE PYRAMID OF LIFE,\nONE MUST COLLECT 4 JIGSAW PIECES AND COMBINE THEM'",
        ["ASK HIM WHERE THESE JIGSAW PIECES ARE", 11]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL, TURNS OUT THE LOCATIONS OF THE JIGSAW PIECES WASN'T PART OF THE AQA SPEC,\nBUT LUCKILY THEY HAD IT IN THIS MORE COMPREHENSIVE RESOURCE NAMED 'WIKIPEDIA''",
        ["REPEAT YOUR QUESTION", 12]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'OKAY, OKAY. THEY ARE HERE, HERE, HERE AND HERE.' HIS FINGER JABS AT TO PAGES SEEMINGLY RANDOMLY\nALL AROUND THE EDGES OF THE DESERT",
        ["ASK HIM WHY HE HASN'T ALREADY REPAIRED THE FOUNTAIN", 13],["ASK WHY HE CAME TO YOU",13]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL...' HE LOOKS EMBARRASSED 'I WENT TO THE LOCATION AND WAS MET WITH A FEARSOME TROLL,\nWHO WAS NOT IN THE MOOD TO GIVE HIS PRECIOUS SHINY JIGSAW PIECE AWAY'",
        ["ASK HIM IF HE EXPECTS YOU TO HELP",14]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL... I SUPPOSE... WELL YES, TO BE FRANK, I WAS CONSIDERING SETTING UP A GUILD'",
        ["SAY THAT SOUNDS LIKE A GREAT IDEA", 15],["SAY THAT SOUNDS LIKE A WASTE OF TIME, EFFORT AND MONEY",15]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'WELL, IN FACT, I ALREADY HAVE. I NAMED IT THE LEAGUE OF DOWSERS! I HAVE NO CHANCE OF PAYING OFF\nMY MAGI UNI DEBT NOW, BUT I THINK IT WAS WORTH IT, THAT IS, IF YOU WERE TO JOIN IT WOULD BE'",
        ["SAY THAT YOU WOULD BE HAPPY TO JOIN IN ON HIS QUEST", 16], ["ASK WHAT'S IN IT FOR YOU", 17]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'HURRAY! LET'S GO COLLECT SOME JIGSAW PIECES AND SAVE THE WORLD!' (QUIN WILL BE IN THE GUILD HALL,\nGO TO THE GUILD HALL IN THE VILLAGE TO GET HIM IN YOUR PARTY)",
        ["EXIT", -1, ["GuildHall",Character("Quin", 1, 4, 8, 4, 12, 12, 10, [["Magical", "Ranged", 5]])]]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'NOT HAVING TO LIVE IN A DESERT@ NOT HAVING TO WORRY EVERY DAY\nIF THE SHIPMENTS OF WATER SUPPLIES HAVE GOTTEN LOST@ BEING A HERO@'",
        ["AGREE AND JOIN", 16],["DECLARE THAT YOU ARE STILL NOT CONVINCED",18]])
    temp_data["EncounterData"]["Dialogue"].append([
        "'OKAY, YOU HAVE PUSHED ME THIS FAR, THAT'S IT. TIME TO BREAK THE FOURTH WALL;\nLOOK, YOU STARTED THIS GAME, IF YOU DIDN'T WANT TO PLAY IT, WHY DID THE HELL YOU CLICK RUN@'",
        ["AGREE AND JOIN (THIS IS THE ONLY OPTION, YOU TERRIBLE PERSON)", 16]])
    save_data, temp_data = init_encounter(save_data, temp_data)

    temp_data["EncounterContent"] = {}

    temp_data["EncounterContent"][4] = {}
    temp_data["EncounterContent"][4]["Type"] = "Dialogue"
    temp_data["EncounterContent"][4]["Background"] = "Town2"
    temp_data["EncounterContent"][4]["Character"] = "None"
    temp_data["EncounterContent"][4]["Dialogue"] = []
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF NIBIRU", ["SHOPS", 1, ["Background", "Town"]], ["GUILD HALL", 2], ["TAVERN", 3],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["'WELCOME ADVENTURER, TO MY HUMBLE STORE, TAKE A LOOK AT MY GOODS;'", ["TAKE A LOOK",-2],["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["YOU ENTER YOUR GUILD HALL, HERE YOU CAN ADD AND SWAP PARTY MEMBERS", ["ADD MEMBER", -3],["SWAP MEMBER",-4]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["YOU ENTER THE TAVERN, YOU CAN REST HERE FOR 60 GOLD RECOVERING ALL HEALTH, STAMINA AND MANA\nOR TRY YOUR LUCK AT CARDS",["REST", -5],["GAMBLE",-7], ["GO BACK", 0]])
    temp_data["EncounterContent"][4]["Dialogue"].append(
        ["SKILL CHECKS ARE STILL A WORK IN PROGRESS",
            ["GO BACK", 0]])

    temp_data["EncounterContent"][8] = {}
    temp_data["EncounterContent"][8]["Type"] = "Dialogue"
    temp_data["EncounterContent"][8]["Background"] = "WaterfallDried"
    temp_data["EncounterContent"][8]["Character"] = "None"
    temp_data["EncounterContent"][8]["Dialogue"] = []
    temp_data["EncounterContent"][8]["Dialogue"].append(
        ["YOU FIND A FOUNTAIN (WIP)",
         ["LEAVE", -1]])

    temp_data["EncounterContent"][1] = {}
    temp_data["EncounterContent"][1]["Type"] = "Dialogue"
    temp_data["EncounterContent"][1]["Background"] = "WaterfallDried"
    temp_data["EncounterContent"][1]["Character"] = "None"
    temp_data["EncounterContent"][1]["Dialogue"] = []
    temp_data["EncounterContent"][1]["Dialogue"].append(
        ["YOU FIND A FOUNTAIN (WIP)",
         ["LEAVE", -1]])

    temp_data["EncounterContent"][5] = {}
    temp_data["EncounterContent"][5]["Type"] = "Dialogue"
    temp_data["EncounterContent"][5]["Background"] = "WaterfallDried"
    temp_data["EncounterContent"][5]["Character"] = "Garik"
    temp_data["EncounterContent"][5]["Dialogue"] = []
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["YOU SEE A SHIRTLESS, TRIBAL LOOKING MAN LOOKING UP AT A GAP IN THE CLIFFSIDE",
            ["APPROACH HIM", 1], ["WALK AWAY AND FIND ANOTHER ROUTE AROUND", -1,["StoryProgress",5,"Done"]]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["THE MAN SHOWS NO REACTION TO YOUR APPROACH, BUT SUDDENLY A DEEP, POWERFUL VOICE SOUNDS",
         ["LISTEN", 2]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["'STRANGER, I DON'T KNOW YOUR NAME, I DON'T KNOW YOUR BACKGROUND, I DON'T YOU PASSIONS AND OR YOUR HATES,\nBUT THAT IS OF NO CONSEQUENCE, THE SPIRITS TOLD BE YOU WOULD COME, AND THAT YOU WOULD BE OUR SAVIOUR'",
         ["ASK HIM WHAT HE MEANS", 3],["RUN AWAY FROM THIS MADMAN, BEFORE YOU GET HURT",-1,["StoryProgress",5,"Done"]]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["'THE FACT YOU HAVE NOT ALREADY FLED IS PROOF ENOUGH FOR ME THAT YOU ARE WORTHY, I WILL JOIN YOU ON THIS QUEST'",
         ["SAY YOU WILL MEET HIM BACK AT THE GUILD HALL", -1,["StoryProgress",5,"Done"],["GuildHall", Character("Garik",1,12,14,2,8,10,4,[["Physical","Melee",5]])]],["REFUSE HIS OFFER",6]])
    temp_data["EncounterContent"][5]["Dialogue"].append(
        ["'YOU ARE MAKING A GRAVE MISTAKE' THE MAN SUDDENLY JUMPS OUT OF SIGHT BETWEEN THE CREVICES IN THE CLIFFS, HE IS GONE",
            ["LEAVE", -1,["StoryProgress",5,"Done"]]])

    temp_data["EncounterContent"][2] = {}
    temp_data["EncounterContent"][2]["Type"] = "Dialogue"
    temp_data["EncounterContent"][2]["Background"] = "ForestDried"
    temp_data["EncounterContent"][2]["Character"] = "Loran"
    temp_data["EncounterContent"][2]["Dialogue"] = []
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["YOU FIND AN ELF, RARE IN THESE PARTS, KNEELING BY A DEAD SAPLING,\nKILLED BY THE HARSH SUN AND LACK OF WATER",
         ["APPROACH HIM", 1], ["WALK AWAY, YOU DON'T TRUST ELVES", -1, ["StoryProgress", 2, "Done"]]])
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["YOU WALK QUIETLY, BUT HIS EARS PICK YOU UP FROM METERS AWAY,\n'THIS WOULD HAVE GROWN INTO A HUGE, BEAUTIFUL OAK, IF IT HAD TIME TO FLOURISH'",
         ["NOD", 3], ["SAY THAT YOU DON'T GIVE A DAMN ABOUT TREES, ITS PEOPLE THAT MATTER", 2]])
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["'AYE, YOU'RE HALF-RIGHT, BUT WHERE WOULD YOU BE WITHOUT THE FIELDS THAT FEED YOU,\nTHE WOOD THAT SUPPORTS YOUR ROOF@'",
         ["CONTINUE", 3]])
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["'ANYWAY, A LITTLE BIRD TOLD ME YOU ARE THE ONLY ONE TRYING TO FIX THIS MESS,\nNOW YOU DON'T LOOK LIKE MUCH TO ME, BUT BEGGARS CAN'T BE CHOOSERS'",
            ["LET HIM CONTINUE", 5],["RETORT THAT ALL ELVES ARE DAMN BEGGARS, LIVING OF THE WEALTH OF HONEST WORK", 4]])
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["'OH, SO YOU'RE JUST LIKE THE OTHER HUMANS. I SUPPOSE I'M A FOOL FOR THINKING OTHERWISE, FAREWELL'\nHE VANISHES",
            ["LEAVE", -1, ["StoryProgress", 2, "Done"]]])
    temp_data["EncounterContent"][2]["Dialogue"].append(
        ["'SO, QUITE FRANKLY, I WANT TO JOIN YOU, HELP YOU IN YOUR STRUGGLE,I WON'T TAKE PLEASURE IN WORKING\nWITH YOU HUMANS, BUT THE ENEMY OF MY ENEMY IS MY FRIEND OR SO THEY SAY'",
            ["SAY YOU WILL MEET HIM BACK AT THE GUILD HALL", -1,["StoryProgress",2,"Done"],["GuildHall", Character("Loran",1,8,6,14,8,8,6,[["Physical","Melee",4],["Physical","Ranged",4]])]],
            ["SAY THAT YOU DON'T WANT ANY DAMN THIEVING ELVES IN YOUR PARTY", 4]])

    temp_data["EncounterContent"][0] = {}
    temp_data["EncounterContent"][0]["Type"] = "Dialogue"
    temp_data["EncounterContent"][0]["Background"] = "EncounterBack"
    temp_data["EncounterContent"][0]["Character"] = "Turncoat"
    temp_data["EncounterContent"][0]["Dialogue"] = []
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["YOU FIND A GOBLIN AND PREPARE TO ATTACK WHEN SUDDENLY, IT DROPS IT'S WEAPON ON THE GROUND",
         ["DROP YOUR WEAPON AND APPROACH", 1], ["KEEP YOUR WEAPON AT THE READY AND APPROACH", 2], ["ATTACK",3]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["THE GOBLIN SQUEAKS AND SQUEALS IN INCOMPREHENSIBLE SYLLABLES AND THE OFFERS ITS HAND",
         ["SHAKE ITS HAND", 4],["RUN AWAY", -1, ["StoryProgress", 0, "Done"]]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["THE GOBLIN SQUEALS AND FURIOUSLY POINTS AT YOUR WEAPON AND THEN TO THE GROUND",
         ["DROP YOUR WEAPON", 1], ["KEEP HOLDING IT AND MOVE FORWARDS", 5, ],["ATTACK", 3]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["YOU KILL THE GOBLIN QUICKLY AT TAKE A LARGE SATCHEL OF 100 GOLD OF ITS CORPSE",
         ["LEAVE", -1,["StoryProgress", 0, "Done"], ["Inventory","Gold",100]]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["THE GOBLIN SHAKES IT THOROUGHLY AND THEN RUNS OFF TOWARDS YOUR GUILD HALL",
         ["YOU GUESS YOU WILL FIND HIM AGAIN THERE", -1, ["StoryProgress", 0, "Done"],["GuildHall", Character("Turncoat",1,8,8,16,6,6,6,[["Physical","Melee",5]])]]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["AS YOU APPROACH, THE GOBLIN GETS MORE AND MORE FRUSTRATED AND\n   IT'S POINTING GETS MORE AND MORE FRANTIC",
         ["DROP YOUR WEAPON", 1], ["KEEP WALKING AND GRIP YOUR WEAPON TIGHTER",6]])
    temp_data["EncounterContent"][0]["Dialogue"].append(
        ["THE GOBLIN CAN'T TAKE IT ANYMORE, THEY JUMP AWAY SEEMINGLY INTO THIN AIR",
         ["LEAVE", -1, ["StoryProgress", 0, "Done"]]])

    temp_data["EncounterContent"][7] = {}
    temp_data["EncounterContent"][7]["Type"] = "Dialogue"
    temp_data["EncounterContent"][7]["Background"] = "WaterfallDried"
    temp_data["EncounterContent"][7]["Character"] = "Grungeldelf"
    temp_data["EncounterContent"][7]["Dialogue"] = []
    temp_data["EncounterContent"][7]["Dialogue"].append(
        ["YOU ARE WALKING ACROSS THE DESERT WHEN YOU FIND A VERY SHORT INDIVIDUAL WITH A VERY LARGE CROSSBOW",
         ["GREET HIM", 1], ["THAT CROSSBOW LOOKS INTIMIDATING, RUN AWAY", -1]])
    temp_data["EncounterContent"][7]["Dialogue"].append(
        ["''ELLO STRANGER, YOUR THE FIRST PERSON I HAVE SEEN WHO AIN'T A BLINKIN' GOBLIN OR ORC'",
         ["ASK WHAT A DWARF IS DOING HERE", 2], ["MENTION THAT HE SEEMS A LITTLE OUT OF PLACE HIMSELF IN THE DESERT", 2]])
    temp_data["EncounterContent"][7]["Dialogue"].append(
        ["'WELL YA SEE LADDY, THAT'S THE THING, THIS BLASTED DROUGHT HAS DONE WEIRD THINGS WITH THE\nWEATHER AND NOW MY PATH HOME TO THE FROSTBACKS IS FROZEN OVER'",
         ["MENTION THAT YOU ARE PART OF A GUILD SET UP TO FIX THIS MESS", 3],
         ["SAY HOW THAT'S VERY SAD AND THEN GO ON YOUR WAY", -1]])
    temp_data["EncounterContent"][7]["Dialogue"].append(
        ["'OH REALLY, TELL YA WHAT. I THINK I'LL JOIN MYSELF, GET TA' KILL SOME OF THEM DAMN GOBLINS AND\nGET BACK HOME AT THE SAME TIME!'",
            ["SAY YOU'LL MEET HIM BACK AT THE GUILD HALL", -1, ["StoryProgress", 7, "Done"],["GuildHall", Character("Grungeldelf",1,12,10,12,4,6,6,[["Physical","Ranged",5]])]],
            ["SAY THAT, ON SECOND THOUGHT, YOU DON'T REALLY WANT A DWARF IN YOUR PARTY", -1]])

    temp_data["EncounterContent"][6] = {}
    temp_data["EncounterContent"][6]["Type"] = "Dialogue"
    temp_data["EncounterContent"][6]["Background"] = "Town2"
    temp_data["EncounterContent"][6]["Character"] = "None"
    temp_data["EncounterContent"][6]["Dialogue"] = []
    temp_data["EncounterContent"][6]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF LEDONIA", ["SHOPS", 1, ["Background", "Town"]], ["TAVERN", 2],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][6]["Dialogue"].append(
        ["'WELCOME ADVENTURER, TO MY HUMBLE STORE, TAKE A LOOK AT MY GOODS;'", ["TAKE A LOOK", -2],
         ["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][6]["Dialogue"].append(
        [
            "YOU ENTER THE TAVERN, YOU CAN REST HERE FOR 60 GOLD RECOVERING ALL HEALTH, STAMINA AND MANA\nOR TRY YOUR LUCK AT CARDS",
            ["REST", -5], ["GAMBLE", -7], ["GO BACK", 0]])

    temp_data["EncounterContent"][3] = {}
    temp_data["EncounterContent"][3]["Type"] = "Dialogue"
    temp_data["EncounterContent"][3]["Background"] = "Town2"
    temp_data["EncounterContent"][3]["Character"] = "None"
    temp_data["EncounterContent"][3]["Dialogue"] = []
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["WELCOME TO THE VILLAGE OF QUINTUSINHORTO", ["SHOPS", 1, ["Background", "Town"]], ["TAVERN", 2],
         ["LEAVE", -1]])
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["'WELCOME ADVENTURER, TO MY HUMBLE STORE, TAKE A LOOK AT MY GOODS;'", ["TAKE A LOOK", -2],
         ["GO BACK", 0, ["Background", "Town2"]]])
    temp_data["EncounterContent"][3]["Dialogue"].append(
        ["YOU ENTER THE TAVERN, YOU CAN REST HERE FOR 60 GOLD RECOVERING ALL HEALTH, STAMINA AND MANA\nOR TRY YOUR LUCK AT CARDS",
            ["REST", -5], ["GAMBLE", -7], ["GO BACK", 0]])

    temp_data["EnemyNPCs"]={}
    temp_data["EnemyNPCs"]["Goblin"]=Character("Goblin", 1, 8, 4, 10, 2, 2, 6, [["Physical", "Melee", 3]])
    temp_data["EnemyNPCs"]["GoblinArcher"] = Character("GoblinArcher", 2, 10, 5, 12, 2, 2, 6, [["Physical", "Ranged", 4]])
    temp_data["EnemyNPCs"]["Orc"] = Character("Orc", 3, 14, 14, 6, 2, 2, 2, [["Physical", "Melee", 5]])
    temp_data["EnemyNPCs"]["RedGoblin"] = Character("WeirdGoblin", 6,  12, 6, 16, 10, 5, 6, [["Physical", "Melee", 8]])
    temp_data["EnemyNPCs"]["RedGoblinArcher"] = Character("WeirdGoblinArcher", 6,  14, 6, 18, 10, 6, 6,[["Physical", "Ranged", 9]])
    temp_data["EnemyNPCs"]["RedOrc"] = Character("WeirdOrc", 8, 18, 18, 10, 8, 8, 5, [["Physical", "Melee", 10]])
    temp_data["EnemyNPCs"]["Boss1"] = Character("Troll", 3, 10, 10, 10, 10, 10, 10, [["Physical", "Melee", 5]])
    temp_data["EnemyNPCs"]["Boss2"] = Character("Golem", 5, 12, 12, 12, 12, 12, 12, [["Physical", "Melee", 7]])
    temp_data["EnemyNPCs"]["Boss3"] = Character("Orb", 7, 14, 14, 14, 14, 14, 14, [["Physical", "Melee", 8],["Magical", "Ranged", 8]]) #2 attacks so 8 instead of 9
    temp_data["EnemyNPCs"]["Boss4"] = Character("Slime", 8, 16, 16, 16, 16, 16, 16, [["Magical", "Ranged", 10]])
    temp_data["EnemyNPCs"]["Boss5"] = Character("Dragon", 10, 20, 20, 20, 20, 20, 20, [["Magical", "Ranged", 10],["Physical","Melee",10]]) #2 attacks so 10 instead of 12

    temp_data["EncounterContent"]["Jigsaw"]=[]
    temp_data["EncounterContent"]["Jigsaw"].append({})
    temp_data["EncounterContent"]["Jigsaw"][0]["Type"] = "Battle"
    temp_data["EncounterContent"]["Jigsaw"][0]["EnemyParty"] = []
    temp_data["EncounterContent"]["Jigsaw"][0]["EnemyParty"].append(copy.deepcopy(temp_data["EnemyNPCs"]["Boss1"]))

    temp_data["EncounterContent"]["Jigsaw"].append({})
    temp_data["EncounterContent"]["Jigsaw"][1]["Type"] = "Battle"
    temp_data["EncounterContent"]["Jigsaw"][1]["EnemyParty"] = []
    temp_data["EncounterContent"]["Jigsaw"][1]["EnemyParty"].append(copy.deepcopy(temp_data["EnemyNPCs"]["Boss2"]))

    temp_data["EncounterContent"]["Jigsaw"].append({})
    temp_data["EncounterContent"]["Jigsaw"][2]["Type"] = "Battle"
    temp_data["EncounterContent"]["Jigsaw"][2]["EnemyParty"] = []
    temp_data["EncounterContent"]["Jigsaw"][2]["EnemyParty"].append(copy.deepcopy(temp_data["EnemyNPCs"]["Boss3"]))

    temp_data["EncounterContent"]["Jigsaw"].append({})
    temp_data["EncounterContent"]["Jigsaw"][3]["Type"] = "Battle"
    temp_data["EncounterContent"]["Jigsaw"][3]["EnemyParty"] = []
    temp_data["EncounterContent"]["Jigsaw"][3]["EnemyParty"].append(copy.deepcopy(temp_data["EnemyNPCs"]["Boss4"]))

    temp_data["EncounterContent"]["Jigsaw"].append({})
    temp_data["EncounterContent"]["Jigsaw"][4]["Type"] = "Battle"
    temp_data["EncounterContent"]["Jigsaw"][4]["EnemyParty"] = []
    temp_data["EncounterContent"]["Jigsaw"][4]["EnemyParty"].append(copy.deepcopy(temp_data["EnemyNPCs"]["Boss5"]))

    temp_data["EncounterContent"]["Empty"] = {}
    temp_data["EncounterContent"]["Empty"]["Type"] = "Dialogue"
    temp_data["EncounterContent"]["Empty"]["Background"] = "EncounterBack"
    temp_data["EncounterContent"]["Empty"]["Character"] = "None"
    temp_data["EncounterContent"]["Empty"]["Dialogue"] = []
    temp_data["EncounterContent"]["Empty"]["Dialogue"].append(
        ["THERE IS NOTHING HERE BUT SAND, SAND AND ROCKS", ["LEAVE", -1]])

    temp_data["PositionData"] = []
    temp_data["PositionData"].append([[43, 125], [-1, 2, 3, 11]])  # Links are done up down left right -1 means no link
    temp_data["PositionData"].append([[122, 229], [-1, -1, 2, 12]])
    temp_data["PositionData"].append([[144, 152], [1, 4, 3, 0]])
    temp_data["PositionData"].append([[173, 40], [2, -1, -1, 0]])
    temp_data["PositionData"].append([[224, 229], [-1, 5, -1, 2]])
    temp_data["PositionData"].append([[319, 184], [-1, 8, 7, 4]])
    temp_data["PositionData"].append([[321, 22], [7, 10, -1, -1]])
    temp_data["PositionData"].append([[365, 104], [5, 8, 6, -1]])
    temp_data["PositionData"].append([[394, 162], [-1, 9, 7, 5]])

    temp_data["PositionData"].append([[435, 230], [-1, -1, 8, 8]])
    temp_data["PositionData"].append([[435, 30], [-1, -1, -1, 6]])
    temp_data["PositionData"].append([[28, 30], [0, 0,  -1, -1]])
    temp_data["PositionData"].append([[28, 230], [-1, 1, -1, -1]])
    temp_data["AnimateTick"] = 0
    temp_data["Moving"] = [False, 0, 0]
    save_data["Encounters"] = []
    temp_data["Airships"] = []
    to_delete = []
    for i in range(0, 6):
        save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
        while save_data["Encounters"][i][1] == -1 :
            save_data["Encounters"][i][1] = random.choice(temp_data["PositionData"][save_data["Encounters"][i][0]][1])
        for i2 in range(0, i):
            if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                to_delete.append(i)
    for i in range(0, len(to_delete)):
        if len(save_data["Encounters"])>0:
            save_data["Encounters"].pop(to_delete[i] - i)
        else:
            print("ERROR - UNKNOWN")
    return save_data, temp_data


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
            self.Images[Image[:-4]] = pygame.image.load(r"Images\{0}".format(Image)).convert_alpha()
            self.Images[Image[:-4]] = pygame.transform.scale(self.Images[Image[:-4]],
                                                             (self.Images[Image[:-4]].get_size()[0] * self.ResRatio[0],
                                                              self.Images[Image[:-4]].get_size()[1] * self.ResRatio[1]))

    def place_image(self, image_id, x, y, *x_flip):
        if x_flip == ():
            x_flip = False
        if image_id in self.Images.keys():
            y = self.GameRes[1] - y - (self.Images[image_id].get_size()[1] / self.ResRatio[1])
            if x_flip:
                self.Window.blit(pygame.transform.flip(self.Images[image_id], True, False), (int(x) * self.ResRatio[0],
                                                                                             int(y) * self.ResRatio[1]))
            else:
                self.Window.blit(self.Images[image_id],
                                 (int(x) * self.ResRatio[0], int(y) * self.ResRatio[1]))
        else:
            print(
                "ERROR: Image " + image_id + " has not been loaded. Make sure you have placed the image in the images "
                                             "folder and spelt the file name correctly.")

    def place_text(self, text, x, y):
        x2 = x
        for Letter in text:
            if Letter in self.Images.keys():
                y2 = self.GameRes[1] - y - (self.Images[Letter].get_size()[1] / self.ResRatio[1])
                self.Window.blit(self.Images[Letter], (round(x2) * self.ResRatio[0], round(y2) * self.ResRatio[1]))
                x2 += (self.Images[Letter].get_size()[0] / self.ResRatio[0]) + 1
            elif Letter == "\n":
                y += -6
                x2 = x
            elif Letter == " ":
                x2 += 4
            else:
                print(
                    "ERROR: Character " + Letter + " has not been loaded. Make sure the character is "
                                                   "present in the images folder.")

    def place_rectangle(self, colour, x, y, width, height):
        y = self.GameRes[1] - y - height
        pygame.draw.rect(self.Window, colour,
                         (int(x) * self.ResRatio[0], int(y) * self.ResRatio[1], int(width) * self.ResRatio[0],
                          int(height) * self.ResRatio[1]))

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
            self.Sounds[Sound[:-4]] = pygame.mixer.Sound(r"Sounds\{0}".format(Sound))

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


class Character:
    def __init__(self, name, level, strength, constitution, dexterity, intelligence, wisdom, charisma, attacks):
        self.name = name
        self.level = level
        self.exp=0
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.attacks = attacks
        # Initialises variables to be set in update_stats to prevent pycharm from having a fit
        self.mods = {}
        self.health_max = 0
        self.dodge_bonus = 0
        self.attack_bonus = 0
        self.spell_bonus = 0
        self.stamina_max = 0
        self.stamina_regen = 0
        self.mana_max = 0
        self.mana_regen = 0
        self.health_current = 0
        self.stamina_current = 0
        self.mana_current = 0
        self.initiative_bonus=0
        self.unspent_points=0
        self.level_up()

    def level_up(self):
        self.mods = {"Strength": self.strength / 4,
                     "Constitution": self.constitution / 4,
                     "Dexterity": self.dexterity / 4,
                     "Intelligence": self.intelligence / 4,
                     "Wisdom": self.wisdom / 4,
                     "Charisma": self.charisma / 4}
        self.health_max = int(self.mods["Constitution"] + 10 + (self.mods["Constitution"] + 5) * (self.level - 1))
        self.dodge_bonus = int(self.mods["Dexterity"] * 7)
        self.attack_bonus = int((self.mods["Dexterity"] * 5)+(self.mods["Strength"] * 2))
        self.spell_bonus = int((self.mods["Charisma"] * 5)+(self.mods["Intelligence"] * 2))
        self.stamina_max = int(self.level * 10 + self.mods["Strength"] * 5)
        self.stamina_regen = int(self.level + self.mods["Constitution"] * 2)
        self.mana_max = int(self.level * 10 + self.mods["Wisdom"] * 5)
        self.mana_regen = int(self.level + self.mods["Intelligence"] * 2)
        self.health_current = self.health_max
        self.stamina_current = self.stamina_max
        self.mana_current = self.mana_max
        self.initiative_bonus=int(self.mods["Dexterity"]*5+self.mods["Charisma"]*2)

    def increase_stats(self):
        self.mods = {"Strength": self.strength / 4,
                     "Constitution": self.constitution / 4,
                     "Dexterity": self.dexterity / 4,
                     "Intelligence": self.intelligence / 4,
                     "Wisdom": self.wisdom / 4,
                     "Charisma": self.charisma / 4}
        self.health_max = int(self.mods["Constitution"] + 10 + (self.mods["Constitution"] + 5) * (self.level - 1))
        self.dodge_bonus = int(self.mods["Dexterity"] * 7)
        self.attack_bonus = int((self.mods["Dexterity"] * 5) + (self.mods["Strength"] * 2))
        self.spell_bonus = int((self.mods["Charisma"] * 5) + (self.mods["Intelligence"] * 2))
        self.stamina_max = int(self.level * 10 + self.mods["Strength"] * 5)
        self.stamina_regen = int(self.level + self.mods["Constitution"] * 2)
        self.mana_max = int(self.level * 10 + self.mods["Wisdom"] * 5)
        self.mana_regen = int(self.level + self.mods["Intelligence"] * 2)
        self.initiative_bonus = int(self.mods["Dexterity"] * 5 + self.mods["Charisma"] * 2)

    def check_for_level_up(self):
        if self.exp>=100*self.level:
            self.unspent_points+=5
            self.exp=0
            self.level+=1
            self.level_up()
def save(data):
    _pickle.dump(data, open(r"Saves\SaveFile.sav", "wb"))


def load():
    for SaveFile in os.listdir("Saves"):
        save_data = _pickle.load(open(r"Saves\{0}".format(SaveFile), "rb"))
        return save_data
    print("ERROR: save file not present")
    return "ERROR"


def overworld(screen, mixer, save_data, temp_data):
    temp_data["ActiveScreen"] = "Overworld"
    temp_data["EncounterData"] = None
    if save_data["StoryProgress"]["JigsawPieces"]<4:
        screen.place_image("Map", 0, 0)
    else:
        if len(temp_data["PositionData"])==13:
            temp_data["PositionData"].append([[231, 128], [-1, -1, -1, -1]])
            temp_data["PositionData"][3][1][1] = 13
            temp_data["PositionData"][6][1][3] = 13
    if not temp_data["Moving"][0]:
        screen.place_image("Flag2", temp_data["PositionData"][save_data["Position"]][0][0],
                           temp_data["PositionData"][save_data["Position"]][0][1])
        input_keys = pygame.key.get_pressed()
        if input_keys[pygame.K_w] and not (temp_data["PositionData"][save_data["Position"]][1][0] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][0]
        elif input_keys[pygame.K_d] and not (temp_data["PositionData"][save_data["Position"]][1][1] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][1]
        elif input_keys[pygame.K_s] and not (temp_data["PositionData"][save_data["Position"]][1][2] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][2]
        elif input_keys[pygame.K_a] and not (temp_data["PositionData"][save_data["Position"]][1][3] == -1):
            mixer.play_sound("ExampleSound", 0)
            temp_data["Moving"][0] = True
            temp_data["Moving"][1] = temp_data["PositionData"][save_data["Position"]][1][3]
        elif input_keys[pygame.K_SPACE]:
            mixer.play_sound("ExampleSound", 0)
            try:
                if not save_data["Position"] in save_data["StoryProgress"].keys():
                    temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"][save_data["Position"]])
                    save_data, temp_data = init_encounter(save_data, temp_data)
                elif not save_data["StoryProgress"][save_data["Position"]]=="Done":
                    temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"][save_data["Position"]])
                    save_data, temp_data = init_encounter(save_data, temp_data)
                else:
                    temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"]["Empty"])
                    save_data, temp_data = init_encounter(save_data, temp_data)
            except KeyError:
                if save_data["Position"]==9 or save_data["Position"]==10 or save_data["Position"]==11 or save_data["Position"]==12 or save_data["Position"]==13:
                    if not save_data["Position"] in save_data["StoryProgress"].keys():
                        temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"]["Jigsaw"][save_data["StoryProgress"]["JigsawPieces"]])
                        print(save_data["StoryProgress"]["JigsawPieces"])
                        save_data, temp_data = init_encounter(save_data, temp_data)
                        save_data["StoryProgress"]["JigsawPieces"] += 1
                        save_data["Inventory"]["Jigsaw Pieces"] += 1
                        save_data["StoryProgress"][save_data["Position"]] = "Done"
                        save_data["Encounters"]=[]
                        to_delete = []
                        for i in range(0, 6):
                            save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
                            while save_data["Encounters"][i][1] == -1:
                                save_data["Encounters"][i][1] = random.choice(
                                    temp_data["PositionData"][save_data["Encounters"][i][0]][1])
                            for i2 in range(0, i):
                                if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                                    to_delete.append(i)
                        for i in range(0, len(to_delete)):
                            if len(save_data["Encounters"]) > 0:
                                save_data["Encounters"].pop(to_delete[i] - i)
                            else:
                                print("ERROR - UNKNOWN")
                    elif not save_data["StoryProgress"][save_data["Position"]] == "Done":
                        temp_data["EncounterData"] = copy.deepcopy(
                            temp_data["EncounterContent"]["Jigsaw"][save_data["StoryProgress"]["JigsawPieces"]])
                        print(save_data["StoryProgress"]["JigsawPieces"])
                        save_data, temp_data = init_encounter(save_data, temp_data)
                        save_data["StoryProgress"]["JigsawPieces"] += 1
                        save_data["Inventory"]["Jigsaw Pieces"] += 1
                        save_data["StoryProgress"][save_data["Position"]] = "Done"
                        save_data["Encounters"] = []
                        to_delete = []
                        for i in range(0, 6):
                            save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
                            while save_data["Encounters"][i][1] == -1:
                                save_data["Encounters"][i][1] = random.choice(
                                    temp_data["PositionData"][save_data["Encounters"][i][0]][1])
                            for i2 in range(0, i):
                                if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                                    to_delete.append(i)
                        for i in range(0, len(to_delete)):
                            if len(save_data["Encounters"]) > 0:
                                save_data["Encounters"].pop(to_delete[i] - i)
                            else:
                                print("ERROR - UNKNOWN")
                    else:
                        temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"]["Empty"])
                        save_data, temp_data = init_encounter(save_data, temp_data)
                else:
                    print("ERROR: NO ENCOUNTER AT POSITION "+str(save_data["Position"]))
        elif input_keys[pygame.K_i]:
            temp_data["ActiveScreen"] = "Inventory"
            temp_data["UIPos"]=0
            temp_data["Selection"]={}
            while input_keys[pygame.K_i]:
                screen.update()
                input_keys = pygame.key.get_pressed()
        elif input_keys[pygame.K_ESCAPE]:
            temp_data["ActiveScreen"] = "Settings"
            while input_keys[pygame.K_ESCAPE]:
                screen.update()
                input_keys = pygame.key.get_pressed()
    else:
        if temp_data["Moving"][2] == 30:
            save_data["Position"] = temp_data["Moving"][1]
            temp_data["Moving"] = [False, 0, 0]
            try:
                if not save_data["Position"] in save_data["StoryProgress"].keys():
                    temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"][save_data["Position"]])
                    save_data, temp_data = init_encounter(save_data, temp_data)
                elif not save_data["StoryProgress"][save_data["Position"]] == "Done":
                    temp_data["EncounterData"] = copy.deepcopy(temp_data["EncounterContent"][save_data["Position"]])
                    save_data, temp_data = init_encounter(save_data, temp_data)
                else:
                    pass
            except KeyError:
                if save_data["Position"] == 9 or save_data["Position"] == 10 or save_data["Position"] == 11 or \
                        save_data["Position"] == 12 or save_data["Position"] == 13:
                    if not save_data["Position"] in save_data["StoryProgress"].keys():
                        temp_data["EncounterData"] = copy.deepcopy(
                            temp_data["EncounterContent"]["Jigsaw"][save_data["StoryProgress"]["JigsawPieces"]])
                        print(save_data["StoryProgress"]["JigsawPieces"])
                        save_data, temp_data = init_encounter(save_data, temp_data)
                        save_data["StoryProgress"]["JigsawPieces"] += 1
                        save_data["Inventory"]["Jigsaw Pieces"] += 1
                        save_data["StoryProgress"][save_data["Position"]] = "Done"
                        save_data["Encounters"] = []
                        to_delete = []
                        for i in range(0, 6):
                            save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
                            while save_data["Encounters"][i][1] == -1:
                                save_data["Encounters"][i][1] = random.choice(
                                    temp_data["PositionData"][save_data["Encounters"][i][0]][1])
                            for i2 in range(0, i):
                                if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                                    to_delete.append(i)
                        for i in range(0, len(to_delete)):
                            if len(save_data["Encounters"]) > 0:
                                save_data["Encounters"].pop(to_delete[i] - i)
                            else:
                                print("ERROR - UNKNOWN")
                    elif not save_data["StoryProgress"][save_data["Position"]] == "Done":
                        temp_data["EncounterData"] = copy.deepcopy(
                            temp_data["EncounterContent"]["Jigsaw"][save_data["StoryProgress"]["JigsawPieces"]])
                        print(save_data["StoryProgress"]["JigsawPieces"])
                        save_data, temp_data = init_encounter(save_data, temp_data)
                        save_data["StoryProgress"]["JigsawPieces"] += 1
                        save_data["Inventory"]["Jigsaw Pieces"] += 1
                        save_data["StoryProgress"][save_data["Position"]] = "Done"
                        save_data["Encounters"] = []
                        to_delete = []
                        for i in range(0, 6):
                            save_data["Encounters"].append([random.randint(0, len(temp_data["PositionData"]) - 1), -1])
                            while save_data["Encounters"][i][1] == -1:
                                save_data["Encounters"][i][1] = random.choice(
                                    temp_data["PositionData"][save_data["Encounters"][i][0]][1])
                            for i2 in range(0, i):
                                if save_data["Encounters"][i2] == save_data["Encounters"][i]:
                                    to_delete.append(i)
                        for i in range(0, len(to_delete)):
                            if len(save_data["Encounters"]) > 0:
                                save_data["Encounters"].pop(to_delete[i] - i)
                            else:
                                print("ERROR - UNKNOWN")
                    else:
                        pass
                else:
                    print("ERROR: NO ENCOUNTER AT POSITION " + str(save_data["Position"]))
        elif temp_data["Moving"][2]==15:
            for temp_encounter in save_data["Encounters"]:
                if temp_data["Moving"][1] in temp_encounter and save_data["Position"] in temp_encounter:
                    stat_target = 0
                    for character in save_data["Party"]:
                        stat_target += character.level
                    stat_target=stat_target
                    inaccuracy=0.25
                    stat_total = 0
                    while not int(stat_target/inaccuracy)==int(stat_total/inaccuracy):
                        temp_data["EncounterData"] = {}
                        temp_data["EncounterData"]["Type"] = "Battle"
                        temp_data["EncounterData"]["EnemyParty"] = []
                        temp_data["EncounterData"]["EnemyParty"].append(
                            copy.deepcopy(random.choice(list(temp_data["EnemyNPCs"].values())[:-5])))
                        if random.randint(0,1)==0:
                            temp_data["EncounterData"]["EnemyParty"].append(
                                copy.deepcopy(random.choice(list(temp_data["EnemyNPCs"].values())[:-5])))
                        if random.randint(0,1)==0:
                            temp_data["EncounterData"]["EnemyParty"].append(
                                copy.deepcopy(random.choice(list(temp_data["EnemyNPCs"].values())[:-5])))
                        stat_total = 0
                        for character in temp_data["EncounterData"]["EnemyParty"]:
                            stat_total += character.level
                        inaccuracy += 0.25
                    save_data, temp_data = init_encounter(save_data, temp_data)
                    save_data["Encounters"].remove(temp_encounter)
        if not temp_data["ActiveScreen"]=="Encounter" and temp_data["Moving"][0]:
            temp_data["Moving"][2] += 1
            screen.place_image("Flag2",
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][0] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][0] * (
                                        30 - temp_data["Moving"][2])) / 30,
                               (temp_data["PositionData"][temp_data["Moving"][1]][0][1] * (temp_data["Moving"][2]) +
                                temp_data["PositionData"][save_data["Position"]][0][1] * (
                                        30 - temp_data["Moving"][2])) / 30)
    for temp_encounter in save_data["Encounters"]:
        screen.place_image("Alert1", (temp_data["PositionData"][temp_encounter[0]][0][0] +
                                      temp_data["PositionData"][temp_encounter[1]][0][0]) / 2 - 1,
                           (temp_data["PositionData"][temp_encounter[0]][0][1] +
                            temp_data["PositionData"][temp_encounter[1]][0][1]) / 2 + 6 + math.sin(
                               temp_data["AnimateTick"] / 35) * -0.9)
        screen.place_image("Alert2", (temp_data["PositionData"][temp_encounter[0]][0][0] +
                                      temp_data["PositionData"][temp_encounter[1]][0][0]) / 2,
                           (temp_data["PositionData"][temp_encounter[0]][0][1] +
                            temp_data["PositionData"][temp_encounter[1]][0][1]) / 2)
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
    return save_data, temp_data


def init_encounter(save_data, temp_data):
    temp_data["ActiveScreen"] = "Encounter"
    if temp_data["EncounterData"]["Type"] == "Battle":
        temp_data["EncounterData"]["Turn"] = 0
        temp_data["EncounterData"]["UIPos"] = 0
        temp_data["EncounterData"]["Selection"] = {"Attack": 0, "Enemy": 0}
        temp_data["EncounterData"]["AttackAnimProg"] = 0
        temp_data["EncounterData"]["TurnOrder"]=[]
        temp_list=[]
        for character in save_data["Party"]:
            temp_list.append(character.initiative_bonus)
        for character in temp_data["EncounterData"]["EnemyParty"]:
            temp_list.append(character.initiative_bonus)
        used_list=[]
        while len(temp_data["EncounterData"]["TurnOrder"])<len(save_data["Party"])+len(temp_data["EncounterData"]["EnemyParty"]):
            maximum=[-1,0]
            for character_num in range(0,len(temp_list)):
                if temp_list[character_num]>maximum[0] and not (character_num in used_list):
                    maximum=[temp_list[character_num],character_num]
            temp_data["EncounterData"]["TurnOrder"].append(maximum[1])
            used_list.append(maximum[1])
        temp_data["EncounterData"]["TurnPos"]=0
        temp_data["EncounterData"]["Turn"] = temp_data["EncounterData"]["TurnOrder"][temp_data["EncounterData"]["TurnPos"]]
    elif temp_data["EncounterData"]["Type"] == "Dialogue":
        temp_data["PageNumber"] = 0
    return save_data, temp_data


def encounter(screen, mixer, save_data, temp_data):
    if temp_data["EncounterData"]["Type"] == "Battle":
        screen.place_image("EncounterBack", 0, 0)
        for i in range(len(save_data["Party"]) - 1, -1, -1):
            if not (temp_data["EncounterData"]["AttackAnimProg"] > 0 and temp_data["EncounterData"]["Turn"] == i):
                if not save_data["Party"][i].name == save_data["Name"]:
                    screen.place_image(save_data["Party"][i].name,
                                       i * 30 + 40,
                                       i * 60 + 40)
                else:
                    screen.place_image("Spellsword",
                                       i * 30 + 40,
                                       i * 60 + 40)
                offset = 0
                screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120, 48, 5)
                screen.place_rectangle((255, 0, 0), i * 30 + 40, i * 60 + 120, (save_data["Party"][i].health_current /
                                                                                save_data["Party"][i].health_max) * 48,
                                       5)
                offset += 6
                physical = False
                magical = False
                for Attack in save_data["Party"][i].attacks:
                    if "Physical" in Attack:
                        physical = True
                    elif "Magical" in Attack:
                        magical = True
                if physical:
                    screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 255, 0), i * 30 + 40, i * 60 + 120 - offset,
                                           (save_data["Party"][i].stamina_current /
                                            save_data["Party"][i].stamina_max) * 48, 5)
                    offset += 6
                if magical:
                    screen.place_rectangle((0, 0, 0), i * 30 + 40, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 0, 255), i * 30 + 40, i * 60 + 120 - offset,
                                           (save_data["Party"][i].mana_current /
                                            save_data["Party"][i].mana_max) * 48, 5)
                    offset += 6
            else:
                if save_data["Party"][i].attacks[temp_data["EncounterData"]["Selection"]["Attack"]][1] == "Melee":
                    if not save_data["Party"][i].name == save_data["Name"]:
                        screen.place_image(save_data["Party"][i].name,
                                           ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30,
                                           ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 40) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30)
                    else:
                        screen.place_image("Spellsword",
                                           ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30,
                                           ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                            ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 60 + 40) *
                                            temp_data["EncounterData"][
                                                "AttackAnimProg"]) / 30)
                elif save_data["Party"][i].attacks[temp_data["EncounterData"]["Selection"]["Attack"]][0] == "Magical":
                    if not save_data["Party"][i].name == save_data["Name"]:
                        screen.place_image(save_data["Party"][i].name,
                                           i * 30 + 40,
                                           i * 60 + 40)
                    else:
                        screen.place_image("Spellsword",
                                           i * 30 + 40,
                                           i * 60 + 40)
                    screen.place_image("ProjectileMagic",
                                       ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30)
                else:
                    if not save_data["Party"][i].name == save_data["Name"]:
                        screen.place_image(save_data["Party"][i].name,
                                           i * 30 + 40,
                                           i * 60 + 40)
                    else:
                        screen.place_image("Spellsword",
                                           i * 30 + 40,
                                           i * 60 + 40)
                    screen.place_image("ProjectilePhysical",
                                       ((i * 30 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * -30 + 400) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30)
        for i in range(len(temp_data["EncounterData"]["EnemyParty"]) - 1, -1, -1):
            if not (temp_data["EncounterData"]["AttackAnimProg"] > 0 and temp_data["EncounterData"]["Turn"] - len(
                    save_data["Party"]) == i):
                screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                   i * - 30 + 400,
                                   i * 60 + 40, True)
                offset = 0
                screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                screen.place_rectangle((255, 0, 0), i * -30 + 400, i * 60 + 120 - offset,
                                       (temp_data["EncounterData"]["EnemyParty"][i].health_current /
                                        temp_data["EncounterData"]["EnemyParty"][i].health_max) * 48, 5)
                offset += 6
                physical = False
                magical = False
                for Attack in temp_data["EncounterData"]["EnemyParty"][i].attacks:
                    if "Physical" in Attack:
                        physical = True
                    elif "Magical" in Attack:
                        magical = True
                if physical:
                    screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 255, 0), i * -30 + 400, i * 60 + 120 - offset,
                                           (temp_data["EncounterData"]["EnemyParty"][i].stamina_current /
                                            temp_data["EncounterData"]["EnemyParty"][i].stamina_max) * 48, 5)
                    offset += 6
                if magical:
                    screen.place_rectangle((0, 0, 0), i * -30 + 400, i * 60 + 120 - offset, 48, 5)
                    screen.place_rectangle((0, 0, 255), i * -30 + 400, i * 60 + 120 - offset,
                                           (temp_data["EncounterData"]["EnemyParty"][i].mana_current /
                                            temp_data["EncounterData"]["EnemyParty"][i].mana_max) * 48, 5)
                    offset += 6
            else:
                if temp_data["EncounterData"]["EnemyParty"][i].attacks[
                    temp_data["EncounterData"]["Selection"]["Attack"]][1] == "Melee":
                    screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                       ((i * -30 + 400) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 30 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 40) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,True)
                elif temp_data["EncounterData"]["EnemyParty"][i].attacks[
                    temp_data["EncounterData"]["Selection"]["Attack"]][0] == "Magical":
                    screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                       i * - 30 + 400,
                                       i * 60 + 40, True)
                    screen.place_image("ProjectileMagic",
                                       ((i * -30 + 400) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 30 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30, True)
                else:
                    screen.place_image(temp_data["EncounterData"]["EnemyParty"][i].name,
                                       i * - 30 + 400,
                                       i * 60 + 40, True)
                    screen.place_image("ProjectilePhysical",
                                       ((i * -30 + 400) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        ((temp_data["EncounterData"]["Selection"]["Enemy"]) * 30 + 40) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30,
                                       ((i * 60 + 64) * (30 - temp_data["EncounterData"]["AttackAnimProg"]) +
                                        (temp_data["EncounterData"]["Selection"]["Enemy"] * 60 + 64) *
                                        temp_data["EncounterData"][
                                            "AttackAnimProg"]) / 30, True)
        if temp_data["EncounterData"]["Turn"] < len(save_data["Party"]) and temp_data["EncounterData"][
            "AttackAnimProg"] == 0:
            screen.place_image("UIBox2", 5, 1)
            if temp_data["EncounterData"]["UIPos"] == 0:
                for OptionNum in range(0, len(save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks)):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                          0].upper() + " " +
                                      save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                          1].upper() + " (" +
                                      str(save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[OptionNum][
                                              2]) + " " +
                                      "DMG)", 10,
                                      30 - OptionNum * 10)
                    input_keys = pygame.key.get_pressed()
                    if input_keys[pygame.K_1] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 0:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 0
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    elif input_keys[pygame.K_2] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 1:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 1
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    elif input_keys[pygame.K_3] and len(
                            save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks) > 2:
                        temp_data["EncounterData"]["Selection"]["Attack"] = 2
                        temp_data["EncounterData"]["UIPos"] += 1
                        mixer.play_sound("ExampleSound", 0)
                    while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
            elif temp_data["EncounterData"]["UIPos"] == 1:
                for OptionNum in range(0, len(temp_data["EncounterData"]["EnemyParty"])):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      temp_data["EncounterData"]["EnemyParty"][OptionNum].name.upper() + " (" + str(
                        temp_data["EncounterData"]["EnemyParty"][OptionNum].health_current) + " HP)", 10,
                                      30 - OptionNum * 10)
                input_keys = pygame.key.get_pressed()
                if input_keys[pygame.K_1] and len(temp_data["EncounterData"]["EnemyParty"]) > 0:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 0
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
                elif input_keys[pygame.K_2] and len(temp_data["EncounterData"]["EnemyParty"]) > 1:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 1
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
                elif input_keys[pygame.K_3] and len(temp_data["EncounterData"]["EnemyParty"]) > 2:
                    temp_data["EncounterData"]["Selection"]["Enemy"] = 2
                    temp_data["EncounterData"]["UIPos"] = 0
                    temp_data["EncounterData"]["AttackAnimProg"] = 1
                    mixer.play_sound("ExampleSound", 0)
        elif temp_data["EncounterData"]["AttackAnimProg"] == 0:
            temp_data["EncounterData"]["Selection"]["Enemy"]=random.randrange(0,len(save_data["Party"]))
            temp_data["EncounterData"]["Selection"]["Attack"] = random.randrange(
                0, len(temp_data["EncounterData"]["EnemyParty"][
                           temp_data["EncounterData"]["Turn"]-len(save_data["Party"])].attacks))
            temp_data["EncounterData"]["AttackAnimProg"] = 1
        else:
            if temp_data["EncounterData"]["AttackAnimProg"] < 30:
                temp_data["EncounterData"]["AttackAnimProg"] += 1
            else:
                temp_data["EncounterData"]["AttackAnimProg"] = 0
                if temp_data["EncounterData"]["Turn"]<len(save_data["Party"]):
                    if save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][0]=="Physical":
                        if random.randint(0,100)>(-50/(0.1*temp_data["EncounterData"]["EnemyParty"][
                            temp_data["EncounterData"]["Selection"]["Enemy"]].dodge_bonus+1))+(50/(0.1*save_data["Party"][temp_data["EncounterData"]["Turn"]].attack_bonus+1))+50:
                            temp_data["EncounterData"]["EnemyParty"][
                                temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][2]
                            if temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].exp += temp_data[
                                    "EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Selection"]["Enemy"]].level*30+10
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].check_for_level_up()
                                save_data["Inventory"]["Gold"]+=random.randint(0,5)*10
                                temp_data["EncounterData"]["EnemyParty"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                                temp_data["EncounterData"]["TurnOrder"].remove(
                                    temp_data["EncounterData"]["Selection"]["Enemy"] + len(save_data["Party"]))
                                for temp_temp in range(0,len(temp_data["EncounterData"]["TurnOrder"])):
                                    if temp_data["EncounterData"]["TurnOrder"][temp_temp]>temp_data["EncounterData"]["Selection"]["Enemy"] + len(save_data["Party"]):
                                        temp_data["EncounterData"]["TurnOrder"][temp_temp]-=1
                                if len(temp_data["EncounterData"]["EnemyParty"])<1:
                                    temp_data["ActiveScreen"]="Overworld"
                    elif save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][0]=="Magical":
                        if random.randint(0,100)>(-50/(0.1*temp_data["EncounterData"]["EnemyParty"][
                            temp_data["EncounterData"]["Selection"]["Enemy"]].dodge_bonus+1))+(50/(0.1*save_data["Party"][temp_data["EncounterData"]["Turn"]].spell_bonus+1))+50:
                            temp_data["EncounterData"]["EnemyParty"][
                                temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][2]
                            if temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].exp += temp_data[
                                    "EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Selection"]["Enemy"]].level*30+10
                                save_data["Party"][temp_data["EncounterData"]["Turn"]].check_for_level_up()
                                save_data["Inventory"]["Gold"] += random.randint(0, 5) * 10
                                temp_data["EncounterData"]["EnemyParty"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                                temp_data["EncounterData"]["TurnOrder"].remove(
                                    temp_data["EncounterData"]["Selection"]["Enemy"]+len(save_data["Party"]))
                                for temp_temp in range(0,len(temp_data["EncounterData"]["TurnOrder"])):
                                    if temp_data["EncounterData"]["TurnOrder"][temp_temp]>temp_data["EncounterData"]["Selection"]["Enemy"] + len(save_data["Party"]):
                                        temp_data["EncounterData"]["TurnOrder"][temp_temp]-=1
                                if len(temp_data["EncounterData"]["EnemyParty"])<1:
                                    temp_data["ActiveScreen"]="Overworld"
                else:
                    if temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                            save_data["Party"])].attacks[
                            temp_data["EncounterData"]["Selection"]["Attack"]][0] == "Physical":
                        if random.randint(0, 100) > (-50 / (0.1 * save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].dodge_bonus+1)) + (
                                50 /(0.1 * temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                                    save_data["Party"])].attack_bonus + 1)) + 50:
                            save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                                temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                                    save_data["Party"])].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][2]
                            if save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                                if temp_data["EncounterData"]["Selection"]["Enemy"]==0:
                                    pygame.quit()
                                    while True:
                                        pass
                                save_data["Party"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                                temp_data["EncounterData"]["TurnOrder"].remove(
                                    temp_data["EncounterData"]["Selection"]["Enemy"])
                                for temp_temp in range(0,len(temp_data["EncounterData"]["TurnOrder"])):
                                    if temp_data["EncounterData"]["TurnOrder"][temp_temp]>temp_data["EncounterData"]["Selection"]["Enemy"]:
                                        temp_data["EncounterData"]["TurnOrder"][temp_temp]-=1
                    elif temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                            save_data["Party"])].attacks[
                            temp_data["EncounterData"]["Selection"]["Attack"]][0] == "Magical":
                        if random.randint(0, 100) > (-50 / (0.1 * save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].dodge_bonus+1)) + (
                                50 / (0.1 * temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                                    save_data["Party"])].spell_bonus + 1)) + 50:
                            save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current-=\
                                temp_data["EncounterData"]["EnemyParty"][temp_data["EncounterData"]["Turn"]-len(
                                    save_data["Party"])].attacks[
                                    temp_data["EncounterData"]["Selection"]["Attack"]][2]
                            if save_data["Party"][temp_data["EncounterData"]["Selection"]["Enemy"]].health_current<=0:
                                if temp_data["EncounterData"]["Selection"]["Enemy"]==0:
                                    pygame.quit()
                                    while True:
                                        pass
                                save_data["Party"].pop(temp_data["EncounterData"]["Selection"]["Enemy"])
                                temp_data["EncounterData"]["TurnOrder"].remove(temp_data["EncounterData"]["Selection"]["Enemy"])
                                for temp_temp in range(0,len(temp_data["EncounterData"]["TurnOrder"])):
                                    if temp_data["EncounterData"]["TurnOrder"][temp_temp]>temp_data["EncounterData"]["Selection"]["Enemy"]:
                                        temp_data["EncounterData"]["TurnOrder"][temp_temp]-=1
                temp_data["EncounterData"]["TurnPos"] += 1
                if temp_data["EncounterData"]["TurnPos"] >= len(save_data["Party"]) + len(temp_data["EncounterData"]["EnemyParty"]):
                    temp_data["EncounterData"]["TurnPos"] = 0
                temp_data["EncounterData"]["Turn"]=temp_data["EncounterData"]["TurnOrder"][temp_data["EncounterData"]["TurnPos"]]
    #
    #
    # Non-battle code
    elif temp_data["EncounterData"]["Type"] == "Dialogue":
        screen.place_image(temp_data["EncounterData"]["Background"], 0, 0)
        screen.place_image("UIBox",5,15)
        if not temp_data["EncounterData"]["Character"] == "None":
            screen.place_image(temp_data["EncounterData"]["Character"], 50, 100)
        if temp_data["PageNumber"] > -1:
            screen.place_text(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][0], 10, 80)
            for OptionNum in range(0, len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) - 1):
                screen.place_text(str(OptionNum + 1) + "; " +
                                  temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][OptionNum + 1][0], 10,
                                  60 - OptionNum * 10)
            input_keys = pygame.key.get_pressed()
            dialogue_script = [False, 0]
            if input_keys[pygame.K_1] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 1:
                if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1]) > 2:
                    dialogue_script = [True, temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][2:]]
                temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][1][1]
                mixer.play_sound("ExampleSound", 0)
            elif input_keys[pygame.K_2] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 2:
                if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2]) > 2:
                    dialogue_script = [True, temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][2:]]
                temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][2][1]
                mixer.play_sound("ExampleSound", 0)
            elif input_keys[pygame.K_3] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 3:
                if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3]) > 2:
                    dialogue_script = [True, temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][2:]]
                temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][3][1]
                mixer.play_sound("ExampleSound", 0)
            elif input_keys[pygame.K_4] and len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]]) > 4:
                if len(temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4]) > 2:
                    dialogue_script = [True, temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][2:]]
                temp_data["PageNumber"] = temp_data["EncounterData"]["Dialogue"][temp_data["PageNumber"]][4][1]
                mixer.play_sound("ExampleSound", 0)
            if dialogue_script[0]:
                for script in dialogue_script[1]:
                    if script[0] in temp_data["EncounterData"].keys():
                        temp_data["EncounterData"][script[0]] = script[1]
                    elif script[0] == "Inventory":
                        if script[1] in save_data["Inventory"].keys():
                            save_data["Inventory"][script[1]] += script[2]
                        else:
                            save_data["Inventory"][script[1]] = script[2]
                    elif script[0] == "Party":
                        if len(save_data["Party"]) < 3:
                            save_data["Party"].append(script[1])
                        else:
                            save_data["GuildHall"].append(script[1])
                    elif script[0] == "GuildHall":
                        save_data["GuildHall"].append(script[1])
                    elif script[0]=="StoryProgress":
                        save_data["StoryProgress"][script[1]]=script[2]
            while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3] or input_keys[pygame.K_4]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif temp_data["PageNumber"]==-1:
            if not save_data["Tutorial"]:
                temp_data["ActiveScreen"] = "Overworld"
            else:
                temp_data["EncounterData"]=temp_data["EncounterContent"][4]
                temp_data["PageNumber"]=0
                temp_data["ActiveScreen"] = "Encounter"
                save_data["Tutorial"]=False
            return save_data, temp_data
        elif temp_data["PageNumber"]==-2:
            input_keys = pygame.key.get_pressed()
            screen.place_text("YOU CAN UPGRADE THE EQUIPMENT OF 1 PARTY MEMBER FOR 100 GOLD, WHICH ONE?", 10, 80)
            OptionNum=0
            for OptionNum in range(0, len(save_data["Party"])):
                screen.place_text(str(OptionNum + 1) + "; " +
                                  save_data["Party"][OptionNum].name.upper(), 10, 60 - OptionNum * 10)
            OptionNum+=1
            screen.place_text(str(OptionNum + 1) + "LEAVE", 10, 60 - OptionNum * 10)
            if input_keys[pygame.K_1]:
                if len(save_data["Party"])>0:
                    mixer.play_sound("ExampleSound", 0)
                    if save_data["Inventory"]["Gold"]>100:
                        for attack_num in range(0,len(save_data["Party"][0].attacks)):
                            save_data["Party"][0].attacks[attack_num][2]+=1
                        temp_data["PageNumber"] = 0
                        temp_data["EncounterData"]["Background"] = "Town2"
                        save_data["Inventory"]["Gold"]-=100
                    else:
                        temp_data["PageNumber"] = -6
                        temp_data["EncounterData"]["Background"] = "Town2"
                elif len(save_data["Party"])==0:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"]=0
                    temp_data["EncounterData"]["Background"]="Town2"
            elif input_keys[pygame.K_2]:
                if len(save_data["Party"])>1:
                    mixer.play_sound("ExampleSound", 0)
                    if save_data["Inventory"]["Gold"]>100:
                        for attack_num in range(0,len(save_data["Party"][1].attacks)):
                            save_data["Party"][1].attacks[attack_num][2]+=1
                        temp_data["PageNumber"] = 0
                        temp_data["EncounterData"]["Background"] = "Town2"
                        save_data["Inventory"]["Gold"]-=100
                    else:
                        temp_data["PageNumber"] = -6
                        temp_data["EncounterData"]["Background"] = "Town2"
                elif len(save_data["Party"])==1:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"]=0
                    temp_data["EncounterData"]["Background"]="Town2"
            elif input_keys[pygame.K_3]:
                if len(save_data["Party"])>2:
                    mixer.play_sound("ExampleSound", 0)
                    if save_data["Inventory"]["Gold"]>100:
                        for attack_num in range(0,len(save_data["Party"][2].attacks)):
                            save_data["Party"][2].attacks[attack_num][2]+=1
                        temp_data["PageNumber"] = 0
                        temp_data["EncounterData"]["Background"] = "Town2"
                        save_data["Inventory"]["Gold"]-=100
                    else:
                        temp_data["PageNumber"] = -6
                        temp_data["EncounterData"]["Background"] = "Town2"
                elif len(save_data["Party"])==2:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"]=0
                    temp_data["EncounterData"]["Background"]="Town2"
            elif input_keys[pygame.K_4]:
                if len(save_data["Party"]) > 3:
                    mixer.play_sound("ExampleSound", 0)
                    if save_data["Inventory"]["Gold"] > 100:
                        for attack_num in range(0, len(save_data["Party"][3].attacks)):
                            save_data["Party"][3].attacks[attack_num][2] += 1
                        temp_data["PageNumber"] = 0
                        temp_data["EncounterData"]["Background"] = "Town2"
                        save_data["Inventory"]["Gold"] -= 100
                    else:
                        temp_data["PageNumber"] = -6
                        temp_data["EncounterData"]["Background"] = "Town2"
                elif len(save_data["Party"]) == 3:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"] = 0
                    temp_data["EncounterData"]["Background"] = "Town2"
        elif temp_data["PageNumber"]==-3:
            input_keys = pygame.key.get_pressed()
            if len(save_data["GuildHall"])>0:
                if len(save_data["Party"])<3:
                    screen.place_text("LIST OF PARTY MEMBERS TO ADD;", 10, 80)
                    for OptionNum in range(0, len(save_data["GuildHall"])):
                        screen.place_text(str(OptionNum + 1) + "; " +
                                          save_data["GuildHall"][OptionNum].name.upper(), 10,60 - OptionNum * 10)
                    if input_keys[pygame.K_1] and len(save_data["GuildHall"])>0:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["Party"].append(copy.deepcopy(save_data["GuildHall"][0]))
                        save_data["GuildHall"].pop(0)
                        temp_data["PageNumber"]=0
                    elif input_keys[pygame.K_2] and len(save_data["GuildHall"])>1:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["Party"].append(copy.deepcopy(save_data["GuildHall"][1]))
                        save_data["GuildHall"].pop(1)
                        temp_data["PageNumber"] = 0
                    elif input_keys[pygame.K_3] and len(save_data["GuildHall"]) > 2:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["Party"].append(copy.deepcopy(save_data["GuildHall"][2]))
                        save_data["GuildHall"].pop(2)
                        temp_data["PageNumber"] = 0
                    elif input_keys[pygame.K_4] and len(save_data["GuildHall"]) > 3:
                        mixer.play_sound("ExampleSound", 0)
                        temp_data["PageNumber"] = 0
                        save_data["Party"].append(copy.deepcopy(save_data["GuildHall"][3]))
                        save_data["GuildHall"].pop(3)
                    elif input_keys[pygame.K_5] and len(save_data["GuildHall"]) > 4:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["Party"].append(copy.deepcopy(save_data["GuildHall"][4]))
                        save_data["GuildHall"].pop(4)
                        temp_data["PageNumber"] = 0
                    while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3] or input_keys[pygame.K_4] or input_keys[pygame.K_5]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
                else:
                    screen.place_text("YOUR PARTY IS FULL, TRY SWAPPING A PARTY MEMBER INSTEAD", 10, 80)
                    for OptionNum in range(0, 1):
                        screen.place_text(str(OptionNum + 1) + "; " +
                                          "GO BACK", 10,60 - OptionNum * 10)
                    if input_keys[pygame.K_1]:
                        mixer.play_sound("ExampleSound", 0)
                        temp_data["PageNumber"] = 0
                    while input_keys[pygame.K_1]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
            else:
                screen.place_text("YOUR GUILD HALL IS EMPTY, TRY RECRUITING NEW COMPANIONS BY VISITING LOCATIONS ON THE MAP", 10, 80)
                for OptionNum in range(0, 1):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      "GO BACK", 10, 60 - OptionNum * 10)
                if input_keys[pygame.K_1]:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"] = 0
                while input_keys[pygame.K_1]:
                    input_keys = pygame.key.get_pressed()
                    pygame.event.get()
        elif temp_data["PageNumber"]==-4:
            input_keys = pygame.key.get_pressed()
            if len(save_data["GuildHall"])>0:
                if len(save_data["Party"])>1:
                    screen.place_text("LIST OF PARTY MEMBERS TO REMOVE;", 10, 80)
                    for OptionNum in range(1, len(save_data["Party"])):
                        screen.place_text(str(OptionNum) + "; " +
                                          save_data["Party"][OptionNum].name.upper(), 10,60 - (OptionNum-1) * 10)
                    if input_keys[pygame.K_1] and len(save_data["Party"])>1:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["GuildHall"].append(copy.deepcopy(save_data["Party"][1]))
                        save_data["Party"].pop(1)
                        temp_data["PageNumber"] = -3
                    elif input_keys[pygame.K_2] and len(save_data["Party"]) > 2:
                        mixer.play_sound("ExampleSound", 0)
                        save_data["GuildHall"].append(copy.deepcopy(save_data["Party"][2]))
                        save_data["Party"].pop(2)
                        temp_data["PageNumber"] = -3
                    while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
                else:
                    screen.place_text("YOUR PARTY IS EMPTY (YOU MAY NOT SWAP OUT YOUR PLAYER CHARACTER)\nTRY ADDING A MEMBER TO YOUR PARTY INSTEAD", 10, 80)
                    for OptionNum in range(0, 1):
                        screen.place_text(str(OptionNum + 1) + "; " +
                                          "GO BACK", 10,60 - OptionNum * 10)
                    if input_keys[pygame.K_1]:
                        mixer.play_sound("ExampleSound", 0)
                        temp_data["PageNumber"] = 0
                    while input_keys[pygame.K_1]:
                        input_keys = pygame.key.get_pressed()
                        pygame.event.get()
            else:
                screen.place_text("YOUR GUILD HALL IS EMPTY, TRY RECRUITING NEW COMPANIONS BY VISITING LOCATIONS ON THE MAP", 10, 80)
                for OptionNum in range(0, 1):
                    screen.place_text(str(OptionNum + 1) + "; " +
                                      "GO BACK", 10, 60 - OptionNum * 10)
                if input_keys[pygame.K_1]:
                    mixer.play_sound("ExampleSound", 0)
                    temp_data["PageNumber"] = 0
                while input_keys[pygame.K_1]:
                    input_keys = pygame.key.get_pressed()
                    pygame.event.get()
        elif temp_data["PageNumber"] == -5:
            input_keys = pygame.key.get_pressed()
            screen.place_text("IT COSTS 60 GOLD TO REST BUT WILL REPLENISH ALL CURRENT PARTY MEMBERS' HP, STAMINA AND MANA", 10, 80)
            screen.place_text(str(1) + "; " +
                                  "PAY UP", 10, 60 - 0 * 10)
            screen.place_text(str(2) + "; " +
                              "LEAVE", 10, 60 - 1 * 10)
            if input_keys[pygame.K_1]:
                mixer.play_sound("ExampleSound", 0)
                if save_data["Inventory"]["Gold"]>60:
                    temp_data["PageNumber"] = 0
                    save_data["Inventory"]["Gold"]-=60
                    for character_num in range(0,len(save_data["Party"])):
                        save_data["Party"][character_num].health_current=save_data["Party"][character_num].health_max
                        save_data["Party"][character_num].mana_current = save_data["Party"][character_num].mana_max
                        save_data["Party"][character_num].stamina_current = save_data["Party"][character_num].stamina_max
                else:
                    temp_data["PageNumber"]=-6
            elif input_keys[pygame.K_2]:
                mixer.play_sound("ExampleSound", 0)
                temp_data["PageNumber"] = 0
            while input_keys[pygame.K_1] or input_keys[pygame.K_2]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif temp_data["PageNumber"] == -6:
            input_keys = pygame.key.get_pressed()
            screen.place_text(
                "YOU DO NOT HAVE ENOUGH MONEY", 10, 80)
            screen.place_text(str(1) + "; " +
                              "LEAVE", 10, 60 - 0 * 10)
            if input_keys[pygame.K_1]:
                mixer.play_sound("ExampleSound", 0)
                temp_data["PageNumber"] = 0
            while input_keys[pygame.K_1] or input_keys[pygame.K_2]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()
        elif temp_data["PageNumber"] == -7:
            input_keys = pygame.key.get_pressed()
            screen.place_text(
                "YOU LOST ALL YOUR GOLD ;(", 10, 80)
            save_data["Inventory"]["Gold"]=0
            screen.place_text(str(1) + "; " +
                              "LEAVE", 10, 60 - 0 * 10)
            if input_keys[pygame.K_1]:
                mixer.play_sound("ExampleSound", 0)
                temp_data["PageNumber"] = 0
            while input_keys[pygame.K_1] or input_keys[pygame.K_2]:
                input_keys = pygame.key.get_pressed()
                pygame.event.get()

    return save_data, temp_data


def inventory(screen, mixer, save_data, temp_data):
    screen.place_image("BlankWhite", 0, 0)
    for i in range(0,len(save_data["Party"])):
        offset=0
        screen.place_text(save_data["Party"][i].name.upper()+";",20+i*110,260+offset)
        offset+=20
        screen.place_text(str("LVL "+str(save_data["Party"][i].level)) + " ("+str(save_data["Party"][i].exp)+" EXP)", 20+i*110,260-offset)
        if not save_data["Party"][i].name==save_data["Name"]:
            screen.place_image(save_data["Party"][i].name,20+i*110,260-offset-70)
        else:
            screen.place_image("Spellsword", 20+i*110, 260 - offset-70)
        offset+=80
        screen.place_text(str(save_data["Party"][i].health_current)+" OUT OF "+str(save_data["Party"][i].health_max)+" HP", 20+i*110,260-offset)
        physical = False
        magical = False
        for Attack in save_data["Party"][i].attacks:
            if "Physical" in Attack:
                physical = True
            elif "Magical" in Attack:
                magical = True
        if physical:
            offset+=10
            screen.place_text(
                str(save_data["Party"][i].stamina_current) + " OUT OF " + str(save_data["Party"][i].stamina_max) + " STAMINA",
                20+i*110, 260 - offset)
        if magical:
            offset += 10
            screen.place_text(
                str(save_data["Party"][i].mana_current) + " OUT OF " + str(save_data["Party"][i].mana_max) + " MANA",
                20+i*110, 260 - offset)
        offset=140
        screen.place_text(str(save_data["Party"][i].initiative_bonus) + " INITIATIVE BONUS",20+i*110, 260 - offset)
        offset+=10
        if physical:
            screen.place_text(str(save_data["Party"][i].attack_bonus) + " PHYSICAL BONUS", 20+i*110, 260 - offset)
            offset += 10
        if magical:
            screen.place_text(str(save_data["Party"][i].spell_bonus) + " MAGIC BONUS", 20+i*110, 260 - offset)
            offset += 10
        screen.place_text(str(save_data["Party"][i].initiative_bonus) + " DODGE BONUS", 20 + i * 110, 260 - offset)
        offset = 190
        if temp_data["UIPos"]==0:
            screen.place_text(str(i + 1) + "; " + str(save_data["Party"][i].unspent_points) + " UNSPENT POINTS",
                              20 + i * 110, 260 - offset)
            offset += 10
        else:
            screen.place_text(str(save_data["Party"][i].unspent_points) + " UNSPENT POINTS",
                              20 + i * 110, 260 - offset)
            offset += 10
        if temp_data["UIPos"]==0 or not (temp_data["Selection"]["Character"]==i):
            screen.place_text(str(save_data["Party"][i].strength) + " STRENGTH",
                              20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str(save_data["Party"][i].constitution) + " CONSTITUTION",
                              20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str(save_data["Party"][i].dexterity) + " DEXTERITY",
                              20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(
                str(save_data["Party"][i].intelligence) + " INTELLIGENCE",
                20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str(save_data["Party"][i].wisdom) + " WISDOM",
                              20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str(save_data["Party"][i].charisma) + " CHARISMA",
                              20 + i * 110, 260 - offset)
            offset += 10
        else:
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].strength) + " STRENGTH", 20 + i * 110, 260 - offset)
            offset+=10
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].constitution) + " CONSTITUTION", 20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].dexterity) + " DEXTERITY", 20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].intelligence) + " INTELLIGENCE", 20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].wisdom) + " WISDOM", 20 + i * 110, 260 - offset)
            offset += 10
            screen.place_text(str((offset-190)//10)+"; "+str(save_data["Party"][i].charisma) + " CHARISMA", 20 + i * 110, 260 - offset)
            offset += 10
    input_keys=pygame.key.get_pressed()
    if temp_data["UIPos"]==0:
        if input_keys[pygame.K_1] and len(save_data["Party"])>0:
            mixer.play_sound("ExampleSound",0)
            if save_data["Party"][0].unspent_points>0:
                temp_data["UIPos"]=1
                temp_data["Selection"]["Character"]=0
        elif input_keys[pygame.K_2] and len(save_data["Party"])>1:
            mixer.play_sound("ExampleSound",0)
            if save_data["Party"][1].unspent_points>0:
                temp_data["UIPos"]=1
                temp_data["Selection"]["Character"]=1
        elif input_keys[pygame.K_3] and len(save_data["Party"])>2:
            mixer.play_sound("ExampleSound",0)
            if save_data["Party"][2].unspent_points>0:
                temp_data["UIPos"]=1
                temp_data["Selection"]["Character"]=2
    else:
        if input_keys[pygame.K_1]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].strength+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
        elif input_keys[pygame.K_2]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].constitution+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
        elif input_keys[pygame.K_3]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].dexterity+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
        elif input_keys[pygame.K_4]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].intelligence+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
        elif input_keys[pygame.K_5]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].wisdom+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
        elif input_keys[pygame.K_6]:
            mixer.play_sound("ExampleSound",0)
            save_data["Party"][temp_data["Selection"]["Character"]].charisma+=1
            save_data["Party"][temp_data["Selection"]["Character"]].unspent_points-=1
            save_data["Party"][temp_data["Selection"]["Character"]].increase_stats()
            if save_data["Party"][temp_data["Selection"]["Character"]].unspent_points==0:
                temp_data["UIPos"]=0
    while input_keys[pygame.K_1] or input_keys[pygame.K_2] or input_keys[pygame.K_3] or input_keys[pygame.K_4] or input_keys[pygame.K_5] or input_keys[pygame.K_6]:
        input_keys = pygame.key.get_pressed()
        pygame.event.get()
    offset=0
    i=3
    screen.place_text("INVENTORY;", 20 + i * 110, 260 - offset)
    offset+=20
    for i2 in save_data["Inventory"].keys():
        screen.place_text(i2.upper(), 20 + i * 110, 260 - offset)
        screen.place_text(str(save_data["Inventory"][i2]), 100+ i * 110, 260 - offset)
        offset+=10
    if input_keys[pygame.K_i]:
        temp_data["ActiveScreen"] = "Overworld"
        while input_keys[pygame.K_i]:
            screen.update()
            input_keys = pygame.key.get_pressed()
    return save_data, temp_data


def settings(screen, mixer, save_data, temp_data):
    screen.place_image("Blank", 0, 0)
    input_keys = pygame.key.get_pressed()
    screen.update()
    if input_keys[pygame.K_ESCAPE]:
        temp_data["ActiveScreen"] = "Overworld"
        while input_keys[pygame.K_ESCAPE]:
            screen.update()
            input_keys = pygame.key.get_pressed()
    return save_data, temp_data


def main():
    screen = DisplayManager()
    screen.load_images()
    mixer = SoundManager()
    mixer.load_sounds()
    mixer.play_sound("DesertTheme1", -1)
    save_data, temp_data = new_game()
    while True:
        frame_time = time.time()
        if temp_data["ActiveScreen"] == "Encounter":
            save_data, temp_data = encounter(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Inventory":
            save_data, temp_data = inventory(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Overworld":
            save_data, temp_data = overworld(screen, mixer, save_data, temp_data)
        elif temp_data["ActiveScreen"] == "Settings":
            save_data, temp_data = settings(screen, mixer, save_data, temp_data)
        else:
            print("ERROR: Active screen is set to " + temp_data["ActiveScreen"] + " which does not exist")
        temp_data["AnimateTick"] += 1
        screen.update()
        if frame_time + 0.016 > time.time():
            time.sleep(0.017 - (time.time() - frame_time))


main()
