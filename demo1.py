# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1243, 1196)
        Form.setMaximumSize(QtCore.QSize(2400, 1200))
        font = QtGui.QFont()
        font.setFamily("霞鹜文楷 GB 屏幕阅读版 R")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CardWidget = CardWidget(Form)
        self.CardWidget.setGeometry(QtCore.QRect(130, 220, 611, 521))
        font = QtGui.QFont()
        font.setFamily("LXGW WenKai")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.CardWidget.setFont(font)
        self.CardWidget.setObjectName("CardWidget")
        self.BodyLabel = BodyLabel(self.CardWidget)
        self.BodyLabel.setGeometry(QtCore.QRect(170, 460, 261, 51))
        font = QtGui.QFont()
        font.setFamily("LXGW WenKai")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.BodyLabel.setFont(font)
        self.BodyLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BodyLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BodyLabel.setObjectName("BodyLabel")
        self.ProgressBar = ProgressBar(self.CardWidget)
        self.ProgressBar.setGeometry(QtCore.QRect(360, 160, 201, 4))
        self.ProgressBar.setMinimum(1)
        self.ProgressBar.setProperty("value", 80)
        self.ProgressBar.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar.setUseAni(True)
        self.ProgressBar.setVal(80.0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.StrongBodyLabel = StrongBodyLabel(self.CardWidget)
        self.StrongBodyLabel.setGeometry(QtCore.QRect(110, 230, 113, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.StrongBodyLabel.setFont(font)
        self.StrongBodyLabel.setObjectName("StrongBodyLabel")
        self.StateToolTip = StateToolTip('<b>执行中</b>', '正在向服务端获取详细评价', self.CardWidget)
        self.StateToolTip.setGeometry(QtCore.QRect(180, 400, 256, 51))
        self.StateToolTip.setObjectName("StateToolTip")
        self.ProgressBar_3 = ProgressBar(self.CardWidget)
        self.ProgressBar_3.setGeometry(QtCore.QRect(360, 210, 201, 4))
        self.ProgressBar_3.setMinimum(1)
        self.ProgressBar_3.setProperty("value", 34)
        self.ProgressBar_3.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar_3.setUseAni(True)
        self.ProgressBar_3.setVal(34.0)
        self.ProgressBar_3.setObjectName("ProgressBar_3")
        self.ProgressBar_4 = ProgressBar(self.CardWidget)
        self.ProgressBar_4.setGeometry(QtCore.QRect(360, 260, 201, 4))
        self.ProgressBar_4.setMinimum(1)
        self.ProgressBar_4.setProperty("value", 85)
        self.ProgressBar_4.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar_4.setUseAni(True)
        self.ProgressBar_4.setVal(85.0)
        self.ProgressBar_4.setObjectName("ProgressBar_4")
        self.ProgressBar_5 = ProgressBar(self.CardWidget)
        self.ProgressBar_5.setGeometry(QtCore.QRect(360, 310, 201, 4))
        self.ProgressBar_5.setMinimum(1)
        self.ProgressBar_5.setProperty("value", 65)
        self.ProgressBar_5.setOrientation(QtCore.Qt.Horizontal)
        self.ProgressBar_5.setUseAni(True)
        self.ProgressBar_5.setVal(65.0)
        self.ProgressBar_5.setObjectName("ProgressBar_5")
        self.BodyLabel_5 = BodyLabel(self.CardWidget)
        self.BodyLabel_5.setGeometry(QtCore.QRect(280, 150, 71, 19))
        self.BodyLabel_5.setObjectName("BodyLabel_5")
        self.BodyLabel_6 = BodyLabel(self.CardWidget)
        self.BodyLabel_6.setGeometry(QtCore.QRect(280, 200, 71, 19))
        self.BodyLabel_6.setObjectName("BodyLabel_6")
        self.ProgressRing = ProgressRing(self.CardWidget)
        self.ProgressRing.setGeometry(QtCore.QRect(60, 140, 200, 200))
        self.ProgressRing.setMinimumSize(QtCore.QSize(200, 200))
        self.ProgressRing.setMaximumSize(QtCore.QSize(200, 200))
        self.ProgressRing.setMaximum(10)
        self.ProgressRing.setProperty("value", 6)
        self.ProgressRing.setStrokeWidth(16)
        self.ProgressRing.setObjectName("ProgressRing")
        self.BodyLabel_7 = BodyLabel(self.CardWidget)
        self.BodyLabel_7.setGeometry(QtCore.QRect(280, 250, 71, 19))
        self.BodyLabel_7.setObjectName("BodyLabel_7")
        self.BodyLabel_8 = BodyLabel(self.CardWidget)
        self.BodyLabel_8.setGeometry(QtCore.QRect(280, 300, 71, 19))
        self.BodyLabel_8.setObjectName("BodyLabel_8")
        self.CaptionLabel_2 = CaptionLabel(self.CardWidget)
        self.CaptionLabel_2.setGeometry(QtCore.QRect(220, 30, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CaptionLabel_2.setFont(font)
        self.CaptionLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_2.setObjectName("CaptionLabel_2")
        self.CaptionLabel = CaptionLabel(Form)
        self.CaptionLabel.setGeometry(QtCore.QRect(625, 120, 431, 71))
        font = QtGui.QFont()
        font.setFamily("霞鹜文楷 GB 屏幕阅读版 R")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.CaptionLabel.setFont(font)
        self.CaptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel.setProperty("pixelFontSize", -1)
        self.CaptionLabel.setObjectName("CaptionLabel")
        self.CardWidget_2 = CardWidget(Form)
        self.CardWidget_2.setGeometry(QtCore.QRect(1190, 220, 311, 521))
        self.CardWidget_2.setObjectName("CardWidget_2")
        self.SwitchButton_3 = SwitchButton(self.CardWidget_2)
        self.SwitchButton_3.setGeometry(QtCore.QRect(170, 230, 112, 37))
        self.SwitchButton_3.setChecked(True)
        self.SwitchButton_3.setObjectName("SwitchButton_3")
        self.SwitchButton_5 = SwitchButton(self.CardWidget_2)
        self.SwitchButton_5.setGeometry(QtCore.QRect(170, 330, 112, 37))
        self.SwitchButton_5.setChecked(False)
        self.SwitchButton_5.setObjectName("SwitchButton_5")
        self.SwitchButton_4 = SwitchButton(self.CardWidget_2)
        self.SwitchButton_4.setGeometry(QtCore.QRect(170, 280, 112, 37))
        self.SwitchButton_4.setChecked(True)
        self.SwitchButton_4.setObjectName("SwitchButton_4")
        self.SwitchButton = SwitchButton(self.CardWidget_2)
        self.SwitchButton.setGeometry(QtCore.QRect(170, 180, 112, 37))
        self.SwitchButton.setChecked(True)
        self.SwitchButton.setObjectName("SwitchButton")
        self.DropDownPushButton = DropDownPushButton(self.CardWidget_2)
        self.DropDownPushButton.setGeometry(QtCore.QRect(120, 60, 161, 32))
        self.DropDownPushButton.setObjectName("DropDownPushButton")
        self.DropDownPushButton_2 = DropDownPushButton(self.CardWidget_2)
        self.DropDownPushButton_2.setGeometry(QtCore.QRect(120, 110, 161, 32))
        self.DropDownPushButton_2.setObjectName("DropDownPushButton_2")
        self.BodyLabel_3 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_3.setGeometry(QtCore.QRect(40, 70, 65, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BodyLabel_3.setFont(font)
        self.BodyLabel_3.setObjectName("BodyLabel_3")
        self.BodyLabel_4 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_4.setGeometry(QtCore.QRect(40, 120, 65, 19))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BodyLabel_4.setFont(font)
        self.BodyLabel_4.setObjectName("BodyLabel_4")
        self.CheckBox = CheckBox(self.CardWidget_2)
        self.CheckBox.setGeometry(QtCore.QRect(40, 400, 93, 22))
        self.CheckBox.setChecked(True)
        self.CheckBox.setObjectName("CheckBox")
        self.CheckBox_2 = CheckBox(self.CardWidget_2)
        self.CheckBox_2.setGeometry(QtCore.QRect(180, 400, 93, 22))
        self.CheckBox_2.setObjectName("CheckBox_2")
        self.PushButton = PushButton(self.CardWidget_2)
        self.PushButton.setGeometry(QtCore.QRect(90, 440, 131, 51))
        font = QtGui.QFont()
        font.setFamily("JetBrainsMono Nerd Font")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.PushButton.setFont(font)
        self.PushButton.setObjectName("PushButton")
        self.TableWidget = TableWidget(self.CardWidget_2)
        self.TableWidget.setGeometry(QtCore.QRect(40, 180, 101, 181))
        self.TableWidget.setObjectName("TableWidget")
        self.TableWidget.setColumnCount(0)
        self.TableWidget.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.TableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TableWidget.setVerticalHeaderItem(6, item)
        self.CaptionLabel_3 = CaptionLabel(self.CardWidget_2)
        self.CaptionLabel_3.setGeometry(QtCore.QRect(70, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.CaptionLabel_3.setFont(font)
        self.CaptionLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.CaptionLabel_3.setObjectName("CaptionLabel_3")
        self.ImageLabel = ImageLabel(Form)
        self.ImageLabel.setGeometry(QtCore.QRect(770, 500, 1100, 250))
        self.ImageLabel.setMinimumSize(QtCore.QSize(1100, 250))
        self.ImageLabel.setMaximumSize(QtCore.QSize(900, 250))
        self.ImageLabel.setProperty("topLeftRadius", 15)
        self.ImageLabel.setProperty("topRightRadius", 15)
        self.ImageLabel.setProperty("bottomLeftRadius", 15)
        self.ImageLabel.setProperty("bottomRightRadius", 15)
        self.ImageLabel.setObjectName("ImageLabel")
        self.ImageLabel.setImage("src/img/curl.png")
        self.ImageLabel.setFixedSize(400, 250)

        self.ImageLabel_2 = ImageLabel(Form)
        self.ImageLabel_2.setGeometry(QtCore.QRect(770, 220, 400, 500))
        self.ImageLabel_2.setMinimumSize(QtCore.QSize(350, 500))
        self.ImageLabel_2.setMaximumSize(QtCore.QSize(400, 250))
        self.ImageLabel_2.setProperty("topLeftRadius", 15)
        self.ImageLabel_2.setProperty("topRightRadius", 15)
        self.ImageLabel_2.setProperty("bottomLeftRadius", 15)
        self.ImageLabel_2.setProperty("bottomRightRadius", 15)
        self.ImageLabel_2.setObjectName("ImageLabel_2")
        self.ImageLabel_2.setImage("src/img/teacher.png")
        self.ImageLabel_2.setFixedSize(400, 250)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.BodyLabel.setText(_translate("Form", "正在反馈输入信息"))
        self.StrongBodyLabel.setText(_translate("Form", "综合评价：76"))
        self.BodyLabel_5.setText(_translate("Form", "姿态准确度"))
        self.BodyLabel_6.setText(_translate("Form", "速度匹配度"))
        self.BodyLabel_7.setText(_translate("Form", "掌握置信度"))
        self.BodyLabel_8.setText(_translate("Form", "语义理解度"))
        self.CaptionLabel_2.setText(_translate("Form", "评价结果"))
        self.CaptionLabel.setText(_translate("Form", "三维手语教学平台"))
        self.SwitchButton_3.setText(_translate("Form", "人体重建"))
        self.SwitchButton_3.setOnText(_translate("Form", "人体重建"))
        self.SwitchButton_3.setOffText(_translate("Form", "人体重建"))
        self.SwitchButton_5.setText(_translate("Form", "在线评价"))
        self.SwitchButton_5.setOnText(_translate("Form", "在线评价"))
        self.SwitchButton_5.setOffText(_translate("Form", "在线评价"))
        self.SwitchButton_4.setText(_translate("Form", "评价反馈"))
        self.SwitchButton_4.setOnText(_translate("Form", "评价反馈"))
        self.SwitchButton_4.setOffText(_translate("Form", "评价反馈"))
        self.SwitchButton.setText(_translate("Form", "动作捕捉"))
        self.SwitchButton.setOnText(_translate("Form", "动作捕捉"))
        self.SwitchButton.setOffText(_translate("Form", "动作捕捉"))
        self.DropDownPushButton.setText(_translate("Form", "FrankMocap"))
        self.DropDownPushButton_2.setText(_translate("Form", "DTW动态时间扭曲"))
        self.BodyLabel_3.setText(_translate("Form", "姿态引擎"))
        self.BodyLabel_4.setText(_translate("Form", "评价算法"))
        self.CheckBox.setText(_translate("Form", "隐私保护"))
        self.CheckBox_2.setText(_translate("Form", "数据加密"))
        self.PushButton.setText(_translate("Form", "GO!"))
        item = self.TableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "当前配置"))
        item = self.TableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "FrankMoCap"))
        item = self.TableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "DTW"))
        item = self.TableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "动作捕捉"))
        item = self.TableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "人体重建"))
        item = self.TableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "评价反馈"))
        item = self.TableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "隐私保护"))
        self.CaptionLabel_3.setText(_translate("Form", "控制台"))


from qfluentwidgets import BodyLabel, CaptionLabel, CardWidget, CheckBox, DropDownPushButton, ImageLabel, ProgressBar, \
    ProgressRing, PushButton, StateToolTip, StrongBodyLabel, SwitchButton, TableWidget
