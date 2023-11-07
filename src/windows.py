from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QGridLayout, QSlider, QLabel, QListWidget, QTextBrowser, QListWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QColor
import sys
from src.readFiles import readPacients
from library.cPacient import cPacient
from library.cColour import cColour
from library.cNurse import cNurse


def convert(coloraux: cColour) -> QColor:
    if (coloraux.value == 5):
        return QColor("red")
    elif (coloraux.value == 4):
        return QColor("orange")
    elif (coloraux.value == 3):
        return QColor("yellow")
    elif (coloraux.value == 2):
        return QColor("green")
    else:
        return QColor("blue")

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
        listitaaux: list[cPacient] = readPacients("DATA_PACIENT.csv")
        enfermeritoaux = cNurse("carlos", "perazzo", "2111212", "safffdfdsfds")

        #inicializacion de widgets
        self.__labelTitle = QLabel("")
        self.__list_widget = QListWidget()
        self.__text_browser = QTextBrowser()


        for i in range (len(listitaaux)):
            dummy = enfermeritoaux.diagnose(listitaaux[i])
            paciente = listitaaux[i]
            nombre = paciente.name
            color = paciente.colour

            item = QListWidgetItem(nombre)

            item.setForeground(convert(color))

            self.__list_widget.addItem(item)


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
        layout.addWidget(self.__list_widget, 20, 0, 1, 1)


        #Configuraciones del widget central y del layout
        widgetCentral.setLayout(layout)
        self.setCentralWidget(widgetCentral)




if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
