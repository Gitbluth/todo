# -*- coding:utf-8 -*-

from PyQt4 import QtGui, QtCore, Qt


class Main(QtGui.QWidget):

    window_title = 'Todo List'

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.body()

    def body(self):

        self.setGeometry(800, 100, 350, 600)
        self.setWindowTitle(self.window_title)
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)

        # 设置背景图片
        palette = QtGui.QPalette()
        icon = QtGui.QPixmap('image/bg.jpg')
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        # 标题栏

        wid = TitleBar()
        wid.resize(350, 600)

        vbox = QtGui.QVBoxLayout()
        vbox.setMargin(0)
        vbox.addWidget(wid)

        """
        hbox = QtGui.QHBoxLayout()
        hbox.setMargin(0)
        hbox.addWidget(wid)
        """


        btn = QtGui.QPushButton('Quit', self)
        btn.setShortcut("Ctrl+q")
        self.connect(btn, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT("quit()"))
        vbox.addWidget(btn)

        self.setLayout(vbox)



    #def buttonClicked(self):


"""
    def paintEvent(self, e):
        qp = QtGui.QPainter()

        qp.begin(self)
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        qp.setPen(QtGui.QColor(0, 0, 0, 0))

        brush.setColor(QtGui.QColor(0, 0, 0, 120))
        qp.setBrush(brush)
        qp.drawRect(0, 0, 500, 50)
        qp.end()
"""


class TitleBar(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.bar()

    def bar(self):

        self.resize(350, 600)

        # Title
        label = QtGui.QLabel('Hello World', self)
        label.setStyleSheet("color: white;")
        label.resize(self.width(), 50)
        label.setAlignment(QtCore.Qt.AlignCenter)

        #self.connect(self.icon_settings, QtCore.SIGNAL('clicked()'), self.test)
        #setting_btn = SettingButton()
        #setting_btn.setGeometry(10, 10, 50, 50)





    def paintEvent(self, e):
        qp = QtGui.QPainter()

        qp.begin(self)
        brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        brush.setColor(QtGui.QColor(0, 0, 0, 120))
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(brush)
        qp.drawRect(0, 0, 9999, 50)

        qp.end()

    def enterEvent(self, event):
        pass

    def mousePressEvent(self, QMouseEvent):
        pass


class SettingButton(QtGui.QPushButton):

    def __init__(self):
        super(SettingButton, self).__init__()
        self.icon_settings = QtGui.QPixmap("image/icon_settings.png")
        self.setUI()

    def setUI(self):
        pass

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.drawPixmap(12, 12, 25, 25, self.icon_settings)
        qp.end()


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    dialog = Main()
    dialog.show()
    sys.exit(app.exec_())