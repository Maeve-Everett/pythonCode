import sys
from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
button = QPushButton("Hello World")
button.show()
app.exec()