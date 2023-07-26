import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationAvatarWidget, NavigationItemPosition, setTheme, \
    Theme, setThemeColor, ThemeColor
from qfluentwidgets.components.widgets.acrylic_label import AcrylicLabel

from FocusInterFace import Page, Page1, Page2, Page3


class MainInterFace(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        # self.setWindowTitle('Demo')
        # self.setWindowIcon(QIcon('./src/img/icon.png'))
        # self.setGeometry(50, 50, 1600, 800)

        self.focusInterFace = Page(self)
        self.focusInterFace1 = Page1(self)
        self.focusInterFace2 = Page2(self)
        self.focusInterFace3 = Page3(self)
        # self.w = AcrylicLabel(20, QColor(105, 114, 168, 102), parent=self)
        # self.focusInterFace1 = SubPage1(self)
        self.addSubInterface(self.focusInterFace, FluentIcon.HOME, 'xy')
        self.addSubInterface(self.focusInterFace1, FluentIcon.TAG, 'xyz')
        self.addSubInterface(self.focusInterFace2, FluentIcon.UPDATE, 'xy1z')
        self.addSubInterface(self.focusInterFace3, FluentIcon.TRAIN, 'xy1z1')
        # self.addSubInterface(self.focusInterFace1, FluentIcon.ADD, 'xy1')
        # self.addSubInterface(self.focusInterFace1, FluentIcon.HOME, 'xy2')
        # self.addSubInterface(self.w, FluentIcon.CAFE, 'xy1')

        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('whl', './src/img/avatar.png'),
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.addItem(
            routeKey='setting',
            icon=FluentIcon.SETTING,
            text='设置',
            position=NavigationItemPosition.BOTTOM
        )

        self.navigationInterface.setExpandWidth(280)
        self.initWindow()

    def initWindow(self):
        self.resize(1200, 800)
        self.setWindowIcon(QIcon('./src/img/logo.png'))
        self.setWindowTitle('Demo')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w // 2 - self.width() // 2, h // 2 - self.height() // 2)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    setTheme(Theme.DARK)
    setThemeColor('#0065d5')

    app = QApplication(sys.argv)
    w = MainInterFace()
    w.show()
    sys.exit(app.exec_())
