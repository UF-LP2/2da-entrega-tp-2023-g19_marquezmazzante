import sys
import time

from PyQt6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QListWidget,QListWidgetItem)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt, QTimer

from src.readFiles import readPacients
from library.cPacient import cPacient
from library.cNurse import cNurse
from library.attention import attend

class Interfaz(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(800, 800)

        self.layout_principal = QVBoxLayout()

        #layout para rotulos
        layout_rotulos = QHBoxLayout()

        #rotulos de las listas
        self.label_pacientes = QLabel("PACIENTES")
        self.label_espera = QLabel("LISTA DE ESPERA")
        self.label_atendidos = QLabel("LISTA DE ATENDIDOS")
        self.nurse = cNurse("lorenzo","mazzante", "44958354", "321-2132-123")

        #fuente para titulos
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_pacientes.setFont(font)
        self.label_espera.setFont(font)
        self.label_atendidos.setFont(font)

        layout_rotulos.addWidget(self.label_pacientes)
        layout_rotulos.addWidget(self.label_espera)
        layout_rotulos.addWidget(self.label_atendidos)

        # Layout para las listas
        layout_listas = QHBoxLayout()

        #listas widgets
        self.listapacientes = QListWidget(self)
        self.listaespera = QListWidget(self)
        self.listaatendidos = QListWidget(self)

        #ocultar titulos y listas al principio
        self.label_pacientes.hide()
        self.label_espera.hide()
        self.label_atendidos.hide()
        self.listapacientes.hide()
        self.listaespera.hide()
        self.listaatendidos.hide()

        layout_listas.addWidget(self.listapacientes)
        layout_listas.addWidget(self.listaespera)
        layout_listas.addWidget(self.listaatendidos)

        #boton para simular
        self.boton_iniciar = QPushButton(self)
        self.boton_iniciar.setText("Iniciar simulación")  # Establecer el texto en negrita
        self.boton_iniciar.setFixedSize(300, 150)  # Cambiar el tamaño del botón
        self.boton_iniciar.setStyleSheet("QPushButton { background-color: white; }"
                                         "QPushButton:hover { background-color: green; }")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.boton_iniciar.setFont(font)

        self.boton_iniciar.clicked.connect(self.mostrarListas)

        #agregar los layouts al diseño principal
        self.layout_principal.addLayout(layout_rotulos)
        self.layout_principal.addLayout(layout_listas)
        self.layout_principal.addWidget(self.boton_iniciar, alignment=Qt.AlignmentFlag.AlignCenter)

        #fuente para las listas
        font_listas = QFont()
        font_listas.setPointSize(22)
        self.listapacientes.setFont(font_listas)
        self.listaespera.setFont(font_listas)
        self.listaatendidos.setFont(font_listas)

        self.setLayout(self.layout_principal)
        self.setWindowTitle('INTERFAZ: MARQUEZ-MAZZANTE')
        self.listitaaux = readPacients("Mock_Data_Pacients.csv", 30)
        self.listitapacaux = []
        self.listaesperaaux = []

        #timer para llamar funciones
        self.timer_agregar_paciente = QTimer(self)
        self.timer_agregar_paciente.timeout.connect(self.agregarPaciente)
        self.timer_diagnosticar_paciente = QTimer(self)
        self.timer_diagnosticar_paciente.timeout.connect(self.diagnosticarPaciente)
        self.timer_atender_paciente = QTimer(self)
        self.timer_atender_paciente.timeout.connect(self.atenderPaciente)

        #variable para rastrear el estado de la simulación
        self.simulacion_activa = False

        layout_botones = QVBoxLayout()

        font.setBold(False)
        #botón para detener simulación
        self.boton_detener = QPushButton("Detener simulación", self)
        self.boton_detener.clicked.connect(self.detenerSimulacion)
        layout_botones.addWidget(self.boton_detener)
        self.boton_detener.setFont(font)
        self.boton_detener.hide()

        #boton para resumir simulación
        self.boton_resumir = QPushButton("Resumir Simulación")
        self.boton_resumir.clicked.connect(self.resumirSimulacion)
        layout_botones.addWidget(self.boton_resumir)
        self.boton_resumir.setFont(font)
        self.boton_resumir.hide()

        self.layout_principal.addLayout(layout_botones)

        #muestro en pantalla completa
        self.showMaximized()

    def mostrarListas(self):
        # Ocultar el botón de iniciar simulación
        self.boton_iniciar.hide()
        self.boton_detener.show()
        self.boton_resumir.show()

        # Mostrar los nombres
        self.label_pacientes.show()
        self.label_espera.show()
        self.label_atendidos.show()

        # Mostrar las listas
        self.listapacientes.show()
        self.listaespera.show()
        self.listaatendidos.show()

        self.timer_agregar_paciente.start(1000)
        self.timer_diagnosticar_paciente.start(1500)
        self.timer_atender_paciente.start(3000)

        self.simulacion_activa = True

    def detenerSimulacion(self):
        # Detener los temporizadores
        self.timer_agregar_paciente.stop()
        self.timer_diagnosticar_paciente.stop()
        self.timer_atender_paciente.stop()
        self.simulacion_activa = False

    def resumirSimulacion(self):
        self.timer_agregar_paciente.start(1000)
        self.timer_diagnosticar_paciente.start(2000)
        self.timer_atender_paciente.start(3000)
        self.simulacion_activa = True

    def agregarPaciente(self):
        if self.simulacion_activa and self.listitaaux:
            paciente_aux = self.listitaaux.pop(0)
            self.listitapacaux.append(paciente_aux)
            nuevo_paciente = "Paciente " + str(paciente_aux.name)
            item1 = QListWidgetItem(nuevo_paciente)
            item1.setBackground(QColor("grey"))
            self.listapacientes.addItem(item1)
        else:
            self.timer_agregar_paciente.stop()

    def diagnosticarPaciente(self):
        if self.simulacion_activa and self.listitapacaux:
            pac_a_diagnosticar = self.listapacientes.takeItem(0)
            paciente_aux: cPacient = self.listitapacaux.pop(0)
            self.nurse.diagnose(paciente_aux)
            pac_a_diagnosticar.setBackground(QColor(paciente_aux.colour.name))
            if paciente_aux.colour.value == 5:
                self.listaatendidos.insertItem(0,pac_a_diagnosticar)
            else:
                self.listaespera.addItem(pac_a_diagnosticar)
                self.listaesperaaux.append(paciente_aux)
        else:
            self.timer_diagnosticar_paciente.stop()

    def atenderPaciente(self):
        if self.simulacion_activa and self.listaesperaaux:
            pacaux = attend(self.listaesperaaux, 0, len(self.listaesperaaux))
            nuevo_paciente = "Paciente " + str(pacaux.name)


            item1 = QListWidgetItem(nuevo_paciente)
            item1.setBackground(QColor(pacaux.colour.name))

            pos=0
            for i in range(len(self.listaesperaaux)):
                if self.listaesperaaux[i]==pacaux:
                    pos=i
                    break

            self.listaesperaaux.remove(pacaux)
            self.listaespera.takeItem(pos)
            self.listaatendidos.insertItem(0,item1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())