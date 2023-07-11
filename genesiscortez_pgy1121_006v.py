# -*- coding: utf-8 -*-
"""GenesisCortez_PGY1121_006V

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pYDHXfuFyEvB8YoRyRL7hlJowsmuirCq
"""

deptos = np.array([
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
    [['','valor: UF 3800',''], ['','valor: UF 3000',''], ['','valor: UF 2800',''],['', 'valor: UF 3500']],
])
def mostrar_menu():
  print("------Departamentos------")
  print("1. Comprar Departamentos")
  print("2. Mostrar Departamentos disponibles")
  print("3. Ver listado de compradores")
  print("4. Mostrar ganancias totales")
  print("5. Salir")
  opcion = input("Seleccione una opción: ")

def mostrar_deptos():
    print("Departamentos Disponibles:")
    for i in range(4):
        for j in range(5):
            if deptos_vendidos[i][j]:
                print("[X]", end=" ")
            else:
                print(deptos_disponibles[i][j], end=" ")
        print()

def seleccionar_depto():
    mostrar_depto()
    fila = int(input("Ingrese el número de piso del 1 al 10: "))
    area = int(input("Ingrese A, B, C, D: "))

    if fila < 1 or fila > 4 or area < 1 or area > 5:
        print("Coordenadas inválidas. Por favor, ingrese nuevamente.")
        return

    if deptos_vendidos[fila - 1][area - 1]:
        print("El departamento seleccionado no está disponible.")
    else:
        print("Opción inválida. Inténtelo de nuevo.")

class depto:
    def __init__(self, numero_depto, precio, estado):
        self.numero_depto = numero_class Terreno:
    def __init__(self, numero_lote, area, precio, estado):
        self.numero_lote = numero_lote
        self.area = area
        self.precio = precio
        self.estado = estado  # Puede ser "Disponible" o "Vendido"

class Loteo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.deptos_disponibles = []

    def agregar_depto(self, depto):
        self.deptos_disponibles.append(deptos)

    def mostrar_deptos_disponibles(self):
        if not self.deptos_disponibles:
            print("No hay Departamentos disponibles.")
        else:
            print("Departamentos disponibles:")
            for depto in self.deptos_disponibles:
                print(f"Número de piso: {depto.numero_piso}")
                print(f"Área: {depto.area}")
                print(f"Precio: ${depto.precio}")
                print(f"Estado: {depto.estado}")
                print("--------------")

    def vender_depto(self, numero_piso):
        for depto in self.deptos_disponibles:
            if depto.numero_piso == numero_piso:
                depto.estado = "Vendido"
                self.deptos_disponibles.remove(depto)
                print(f"Departamento número {numero_piso} vendido exitosamente.")
                return
        print(f"No se encontró el terreno número {numero_piso}.")

piso1 = piso("piso Ejemplo")

depto1 = depto(1, A, "UF",3800, "Disponible")
depto2 = depto(2, B, "UF" 3000, "Disponible")
piso1.agregar_depto(depto1)
piso1.agregar_depto(depto2)

piso1.mostrar_deptos_disponibles()

piso1.vender_depto(1)

piso1.mostrar_deptos_disponibles()
        self.area = area
        self.precio = precio
        self.estado = estado

class piso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.deptos_disponibles = []

    def agregar_depto(self, depto):
        self.deptos_disponibles.append(depto)

    def mostrar_deptos_disponibles(self):
        if not self.deptos_disponibles:
            print("No hay Departamentos disponibles.")
        else:
            print("Departamentos disponibles:")
            for depto in self.deptos_disponibles:
                print(f"Número de piso: {depto.numero_piso}")
                print(f"Área: {depto.area} m²")
                print(f"Precio: ${depto.precio}")
                print(f"Estado: {depto.estado}")
                print("--------------")

    def vender_terreno(self, numero_lote):
        for depto in self.depto_disponibles:
            if depto.numero_piso == numero_piso:
                depto.estado = "Vendido"
                self.deptos_disponibles.remove(depto)
                print(f"Departamento número {numero_piso} vendido exitosamente.")
                return
        print(f"No se encontró el departamento número {numero_piso}.")