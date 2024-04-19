"""
Bu Programda Başta HTTP Hatası Olmak Üzere Çeşitli Hatalar Çıkması Durumunda
python -m pip uninstall pytube
Komutu ile CMD den önce mevcut kütüphane silinip ardından
python -m pip install pytube
Komutu ile tekrak yüklenebilir.

BUNUN SORUNU res Pramaetresinde her video 720p olmuyor.
link.stream ile değerler kontrol edilebilir.
progressive true ve en yüksek res indirilebilir.
"""
import tkinter as tk
from pytube import YouTube as yt

penecere = tk.Tk()
penecere.title("Youtube Video İndirme Programı")
penecere.geometry("500x100")
penecere.resizable(False,False)

bilgi = tk.Label(text = "Bu kutucuğa adresi giriniz.")
bilgi.pack()

kutucuk = tk.Entry(width = 50 , bd = 5)
kutucuk.pack()


def indir():
    adres = kutucuk.get()
    link = yt(adres)
    title = link.title
    stream = link.streams.filter(progressive = True , res = "720p").first()
    fName = title + ".mp4"
    stream.download("C:/Users/$UserName/Downloads/", filename=fName)


button = tk.Button(text = "İndir",command = indir , bg = "red", relief = tk.RAISED)
button.pack(side = tk.BOTTOM , fill = tk.X)

penecere.mainloop()
