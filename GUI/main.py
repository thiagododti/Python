import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.show()

central_widget = QWidget()

layout = QVBoxLayout()

central_widget.setLayout(layout)

layout.addWidget(botao)

central_widget.show()

app.exec()
