from tkinter import *

def kerulet ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            b = float(bE.get())

            if a <= 0 or b <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                A = round (2*(a+b))
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, str(A))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        aE.delete (0, END)
        bE.delete (0, END)
        eredmenyE.delete (0, END)

    teglalapker = Tk ()

    teglalapker.title ('Trapéz kerülete')
    teglalapker.minsize (width=300, height=100)

    aL = Label (teglalapker, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (teglalapker, width=27)
    aE.grid (column=2, row=1)

    bL = Label (teglalapker, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (teglalapker, width=27)
    bE.grid (column=2, row=2)

    eredmenyL = Label (teglalapker, text='Kerület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (teglalapker, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (teglalapker, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (teglalapker, text='Kilépés', command=teglalapker.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (teglalapker, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    teglalapker.mainloop ()



def terulet ():
    def szamitas ():
        if aE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())

            if a <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                A = round (a*b)
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, str(A))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        aE.delete (0, END)
        eredmenyE.delete (0, END)

    teglalapter = Tk ()

    teglalapter.title ('Trapéz területe')
    teglalapter.minsize (width=300, height=100)

    aL = Label (teglalapter, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (teglalapter, width=27)
    aE.grid (column=2, row=1)

    ma = Label (teglalapter, text='m:')
    ma.grid (column=1, row=2, sticky=E)
    ma = Entry (teglalapter, width=27)
    ma.grid (column=2, row=2)

    eredmenyL = Label (teglalapter, text='Terület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (teglalapter, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (teglalapter, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (teglalapter, text='Kilépés', command=teglalapter.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (teglalapter, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    teglalapter.mainloop ()