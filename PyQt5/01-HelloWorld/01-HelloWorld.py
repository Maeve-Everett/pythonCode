import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(400,400,300,300) # X, Y on screen, window Height, Width... why
window.setWindowTitle("Hello World")

button = QPushButton(window)
button.setText("Hello World")
#button.show() # Only needed if not using a QMainWindow
button.move(100,100)

window.show()
app.exec()