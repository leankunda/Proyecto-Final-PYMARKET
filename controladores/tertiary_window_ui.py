# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tertiary_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaTerciaria(object):
    def setupUi(self, VentanaTerciaria):
        VentanaTerciaria.setObjectName("VentanaTerciaria")
        VentanaTerciaria.resize(1000, 600)
        VentanaTerciaria.setMinimumSize(QtCore.QSize(1000, 600))
        VentanaTerciaria.setMaximumSize(QtCore.QSize(1000, 600))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        VentanaTerciaria.setPalette(palette)
        self.verticalLayout = QtWidgets.QVBoxLayout(VentanaTerciaria)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lVENDER = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lVENDER.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.lVENDER.setFont(font)
        self.lVENDER.setObjectName("lVENDER")
        self.horizontalLayout.addWidget(self.lVENDER)
        self.pPUBLICAR = QtWidgets.QPushButton(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.pPUBLICAR.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pPUBLICAR.setFont(font)
        self.pPUBLICAR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pPUBLICAR.setObjectName("pPUBLICAR")
        self.horizontalLayout.addWidget(self.pPUBLICAR)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.lNOMBRE = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lNOMBRE.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.lNOMBRE.setFont(font)
        self.lNOMBRE.setObjectName("lNOMBRE")
        self.verticalLayout_4.addWidget(self.lNOMBRE)
        self.lineNOMBRE = QtWidgets.QLineEdit(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(154, 153, 150))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        self.lineNOMBRE.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineNOMBRE.setFont(font)
        self.lineNOMBRE.setText("")
        self.lineNOMBRE.setObjectName("lineNOMBRE")
        self.verticalLayout_4.addWidget(self.lineNOMBRE)
        self.lDESCRIPCION = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lDESCRIPCION.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lDESCRIPCION.setFont(font)
        self.lDESCRIPCION.setObjectName("lDESCRIPCION")
        self.verticalLayout_4.addWidget(self.lDESCRIPCION)
        self.lineDESCRIPCION = QtWidgets.QLineEdit(VentanaTerciaria)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineDESCRIPCION.setFont(font)
        self.lineDESCRIPCION.setText("")
        self.lineDESCRIPCION.setObjectName("lineDESCRIPCION")
        self.verticalLayout_4.addWidget(self.lineDESCRIPCION)
        self.lPRECIO = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Highlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 116, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 145))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Highlight, brush)
        self.lPRECIO.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lPRECIO.setFont(font)
        self.lPRECIO.setObjectName("lPRECIO")
        self.verticalLayout_4.addWidget(self.lPRECIO)
        self.linePRECIO = QtWidgets.QLineEdit(VentanaTerciaria)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.linePRECIO.setFont(font)
        self.linePRECIO.setText("")
        self.linePRECIO.setObjectName("linePRECIO")
        self.verticalLayout_4.addWidget(self.linePRECIO)
        self.lSTOCK = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lSTOCK.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lSTOCK.setFont(font)
        self.lSTOCK.setObjectName("lSTOCK")
        self.verticalLayout_4.addWidget(self.lSTOCK)
        self.lineSTOCK = QtWidgets.QLineEdit(VentanaTerciaria)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lineSTOCK.setFont(font)
        self.lineSTOCK.setText("")
        self.lineSTOCK.setObjectName("lineSTOCK")
        self.verticalLayout_4.addWidget(self.lineSTOCK)
        self.lPESO = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lPESO.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lPESO.setFont(font)
        self.lPESO.setObjectName("lPESO")
        self.verticalLayout_4.addWidget(self.lPESO)
        self.linePESO = QtWidgets.QLineEdit(VentanaTerciaria)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.linePESO.setFont(font)
        self.linePESO.setText("")
        self.linePESO.setObjectName("linePESO")
        self.verticalLayout_4.addWidget(self.linePESO)
        self.lCATEGORIA = QtWidgets.QLabel(VentanaTerciaria)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lCATEGORIA.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.lCATEGORIA.setFont(font)
        self.lCATEGORIA.setObjectName("lCATEGORIA")
        self.verticalLayout_4.addWidget(self.lCATEGORIA)
        self.comboCATEGORIA = QtWidgets.QComboBox(VentanaTerciaria)
        font = QtGui.QFont()
        font.setFamily("San Francisco Display")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboCATEGORIA.setFont(font)
        self.comboCATEGORIA.setCursor(QtGui.QCursor(QtCore.Qt.SizeAllCursor))
        self.comboCATEGORIA.setObjectName("comboCATEGORIA")
        self.comboCATEGORIA.addItem("")
        self.comboCATEGORIA.addItem("")
        self.comboCATEGORIA.addItem("")
        self.comboCATEGORIA.addItem("")
        self.verticalLayout_4.addWidget(self.comboCATEGORIA)
        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.retranslateUi(VentanaTerciaria)
        QtCore.QMetaObject.connectSlotsByName(VentanaTerciaria)

    def retranslateUi(self, VentanaTerciaria):
        _translate = QtCore.QCoreApplication.translate
        VentanaTerciaria.setWindowTitle(_translate("VentanaTerciaria", "Ventana Terciaria"))
        self.lVENDER.setText(_translate("VentanaTerciaria", "VENDER"))
        self.pPUBLICAR.setText(_translate("VentanaTerciaria", "PUBLICAR PRODUCTO"))
        self.lNOMBRE.setText(_translate("VentanaTerciaria", "Nombre del producto"))
        self.lDESCRIPCION.setText(_translate("VentanaTerciaria", "Descripcion corta"))
        self.lPRECIO.setText(_translate("VentanaTerciaria", "Precio"))
        self.lSTOCK.setText(_translate("VentanaTerciaria", "Stock disponible"))
        self.lPESO.setText(_translate("VentanaTerciaria", "Peso"))
        self.lCATEGORIA.setText(_translate("VentanaTerciaria", "Categoria"))
        self.comboCATEGORIA.setItemText(0, _translate("VentanaTerciaria", "Arte"))
        self.comboCATEGORIA.setItemText(1, _translate("VentanaTerciaria", "Tecnologia"))
        self.comboCATEGORIA.setItemText(2, _translate("VentanaTerciaria", "Vehiculos"))
        self.comboCATEGORIA.setItemText(3, _translate("VentanaTerciaria", "Comida"))
