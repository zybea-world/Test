from multiprocessing import Process
from random import randint
from time import sleep
import time

# class Download(Process):
#
#     def __init__(self,filename):
#         super().__init__()
#         self._filename = filename
#
#     @property
#     def filename(self):
#         return self._filename
#
#     def run(self):
#         print(f"开始下载‘{self.filename}’")
#         time_to_download = randint(3,10)
#         sleep(time_to_download)
#         print(f"下载完成，总共消耗时间{time_to_download}秒")
#
# def main():
#     star = time.perf_counter()
#     p1 = Download('Python 从入门到放弃.PDF')
#     p1.start()
#     p2 = Download('Yang.avi')
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.perf_counter()
#     print('总共消耗了{:.2f}秒'.format(end-star))

def download(filename):
    print(f"'{filename}'开始下载.......")
    time = randint(1,6)
    sleep(time)
    print(f"{filename}消耗时间{time}秒")

def main():
    st = time.perf_counter()
    p1 = Process(target=download,args=('Python 从入门到放弃.pdf',))#Python 从入门到放弃.pdf消耗时间6秒
    p1.start()
    p2 = Process(target=download,args=('Yang.avi',))#Yang.avi消耗时间5秒
    p2.start()
    p1.join()
    p2.join()
    end = time.perf_counter()
    print("总共消耗{}秒".format(end-st)) #总共消耗7.7664454秒

if __name__=="__main__":
    main()


