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

        self.label = QLabel("Results")
        self.label.adjustSize()
        right_pane.addWidget(self.label)
 
        button = QPushButton("Calculate")
        button.clicked.connect(self.update)
        right_pane.addWidget(button)

 
    def update(self):
        self.label.setText("Grass")
     
    def get(self):
        print(self.label.text())

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()