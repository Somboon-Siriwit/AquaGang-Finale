from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QSlider,
    QVBoxLayout,
    QWidget,
    QListWidget,
)

from pondFrame import PondFrame
import numpy as np

class PondDashboard(QMainWindow):
    def __init__(self,connected_pond):
        super().__init__()
        self.connected_ponds = connected_pond
        self.label = QLabel(self)
        self.list_widget = QListWidget(self)
        self.update_dashboard()
        self.initUI()

    def update_dashboard(self):
        # self.connected_ponds = connected_ponds
        temp = self.connected_ponds.values()
        self.list_widget.clear()
        for items in temp:
            
            self.list_widget.addItem(str(items))
        # for items in temp:
        #     self.label.setText(f"{items}")

    def initUI(self):

        self.scroll = (
            QScrollArea()
        )  # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = (
            QVBoxLayout()
        )  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.grid = QGridLayout()
        self.graph_button = QPushButton("Graph")
        # self.graph_button.clicked.connect(self.graph)
        # print(self.fishe[0].getFishData().getGenesis())
        # num = len(self.fished)
        # num = len(self.ponds)

        # i, j, temp = 0, 0, 0
        # for r in range(0, num):
        #     # print("out", i, temp, j)
        #     while j < 2 and i < num:
        #         # print("here", i, temp, j)
        #         info = [
        #             self.ponds[i].getPondName(),
        #             self.ponds[i].getPopulation(),
        #             self.ponds[i].fishes,
        #         ]
        #         self.grid.addWidget(PondFrame(info, self.widget), temp, j)
        #         i += 1
        #         j += 1
        #     j = 0
        #     temp += 1





        font = self.label.font()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.connectLabel = QLabel()
        self.connectLabel.setText("Connected Ponds:")
        self.connectLabel.setFont(font)

        self.vbox.addWidget(self.connectLabel)
        # self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.list_widget)
        self.vbox.addLayout(self.grid)
        # self.vbox.addWidget(self.graph_button)
        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(0, 20, 800, 300)
        self.setWindowTitle("Vivisystem Dashboard")
        self.show()

        return

    def update(self):
        pass
