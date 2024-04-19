"""
HATALAR
-------

Bu Programda Başta HTTP Hatası Olmak Üzere Çeşitli Hatalar Çıkması Durumunda
python -m pip uninstall pytube
Komutu ile CMD den önce mevcut kütüphane silinip ardından
python -m pip install pytube
Komutu ile tekrak yüklenebilir.

BUNUN SORUNU res Pramaetresinde her video 720p olmuyor.
link.stream ile değerler kontrol edilebilir.
progressive true ve en yüksek res indirilebilir.

Bazı hatalalarda dosya adından dolayı olabiliyor
"""
"""
GÜNCELLEMELER
-------------

Genel bir güncelleme yaptım
Daha Kullanışlı oldu

Yenilikler :
* 4 Tür Çözünürlük button eklendi
* Stil güncelemeleri yapıldı

Bir sonraki güncellemede yapılabilecekler :
* Diğer kutucuğu ile butonlarda olmayan çözünürlüklerin indirilmesi
* Tkinter-window.py dosyasındaki title bar'ı eklemek

Güncelleme Tarihi : 03.02.2024 

"""
import tkinter as tk
from pytube import YouTube as yt

# Colors
c_gray = "gray"
c_black = "black"
c_white = "white"

penecere = tk.Tk()
#penecere.overrideredirect(True)
penecere.geometry("500x200")
penecere.resizable(False,False)
penecere.configure(bg="black")

bilgi = tk.Label(text = "Bu kutucuğa adresi giriniz." , bg = "black" , fg = "gray")
bilgi.pack()

kutucuk = tk.Entry(width = 75 , bd = 5 , bg = "black" , fg = "gray" , relief = "ridge")
kutucuk.config(insertbackground  = "gray")
kutucuk.pack()

# $UserName must be your own user name

def indir360():
    adres = kutucuk.get()
    link = yt(adres)
    title = link.title
    stream = link.streams.filter(progressive = True , res = "360p").first()
    fName = title + ".mp4"
    stream.download("C:/Users/$UserName/Downloads/", filename=fName)

def indir480():
    adres = kutucuk.get()
    link = yt(adres)
    title = link.title
    stream = link.streams.filter(progressive = True , res = "480p").first()
    fName = title + ".mp4"
    stream.download("C:/Users/$UserName/Downloads/", filename=fName)

def indir720():
    adres = kutucuk.get()
    link = yt(adres)
    title = link.title
    stream = link.streams.filter(progressive = True , res = "720p").first()
    fName = title + ".mp4"
    stream.download("C:/Users/$UserName/Downloads/", filename=fName)


def indir1080():
    adres = kutucuk.get()
    link = yt(adres)
    title = link.title
    stream = link.streams.filter(progressive = True , res = "1080p").first()
    fName = title + ".mp4"
    stream.download("C:/Users/$UserName/Downloads/", filename=fName)

button360 = tk.Button(text = "360p" , command = indir360 , bg = "green" , fg = c_white , relief = tk.RAISED , pady = 25 , padx = 110 , cursor = 'dotbox')
button360.place(y = 52 , x = 0)

button480 = tk.Button(text = "480p" , command = indir480 , bg = "gray", fg = c_white , relief = tk.RAISED , pady = 25 , padx = 110 , cursor = 'dotbox')
button480.place(y = 52 , x = 250)

button720 = tk.Button(text = "720p" , command = indir720 , bg = "gray", fg = c_white , relief = tk.RAISED , pady = 25 , padx = 110 , cursor = 'dotbox')
button720.place(y = 126 , x = 0)
#button720.pack()
"""
button720.bind("<Enter>", on_enter)
button720.bind("<Leave>", on_leave)

button'a hover olduğunda olacakları belirler
on_enter ve on_leave fonksiyonların adı
bir gün belki lazım olur diye silmedim
"""

button1080 = tk.Button(text = "1080p" , command = indir1080 , bg = "green" , fg = c_white , relief = tk.RAISED , pady = 25 , padx = 125 , cursor = 'dotbox')
button1080.place(y = 126 , x = 250)
#button1080.pack(side = tk.BOTTOM)

penecere.mainloop()
