import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from library.cNurse import cNurse
from library.cPacient import cPacient
from src.readFiles import readPacients,readNurses

class Simulacion(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Simulación de Pacientes')
        self.setGeometry(100, 100, 900, 600)

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

        self.setLayout(layout)


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
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Simulacion()
    ventana.show()
    sys.exit(app.exec())








