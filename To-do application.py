from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from sys import argv


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

class TaskWidget(QWidget):
    def __init__(self, task, parent=None):
        super().__init__(parent)
        self.task = task

        self.task_label = QLabel(task.description, self)
        self.complete_button = QPushButton("Complete", self)
        self.delete_button = QPushButton("Delete", self)

        self.complete_button.clicked.connect(self.toggle_completion)
        self.delete_button.clicked.connect(self.delete_task)

        layout = QHBoxLayout()
        layout.addWidget(self.task_label)
        layout.addWidget(self.complete_button)
        layout.addWidget(self.delete_button)
        self.setLayout(layout)

    def toggle_completion(self):
        self.task.completed = not self.task.completed
        self.complete_button.setText("Uncomplete" if self.task.completed else "Complete")

    def delete_task(self):
        parent_menu = self.parentWidget().parentWidget()
        if parent_menu:
            parent_menu.remove_task_widget(self)


class MainMenu(QMainWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setWindowTitle('To-Do')
        #self.setWindowIcon(QIcon('./assets/editor.png'))
        self.completed = 0
        self.uncompleted = 0
        self.tasks = []
        self.completed_tasks = []
        self.uncompleted_tasks = []
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
        self.input.editingFinished.connect(self.add_task)
        combo_style = "border: 3px solid black; background-color: lightblue; font-size: 29px;"
        self.list_status = QComboBox(self)
        self.list_status.addItems(["All", "Completed", "Uncompleted"])
        self.list_status.setStyleSheet(combo_style)
        self.list_status.setFixedSize(200,50)
        self.list_status.currentIndexChanged.connect(self.update_task_list)
        self.task_list_widget = QListWidget()
        self.grid_layout.addWidget(completed,1,1)
        self.grid_layout.addWidget(uncompleted,1,2)
        self.grid_layout.addWidget(self.input,2,1,1,2)
        self.grid_layout.addWidget(self.list_status,2,3)
        self.grid_layout.addWidget(self.task_list_widget, 4,1,1,3)
        self.setCentralWidget(self.central_widget)



    def add_task(self) -> None:
        description = self.input.text()
        if description:
            task = Task(description)
            task_widget = TaskWidget(task)
            self.tasks.append(task_widget)
            item = QListWidgetItem()
            item.setSizeHint(task_widget.sizeHint())
            self.task_list_widget.addItem(item)
            self.task_list_widget.setItemWidget(item, task_widget)
            self.input.clear()
            self.update_task_list()

    def update_task_list(self):
        filter_option = self.list_status.currentText()
        for task_widget in self.tasks:
            task = task_widget.task
            if filter_option == "All" or (filter_option == "Completed" and task.completed) or (filter_option == "Uncompleted" and not task.completed):
                task_widget.show()
            else:
                task_widget.hide()

    def remove_task_widget(self, task_widget):
        self.tasks.remove(task_widget)
        item = self.task_list_widget.item(self.task_list_widget.indexFromItemWidget(task_widget).row())
        self.task_list_widget.takeItem(self.task_list_widget.row(item))

        for task in tasks_to_display:
            item = QListWidgetItem(task.description)

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