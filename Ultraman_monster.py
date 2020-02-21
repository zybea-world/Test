from abc import ABCMeta,abstractmethod
from random import randint,choice
from time import sleep

class Fighter(object,metaclass=ABCMeta):

    def __init__(self,name,hp):

        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self,hp):
        self._hp = hp

    @abstractmethod
    def attack(self,other):
        pass

class Ultra(Fighter):

    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self,mp):
        self._mp = mp


    def attack(self,other):
        damage = randint(30,50)
        other.hp-=damage
        print(f"{self.name}使用普通攻击对{other.name}造成了{damage}伤害")

    def magic_attack(self,other):

        if self.mp >= 50:
            self.mp -= 50
            damage = randint(50,100)
            other.hp -= damage
            print(f"{self.name}使用魔法攻击对{other.name}造成了{damage}伤害,魔法值下降50点")
        else:
            print(f"{self.name}魔法值目前为{self.mp},无法施展魔法攻击，进行普通攻击")
            self.attack(other)
            self.resume()

    def max_attack(self,other):

        if self.mp>=50:
            damage = 150 if other.hp>50 else other.hp*3/4
            print(f"{self.name}使用究极攻击对{other.name}造成了{damage}伤害")
            other.hp -= damage
        else:
            self.attack(other)
            self.resume()

    def resume(self):
        self.mp += 40
        print(f"{self.name}魔法值恢复了40点")
        pass

    def __str__(self):
        return f"{self.name}目前状态生命值:{self.hp}/魔法值:{self.mp}"


class Monster(Fighter):


    def attack(self,other):
        damage = randint(40, 80)
        other.hp -= damage
        print(f"{self.name}使用普通攻击对{other.name}造成了{damage}伤害")

    def __str__(self):

        self.hp = self.hp if self._hp>0 else 0
        return f"{self.name}生命值:{self.hp}."


def main():
    monster_list = [Monster("哥斯拉",hp=1000),Monster("点子狗",hp=1500),Monster("弱鸡洋",hp=800),
                    Monster("狗急拉",hp=1200)]

    monster = choice(monster_list)
    ultarman = Ultra('邵美丽',2000,300)
    count = 0
    while monster.hp >0 :
        count+=1
        sleep(1)
        print(f"第{count}回合".center(50,'*'))
        point = randint(1,8)
        if point in [1,2,3,4,5]:
            print(f"{monster.name}发动攻击....准备中")
            sleep(1)
            monster.attack(ultarman)
        else:
            print(f"{ultarman.name}发动攻击....准备中")
            sleep(1)
            if point == 6:
                ultarman.attack(monster)
            elif point==7:
                ultarman.magic_attack(monster)
            elif point==8:
                ultarman.max_attack(monster)
        print(ultarman,monster)

if __name__=="__main__":
    main()





