class human:
    def __init__(self, height, age):
        self.height = height
        self.age = age
        
    def how_old(self):
        print(self.age,"살 입니다.")
    
    def how_tall(self):
        print(self.height,"cm 입니다.")
    
Seunghyun = human(180, 31)

Seunghyun.height

Seunghyun.how_old()

human.how_old(Seunghyun)


Seunghyun1 = human(180, 31)
Seunghyun2 = human(180, 31)

Seunghyun.how_tall()
human.how_tall(Seunghyun)

