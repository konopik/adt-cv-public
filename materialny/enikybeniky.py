from dataclasses import dataclass

@dataclass
class account:
    money:float

def simTickOne(days, ac:account):
    ac.money -= 300

    if(days%30==15):
        ac.money += 5000

    ac.money = 1.01*ac.money

def simTickTwo(months, ac:account):
    ac.money += 300

    if(months % 3 == 0):
        ac.money += 500

    ac.money= 1.10*ac.money

def main():
    simOne = account(money=25000)

    counter = 0
    simRange = 90

    while counter < simRange:
        counter += 1
        simTickOne(counter, simOne)
        print(counter, simOne.money)

    simTwo = account(money=25000)

    counter = 0
    simRange = 12
    print("----------------")
    while counter < simRange:
        counter += 1
        simTickTwo(counter, simTwo)
        print(counter, simTwo.money)


main()