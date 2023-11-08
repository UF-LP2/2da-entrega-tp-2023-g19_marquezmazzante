import sys
import time

from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget,QListWidgetItem
from src.readFiles import readPacients
from library.cPacient import cPacient

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 600)

        self.layout_principal = QVBoxLayout()

        # Layout para los rótulos
        layout_rotulos = QHBoxLayout()

        # Rótulos para las listas
        self.label_pacientes = QLabel("PACIENTEs")
        self.label_espera = QLabel("LISTA DE ESPERA")
        self.label_atendidos = QLabel("LISTA DE ATENDIDOS")

        layout_rotulos.addWidget(self.label_pacientes)
        layout_rotulos.addWidget(self.label_espera)
        layout_rotulos.addWidget(self.label_atendidos)

        # Layout para las listas
        layout_listas = QHBoxLayout()

        # Listas (inicialmente ocultas)
        self.listapacientes = QListWidget(self)
        self.listaespera = QListWidget(self)
        self.listaatendidos = QListWidget(self)

        # Ocultar inicialmente los titulos
        self.label_pacientes.hide()
        self.label_espera.hide()
        self.label_atendidos.hide()

        # Ocultar las listas inicialmente
        self.listapacientes.hide()
        self.listaespera.hide()
        self.listaatendidos.hide()

        layout_listas.addWidget(self.listapacientes)
        layout_listas.addWidget(self.listaespera)
        layout_listas.addWidget(self.listaatendidos)

        # Botón para iniciar simulación
        self.boton_iniciar = QPushButton("Iniciar simulacion", self)
        self.boton_iniciar.clicked.connect(self.mostrarListas)

        # Agregar los layouts al diseño principal
        self.layout_principal.addLayout(layout_rotulos)
        self.layout_principal.addLayout(layout_listas)
        self.layout_principal.addWidget(self.boton_iniciar)

        self.setLayout(self.layout_principal)
        self.setWindowTitle('INTERFAZ: MARQUEZ-MAZZANTE')
        listitaaux: list[cPacient] = readPacients("Mock_Data_Pacients.csv", 15)
        print("hello world")

    def mostrarListas(self):
        # Ocultar el botón de iniciar simulación
        self.boton_iniciar.hide()

        # Mostrar los nombres
        self.label_pacientes.show()
        self.label_espera.show()
        self.label_atendidos.show()

        # Mostrar las listas
        self.listapacientes.show()
        self.listaespera.show()
        self.listaatendidos.show()

        listitaaux: list[cPacient] = readPacients("Mock_Data_Pacients.csv",15)

        for i in range (len(listitaaux)):
            item = QListWidgetItem(str(listitaaux[i].name))
            self.listapacientes.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())