import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout

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

        self.btnIniciar = QPushButton('Iniciar Simulación', self)
        self.btnIniciar.clicked.connect(self.iniciarSimulacion)
        self.btnIniciar.setStyleSheet('font-size: 18px;')  # Establecer el tamaño del texto del botón

        # Alinea el botón a la izquierda en el diseño horizontal
        hlayout.addWidget(self.btnIniciar)

        layout.addLayout(hlayout)  # Agregar el diseño horizontal al diseño vertical

        self.setLayout(layout)

    def iniciarSimulacion(self):
        # Lógica de simulación
        pacientes = ['Paciente 1', 'Paciente 2', 'Paciente 3', 'Paciente 4', 'Paciente 5']
        random.shuffle(pacientes)  # Mezclar la lista aleatoriamente

        for paciente in pacientes:
            # Diagnóstico y tratamiento simulado
            print(f'Diagnosticando y tratando a: {paciente}')

        # Ocultar el botón al iniciar la simulación
        self.btnIniciar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Simulacion()
    ventana.show()
    sys.exit(app.exec())








