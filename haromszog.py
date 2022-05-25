from tkinter import *
from tkinter import messagebox
import math
import turtle



def kerulet():
    
    def szamit():
        hiba=mezo1.get()
        if len(hiba) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        hiba=int(hiba)

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        kerulet  = a+b+c
        mezo4.delete(0,END)
        mezo4.insert(0,str(kerulet))
    abl3=Tk()
    abl3.title("A Háromszög kerülete")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
    szoveg2 = Label(abl3, text="b")
    szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    c = Canvas(abl3, width=120, height=115, bg="white")
    c.create_polygon(63, 40, 50, 90, 80, 90, outline = "black", width=4, fill="white")  
    c.grid(row=1, column=4, rowspan=6)
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

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        #c = eval(mezo3.get())
        terulet = (a*b)/2
        mezo4.delete(0,END)
        mezo4.insert(0,str(terulet))
    abl3=Tk()
    abl3.title("A Háromszög területe")
    abl3.minsize(width=300, height=100)
    szoveg1 = Label(abl3, text="a")
    szoveg2 = Label(abl3, text="ma(A oldal magassága)")
    #szoveg3 = Label(abl3, text="c")
    szoveg4 = Label(abl3, text="Eredmeny")
    gomb1 = Button(abl3, text ="Számítás", command=szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    #mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row=1)
    szoveg2.grid(row=2)
    #szoveg3.grid(row=3)
    szoveg4.grid(row=5)
    gomb1.grid(row=4, column=2)
    mezo1.grid(row=1, column=2)
    mezo2.grid(row=2, column=2)
    #mezo3.grid(row=3, column=2)
    mezo4.grid(row=5, column=2)
    c = Canvas(abl3, width=120, height=115, bg="white")
    c.create_polygon(63, 40, 50, 90, 80, 90, outline = "black", width=4, fill="white")  
    c.grid(row=1, column=4, rowspan=6)
    abl3.mainloop()


#Térfogat vége



