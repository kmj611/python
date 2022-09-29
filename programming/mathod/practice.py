name = "마린"
hp = 40
damage = 50
print("\n{} 유닛이 생성되었습니다. ".format(name))
print("체력 {0}, 공격력 {1} ".format(hp, damage))


tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("\n{} 유닛이 생성되었습니다. ".format(tank_name))
print("체력 {0}, 공격력 {1} ".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("\n{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
print()

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("\n{} 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1} ".format(self.hp, self.damage))
        
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

wrait1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wrait1.name, wrait1.damage))

wrait2 = Unit("빼앗은 레이스", 80, 5)
wrait2.clocking = True

if wrait2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format.write2.name)

if wrait1.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format.write1.name)
    
if wrait1.clocking == True
    print("{0} 는 현재 클로킹 상태입니다.".format.write2.name)
# marine3 = Unit("마린")
# marine2 = Unit("마린", 40)


class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    def damaged (self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp - damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: XU4.".format(self.name))
# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("00", 50, 16)
firebat1.attack("5/|")
# 공격 2번 받는다고 가정
firebat1.damaged (25)
firebat1.damaged (25)


class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit._init__(self, name, hp)
        self.damage = damage
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))
    def damaged(self, damage):
        print("{0}: {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp == damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} DSXSU4.".format(self.name))
            
            
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit. _init_(self, name, hp, damage)
        Flyable._init__(self, flying_speed)
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("2", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3/|")