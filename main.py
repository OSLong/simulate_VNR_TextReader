from PyQt5.QtWidgets import QApplication,QLabel, QVBoxLayout,QGroupBox,QWidget
from Components.App import App
from Components.Panel import myPanel

main = QApplication([])

app=App()
app.show()


for i in range(5):
   
    for j in range(5):
        group = myPanel("Box %s"%i)
        group.setApp(app)
        group.add_label(QLabel("Apple"))
        group.add_label(QLabel("Apple"))
        group.add_label(QLabel("Apple"))
        group.add_label(QLabel("Apple"))
        group.add_label(QLabel("Apple"))
        group.add_label(QLabel("Apple"))
    app.add(group)





#for j in range(5):
#    #panel=mypanel(app)
#    app.add(panel)
#    for i in range(5):
#        panel.add_label("apple "*100)


main.exec_()