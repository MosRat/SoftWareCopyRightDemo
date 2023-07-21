import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationAvatarWidget, NavigationItemPosition, setTheme, \
    Theme,setThemeColor,ThemeColor

from FocusInterFace import Page


class MainInterFace(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Demo')
        self.setWindowIcon(QIcon('./src/img/icon.png'))

        self.focusInterFace = Page(self)
        self.addSubInterface(self.focusInterFace, FluentIcon.DOWNLOAD, 'xy')

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
