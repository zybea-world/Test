from threading import Thread
from random import randint
import time
from time import sleep


class Download(Thread):

    def __init__(self, filename):

        super().__init__()
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def run(self):
        print(f"{self.filename}开始下载".center(40, '*'))
        ti = randint(4, 6)
        sleep(ti)
        print(f"{self.filename}下载消耗了{ti}秒.")

def main():

    st = time.perf_counter()
    t1 = Download('Python 从入门到放弃.pdf')#Python 从入门到放弃.pdf下载消耗了5秒.
    t1.start()
    t2 = Download('Yang.avi')#Yang.avi下载消耗了5秒.
    t2.start()
    t1.join()
    t2.join()
    end = time.perf_counter()
    print('总共消耗时长{:.2f}秒'.format(end - st))

if __name__ == "__main__":

    main()
"""
对于io密集型的来说，使用多线程优势明显，线程线程切换间的消耗比进程间少得多
"""
