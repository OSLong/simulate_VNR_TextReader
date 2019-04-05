from PyQt5.QtWidgets import QApplication,QLabel
from Components.App import App
from Components.Panel import myPanel

main = QApplication([])

app=App()
app.show()

for j in range(5):
    panel=myPanel(app)
    app.add(panel)
    for i in range(5):
        panel.add_label("Apple"*100)


main.exec_()