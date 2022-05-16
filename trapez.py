from tkinter import *


def trapezK ():
    def szamitas ():
        if aE.get() == '' or bE.get() == '' or cE.get() == '' or dE.get() == '' or mE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            a = float(aE.get())
            b = float(bE.get())
            c = float(cE.get())
            d = float(dE.get())
            m = float(mE.get())

            if a <= 0 or b <= 0 or c <= 0 or d <= 0 or m <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                A = 2 * (a*b + b*c + a*c)
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
        mE.delete (0, END)
        eredmenyE.delete (0, END)

    trapez = Tk ()

    trapez.title ('Trapéz')
    trapez.minsize (width=300, height=100)

    aL = Label (trapez, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (trapez, width=27)
    aE.grid (column=2, row=1)

    bL = Label (trapez, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (trapez, width=27)
    bE.grid (column=2, row=2)

    cL = Label (trapez, text='c:')
    cL.grid (column=1, row=3, sticky=E)
    cE = Entry (trapez, width=27)
    cE.grid (column=2, row=3)

    dL = Label (trapez, text='d:')
    dL.grid (column=1, row=4, sticky=E)
    dE = Entry (trapez, width=27)
    dE.grid (column=2, row=4)

    '''mL = Label (trapez, text='b:')
    mL.grid (column=1, row=5, sticky=E)
    mE = Entry (trapez, width=27)
    mE.grid (column=2, row=5)'''

    eredmenyL = Label (trapez, text='Eredmény:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (trapez, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (trapez, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (trapez, text='Kilépés', command=trapez.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (trapez, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    trapez.mainloop ()

trapezK ()