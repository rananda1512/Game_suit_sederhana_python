import numpy as np
import random
from time import sleep
import time

data1=[]
pil=["batu","gunting","kertas"]

#definisikan class queue menggunakan array
class queue():
    def __init__(self,data):
        self.data=np.array(data)
        self.menang=0
        self.kalah=0
        self.draw=0
        self.pil=["batu","gunting","kertas"]
        self.countGame=1

    #fungsi menambahkan data dibelakang queue
    def add(self,data):
        self.data=np.append(self.data,data)
    
    def delete(self):
        self.data=np.delete(self.data,0)

    #fungsi untuk mengecek menang atau kalah
    def check(self,bot):
        print(f"\t\t{str(self.pil[self.data[0]-1])} VS {str(self.pil[bot-1])}")
        if self.data[0]==1:
            if bot==1:
                self.draw+=1
                print("\t\tdraw")
            elif bot==2:
                self.menang+=1
                print("\t\tmenang")
            elif bot==3:
                self.kalah+=1
                print("\t\tkalah")
        elif self.data[0]==2:
            if bot==1:
                self.kalah+=1
                print("\t\tkalah")
            elif bot==2:
                self.draw+=1
                print("\t\tdraw")
            elif bot==3:
                self.menang+=1
                print("\t\tmenang")
        elif self.data[0]==3:
            if bot==1:
                self.menang+=1
                print("\t\tmenang")
            elif bot==2:
                self.kalah+=1
                print("\t\tkalah")
            elif bot==3:
                self.draw+=1
                print("\t\tdraw")
                
    #fungsi mengetahui hasil apakah kita akan menang melawan bot
    def result(self,bot):
        bot=random.randrange(1,4,1) # nilai bot akan terus berubah ubah selama fungsi di panggil
        if len(self.data)>0:
            print(f"Game ke {self.countGame}")
            self.check(bot)
            self.delete()
            print(f"game selanjutnya akan dimulai dalam dalam hitungan 2 detik") if len(self.data) >= 1 else None
            if len(self.data)<1:
                print("")
            else:
                for i in range(2):
                    time.sleep(2)
                    print(i,"detik")
            print("-"*50)
            self.countGame+=1
            self.result(bot) #memanggil kembali dirinya untuk mengatahui hasil yang akan didapat
        else:
            print("selesai")
        return self.kalah,self.menang,self.draw



print("WELCOME IN GAME BATU GUNTING KERTAS")
while True:
    bot=random.randrange(1,4,1)
    print("Menu")
    print("-"*50)
    print("1.Main 1 game")
    print("2.Main 5 game sekaligus")
    print("3.Keluar")
    pilMenu=int(input("Masukkan pilihan menu :"))
    if(pilMenu==1):
        while True:
            weapon=int(input("Pilih Senjata mu (1=batu,2=gunting,3=kertas) = "))
            if weapon >3 or weapon<1:
                print("tidak ada senjata")
            else:
                break
        data1.append(weapon)
        a=queue(data1)
        a.check(bot)
        data1.pop(0) # membuat list akan empty karena arry mengambil data dari list
    elif(pilMenu==2):
            for i in range(5):
                while True:
                    weapon=int(input("Pilih Senjata mu (1=batu,2=gunting,3=kertas) = "))
                    if weapon >3 or weapon<1:
                        print("tidak ada senjata")
                    else:
                        break
                data1.append(weapon)
            a=queue(data1)
            a.result(random.randrange(1,4,1))
            print(f"Menang = {a.menang} Kalah = {a.kalah} Seri = {a.draw}")
            data1=[]
    elif(pilMenu==3):
            print("ok selamat tinggal")
            break
    

# a.result(random.randrange(1,4,1))   #menggunakan nilai random 1-3 untuk menentukan pilihan bot
