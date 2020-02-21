from pyquery import PyQuery as pq
doc = pq("https://blog.csdn.net/csdn15698845876/article/details/73321593")
print(doc('#content_views p').text())