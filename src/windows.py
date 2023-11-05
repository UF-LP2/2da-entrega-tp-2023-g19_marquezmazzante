from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QGridLayout, QSlider, QLabel
from PyQt6.QtCore import Qt
from src.graphyc_interface import cProyect
import sys

class Window(QMainWindow):      #windget principal

    __title = None
    __top = None
    __left = None
    __width = None
    __height = None

    def __init__(self):
        super().__init__()

        #inicializacion de variables
        self.__title = "Triage: Marquez-Mazzante"
        self.__top = 300
        self.__left = 300
        self.__width = 1000
        self.__height = 700

        #inicializacion de widgets
        self.__labelTitle = QLabel("")


        #geometria de la ventana principal
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__top, self.__left, self.__width, self.__height)


        #declaro e inicializo el widget central y el layout
        widgetCentral = QWidget(self)
        layout = QGridLayout()


        #Configuracion del layout
        layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)


        #agrego los widgets al layout
        layout.addWidget(self.__labelTitle, 8, 0, 1, 1)


        #Configuraciones del widget central y del layout
        widgetCentral.setLayout(layout)
        self.setCentralWidget(widgetCentral)



if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
