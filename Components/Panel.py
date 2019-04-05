from PyQt5.QtWidgets import QLabel,QVBoxLayout
from win32api import GetSystemMetrics

class myPanel(QVBoxLayout):
    def __init__(self, QWidget):
        super().__init__(QWidget)
        self.initUI()

    def initUI(self):
        self.setContentsMargins(0,50,0,50)

    def add_label(self,text):
        lb=QLabel(text)
        lb.setMargin(10)
        self.addWidget(lb,1)
        self.stretch(1)
        lb.setWordWrap(True)
        lb.setFixedWidth(GetSystemMetrics(0)/2.3)
