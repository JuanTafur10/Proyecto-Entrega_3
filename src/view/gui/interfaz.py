import sys
sys.path.append("src")
from model.logic import *


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class ErrorFaltaDeDatos(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)


class Calculadora_de_ahorro(App):
    def build(self):
        contenedor = GridLayout(cols = 2)

        boton_para_calcular = Button()
        self.monto_inicial = TextInput()
        self.tasa_de_interes = TextInput()
        self.numero_de_periodos = TextInput() 
        self.aporte_periodico = TextInput()

        contenedor.add_widget(Label(text = "ingresa el monto inicial: "))
        contenedor.add_widget(self.monto_inicial)

        contenedor.add_widget(Label(text = "ingresa el aporte periodico: "))
        contenedor.add_widget(self.aporte_periodico)

        contenedor.add_widget(Label(text = "ingrese el numero de periodos en los que desea pagar: "))
        contenedor.add_widget(self.numero_de_periodos)

        contenedor.add_widget(Label(text = "ingresa la tasa de interes: "))
        contenedor.add_widget(self.tasa_de_interes)

        self.label_del_valor = Label(text="Aqui aparecera el calculo de tu ahorro")
        contenedor.add_widget(self.label_del_valor)
        contenedor.add_widget(boton_para_calcular)

        boton_para_calcular.bind(on_press=self.calcular_ahorro)

        return contenedor
    
    def calcular_ahorro(self, sender):
        try:
            self.validar_entradas()
            monto_inicial, tasa_de_interes, numero_de_periodos, aporte_periodico = float(self.monto_inicial.text), float(self.tasa_de_interes.text), float(self.numero_de_periodos.text), float(self.aporte_periodico.text)
            calcular = calcular_monto(monto_inicial, tasa_de_interes, numero_de_periodos, aporte_periodico)
            resultado = round(calcular)
            self.label_del_valor.text = str(resultado)
        except Exception as exp:
            self.label_del_valor.text = str(exp)
    
    def validar_entradas(self):
        if not self.monto_inicial.text.replace('.', '', 1).isdigit():
            raise ErrorFaltaDeDatos("Falta de monto inicial, ingrese un monto inicial mayor a cero")
        if not self.tasa_de_interes.text.replace('.', '', 1).isdigit():
            raise ErrorFaltaDeDatos("Falta de tasa de interes, ingrese una tasa de interes válida (puede incluir decimales)")
        if not self.numero_de_periodos.text.isdigit():
            raise ErrorFaltaDeDatos("Falta el numero de periodos, ingrese un numero de periodos mayor a cero")
        if not self.aporte_periodico.text.replace('.', '', 1).isdigit():
            raise ErrorFaltaDeDatos("Falta el aporte periodico, ingrese un aporte periodico válido (puede incluir decimales)")

if __name__ == "__main__":
    Calculadora_de_ahorro().run()
