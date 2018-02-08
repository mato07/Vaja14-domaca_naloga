# -*- coding: utf-8 -*-
# Program ki omogoča ugibanje glavnega mesta evropskih držav

import Tkinter as Tk # dobre informacije za Tkinter so na effbot
import tkMessageBox
from functools import partial
import random

main_window = Tk.Tk() # naredimo glavno okno


def preveri_drzavo(drzave_mesta_dict, ugibana_drzava):
    vpisano = vpis.get()
    if vpisano.lower() == drzave_mesta_dict[ugibana_drzava]:
        sporocilo = "Bravo, uganil si!"
    else:
        sporocilo = "Narobe, več sreče naslednjič."
    tkMessageBox.showinfo("Rezultat", sporocilo)

def izberi_nakljucno_drzavo(drzave_mesta_dict):
    # Izberemo nakljucno drzavo med 0 in dolzino vseh drzav
    # Pazi, randint vrne eno vec kot hocemo, zato damo -1
    cifra_drzave = random.randint(0,len(drzave_mesta_dict)-1)
    # Vrnemo to drzavo
    return drzave_mesta_dict.keys()[cifra_drzave]

drzave_mesta_dict = {
    "Slovenija":"ljubljana",
    "Avstrija":"dunaj",
    "Nemčija":"berlin",
    "Italija":"rim",
    "Madžarska":"budimpesta",
    "Francija":"pariz"
    }

napis1 = Tk.Label(main_window, text = "Pozdravljen v igrici: Glavna mesta držav")


drzava = izberi_nakljucno_drzavo(drzave_mesta_dict)

napis2 = Tk.Label(main_window, text = "Ugani glavno mesto drzave " + drzava + " ")

vpis = Tk.Entry(main_window)

gumb1 = Tk.Button(main_window, text="Preveri", command=partial(preveri_drzavo, drzave_mesta_dict, drzava))

napis1.pack()
napis2.pack()
vpis.pack()
gumb1.pack()

main_window.mainloop()

