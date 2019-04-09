from PyQt5.QtWidgets import QApplication,QLabel, QVBoxLayout,QGroupBox,QWidget
from Components.App import App
from Components.Panel import myPanel
from multiprocessing.dummy import Pool
from API.Baidu import Baidu
from API.Youdao import  Youdao


main = QApplication([])

app=App()
app.show()

def clipboardchanged():

    print('=====================================================================')
    print('=====================================================================')
    group = myPanel("Box")
    app.add(group)

    translator=[Baidu,Youdao]
    lbs=[QLabel() for x in range(len(translator))]

    def translation(tup):
        trans,lb=tup
        tran=trans(main.clipboard().text())
        result=tran.result()
        lb.setStyleSheet(tran.stylesheet())
        lb.setText(result)
        group.add_label(lb)
        #group.add_label(QLabel("appl"))
        pass


    pool=Pool(len(translator))
    pool.map(translation,zip(translator,lbs))
    pool.close()
    pool.join()

    print('=====================================================================')
    print('=====================================================================')

main.clipboard().dataChanged.connect(clipboardchanged)

clipboardchanged()

main.exec_()