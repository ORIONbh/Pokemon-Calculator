import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QComboBox, QPushButton,
                             )
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon Calculator")
        main_layout = QHBoxLayout()
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        title_label = QLabel("Pokemon Typing")
        left_pane.addWidget(title_label)

        combo = QComboBox()
        combo.addItems(["Fire", "Water", "Grass"])

        
        
        

        

          
        left_pane.addWidget(combo)      

        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)

        self.strength = QLabel("Strength Result")
        self.strength.adjustSize()
        right_pane.addWidget(self.strength)

        self.weakness = QLabel("Weakness Result")
        self.weakness.adjustSize()
        right_pane.addWidget(self.weakness)
 
        button = QPushButton("Calculate")
        button.clicked.connect(self.updatestrength)
        button.clicked.connect(self.updateweakness)
        right_pane.addWidget(button)

    def updateweakness(self):
        self.weakness.setText("Weak to Water ")
     
    def get(self):
        print(self.weakness.text())
 
    def updatestrength(self):
        self.strength.setText("Strong to Grass ")
     
    def get(self):
        print(self.strength.text())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()