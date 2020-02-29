from threading import Thread,Lock
from multiprocessing import Process,Queue
import time


# def main():
#     st = time.perf_counter()
#     total = 0
#     for i in (x for x in range(50000000)):
#         total += i
#     end = time.perf_counter()
#     print(total)
#     print(f"总共费时{end-st}秒")#总共费时200：5.5743668秒:1000：11.485016秒:5000：56.996584秒


def count(index,quene):
    total = 0
    for i in  (x for x in range(index,index+10000000)):
        total += i
    quene.put(total)

def main():
    queue = Queue()
    total = 0
    index = 0
    st = time.perf_counter()
    p_list = []
    for _ in range(5):
        p = Process(target=count,args=(index,queue))
        p_list.append(p)
        p.start()
        index+= 10000000
    for p in p_list:
        p.join()
    while not queue.empty():
        total+=queue.get()
    print(total)#12499997500000
    end = time.perf_counter()
    print(f"总共费时{end-st}秒")#200：8.593秒，1000：12.160秒，5000：43.94秒

if __name__=="__main__":
    main()

"""
计算密集型的多进程，进程最大数与CPU的 core数一致，我的电脑是双核的,当计算密度比较小时，例如2000000内的自加求和，
多进程时间为8.593秒，而单进程直接运算5.574s,明显进程间的数据交换时间消耗比较大，理想的极限状态应该是一倍左右
     多进程
"""

