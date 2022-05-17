from tkinter import *


def kerulet ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '' or cE.get() == '' or dE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            b = float(bE.get())
            c = float(cE.get())
            d = float(dE.get())

            if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                A = round (a + b + c + d, 2)
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
        cE.delete (0, END)
        dE.delete (0, END)
        eredmenyE.delete (0, END)

    trapezker = Tk ()

    trapezker.title ('Trapéz kerülete')
    trapezker.minsize (width=300, height=100)

    aL = Label (trapezker, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (trapezker, width=27)
    aE.grid (column=2, row=1)

    bL = Label (trapezker, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (trapezker, width=27)
    bE.grid (column=2, row=2)

    cL = Label (trapezker, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (trapezker, width=27)
    cE.grid (column=2, row=3)

    dL = Label (trapezker, text='d:')
    dL.grid (column=1, row=4, sticky=E)
    dE = Entry (trapezker, width=27)
    dE.grid (column=2, row=4)

    eredmenyL = Label (trapezker, text='Kerület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (trapezker, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (trapezker, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (trapezker, text='Kilépés', command=trapezker.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (trapezker, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    trapezker.mainloop ()



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
                A = round (a * ma, 2)
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
        maE.delete (0, END)
        eredmenyE.delete (0, END)

    trapezter = Tk ()

    trapezter.title ('Trapéz területe')
    trapezter.minsize (width=300, height=100)

    aL = Label (trapezter, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (trapezter, width=27)
    aE.grid (column=2, row=1)

    ma = Label (trapezter, text='m:')
    ma.grid (column=1, row=2, sticky=E)
    ma = Entry (trapezter, width=27)
    ma.grid (column=2, row=2)

    eredmenyL = Label (trapezter, text='Terület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (trapezter, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (trapezter, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (trapezter, text='Kilépés', command=trapezter.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (trapezter, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    trapezter.mainloop ()
