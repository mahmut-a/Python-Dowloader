# Stream hakkında temel bilgilieri terminalden görüntüler

from pytube import YouTube as yt
link = str(input("Link : "))
link = yt(link)

print(link.title)
print(link.streams)
input()