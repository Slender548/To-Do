from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv

class MainMenu(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle('To-Do')
        #self.setWindowIcon(QIcon('./assets/editor.png'))
        self.completed = 1
        self.uncompleted = 1
        self._run_()
    def _run_(self) -> None:
        self.grid_layout = QGridLayout()
        self.central_widget = QWidget(self)
        self.central_widget.setLayout(self.grid_layout)
        completed = QLabel(f"Completed: {self.completed}",self)
        uncompleted = QLabel(f"Uncompleted: {self.uncompleted}",self)
        completed.setStyleSheet("border: 4px solid black; background-color: green; font-size: 64px;")
        uncompleted.setStyleSheet("border: 4px solid black; background-color: yellow; font-size: 64px;")
        completed.setMaximumHeight(100)
        self.input = QLineEdit(self)
        input_style = "border: 3px solid gray; background-color: white; font-size: 32px;"
        self.input.setStyleSheet(input_style)
        self.input.setGeometry(50, 50, 200, 30)
        combo_style = "border: 3px solid black; background-color: lightblue; font-size: 29px;"
        self.list_status = QComboBox(self)
        self.list_status.addItems(["All", "Completed", "Uncompleted"])
        self.list_status.setStyleSheet(combo_style)
        self.list_status.setFixedSize(200,50)
        self.grid_layout.addWidget(completed,1,1)
        self.grid_layout.addWidget(uncompleted,1,2)
        self.grid_layout.addWidget(self.input,2,1,1,2)
        self.grid_layout.addWidget(self.list_status,2,3)
        self.setCentralWidget(self.central_widget)





    def set_font(self, font:str, size:int, set:QLabel) -> None:
        self.font = QFont(font,size)
        set.setFont(self.font)


    def inputer(self) -> None:
        print(self.input.text())

    def keyPressEvent(self,e) -> None:
        if e.key() == Qt.Key.Key_Escape:
            self.close()



if __name__ == "__main__":
    app = QApplication(argv)
    windows = MainMenu()
    windows.show()
    app.exec_()