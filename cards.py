import time
from random import randint
money = 1000
while money > 0:
    print("你目前的金额还有{}".format(money))
    debt = int(input("请下注："))
    if 0< debt <=money:
        count = 1
        first = randint(1, 6) + randint(1, 6)
        print("第{}次投色子...".format(count))
        time.sleep(1)
        print("此次点数为{},胜点为{}".format(first,[7,11]))
        if first in [7, 11]:
            money += debt
            print("玩家胜，增加金钱{},一共持有{}".format(debt, money))
        elif first in [2, 3, 12]:
            money -= debt
            print("庄家胜，减少金钱{},一共持有{}".format(debt, money))
        else:
            needs_go = True
            while needs_go:
                count += 1
                print("开始第{}次投色子".format(count))
                time.sleep(1)
                num = randint(1, 6) + randint(1, 6)
                print("此次点数为{}，胜点为{}".format(num,first))
                if num == first:
                    money += debt
                    print("玩家胜，增加金钱{},一共持有{}".format(debt, money))
                    needs_go = False
                    print("="*20)
                elif num == 7:
                    money -= debt
                    print("庄家胜，减少金钱{},一共持有{}".format(debt, money))
                    needs_go = False
                    print("=" * 20)
                else:
                    needs_go = True
    else:
        print("金额不足")
    #第一次摇骰子

print("你破产了")


