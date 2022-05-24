from tkinter import *

def kerulet ():
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
                K = round (4*a)
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
        eredmenyE.delete (0, END)

    rombuszker = Tk ()

    rombuszker.title ('Rombusz kerülete')
    rombuszker.minsize (width=300, height=100)

    aL = Label (rombuszker, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (rombuszker, width=27)
    aE.grid (column=2, row=1)

    eredmenyL = Label (rombuszker, text='Kerület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (rombuszker, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (rombuszker, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (rombuszker, text='Kilépés', command=rombuszker.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (rombuszker, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    rombuszker.mainloop ()



def terulet ():
    def szamitas ():
        if eE.get() == '' or fE.get() == '':
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Adjon meg adatokat.' )
        else:
            e = float(eE.get())
            f = float(fE.get())

            if e <= 0 or f <= 0:
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, 'Nincs értelme a számításnak.' )
            else:
                T = round (e*f/2)
                eredmenyE.delete (0, END)
                eredmenyE.insert (0, str(T))

    def hülyee ():
        try:
            szamitas ()
        except:
            eredmenyE.delete (0, END)
            eredmenyE.insert (0, 'Nincs értelme a számításnak.' )

    def törles ():
        eE.delete (0, END)
        fE.delete (0, END)
        eredmenyE.delete (0, END)

    rombuszter = Tk ()

    rombuszter.title ('Rombusz területe')
    rombuszter.minsize (width=300, height=100)

    eL = Label (rombuszter, text='e:')
    eL.grid (column=1, row=1, sticky=E)
    eE = Entry (rombuszter, width=27)
    eE.grid (column=2, row=1)

    fL = Label (rombuszter, text='f:')
    fL.grid (column=1, row=2, sticky=E)
    fE = Entry (rombuszter, width=27)
    fE.grid (column=2, row=2)

    eredmenyL = Label (rombuszter, text='Terület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (rombuszter, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (rombuszter, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (rombuszter, text='Kilépés', command=rombuszter.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (rombuszter, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    rombuszter.mainloop ()