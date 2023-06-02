import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout,QLabel,QComboBox, QPushButton,
                             )
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokemon Calculator")
        self.resize(300, 100)
        main_layout = QHBoxLayout()
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        title_label = QLabel("Pokemon Typing")
        title_label.setStyleSheet("Qlabel { backround-color : red; }")
        left_pane.addWidget(title_label)

        self.combo = QComboBox()
        self.combo.addItems(["Fire", "Water", "Grass"])
        self.combo.currentTextChanged.connect(self.update_advantages)
          
        left_pane.addWidget(self.combo)      

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



    def update_advantages(self):
        #get type
        type = self.combo.currentText()

        #display advantages and disadvantages
        if type == "Fire":
            self.weakness.setText("Weak to Water ")
            self.strength.setText("Strong to Grass ")
        if type == "Water":
            self.weakness.setText("Weak to Grass ")
            self.strength.setText("Strong to Fire ")
        if type == "Grass":
            self.weakness.setText("Weak to Fire ")
            self.strength.setText("Strong to Water ") 
    def get(self):
        print(self.weakness.text())
     
    def get(self):
        print(self.strength.text())

app = QApplication(sys.argv)
app.setStyleSheet("QWidget { font-size: 16px; background-color: red; color: White;}")
window = MainWindow()
window.show()
app.exec()

