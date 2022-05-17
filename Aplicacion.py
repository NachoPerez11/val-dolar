from tkinter import *

import tkinter as tk

from tkinter import ttk, font

import requests

from _datetime import datetime


class App:
    __ventana = None
    __valoresventa = []
    __valorescompra = []
    __valoresnombre = []
    __hora = None

    def __init__(self):
        # Creo una ventana
        self.__ventana = tk.Tk()
        self.__ventana.title('')
        self.__ventana.geometry('500x490')
        frames = {'fill': 'both', 'expand': 'True'}
        labels = {'padx': '5', 'pady': '5'}
        fuente1 = font.Font(weight='bold', size=18)
        fuente2 = font.Font(weight='bold', size=12)
        self.cargardatos()

        # Frame 1
        frame1 = tk.Frame(self.__ventana, background='#85bb65')
        frame1.pack(**frames)
        frame1['borderwidth'] = 0
        ttk.Label(frame1, text='Moneda', font=fuente1, background='#85bb65',
                  foreground='white').pack(side=LEFT, padx=15)
        ttk.Label(frame1, text='Venta', font=fuente1, background='#85bb65',
                  foreground='white').pack(side=RIGHT, padx=15)
        ttk.Label(frame1, text='Compra', font=fuente1, background='#85bb65',
                  foreground='white').pack(side=RIGHT, padx=15)

        # Frame 2
        frame2 = tk.Frame(self.__ventana, background='#e4e8d1')
        frame2.pack(**frames)
        frame2['borderwidth'] = 0
        for i in range(len(self.__valoresnombre)):
            a = tk.Frame(self.__ventana, background='#e4e8d1')
            a.pack(**frames)
            a['borderwidth'] = 0
            ttk.Style().configure('TSeparator', background='#85bb65')
            ttk.Separator(a, orient=HORIZONTAL).pack(side=TOP, ipadx=300, pady=0, padx=0, fill=X, expand=True)
            tk.Label(a, textvariable=self.__valoresnombre[i], background='#e4e8d1',
                     foreground='gray', font=fuente2).pack(side=LEFT, padx=10, pady=5)
            tk.Label(a, textvariable=self.__valoresventa[i], background='#e4e8d1',
                     foreground='gray', font=fuente2).pack(side=RIGHT, padx=10, pady=5)
            tk.Label(a, textvariable=self.__valorescompra[i], background='#e4e8d1',
                     foreground='gray', font=fuente2).pack(side=RIGHT, padx=10, pady=5)

        # Frame 3
        frame3 = tk.Frame(self.__ventana, background='#e4e8d1')
        frame3.pack(side=BOTTOM, fill=BOTH, expand=True)
        frame3['borderwidth'] = 0
        ttk.Style().configure('TSeparator', background='#85bb65')
        ttk.Separator(frame3, orient=HORIZONTAL).pack(side=TOP, ipadx=300, pady=5, fill=X, expand=True)
        tk.Button(frame3, text='Actualizar', background='#159a58', foreground='white',
                  command=self.borrarlista, font=fuente2).pack(side=LEFT, **labels, ipadx=25)
        tk.Label(frame3, textvariable=self.__hora, font=fuente2,
                 foreground='gray', bg='#e4e8d1').pack(side=RIGHT, **labels)
        tk.Label(frame3, text='Actualizado', font=fuente2, foreground='gray',
                 bg='#e4e8d1').pack(side=RIGHT, padx=10)
        self.__ventana.mainloop()

    def cargardatos(self):
        r = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
        datos = r.json()
        for i in range(len(datos)):
            if datos[i]['casa']['nombre'].find('Dolar') == 0:
                if datos[i]['casa']['compra'].lower() != 'no cotiza':
                    self.__valoresventa.append(StringVar(value=datos[i]['casa']['venta']))
                    self.__valorescompra.append(StringVar(value=datos[i]['casa']['compra']))
                    self.__valoresnombre.append(StringVar(value=datos[i]['casa']['nombre']))
        self.__hora = StringVar()
        horas = datetime.now()
        if len(str(horas.minute)) == 1:
            self.__hora.set('{} / {} / {}  {}:{}'.format(horas.day, horas.month, horas.year, horas.hour, "0" + str(horas.minute)))
        else:
            self.__hora.set(
                '{} / {} / {}  {}:{}'.format(horas.day, horas.month, horas.year, horas.hour, horas.minute))

    def borrarlista(self):
        self.__valoresventa = []
        self.__valoresnombre = []
        self.__valorescompra = []
        self.cargardatos()
