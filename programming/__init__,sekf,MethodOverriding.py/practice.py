# name = "마린"
# hp = 40
# damage = 50
# print("\n{} 유닛이 생성되었습니다. ".format(name))
# print("체력 {0}, 공격력 {1} ".format(hp, damage))


# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("\n{} 유닛이 생성되었습니다. ".format(tank_name))
# print("체력 {0}, 공격력 {1} ".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("\n{0} : {1} 방향으로 적군을 공격합니다. 공격력 {2}".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# print()

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("\n{} 유닛이 생성되었습니다. ".format(self.name))
        print("체력 {0}, 공격력 {1} ".format(self.hp, self.damage))
        
marine3 = Unit("마린")
marine2 = Unit("마린", 40)


class Unit:
	def __init(self, name, hp, speed):
		self.name = name
		self.hp = hp
		self.speed = speed
		
	def move(self,location):
		print("[지상 유닛 이동]")
		print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))





class AttackUnit(Unit):
    def _init_(self, name, hp, speed, damage):
        Unit._init_(self, name, hp, speed)
        self.damage = damage
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적을 공격합니다. [공격력 {2}]"
        .format(self.name, location, self.damage))
        
    def damaged (self, damage):
        print("{0}: {1} 데미지를 입었습니다."
        .format(self.name, damage))
        
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다."
        .format(self.name, self.hp))
        
        if self.hp <= 0:
            print("{0} : IXU4.".format(self.name))
    def move(self, location):
        super().move(location)
        print("공격 유닛 입니다")
        
        
marine1 = AttackUnit("마린", 40, 5, 25)
marine1.move("5시")


class BuildingUnit(Unit):
    def __iinit__(self, name,hp,location)
        pass
    
supply_depot = BuildingUnit("서플라이 디폿",500,"7시")




class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        super().__init__(name, hp, 0)
        self.location = location
        
        

class Unit:
    def __init__(self):
        print("Unit ")
class Flyable:
    def __init__(self):
        print("Flyable ")
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super(). __init__()
dropship1 = Flyable()
dropship2 = FlyableUnit()



class Unit:
    def __init__(self):
        print("Unit 생성자")
        
class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
class FlyableUnit (Flyable, Unit):
    def __init__(self):

        Unit._init__(self)
        Flyable. _init__(self)

dropship2 = FlyableUnit()