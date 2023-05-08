import random
import time
from typing import DefaultDict, Dict

from PyQt5.QtCore import Qt

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

import consts
from Fish import FishGroup
from fishFrame import FishFrame
from collections import namedtuple


class Dashboard(QMainWindow):
    def __init__(self, fishes: FishGroup):
        super().__init__()
        self.fishes: FishGroup = fishes
        self.last_updated = time.time()
        self.label = QLabel(self)
        self.label.setFont(QFont('Arial',12))
        self.slicedata = []

        self.sliceColors = ["#82d3e5", "#cfeef5", "#fd635c", "#fdc4c1",
                            "#feb543", "#ffe3b8", "#CCCCFF", "#40E0D0", "#9FE2BF", "#FFA07A"]
        self.PieData = namedtuple(
            'Data', ['name', 'value', 'primary_color', 'secondary_color'])
        percentages = self.fishes.get_percentages()
        self.create_piechart(percentages)

        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
        ]
        self.lines = {}
        self.initUI()

    def update_dashboard(self, pheromone: int):
        current_time = time.time()
        if current_time - self.last_updated < 2:
            return
        self.last_updated = current_time

        percentages = self.fishes.get_percentages()
        percentages_str = ""
        for genesis, p in percentages.items():
            percentages_str += f"{genesis}: {p * 100:.2f}%\n"

        label_str = (
            "Pond Population : " +
            str(self.fishes.get_total()) + "\n" + percentages_str + "\n"
        )
        label_str += f"Pond Pheremone: {pheromone}\n"

        label_str += f"\n \tFish Limit: {consts.FISHES_POND_LIMIT}\n"
        # label_str += f"\tDisplay Limit: {consts.FISHES_DISPLAY_LIMIT}\n"
        # label_str += f"\tBirth Rate: {consts.BIRTH_RATE}x\n"

        fish_list = self.fishes.getFishes()

        self.label.setText(label_str)
        self.create_piechart(percentages)
        self.createFishFrame(fish_list)

    def create_piechart(self, percentages):
        for genesis, s in percentages.items():
            randcol1 = random.choice(self.sliceColors)
            randcol2 = random.choice(self.sliceColors)
            node = self.PieData(genesis, s, QtGui.QColor(
                randcol1), QtGui.QColor(randcol2))
            self.slicedata.append(node)

    
    def createFishFrame(self,fish_list):
        #delete old frames
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            self.grid.removeWidget(widget)
            widget.setParent(None)

        temp = 3
        j = 0
        for i in range(len(fish_list)):
            fish_list[i].updateLifeTime()
            info = [
                fish_list[i].getFishData().getId(),
                fish_list[i].getFishData().getState(),
                fish_list[i].getFishData().getStatus(),
                fish_list[i].getFishData().getGenesis(),
                fish_list[i].getFishData().getLifeTimeLeft()
            ]
            self.grid.addWidget(FishFrame(info, self.widget), temp, j)
            # temp +=1
            j+=1
            if j>3:
                j = 0
                temp+=1


    def initUI(self):

        self.scroll = (
            QScrollArea()
        )  # Scroll Area which contains the widgets, set as the centralWidget

        self.widget = QWidget()  # Widget that contains the collection of Vertical Box

        self.vbox = QVBoxLayout()
        self.h_layout1 = QHBoxLayout()
        self.grid = QGridLayout()


        # print(self.fished[0].getFishData().getGenesis())

        num = len(self.fishes)

        font = self.label.font()

        font.setPointSize(14)

        font.setBold(True)

        self.label.setFont(font)

        #Add components to QVBoxLayout
        self.vbox.addWidget(self.label)
        self.vbox.addLayout(self.h_layout1)
        self.vbox.addLayout(self.grid)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll.setWidgetResizable(True)

        self.scroll.setWidget(self.widget)

        # self.scroll.setWidget(self.graphWidget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(0, 290, 600, 800)

        self.setWindowTitle("Dashboard")

        self.show()

        return
    def update(fishes):

        pass