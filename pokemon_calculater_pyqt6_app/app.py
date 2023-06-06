import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QComboBox, QPushButton,
                             )
from PyQt6.QtGui import QPalette, QColor, QFont, QFontDatabase

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon Calculator")
        self.resize(300, 100)
        main_layout = QHBoxLayout()
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        title_label = QLabel("Pokemon Typing")
        left_pane.addWidget(title_label)
        title_label.setFont(QFont("Impact", 30))

        self.combo = QComboBox()
        self.combo.addItems(["Fire", "Water", "Grass"])
        self.combo.currentTextChanged.connect(self.update_advantages)
        self.combo.setFont(QFont("Impact", 18))
          
        left_pane.addWidget(self.combo)      

        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)
        gui = QWidget()
        gui.setLayout(main_layout)
        self.setCentralWidget(gui)

        self.strength = QLabel("Strength Result")
        self.strength.adjustSize()
        right_pane.addWidget(self.strength)
        self.strength.setFont(QFont("Impact", 17))

        self.weakness = QLabel("Weakness Result")
        self.weakness.adjustSize()
        right_pane.addWidget(self.weakness)
        self.weakness.setFont(QFont("Impact", 17))



    def update_advantages(self):
        #get type
        type = self.combo.currentText()

        #display advantages and disadvantages
        if type == "Fire":
            self.weakness.setText("2x Weak to Water ")
            self.strength.setText("2x Strong to Grass ")
        if type == "Water":
            self.weakness.setText("2x Weak to Grass ")
            self.strength.setText("2x Strong to Fire ")
        if type == "Grass":
            self.weakness.setText("2x Weak to Fire ")
            self.strength.setText("2x Strong to Water ") 
    def get(self):
        print(self.weakness.text())
     
    def get(self):
        print(self.strength.text())

app = QApplication(sys.argv)
app.setStyleSheet("QWidget { font-size: 16px; background-color: Red; color: white; padding: 10px 10px 10px 10px}")
window = MainWindow()
window.show()
app.exec()

