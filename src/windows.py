from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QWidget, QPushButton, QGridLayout, QSlider, QLabel, QListWidget, QTextBrowser, QListWidgetItem
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QTextCursor, QTextCharFormat, QColor, QFont
from library.cPacient import cPacient
from library.cColour import cColour


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

    def __init__(self,listitaaux: list[cPacient]):
        super().__init__()

        #inicializacion de variables
        self.__title = "Triage: Marquez-Mazzante"
        self.__top = 300
        self.__left = 300
        self.__width = 1000
        self.__height = 700
        self.__listitaux: list[cPacient] = listitaaux
        self.setStyleSheet("background-color: black;")

        #inicializacion de widgets
        self.__labelTitle = QLabel("")
        self.__list_widget = QListWidget()
        self.__button_start_sim = QPushButton("Start simulation")

        font = QFont()
        font.setPointSize(16)                   # Tamaño de la letra
        font.setBold(True)                      # Negrita
        self.__list_widget.setFont(font)

        #configuracion inicial
        self.setup_ui()


    def setup_ui(self):
        # Configuración de la interfaz gráfica inicial
        for i in range (len(self.__listitaux)):
            #dummy = enfermeritoaux.diagnose(listitaaux[i])
            paciente =self.__listitaux[i]
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

        # Configuraciones del botonstartsimulation
        #self.__button_start_sim.setGeometry(500 - 120, 35, 120, 20)
        #self.__button_start_sim.setText("Start simulation")

        #agrego los widgets al layout
        layout.addWidget(self.__labelTitle, 8, 0, 1, 1)
        layout.addWidget(self.__list_widget, 1, 50, 1, 1)
        layout.addWidget(self.__button_start_sim, 20, 20, 3, 3)

        #self.__button_start_sim.clicked.connect(self.initiate_simulation)

        #Configuraciones del widget central y del layout
        widgetCentral.setLayout(layout)
        self.setCentralWidget(widgetCentral)


    def actualizar_interfaz(self, listitaaux: list[cPacient]):
        self.__list_widget.clear()

        for i in range(len(listitaaux)):
            paciente = listitaaux[i]
            nombre = paciente.name
            color = paciente.colour
            item = QListWidgetItem(nombre)
            item.setForeground(convert(color))
            self.__list_widget.addItem(item)

        self.__list_widget.scrollToBottom()
    def initiate_simulation(self):
        x = 0
        if x > 5:
            pass


# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec())
