import Tkinter as Tk # dobre informacije za Tkinter so na effbot
import tkMessageBox

def klik_gumba1():
    raz_milje = float(vpis.get()) * 1.6
    tkMessageBox.showinfo("Rezultat", "Razdalja v miljah: %s" % raz_milje)
    vpis.delete(0, Tk.END)

def klik_gumba2():
    raz_km = float(vpis.get()) / 1.6
    tkMessageBox.showinfo("Rezultat", "Razdalja v km: %s" % raz_km)
    vpis.delete(0, Tk.END)


main_window = Tk.Tk() # naredimo glavno okno
greeting = Tk.Label(main_window, text="Pretvornik enot iz km v milje in obratno")
greeting2 = Tk.Label(main_window, text="Vpisi razdaljo:")
gumb1 = Tk.Button(main_window, text="Pretvorba v milje", command=klik_gumba1) # v command dodamo funkcijo
gumb2 = Tk.Button(main_window, text="Pretvorba v km", command=klik_gumba2) # v command dodamo funkcijo

vpis = Tk.Entry(main_window)

greeting.pack()
greeting2.pack()
vpis.pack()
gumb1.pack()
gumb2.pack()

#ent.delete(0, END)



main_window.mainloop()