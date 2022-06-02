###Proyecto INGENIERIA DE SOFTWARE ENERO - JUNIO 2022
### CREADO POR:
### SAMUEL VELAZQUEZ RAMIREZ
### JOSE ANTONIO RIVERA DE LA LUZ
### MARIA BELEN TORICES VELAZQUEZ


from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class Papeleria_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#fd7e1b")
        self.root.title("Sistema de Registro de ventas")
        title = Label(self.root, text="Papeleria Don Quijote", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#3891c8", fg="white").pack(fill=X)
        # ===================================Variables=======================================================================================
        self.Lapiz = IntVar()
        self.Goma = IntVar()
        self.Tijeras = IntVar()
        self.Pegamento = IntVar()
        self.HojasBlancas = IntVar()
        self.HojasColor = IntVar()
        self.Pluma = IntVar()
        self.Libreta = IntVar()
        self.Libro = IntVar()
        self.Comic = IntVar()
        self.Revista = IntVar()
        self.Calendario = IntVar()
        self.Carpeta = IntVar()
        self.Diccionario = IntVar()
        self.Paqhojas = IntVar()
        self.Paqclips = IntVar()
        self.Paqplumas = IntVar()
        self.Paqlapiz = IntVar()
        self.Paqgrapa = IntVar()
        self.Paqtinta = IntVar()
        self.Paqgeo = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()
        # ==========================================Detalles de customizacion=================================================
        details = LabelFrame(self.root, text="Detalles del Cliente", font=(
            "Arial Black", 12), bg="#3891c8", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Nombre del Cliente", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=0, padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="No Contacto", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.phone).grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="No de Factura", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=4, padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.bill_no).grid(row=0, column=5, padx=8)
        # =======================================Productos Simples=================================================================
        producto = LabelFrame(self.root, text="Productos Simples 5%", font=(
            "Arial Black", 12), bg="#3891c8", fg="#ffffff", relief=GROOVE, bd=10)
        producto.place(x=5, y=180, height=380, width=325)

        item1 = Label(producto, text="Lapiz", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item1_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.Lapiz).grid(row=0, column=1, padx=10)

        item2 = Label(producto, text="Goma", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item2_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.Goma).grid(row=1, column=1, padx=10)

        item3 = Label(producto, text="Tijeras", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item3_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.Tijeras).grid(row=2, column=1, padx=10)

        item4 = Label(producto, text="Pegamento", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item4_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.Pegamento).grid(row=3, column=1, padx=10)

        item5 = Label(producto, text="Hojas Blancas", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item5_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.HojasBlancas).grid(row=4, column=1, padx=10)

        item6 = Label(producto, text="Hojas de Color", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item6_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.HojasColor).grid(row=5, column=1, padx=10)

        item7 = Label(producto, text="Pluma", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item7_entry = Entry(producto, borderwidth=2, width=15,
                            textvariable=self.Pluma).grid(row=6, column=1, padx=10)
        # ===================================Libros=====================================================================================
        Libros = LabelFrame(self.root, text="Libros 10%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        Libros.place(x=340, y=180, height=380, width=325)

        item8 = Label(Libros, text="Libreta", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item8_entry = Entry(Libros, borderwidth=2, width=15,
                            textvariable=self.Libreta).grid(row=0, column=1, padx=10)

        item9 = Label(Libros, text="Libro", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item9_entry = Entry(Libros, borderwidth=2, width=15,
                            textvariable=self.Libro).grid(row=1, column=1, padx=10)

        item10 = Label(Libros, text="Comic", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item10_entry = Entry(Libros, borderwidth=2, width=15,
                             textvariable=self.Comic).grid(row=2, column=1, padx=10)

        item11 = Label(Libros, text="Revista", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item11_entry = Entry(Libros, borderwidth=2, width=15,
                             textvariable=self.Revista).grid(row=3, column=1, padx=10)

        item12 = Label(Libros, text="Calendario", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item12_entry = Entry(Libros, borderwidth=2, width=15,
                             textvariable=self.Calendario).grid(row=4, column=1, padx=10)

        item13 = Label(Libros, text="Carpeta", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item13_entry = Entry(Libros, borderwidth=2, width=15,
                             textvariable=self.Carpeta).grid(row=5, column=1, padx=10)

        item14 = Label(Libros, text="Diccionario", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item14_entry = Entry(Libros, borderwidth=2, width=15,
                             textvariable=self.Diccionario).grid(row=6, column=1, padx=10)
        # ========================================Empaquetados===============================================================================
        empq = LabelFrame(self.root, text="Empaquetados 7%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        empq.place(x=677, y=180, height=380, width=325)

        item15 = Label(empq, text="Paquete Hojas Blancas", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item15_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqhojas).grid(row=0, column=1, padx=10)

        item16 = Label(empq, text="Paquete clips", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item16_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqclips).grid(row=1, column=1, padx=10)

        item17 = Label(empq, text="Paquete Plumas", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item17_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqplumas).grid(row=2, column=1, padx=10)

        item18 = Label(empq, text="Paquete Lapices", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item18_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqlapiz).grid(row=3, column=1, padx=10)

        item19 = Label(empq, text="Paquete de grapas", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item19_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqgrapa).grid(row=4, column=1, padx=10)

        item20 = Label(empq, text="Paquete tintas", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item20_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqtinta).grid(row=5, column=1, padx=10)

        item21 = Label(empq, text="Juego Geometria", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item21_entry = Entry(empq, borderwidth=2, width=15,
                             textvariable=self.Paqgeo).grid(row=6, column=1, padx=10)
        # =====================================================billarea==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#3891c8")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Área de Facturación", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#3891c8", fg="#ffffff").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================menu=========================================================================================
        billing_menu = LabelFrame(self.root, text="Resumen de facturación", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_producto = Label(billing_menu, text="Precio Total Prod. Simp.", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=0)
        total_prodcuto_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_sna).grid(row=0, column=1, padx=10, pady=7)

        total_Libros = Label(billing_menu, text="Precio Total Libros", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=0)
        total_Libros_entry = Entry(billing_menu, width=30, borderwidth=2,
                                    textvariable=self.total_gro).grid(row=1, column=1, padx=10, pady=7)

        total_empq = Label(billing_menu, text="Precio Total Empaq.", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=0)
        total_empq_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_hyg).grid(row=2, column=1, padx=10, pady=7)

        tax_producto = Label(billing_menu, text="Impuesto", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=2)
        tax_producto_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(
            row=0, column=3, padx=10, pady=7)

        tax_Libros = Label(billing_menu, text="Impuesto", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=2)
        tax_Libros_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(
            row=1, column=3, padx=10, pady=7)

        tax_empq = Label(billing_menu, text="Impuesto", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=2)
        tax_empq_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(
            row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#fd7e1b")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Total Facturado", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Resetear", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Salir", font=("Arial Black", 15), pady=10, bg="#3891c8",
                             fg="#ffffff", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


def total(self):
    if (self.c_name.get == "" or self.phone.get() == ""):
        messagebox.showerror("Error", "Complete los datos del cliente!!")
    self.nu = self.Lapiz.get()*15
    self.no = self.Goma.get()*2.50
    self.la = self.Tijeras.get()*54
    self.ore = self.Pegamento.get()*20
    self.mu = self.HojasBlancas.get()*1
    self.si = self.HojasColor.get()*1.50
    self.na = self.Pluma.get()*18
    total_producto_price = (
        self.nu +
        self.no +
        self.la +
        self.ore +
        self.mu +
        self.si +
        self.na)
    self.total_sna.set(str(total_producto_price)+" ")
    self.a.set(str(round(total_producto_price*0.05, 3))+" ")

    self.at = self.Libreta.get()*35
    self.pa = self.Libro.get()*350
    self.oi = self.Revista.get()*75
    self.ri = self.Comic.get()*500
    self.su = self.Calendario.get()*150
    self.te = self.Diccionario.get()*150
    self.da = self.Carpeta.get()*100
    total_Libros_price = (
        self.at +
        self.pa +
        self.oi +
        self.ri +
        self.su +
        self.te +
        self.da)

    self.total_gro.set(str(total_Libros_price)+" ")
    self.b.set(str(round(total_Libros_price*0.1, 3))+" ")

    self.so = self.Paqhojas.get()*125
    self.sh = self.Paqclips.get()*45
    self.cr = self.Paqlapiz.get()*145
    self.lo = self.Paqplumas.get()*200
    self.fo = self.Paqgrapa.get()*55
    self.ma = self.Paqtinta.get()*749
    self.sa = self.Paqgeo.get()*120

    total_empq_price = (
        self.so +
        self.sh +
        self.cr +
        self.lo +
        self.fo +
        self.ma +
        self.sa)

    self.total_hyg.set(str(total_empq_price)+" ")
    self.c.set(str(round(total_empq_price*0.07, 3))+" ")
    self.total_all_bill = (total_producto_price +
                           total_Libros_price +
                           total_empq_price +
                           (round(total_Libros_price*0.1, 3)) +
                           (round(total_empq_price*0.07, 3)) +
                           (round(total_producto_price*0.05, 3)))
    self.total_all_bil = str(self.total_all_bill)+" "
    billarea(self)


def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(
        END, "\tBienvenid@ a tu papeleria\n\tTeléfono +427 159 6813")
    self.txtarea.insert(END, f"\n\nFactura Número. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nNombre Cliente : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nTeléfono No. : {self.phone.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProducto\t\tCant\tPrecio\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.Lapiz.get() != 0:
        self.txtarea.insert(
            END, f"Lapiz\t\t {self.Lapiz.get()}\t{self.nu}\n")
    if self.Goma.get() != 0:
        self.txtarea.insert(
            END, f"Goma\t\t {self.Goma.get()}\t{self.no}\n")
    if self.Tijeras.get() != 0:
        self.txtarea.insert(
            END, f"Tijeras\t\t {self.Tijeras.get()}\t{self.la}\n")
    if self.Pegamento.get() != 0:
        self.txtarea.insert(END, f"Pegamento\t\t {self.Pegamento.get()}\t{self.ore}\n")
    if self.HojasBlancas.get() != 0:
        self.txtarea.insert(
            END, f"Hojas Blancas\t\t {self.HojasBlancas.get()}\t{self.mu}\n")
    if self.HojasColor.get() != 0:
        self.txtarea.insert(
            END, f"HojasColor\t\t {self.HojasColor.get()}\t{self.si}\n")
    if self.Pluma.get() != 0:
        self.txtarea.insert(
            END, f"Pluma\t\t {self.Pluma.get()}\t{self.na}\n")
    if self.Libreta.get() != 0:
        self.txtarea.insert(END, f"Libreta\t\t {self.Libreta.get()}\t{self.at}\n")
    if self.Libro.get() != 0:
        self.txtarea.insert(END, f"Libro\t\t {self.Libro.get()}\t{self.pa}\n")
    if self.Comic.get() != 0:
        self.txtarea.insert(
            END, f"Comic\t\t {self.Comic.get()}\t{self.ri}\n")
    if self.Revista.get() != 0:
        self.txtarea.insert(
            END, f"Revista\t\t {self.Revista.get()}\t{self.oi}\n")
    if self.Calendario.get() != 0:
        self.txtarea.insert(
            END, f"Calendario\t\t {self.Calenadario.get()}\t{self.su}\n")
    if self.Carpeta.get() != 0:
        self.txtarea.insert(
            END, f"Carpeta\t\t {self.Carpeta.get()}\t{self.da}\n")
    if self.Diccionario.get() != 0:
        self.txtarea.insert(
            END, f"Diccionario\t\t {self.Diccionario.get()}\t{self.te}\n")
    if self.Paqhojas.get() != 0:
        self.txtarea.insert(END, f"Paqhojas\t\t {self.Paqhojas.get()}\t{self.so}\n")
    if self.Paqclips.get() != 0:
        self.txtarea.insert(
            END, f"Paqclips\t\t {self.Paqclips.get()}\t{self.sh}\n")
    if self.Paqplumas.get() != 0:
        self.txtarea.insert(
            END, f"Paqplumas\t\t {self.Paqplumas.get()}\t{self.lo}\n")
    if self.Paqlapiz.get() != 0:
        self.txtarea.insert(
            END, f"Paqlapiz\t\t {self.Paqlapiz.get()}\t{self.cr}\n")
    if self.Paqgrapa.get() != 0:
        self.txtarea.insert(
            END, f"Paqgrapa\t\t {self.Paqgrapa.get()}\t{self.fo}\n")
    if self.Paqtinta.get() != 0:
        self.txtarea.insert(
            END, f"Máscara-Facial\t\t {self.Paqtinta.get()}\t{self.ma}\n")
    if self.Paqgeo.get() != 0:
        self.txtarea.insert(
            END, f"JuegGeo\t\t {self.Paqgeo.get()}\t{self.sa}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 ":
        self.txtarea.insert(END, f"Total imp: {self.a.get()}\n")
    if self.b.get() != "0.0 ":
        self.txtarea.insert(
            END, f"Total Imp: {self.b.get()}\n")
    if self.c.get() != "0.0 ":
        self.txtarea.insert(
            END, f"Total Imp: {self.c.get()}\n")
    self.txtarea.insert(END, f"Monto total facturado : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.Lapiz.set(0)
    self.Goma.set(0)
    self.Tijeras.set(0)
    self.Pegamento.set(0)
    self.HojasBlancas.set(0)
    self.HojasColor.set(0)
    self.Pluma.set(0)
    self.Libreta.set(0)
    self.Libro.set(0)
    self.Comic.set(0)
    self.Revista.set(0)
    self.Calendario.set(0)
    self.Carpeta.set(0)
    self.Diccionario.set(0)
    self.Paqhojas.set(0)
    self.Paqclips.set(0)
    self.Paqplumas.set(0)
    self.Paqlapiz.set(0)
    self.Paqgrapa.set(0)
    self.Paqtinta.set(0)
    self.Paqgeo.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = Tk()
obj = Papeleria_App(root)
root.mainloop()
