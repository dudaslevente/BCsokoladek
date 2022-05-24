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

    deltoidker = Tk ()

    deltoidker.title ('Deltoid kerülete')
    deltoidker.minsize (width=300, height=100)

    aL = Label (deltoidker, text='a:')
    aL.grid (column=1, row=1, sticky=E)
    aE = Entry (deltoidker, width=27)
    aE.grid (column=2, row=1)

    bL = Label (deltoidker, text='b:')
    bL.grid (column=1, row=2, sticky=E)
    bE = Entry (deltoidker, width=27)
    bE.grid (column=2, row=2)

    eredmenyL = Label (deltoidker, text='Kerület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (deltoidker, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (deltoidker, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (deltoidker, text='Kilépés', command=deltoidker.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (deltoidker, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    deltoidker.mainloop ()



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
                T = round ((e * f) / 2, 2)
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

    deltoidter = Tk ()

    deltoidter.title ('Deltoid területe')
    deltoidter.minsize (width=300, height=100)

    eL = Label (deltoidter, text='e:')
    eL.grid (column=1, row=1, sticky=E)
    eE = Entry (deltoidterr, width=27)
    eE.grid (column=2, row=1)

    fL = Label (deltoidter, text='f:')
    fL.grid (column=1, row=2, sticky=E)
    fE = Entry (deltoidter, width=27)
    fE.grid (column=2, row=2)

    eredmenyL = Label (deltoidter, text='Terület:')
    eredmenyL.grid (column=1, row=6, sticky=E)
    eredmenyE = Entry (deltoidter, width=27)
    eredmenyE.grid (column=2, row=6)

    szamitasB = Button (deltoidter, text='Számítás', command=hülyee)
    szamitasB.grid (column=2, row=7, sticky=W)

    kilepB = Button (deltoidterr, text='Kilépés', command=deltoidter.destroy)
    kilepB.grid (column=2, row=7, sticky=E)

    törlesB = Button (deltoidter, text='Törlés', command=törles)
    törlesB.grid (column=1, row=7)

    deltoidter.mainloop ()

