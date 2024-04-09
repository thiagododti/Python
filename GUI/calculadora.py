# Estrutura QMainWindow e centralWidget

"""

QApplication (app)
    QMainWindow (window->setCentralWidget)
        CentralWidget (central_widget)
            Layout (layout)
                Widget (botao1)
                Widget (botao2)
    Show CentralWidget (central_widget.show)
Execute QApplication (app.exec)

"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, \
    QGridLayout, QMainWindow, QLineEdit

# Inicialização da aplicação
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
# criando as instancias das classes da biblioteca

layout = QGridLayout()

# Criando a central que vai gerenciar o layout
central_widget.setLayout(layout)

# Criando os botões para o widget
n0 = QPushButton('0')
n1 = QPushButton('1')
n2 = QPushButton('2')
n3 = QPushButton('3')
n4 = QPushButton('4')
n5 = QPushButton('5')
n6 = QPushButton('6')
n7 = QPushButton('7')
n8 = QPushButton('8')
n9 = QPushButton('9')
mais = QPushButton('+')
menos = QPushButton('-')
vezes = QPushButton('x')
dividir = QPushButton('/')
virgula = QPushButton(',')
visor = QLineEdit()


# Adicionando os Widgets dentro do layout
layout.addWidget(visor, 1, 1, 1, 4)
layout.addWidget(n7, 2, 1)
layout.addWidget(n8, 2, 2)
layout.addWidget(n9, 2, 3)
layout.addWidget(n4, 3, 1)
layout.addWidget(n5, 3, 2)
layout.addWidget(n6, 3, 3)
layout.addWidget(n1, 4, 1)
layout.addWidget(n2, 4, 2)
layout.addWidget(n3, 4, 3)
layout.addWidget(n0, 5, 2)
layout.addWidget(virgula, 5, 3)
layout.addWidget(mais, 2, 4)
layout.addWidget(menos, 3, 4)
layout.addWidget(vezes, 4, 4)
layout.addWidget(dividir, 5, 4)


# statusBar

status_bar = window.statusBar()
status_bar.showMessage('Mostrar Mensagem')

# slot


def verifica_status(checked):
    print('Está marcado?', checked)


def muda_status(status_bar):
    status_bar.showMessage('Status trocado')


def slot_fecha_rograma():
    exit()

# menuBar


menu = window.menuBar()
menu_principal = menu.addMenu('Arquivo')

menu_opcao_1 = menu_principal.addAction('muda_status')
menu_opcao_1.triggered.connect(
    lambda: muda_status(status_bar)
)
menu_opcao_1.setCheckable(True)
menu_opcao_1.toggled.connect(verifica_status)

menu_opcao_2 = menu_principal.addAction('Sair')
menu_opcao_2.triggered.connect(slot_fecha_rograma)


# Visualização da nossa Central exibindo o layout iniciado
window.show()

# loop de aplicação
app.exec()

""" Resumo de layout

Para que se tenha várias coisas em uma janela precisamos de um Widget Central

E o Widget central precisa de ter 1 ou mais layouts dentro da central

E dentro dos layouts adicionamos tantos widgets que for necessário na aplicação
"""
