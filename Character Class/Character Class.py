class Character:
    def __init__(self, stre, dex, con,  intel, wis, cha):
        self.level = 1
        
        self.str  = stre
        self.dex = dex
        self.con = con
        self.int = intel
        self.wis = wis
        self.cha = cha
        
        self.strmod = (self.str - 10)//2
        self.dexmod = (self.dex - 10)//2
        self.conmod = (self.con - 10)//2
        self.intmod = (self.int - 10)//2
        self.wismod = (self.wis - 10)//2
        self.chamod = (self.cha - 10)//2
        
        self.healthmax = (self.conmod+10+(5+self.conmod)*(self.level-1))
        self.attackBonus = (self.strmod+2)
        self.spellBonus = (self.chamod+2)

        self.staminamax = self.level*10 + self.conmod*5
        self.staminaregen = self.level + self.strmod*2

        self.armourclass = 10 + self.dexmod


class Players(Character):
    def __init__(self, stre, dex, con,  intel, wis, cha):
        super().__init__(stre, dex, con,  intel, wis, cha)
        self.wealth = 10
        self.manamax = self.level*10 + self.intmod*5
        self.manaregen = self.level + self.wismod*2
        self.manacurrent = self.manamax
        
        self.PowerList = []
    def LevelUp(self):
        self.level += 1
        if self.level%4 == 0:
            choice = int(input("Choose which statistic to increase by 1.\n1. Strength\n2. Dexterity\n3. Constitution\n4. Intelligence\n5. Wisdom\n6. Charisma"))
            if choice == 1:
                self.str += 1
            if choice == 2:
                self.dex += 1
            if choice == 3:
                self.con += 1
            if choice == 4:
                self.int += 1
            if choice == 5:
                self.wis += 1
            if choice == 6:
                self.cha += 1
        
        self.strmod = (self.str - 10)//2
        self.dexmod = (self.dex - 10)//2
        self.conmod = (self.con - 10)//2
        self.intmod = (self.int - 10)//2
        self.wismod = (self.wis - 10)//2
        self.chamod = (self.cha - 10)//2
        
        self.health = (self.conmod+10+(5+self.conmod)*(self.level-1))
        self.attackBonus = (self.strmod+2)
        self.spellBonus = (self.chamod+2)

        if self.level%2 == 0:
            # gain another Power/upgrade power
            pass


class Party:
    def __init__(self, Guild):
        self.currentPos = 0
        self.memberList = [0,1,2,3]
        self.partySize = len(self.memberList)
        self.Guild = Guild

    def addMember(self, member):
        if self.partySize < 4:
            self.memberList.append(member)
            self.partySize += 1
        else:
            MemberToRemove = int(input("Choose which party member to remove (1 to 4):"))
            MemberToRemove += -1
            self.SwapMember(member, MemberToRemove, self.Guild)

    def SwapMember(self, MemberToAdd, MemberToRemove, Guild):
        Guild.benchList.append(self.memberList[MemberToRemove])
        self.memberList[MemberToRemove] = MemberToAdd


class Guild:
    def __init__(self):
        self.benchList = []
        self.wealth = 0
    
guild = Guild()
party = Party(guild)

