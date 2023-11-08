import sys
import random
import time
from library.cColour import cColour
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea
from PyQt6.QtCore import QTimer
from library.cNurse import cNurse
from library.cPacient import cPacient
from src.readFiles import readPacients,readNurses
from PyQt6.QtCore import Qt
class Simulacion(QWidget):

    def __init__(self, listpacient=readPacients("DATA_PACIENT.csv", 30)):
        super().__init__()
        self.initUI()
        self.listpacient=listpacient


    def initUI(self):
        self.setWindowTitle('Simulación de Pacientes')
        self.setGeometry(100, 100, 900, 600)

        main_layout = QVBoxLayout()

        layout = QVBoxLayout()

        # Crear un diseño horizontal para contener el botón
        hlayout = QHBoxLayout()

        self.__btnIniciar = QPushButton('Iniciar Simulación', self)
        self.__btnIniciar.clicked.connect(self.iniciarSimulacion)
        self.__btnIniciar.setStyleSheet('font-size: 20px;')  # Establecer el tamaño del texto del botón

        # Alinea el botón a la izquierda en el diseño horizontal
        hlayout.addWidget(self.__btnIniciar)

        layout.addLayout(hlayout)  # Agregar el diseño horizontal al diseño vertical

        # Agregar contenedor para las etiquetas de los enfermeros (inicialmente vacío)
        self.__nurseLabelsContainer = QWidget(self)
        self.__nurseLabelsContainer.hide()  # Ocultar el contenedor al inicio
        layout.addWidget(self.__nurseLabelsContainer)

        # Agregar un diseño vertical para las etiquetas de los enfermeros
        self.__nurseLabelsLayout = QVBoxLayout(self.__nurseLabelsContainer)
        self.__nurseLabelsLayout.setContentsMargins(0, 0, 0, 0)  # Sin márgenes

        self.setLayout(main_layout)

        scroll_area = QScrollArea()
        scroll_content_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_content_widget)  # Layout vertical dentro del widget desplazable

        # Agregar el diseño vertical existente al layout del QScrollArea
        scroll_layout.addLayout(layout)

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_content_widget)

        # Agregar el QScrollArea al diseño principal
        main_layout.addWidget(scroll_area)



    def actualizarEtiquetasEnf(self):

        listauxenf = readNurses()
        for nombre in listauxenf:
            label = QLabel(nombre.name, self)
            label.setFixedSize(100, 100)  # Tamaño cuadrado para el objeto cuadrado del enfermero
            label.setStyleSheet('border: 1px solid black;')  # Borde negro para el objeto cuadrado
            self.__nurseLabelsLayout.addWidget(label)  # Agregar la etiqueta del enfermero al diseño vertical

        # Mostrar el contenedor con las etiquetas después de asignar los nombres
        self.__nurseLabelsContainer.show()

    def iniciarSimulacion(self):
        self.actualizarEtiquetasEnf()
        self.__btnIniciar.hide()

        # Crear temporizador para generar pacientes
        self.timer = QTimer()
        self.timer.timeout.connect(self.generarPaciente)
        self.timer.start(400)  # Genera un paciente cada segundo

    def generarPaciente(self):

        self.patient_index = 0  # Inicializar el índice del paciente

        self.nurse = cNurse("dfsf", "dfs", "dfsds", "dfsd")
        self.timer = QTimer()  # Inicializar el temporizador
        self.timer.timeout.connect(
            self.agregarSiguientePaciente)  # Conectar el temporizador a la función para agregar el siguiente paciente
        self.timer.start(1000)  # Comenzar el temporizador con un intervalo de 1000 milisegundos

    def agregarSiguientePaciente(self):
        if self.patient_index < len(self.listpacient):
            paciente_actual = self.listpacient[self.patient_index]
            self.nurse.diagnose(paciente_actual)
            label_paciente = QLabel(f'Paciente {paciente_actual.name}', self)
            label_paciente.setStyleSheet(
                f'border: 3px solid black; background-color: {paciente_actual.colour.name};')  # Borde negro para representar paciente
            label_paciente.move(800, 10 + self.patient_index * 60)  # Posición inicial del paciente en el borde derecho
            label_paciente.show()
            self.moverPaciente(label_paciente)
            self.patient_index += 1  # Incrementar el índice del paciente

        else:
            self.timer.stop()
    def moverPaciente(self, label_paciente):
        if label_paciente.x() > 100:
            label_paciente.move(label_paciente.x() - 1, label_paciente.y())  # Mover hacia la izquierda
        else:
            label_paciente.hide()  # Ocultar paciente al llegar a los enfermeros



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Simulacion()
    ventana.show()
    sys.exit(app.exec())








