


def terfogat():
    
    def szamit():
        cucc=mezo1.get()
        if len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        cucc=mezo2.get()
        if  len(cucc) == 0:
            messagebox.showerror('Error message box', "üres a mező ")
        else:
            pass  
        cucc=int(cucc)

        a = eval(mezo1.get())
        b = eval(mezo2.get())
        c = eval(mezo3.get())
        terfogat = a**2
        mezo4.delete(0,END)
        mezo4.insert(0,str(terfogat))
    abl3=Toplevel(foablak)
    abl3.title("A Négyzet térfogata")
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
    abl3.mainloop()

#Terület vége

