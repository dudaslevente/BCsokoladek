from tkinter import *
from tkinter import messagebox
import math



def kerulet():
    
    def szamit():
        hiba=mezo1.get()
        if len(hiba) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        hiba=int(hiba)

        r = eval(mezo1.get())
       #b = eval(mezo2.get())
       #c = eval(mezo3.get())
        kerulet  = 2*math.pi*r
        mezo4.delete(0,END)
        mezo4.insert(0,str(kerulet))
    abl3=Tk()
    abl3.title("A Kör kerülete")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="r")
   #szoveg2 = Label(abl3, text="b")
   #szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
   #mezo2 = Entry(abl3)
   #mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
   #szoveg2.grid(row=2)
   #szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
   #mezo2.grid(row=2, column=2)
   #mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()

    #Kerület vége
def terulet():
    
    def szamit():
        hiba=mezo1.get()
        if len(hiba) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        hiba=int(hiba)

        r = eval(mezo1.get())
        #b = eval(mezo2.get())
        #c = eval(mezo3.get())
        terulet = math.pi*r**2
        mezo4.delete(0,END)
        mezo4.insert(0,str(terulet))
    abl3=TK()
    abl3.title("A Kör területe")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="r")
  # szoveg2 = Label(abl3, text="b")
  # szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
   #mezo2 = Entry(abl3)
   #mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
   #szoveg2.grid(row=2)
   #szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
   #mezo2.grid(row=2, column=2)
   #mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    abl3.mainloop()


#Térfogat vége

   

"""
#Főablak
foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height=100)

menusor = Frame(foablak)
menusor.pack(side=TOP, fill=X)

menu2 = Menubutton(menusor, text="Kör", underline=0)
menu2.pack(side = LEFT)
kor=Menu(menu2)
kor.add_command(label="Kerület", command = kerulet, underline=0)
kor.add_command(label="Terület", command = terulet, underline=0)

menu2.config(menu = kor)

"""

foablak.mainloop()