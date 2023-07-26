from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from qfluentwidgets import FluentIcon as FIF

from demo1 import Ui_Form
from teach import Ui_teach
from upload import Ui_Upload
from evals import Ui_Eval


class Page(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setImage("PyQt-Fluent-Widgets/examples/acrylic_label/resource/埃罗芒阿老师.jpg")
        self.setupUi(self)
        self.setShadowEffect(self.CardWidget)
        self.setShadowEffect(self.CardWidget_2)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class Page1(QWidget, Ui_teach):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setImage("PyQt-Fluent-Widgets/examples/acrylic_label/resource/埃罗芒阿老师.jpg")
        self.setupUi(self)
        # self.setShadowEffect(self.CardWidget)
        # self.setShadowEffect(self.CardWidget_2)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class Page2(QWidget, Ui_Upload):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setImage("PyQt-Fluent-Widgets/examples/acrylic_label/resource/埃罗芒阿老师.jpg")
        self.setupUi(self)
        self.setShadowEffect(self.CardWidget)
        self.setShadowEffect(self.CardWidget_2)
        self.PixmapLabel.setPixmap(QPixmap("./src/img/teacher.png"))

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)


class Page3(QWidget, Ui_Eval):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        # self.setImage("PyQt-Fluent-Widgets/examples/acrylic_label/resource/埃罗芒阿老师.jpg")
        self.setupUi(self)
        self.IconWidget.setIcon(FIF.EXPRESSIVE_INPUT_ENTRY)
        self.IconWidget_2.setIcon(FIF.UPDATE)
        self.IconWidget_3.setIcon(FIF.GLOBE)
        self.PixmapLabel_3.setPixmap(
            QPixmap('./src/img/human.jpg').scaled(self.PixmapLabel.width(), self.PixmapLabel.height()))
        self.PixmapLabel_4.setPixmap(
            QPixmap('./src/img/human_dte.jpg').scaled(self.PixmapLabel_2.width(), self.PixmapLabel_2.height()))
        self.PixmapLabel.setPixmap(
            QPixmap('./src/img/curl.png').scaled(self.PixmapLabel_3.width(), self.PixmapLabel_3.height()))
        self.PixmapLabel_2.setPixmap(
            QPixmap('./src/img/curl2.png').scaled(self.PixmapLabel_4.width(), self.PixmapLabel_4.height()))

        # self.setShadowEffect(self.CardWidget)
        # self.setShadowEffect(self.CardWidget_2)

    def setShadowEffect(self, card: QWidget):
        shadowEffect = QGraphicsDropShadowEffect(self)
        shadowEffect.setColor(QColor(0, 0, 0, 15))
        shadowEffect.setBlurRadius(10)
        shadowEffect.setOffset(0, 0)
        card.setGraphicsEffect(shadowEffect)
# class SubPage1(QWidget, Ui_Form):
#     def __init__(self, parent=None):
#         super().__init__(parent=parent)
#         self.setupUi(self)
