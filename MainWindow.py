from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QWidget):

    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.iterations = 0
        self.validationDetails = ""
        self.validation = False
 
        self.setupUI()
    
    def setupUI(self):
        self.setWindowTitle("NOT SILC")

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # experiment info
        self.descriptionPanel = QGroupBox("Description")
        self.descriptionPanel.setFixedSize(200,150)
        self.layout.addWidget(self.descriptionPanel)
        self.descriptionLayout = QGridLayout()
        self.descriptionPanel.setLayout(self.descriptionLayout)

        # params panel, GB can't add widget
        self.buttonsPanel = QGroupBox("Initial params")
        self.buttonsPanel.setFixedSize(200,350)
        self.layout.addWidget(self.buttonsPanel)
        self.buttonsLayout = QGridLayout()
        self.buttonsPanel.setLayout(self.buttonsLayout)

        # control panel
        self.controlPanel = QGroupBox("Control of experiments")
        self.controlPanel.setFixedSize(200,100)
        self.layout.addWidget(self.controlPanel)
        self.controlLayout = QGridLayout()
        self.controlPanel.setLayout(self.controlLayout)

        # origin
        self.labelOrigin = QLabel("Origen de la muestra", self)
        self.descriptionLayout.addWidget(self.labelOrigin) 
        self.inputOrigin = QLineEdit("", self)
        self.descriptionLayout.addWidget(self.inputOrigin) 

        # tipo de muestra
        self.labelType = QLabel("Tipo de la muestra", self)
        self.descriptionLayout.addWidget(self.labelType) 
        self.inputType = QLineEdit("", self)
        self.descriptionLayout.addWidget(self.inputType) 

        # ball size
        self.labelBallSize = QLabel("Tamaño bola", self)
        self.buttonsLayout.addWidget(self.labelBallSize)
        self.comboBoxBallSize = QComboBox()
        self.comboBoxBallSize.addItems(["","Small", "Medium", "Large"])
        self.buttonsLayout.addWidget(self.comboBoxBallSize)

        # chupa buttons
        self.labelHome = QLabel("Set zero",self)
        self.buttonsLayout.addWidget(self.labelHome)
        self.buttonTake = QPushButton("TAKE BALL", self)
        self.buttonsLayout.addWidget(self.buttonTake)

        self.buttonHold = QPushButton("HOLD BALL", self)
        self.buttonsLayout.addWidget(self.buttonHold) 
        self.buttonHold.setEnabled(False)


        # rock height
        self.labelRockHeight = QLabel("Altura rock", self)
        self.buttonsLayout.addWidget(self.labelRockHeight)
        self.buttonRockHeight = QPushButton("Medir altura", self)
        self.buttonsLayout.addWidget(self.buttonRockHeight)
        self.buttonRockHeight.setEnabled(False)
        
        # set distance 
        self.labelDistance = QLabel("Distancia bola-roca", self)
        self.buttonsLayout.addWidget(self.labelDistance)
        self.inputDistance = QLineEdit("", self)
        self.buttonsLayout.addWidget(self.inputDistance)
        self.inputDistance.setEnabled(False)

        # adjust distance
        self.buttonAdjust = QPushButton("SET DISTANCE", self)
        self.buttonsLayout.addWidget(self.buttonAdjust)
        self.buttonAdjust.setEnabled(False)

        # confirm
        self.buttonConfirm= QPushButton("Confirm", self)
        self.controlLayout.addWidget(self.buttonConfirm, 0, 0)
        #self.buttonConfirm.setEnabled(False)

        # launch
        self.buttonLaunch= QPushButton("Launch", self)
        self.controlLayout.addWidget(self.buttonLaunch, 0, 1)
        self.buttonLaunch.setEnabled(False)

        # Finish
        self.buttonFinish = QPushButton("Finish", self)
        self.controlLayout.addWidget(self.buttonFinish, 1, 0, 1, 2)
        self.buttonFinish.setEnabled(True)

        # table
        self.table= QTabWidget()

        tab1 = QWidget()
        self.tableWidget = QTableWidget(0, 4)
        columns = ["Ball size", "Rock size", "Distance", "Register"]
        self.tableWidget.setHorizontalHeaderLabels(columns)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)       
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(self.tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("log file \n ...") # aqui puee ir la consola?

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.table.addTab(tab1, "&Table")
        self.table.addTab(tab2, "&Console")
        self.table.setFixedSize(500,600)

        self.layout.addWidget(self.table, 0, 1, 3, 1)







