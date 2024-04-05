# Estrutura

"""

QApplication (app)
    CentralWidget (central_widget)
        Layout (layout)
            Widget (botao1)
            Widget (botao2)
    Show CentralWidget (central_widget.show)
Execute QApplication (app.exec)

"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

# Inicialização da aplicação
app = QApplication(sys.argv)

# criando as instancias das classes da biblioteca
central_widget = QWidget()
layout = QGridLayout()

# Criando a central que vai gerenciar o layout
central_widget.setLayout(layout)

# Criando os botões para o widget
botao1 = QPushButton('Botão 1')
botao2 = QPushButton('Botão 2')

# Adicionando os Widgets dentro do layout
layout.addWidget(botao1, 1, 2)
layout.addWidget(botao2, 2, 1)

# Visualização da nossa Central exibindo o layout iniciado
central_widget.show()

# loop de aplicação
app.exec()

""" Resumo de layout

Para que se tenha várias coisas em uma janela precisamos de um Widget Central

E o Widget central precisa de ter 1 ou mais layouts dentro da central

E dentro dos layouts adicionamos tantos widgets que for necessário na aplicação
"""
