import random
import csv

t = 0
sv = 0
w = 0

weapon1A = 0
weapon1Skill = 0
weapon1S = 6
weapon1AP = 2

weapon2A = 0
weapon2Skill = 0
weapon2S = 0
weapon2AP = 0

weapon3A = 0
weapon3Skill = 0
weapon3S = 0
weapon3AP = 0

print("Choose the attacker - type the number of the unit")
print("1 - Captain in terminator armour")
print("2 - Librarian in terminator armour")
print("3 - Terminator squad")
print("4 - Infernus squad")
print("5 - Tyranid prime")
print("6 - Psychophage")
print("7 - Termagants")
print("8 - Ripper Swarm")
print("9 - Von Ryan's leapers")
print("10 - Barbgaunts")

choice = input()
rowIndex = int(choice) - 1

def getValue(rowIndex, columnIndex):
    with open('characters.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        header = next(csv_reader)

        for i, row in enumerate(csv_reader):
            if i == rowIndex:
                value = row[columnIndex].strip()
                return value

match choice:
    case "1":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "2":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "3":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "4":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "5":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "6":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "7":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "8":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "9":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case "10":
        t = getValue(rowIndex, 1)
        sv = getValue(rowIndex, 2)
        w = getValue(rowIndex, 3)

        weapon1A = getValue(rowIndex, 4)
        weapon1Skill = getValue(rowIndex, 5)
        weapon1S = getValue(rowIndex, 6)
        weapon1AP = getValue(rowIndex, 7)

        weapon2A = getValue(rowIndex, 8)
        weapon2Skill = getValue(rowIndex, 9)
        weapon2S = getValue(rowIndex, 10)
        weapon2AP = getValue(rowIndex, 11)

        weapon3A = getValue(rowIndex, 12)
        weapon3Skill = getValue(rowIndex, 13)
        weapon3S = getValue(rowIndex, 14)
        weapon3AP = getValue(rowIndex, 15)
    case _:
        print("Wrong number")

print("Weapon number: 1 or 2")

weaponNum = input()

# check what type is it


def RollD6():
    roll = random.randint(1, 6)
    return roll

def HitRoll(weaponSkill):
    roll = RollD6()
    if(roll >= weaponSkill):
        print("Hit Roll succesful")
        return True

def WoundRoll(weaponS, t):
    roll = RollD6()
    if(weaponS >= 2*t):
        if(roll >= 2):
            print("Wounded")
            return True
    elif(weaponS > t):
        if(roll >= 3):
            print("Wounded")
            return True
    elif(weaponS == t):
        if(roll >= 4):
            print("Wounded")
            return True
    elif(weaponS < t):
        if(roll >= 5):
            print("Wounded")
            return True
    elif(2*weaponS <= t):
        if(roll >= 6):
            print("Wounded")
            return True
    else:
        return False

def SavingThrow(sv, weaponAP):
    roll = RollD6()
    if(roll < sv + weaponAP):
        return True
    else:
        return False

def InflictDamage(w):
    w = w - 1
    if(w == 0):
        print("Death, other dealt wounds: " + str(w))
    else:
        print("Remaining wounds: " + str(w))

def FightSequence(enemyT, enemySV, enemyW, weaponA, weaponSkill, weaponS, weaponAP):
    if(HitRoll(weaponSkill)):
        if(WoundRoll(weaponS, enemyT)):
            if(SavingThrow(enemySV, weaponAP)):
                InflictDamage(enemyW)
            else:
                print("Saving throw roll failed")
        else:
            print("Wound roll failed")
    else:
        print("Hit roll failed")

        
if(weaponNum == 1):
    for x in range(weapon1A):
        FightSequence(t, sv, w, weapon1A, weapon1Skill, weapon1S, weapon1AP)
elif(weaponNum == 2):
    for x in range(weapon2A):
        FightSequence(t, sv, w, weapon2A, weapon2Skill, weapon2S, weapon2AP)
elif(weaponNum == 3):
    for x in range(weapon3A):
        FightSequence(t, sv, w, weapon3A, weapon3Skill, weapon3S, weapon3AP)