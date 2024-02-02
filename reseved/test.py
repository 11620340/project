import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QStackedWidget

class MultiPageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Multi-Page Window')

        # 创建页面堆栈
        self.stackedWidget = QStackedWidget(self)

        # 创建页面1
        page1 = QWidget()
        layout1 = QVBoxLayout()
        layout1.addWidget(QPushButton('Next Page', clicked=lambda: self.changePage(1)))
        page1.setLayout(layout1)

        # 创建页面2
        page2 = QWidget()
        layout2 = QVBoxLayout()
        layout2.addWidget(QPushButton('Previous Page', clicked=lambda: self.changePage(0)))
        page2.setLayout(layout2)

        # 将页面添加到堆栈
        self.stackedWidget.addWidget(page1)
        self.stackedWidget.addWidget(page2)

        # 创建主布局
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(self.stackedWidget)

        self.show()

    def changePage(self, index):
        # 切换页面
        self.stackedWidget.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiPageWindow()
    sys.exit(app.exec_())
