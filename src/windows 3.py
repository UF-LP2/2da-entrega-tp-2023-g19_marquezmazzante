import sys
import time

from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget,QListWidgetItem)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, QTimer

from src.readFiles import readPacients
from library.cPacient import cPacient
from library.cNurse import cNurse

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 800)

        self.layout_principal = QVBoxLayout()

        # Layout para los rótulos
        layout_rotulos = QHBoxLayout()

        # Rótulos para las listas
        self.label_pacientes = QLabel("PACIENTES")
        self.label_espera = QLabel("LISTA DE ESPERA")
        self.label_atendidos = QLabel("LISTA DE ATENDIDOS")
        self.nurse = cNurse("lorenzo","mazzante", "44958354", "321-2132-123")

        font = QFont()
        font.setPointSize(16)  # Tamaño de la fuente
        self.label_pacientes.setFont(font)
        self.label_espera.setFont(font)
        self.label_atendidos.setFont(font)

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
        self.boton_iniciar = QPushButton(self)
        self.boton_iniciar.setText("Iniciar simulación")  # Establecer el texto en negrita
        self.boton_iniciar.setFixedSize(300, 150)  # Cambiar el tamaño del botón
        self.boton_iniciar.setStyleSheet("QPushButton { background-color: white; }"
                                         "QPushButton:hover { background-color: green; }")
        self.boton_iniciar.setFont(font)

        self.boton_iniciar.clicked.connect(self.mostrarListas)

        # Agregar los layouts al diseño principal
        self.layout_principal.addLayout(layout_rotulos)
        self.layout_principal.addLayout(layout_listas)
        self.layout_principal.addWidget(self.boton_iniciar, alignment=Qt.AlignmentFlag.AlignCenter)

        font_listas = QFont()
        font_listas.setPointSize(16)
        self.listapacientes.setFont(font_listas)
        self.listaespera.setFont(font_listas)
        self.listaatendidos.setFont(font_listas)

        self.setLayout(self.layout_principal)
        self.setWindowTitle('INTERFAZ: MARQUEZ-MAZZANTE')
        self.listitaaux = readPacients("Mock_Data_Pacients.csv", 30)
        self.listitapacaux = []
        self.listaesperaaux = []

        self.timer_agregar_paciente = QTimer(self)
        self.timer_agregar_paciente.timeout.connect(self.agregarPaciente)

        self.timer_diagnosticar_paciente = QTimer(self)
        self.timer_diagnosticar_paciente.timeout.connect(self.diagnosticarPaciente)

        self.simulacion_activa = False  # Variable para rastrear el estado de la simulación

        layout_botones = QVBoxLayout()

        # Botón para detener simulación
        self.boton_detener = QPushButton("Detener simulación", self)
        self.boton_detener.clicked.connect(self.detenerSimulacion)
        layout_botones.addWidget(self.boton_detener)

        self.layout_principal.addLayout(layout_botones)

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

        self.timer_agregar_paciente.timeout.connect(self.agregarPaciente)
        self.timer_agregar_paciente.start(2000)

        self.timer_diagnosticar_paciente.timeout.connect(self.diagnosticarPaciente)
        self.timer_diagnosticar_paciente.start(4500)

        self.simulacion_activa = True

    def detenerSimulacion(self):
        # Detener los temporizadores
        self.timer_agregar_paciente.stop()
        self.timer_diagnosticar_paciente.stop()
        self.simulacion_activa = False

    def agregarPaciente(self):
        if self.simulacion_activa:
            paciente_aux = self.listitaaux.pop(0)
            self.listitapacaux.append(paciente_aux)
            nuevo_paciente = "Paciente " + str(paciente_aux.name)
            item1 = QListWidgetItem(nuevo_paciente)
            item1.setBackground(QColor("grey"))
            self.listapacientes.addItem(item1)

    def diagnosticarPaciente(self):
        if self.simulacion_activa:
            pac_a_diagnosticar = self.listapacientes.takeItem(0)
            paciente_aux: cPacient = self.listitapacaux.pop(0)
            self.nurse.diagnose(paciente_aux)
            pac_a_diagnosticar.setBackground(QColor(paciente_aux.colour.name))
            if paciente_aux.colour.value == 5:
                self.listaatendidos.addItem(pac_a_diagnosticar)
            else:
                self.listaespera.addItem(pac_a_diagnosticar)
                self.listaesperaaux.append(paciente_aux)





        # for i in range (len(self.listitaaux)):
        #     item = QListWidgetItem(str(self.listitaaux[i].name))
        #     self.listapacientes.addItem(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())