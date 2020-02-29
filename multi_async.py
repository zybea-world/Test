from multiprocessing import Process
from queue import Queue
import asyncio
import aiohttp
import time
from lxml.etree import HTML

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.\
    100 Safari/537.36",
}

urls = ["https://www.baidu.com"]*100

async def get_page(url,i=0):
    async with aiohttp.ClientSession() as se:
        try:
            async with se.get(url,timeout = 10,headers = header) as resp:
                stat  = resp.status
                r = await resp.text()
                res = HTML(r)
                word = res.xpath("//head/title/text()")[0]
                #print(f"Start Process_{i}")
                print(url,stat,word)
        except Exception as e:
            print(url,e)
def run():
    loop = asyncio.get_event_loop()
    tasks = [get_page(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

def main():
    p_list = []
    for i in range(0,100,20):
        url_list = urls[i:i+20]
        p = Process(target=run,args=(url_list,int(i/20)))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()


if __name__=="__main__":
    start = time.perf_counter()
    run()
    #main()
    end = time.perf_counter()
    print(f"总耗时{end - start}")




