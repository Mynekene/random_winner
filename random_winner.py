from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])
window = QWidget()
window.resize(300, 300)
window.move(400, 200)

text = QLabel("Натисніть на кнопку щоб отримати переможця")
text1 = QLabel("???")
button = QPushButton("Згенерувати")

layout = QVBoxLayout()
layout.addWidget(text, alignment = Qt.AlignCenter)
layout.addWidget(text1, alignment = Qt.AlignCenter)
layout.addWidget(button, alignment = Qt.AlignCenter)

window.setLayout(layout)

def show_winner():
    text.setText("Переможець:")
    text1.setText(str(randint(1, 100)))

button.clicked.connect(show_winner)

window.show() 
app.exec_()
