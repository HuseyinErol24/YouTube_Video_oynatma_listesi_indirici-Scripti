from selenium import webdriver

import time

from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

from pytube import YouTube

import time

import colorama

class youtube():
    
    def __init__(self,k):
        if(k!=1):
         self.tarayici = webdriver.Firefox()
         self.link = []
         self.indirmebaglantısı = []
         time.sleep(1)
        else:
            pass
    
    def linkegit(self,link):
        self.tarayici.get(link)
        time.sleep(3)
    
    def htmlal(self):
        time.sleep(2)
        return self.tarayici.page_source
    
    def linkcek(self):
        düzenlihtml = BeautifulSoup(self.htmlal(),"html.parser")
        gerekli = düzenlihtml.find("ytd-two-column-browse-results-renderer").find("div",{"id":"primary"}).find("div",{"id":"contents"}).find("div",{"id":"contents"}).find_all("ytd-playlist-video-renderer")
        for i in gerekli:
           gecicilink = i.find("div",{"id":"content"}).find("div",{"id":"container"}).find("ytd-thumbnail").find("a").get("href")
           self.linkkontrol(gecicilink)

    def linkkontrol(self,link):
        if(self.link.count(link)==0):
            self.link.append(link)
        else:
            pass
    
    def kaydir(self,m):
        self.tarayici.execute_script(f"window.scrollTo(0, {m})")
    
    def videosayisi(self):
        time.sleep(2)
        y = self.tarayici.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-playlist-header-renderer/div/div[2]/div[1]/div/div[1]/div[1]/ytd-playlist-byline-renderer/div/yt-formatted-string[1]').text
        gecicideegisken= y.split(" ")
        self.videosayisim = int(gecicideegisken[0])
        #print("oynatma listesindeki video sayisi ",self.videosayisi)
        return self.videosayisim
    
    def string(self):
        print("oynatma listsindeki video sayisi ",self.videosayisi())
    
    
    def son(self):
        m = 0
        while self.videosayisi()>=len(self.link):
           self.htmlal()
           self.linkcek()
           self.kaydir(m)
           m +=600
           if(self.videosayisi()==len(self.link)):
               break
           else:
               continue 
        
    def yazdir(self):
        a = f" {len(self.link)} adet videonun linki çekildi "
        print(a.center(100,"*"))
        print("\n")
        for i in self.link:
            self.indirmebaglantısı.append("https://www.youtube.com"+i)
        #indirme baglantısının tüm linkleri geldi  burdaki linkleri indiricek
    
    def oynatmalistesivideoindir(self,indirmesekli):
       if(indirmesekli == "mp4"):
           for i in self.indirmebaglantısı:
                time.sleep(0.4)
                YouTube(i).streams.get_highest_resolution().download()
                
                yt = YouTube(i)
                print(colorama.Fore.GREEN,f"{yt.title} baslikli video indirildi")
                print(colorama.Fore.YELLOW)
                time.sleep(0.3)

       if(indirmesekli=="mp3"):
           for i in self.indirmebaglantısı:
                time.sleep(0.4)
                YouTube(i).streams.get_audio_only().download()#get_auidy_only sadece sesleri alıyor
                yt = YouTube(i)
                
                print(colorama.Fore.GREEN,f"{yt.title} baslikli video indirildi")
                print(colorama.Fore.YELLOW)
                time.sleep(0.3)
   
    def videoindir(self,videonunlinki,indirmesekli):
        if(indirmesekli=="mp3"):
            YouTube(videonunlinki).streams.get_audio_only().download()
            yt = YouTube(videonunlinki)
            
            print(colorama.Fore.GREEN,f"{yt.title} baslikli vide indirildi") 
            print(colorama.Fore.YELLOW)
            time.sleep(0.3)
        
        else:
            YouTube(videonunlinki).streams.get_highest_resolution().download() 
            yt = YouTube(videonunlinki)
            
            print(colorama.Fore.GREEN,f"{yt.title} baslikli video indirildi")
            print(colorama.Fore.YELLOW)
            time.sleep(0.3)                
    
    def __del__(self):
        print("\n\ndisctuctor calişiyor ... \nnesene silindi....")
  
        
k = int(input("video indirmke için 1 \noynatma listesinin tamamını indirmek için 0 basın : "))       

if(k==0):
 
 link = input("oynatma listesinin linkini giriniz = ")
 indirmesekli = input("oynatma listesini mp4 olarak indirmek için mp4 mp3 olarak indirmek için mp3 yazın : ")
 t = youtube(k)
 t.linkegit(link)
 t.videosayisi()
 t.string()
 t.son()
 t.yazdir()
 t.oynatmalistesivideoindir(indirmesekli)
 
elif(k==1):
    
    link = input("videonun linkini giriniz = ")
    indirmesekli = input("videonun mp4 olarak indirmek için mp4 mp3 olarak indirmek için mp3 yazın : ")
    t = youtube(k)
    t.videoindir(link,indirmesekli)

del t
