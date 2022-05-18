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
                K = round (2 * (a + b), 2)
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, str(K))

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

    paralelogrammaker = Tk ()

    paralelogrammaker.title ('Paralelogramma kerülete')
    paralelogrammaker.minsize (width=300, height=100)

    aL = Label (paralelogrammaker, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (paralelogrammaker, width=27)
    aE.grid (column=2, row=1)

    bL = Label (paralelogrammaker, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (paralelogrammaker, width=27)
    bE.grid (column=2, row=2)

    eredmenyL = Label (paralelogrammaker, text='Kerület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (paralelogrammaker, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (paralelogrammaker, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (paralelogrammaker, text='Kilépés', command=paralelogrammaker.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (paralelogrammaker, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    paralelogrammaker.mainloop ()



def terulet ():
    def szamitas ():
        if aE.get() == '' or maE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            ma = float(bmaE.get())

            if a <= 0 or ma <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                T = round (a * ma, 2)
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, str(T))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        aE.delete (0, END)
        maE.delete (0, END)
        eredmenyE.delete (0, END)

    paralelogrammater = Tk ()

    paralelogrammater.title ('Paralelogramma területe')
    paralelogrammater.minsize (width=300, height=100)

    aL = Label (paralelogrammater, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (paralelogrammater, width=27)
    aE.grid (column=2, row=1)

    maL = Label (paralelogrammater, text='m:')
    maL.grid (column=1, row=2, sticky=E)
    maE = Entry (paralelogrammater, width=27)
    maE.grid (column=2, row=2)

    eredmenyL = Label (paralelogrammater, text='Terület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (paralelogrammater, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (paralelogrammater, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (paralelogrammater, text='Kilépés', command=paralelogrammater.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (paralelogrammater, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    paralelogrammater.mainloop ()

kerulet()