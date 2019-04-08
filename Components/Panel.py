from PyQt5.QtWidgets import QLabel,QVBoxLayout,QGroupBox
from win32api import GetSystemMetrics

class myPanel(QGroupBox):
    def __init__(self, str, parent=None):

        super().__init__(str, parent=parent)
        self.container=QVBoxLayout()
        self.setLayout(self.container)
    

    def setApp(self,app):
        self.app=app

    def initUI(self):
        self.setContentsMargins(0,50,0,50)

    def add_label(self,lb):
        lb.setMargin(10)
        self.container.addWidget(lb,1)
        lb.setStyleSheet("color:white")
        lb.setWordWrap(True)
        lb.setFixedWidth(GetSystemMetrics(0)/2.3)
