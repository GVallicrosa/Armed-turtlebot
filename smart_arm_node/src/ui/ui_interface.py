# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created: Wed Nov  7 17:52:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(700, 410)
        Dialog.setMinimumSize(QtCore.QSize(700, 410))
        Dialog.setMaximumSize(QtCore.QSize(700, 410))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/all/icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout_9 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinj1 = QtGui.QDoubleSpinBox(Dialog)
        self.spinj1.setObjectName(_fromUtf8("spinj1"))
        self.gridLayout.addWidget(self.spinj1, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.spinj3 = QtGui.QDoubleSpinBox(Dialog)
        self.spinj3.setObjectName(_fromUtf8("spinj3"))
        self.gridLayout.addWidget(self.spinj3, 0, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinj2 = QtGui.QDoubleSpinBox(Dialog)
        self.spinj2.setObjectName(_fromUtf8("spinj2"))
        self.gridLayout.addWidget(self.spinj2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.spinj4 = QtGui.QDoubleSpinBox(Dialog)
        self.spinj4.setObjectName(_fromUtf8("spinj4"))
        self.gridLayout.addWidget(self.spinj4, 1, 3, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout)
        self.pushButton_mjnts = QtGui.QPushButton(Dialog)
        self.pushButton_mjnts.setObjectName(_fromUtf8("pushButton_mjnts"))
        self.verticalLayout_6.addWidget(self.pushButton_mjnts)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        spacerItem = QtGui.QSpacerItem(58, 86, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label_j3 = QtGui.QLabel(Dialog)
        self.label_j3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j3.setObjectName(_fromUtf8("label_j3"))
        self.verticalLayout_4.addWidget(self.label_j3)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.pushButton_j3min = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j3min.sizePolicy().hasHeightForWidth())
        self.pushButton_j3min.setSizePolicy(sizePolicy)
        self.pushButton_j3min.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j3min.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j3min.setObjectName(_fromUtf8("pushButton_j3min"))
        self.horizontalLayout_8.addWidget(self.pushButton_j3min)
        self.pushButton_j3plus = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j3plus.sizePolicy().hasHeightForWidth())
        self.pushButton_j3plus.setSizePolicy(sizePolicy)
        self.pushButton_j3plus.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j3plus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j3plus.setObjectName(_fromUtf8("pushButton_j3plus"))
        self.horizontalLayout_8.addWidget(self.pushButton_j3plus)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.slider_j3 = QtGui.QSlider(Dialog)
        self.slider_j3.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_j3.sizePolicy().hasHeightForWidth())
        self.slider_j3.setSizePolicy(sizePolicy)
        self.slider_j3.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_j3.setMaximum(100)
        self.slider_j3.setOrientation(QtCore.Qt.Horizontal)
        self.slider_j3.setObjectName(_fromUtf8("slider_j3"))
        self.verticalLayout_4.addWidget(self.slider_j3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        spacerItem3 = QtGui.QSpacerItem(15, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_j4 = QtGui.QLabel(Dialog)
        self.label_j4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j4.setObjectName(_fromUtf8("label_j4"))
        self.verticalLayout_5.addWidget(self.label_j4)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.pushButton_j4min = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j4min.sizePolicy().hasHeightForWidth())
        self.pushButton_j4min.setSizePolicy(sizePolicy)
        self.pushButton_j4min.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_j4min.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j4min.setObjectName(_fromUtf8("pushButton_j4min"))
        self.horizontalLayout_7.addWidget(self.pushButton_j4min)
        self.pushButton_j4plus = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j4plus.sizePolicy().hasHeightForWidth())
        self.pushButton_j4plus.setSizePolicy(sizePolicy)
        self.pushButton_j4plus.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j4plus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j4plus.setObjectName(_fromUtf8("pushButton_j4plus"))
        self.horizontalLayout_7.addWidget(self.pushButton_j4plus)
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.slider_j4 = QtGui.QSlider(Dialog)
        self.slider_j4.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_j4.sizePolicy().hasHeightForWidth())
        self.slider_j4.setSizePolicy(sizePolicy)
        self.slider_j4.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_j4.setMaximum(100)
        self.slider_j4.setOrientation(QtCore.Qt.Horizontal)
        self.slider_j4.setObjectName(_fromUtf8("slider_j4"))
        self.verticalLayout_5.addWidget(self.slider_j4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem6 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_10.addWidget(self.label_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.increment_spin = QtGui.QDoubleSpinBox(Dialog)
        self.increment_spin.setMaximum(1.0)
        self.increment_spin.setSingleStep(0.01)
        self.increment_spin.setProperty("value", 0.05)
        self.increment_spin.setObjectName(_fromUtf8("increment_spin"))
        self.horizontalLayout_5.addWidget(self.increment_spin)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        spacerItem8 = QtGui.QSpacerItem(149, 13, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_j2 = QtGui.QLabel(Dialog)
        self.label_j2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j2.setObjectName(_fromUtf8("label_j2"))
        self.verticalLayout_2.addWidget(self.label_j2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.pushButton_j2min = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j2min.sizePolicy().hasHeightForWidth())
        self.pushButton_j2min.setSizePolicy(sizePolicy)
        self.pushButton_j2min.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j2min.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j2min.setObjectName(_fromUtf8("pushButton_j2min"))
        self.horizontalLayout_6.addWidget(self.pushButton_j2min)
        self.pushButton_j2plus = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j2plus.sizePolicy().hasHeightForWidth())
        self.pushButton_j2plus.setSizePolicy(sizePolicy)
        self.pushButton_j2plus.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j2plus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j2plus.setObjectName(_fromUtf8("pushButton_j2plus"))
        self.horizontalLayout_6.addWidget(self.pushButton_j2plus)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.slider_j2 = QtGui.QSlider(Dialog)
        self.slider_j2.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_j2.sizePolicy().hasHeightForWidth())
        self.slider_j2.setSizePolicy(sizePolicy)
        self.slider_j2.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_j2.setMaximum(100)
        self.slider_j2.setOrientation(QtCore.Qt.Horizontal)
        self.slider_j2.setObjectName(_fromUtf8("slider_j2"))
        self.verticalLayout_2.addWidget(self.slider_j2)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        spacerItem11 = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem11)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_j1 = QtGui.QLabel(Dialog)
        self.label_j1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_j1.setObjectName(_fromUtf8("label_j1"))
        self.verticalLayout.addWidget(self.label_j1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        self.pushButton_j1min = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j1min.sizePolicy().hasHeightForWidth())
        self.pushButton_j1min.setSizePolicy(sizePolicy)
        self.pushButton_j1min.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j1min.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j1min.setObjectName(_fromUtf8("pushButton_j1min"))
        self.horizontalLayout_2.addWidget(self.pushButton_j1min)
        self.pushButton_j1plus = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_j1plus.sizePolicy().hasHeightForWidth())
        self.pushButton_j1plus.setSizePolicy(sizePolicy)
        self.pushButton_j1plus.setMinimumSize(QtCore.QSize(40, 0))
        self.pushButton_j1plus.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_j1plus.setObjectName(_fromUtf8("pushButton_j1plus"))
        self.horizontalLayout_2.addWidget(self.pushButton_j1plus)
        spacerItem13 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.slider_j1 = QtGui.QSlider(Dialog)
        self.slider_j1.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider_j1.sizePolicy().hasHeightForWidth())
        self.slider_j1.setSizePolicy(sizePolicy)
        self.slider_j1.setMinimumSize(QtCore.QSize(150, 0))
        self.slider_j1.setMaximum(100)
        self.slider_j1.setSingleStep(2)
        self.slider_j1.setTracking(True)
        self.slider_j1.setOrientation(QtCore.Qt.Horizontal)
        self.slider_j1.setInvertedAppearance(False)
        self.slider_j1.setInvertedControls(False)
        self.slider_j1.setTickPosition(QtGui.QSlider.NoTicks)
        self.slider_j1.setObjectName(_fromUtf8("slider_j1"))
        self.verticalLayout.addWidget(self.slider_j1)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/all/schematic.svg")))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_7.addWidget(self.label_5)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.stat_j1 = QtGui.QLabel(Dialog)
        self.stat_j1.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_j1.setObjectName(_fromUtf8("stat_j1"))
        self.horizontalLayout.addWidget(self.stat_j1)
        self.stat_j2 = QtGui.QLabel(Dialog)
        self.stat_j2.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_j2.setObjectName(_fromUtf8("stat_j2"))
        self.horizontalLayout.addWidget(self.stat_j2)
        self.stat_j3 = QtGui.QLabel(Dialog)
        self.stat_j3.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_j3.setObjectName(_fromUtf8("stat_j3"))
        self.horizontalLayout.addWidget(self.stat_j3)
        self.stat_j4 = QtGui.QLabel(Dialog)
        self.stat_j4.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_j4.setObjectName(_fromUtf8("stat_j4"))
        self.horizontalLayout.addWidget(self.stat_j4)
        self.stat_j5 = QtGui.QLabel(Dialog)
        self.stat_j5.setAlignment(QtCore.Qt.AlignCenter)
        self.stat_j5.setWordWrap(True)
        self.stat_j5.setObjectName(_fromUtf8("stat_j5"))
        self.horizontalLayout.addWidget(self.stat_j5)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem14 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem14)
        self.pushButton_grab = QtGui.QPushButton(Dialog)
        self.pushButton_grab.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton_grab.setObjectName(_fromUtf8("pushButton_grab"))
        self.verticalLayout_3.addWidget(self.pushButton_grab)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem15)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_13)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.stat_y = QtGui.QLabel(Dialog)
        self.stat_y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stat_y.setObjectName(_fromUtf8("stat_y"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.stat_y)
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.stat_z = QtGui.QLabel(Dialog)
        self.stat_z.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stat_z.setObjectName(_fromUtf8("stat_z"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.stat_z)
        self.stat_x = QtGui.QLabel(Dialog)
        self.stat_x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stat_x.setObjectName(_fromUtf8("stat_x"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.stat_x)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem16)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.stat_j5_2 = QtGui.QLabel(Dialog)
        self.stat_j5_2.setObjectName(_fromUtf8("stat_j5_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.stat_j5_2)
        self.spinx = QtGui.QDoubleSpinBox(Dialog)
        self.spinx.setMinimum(-0.5)
        self.spinx.setMaximum(0.5)
        self.spinx.setSingleStep(0.1)
        self.spinx.setObjectName(_fromUtf8("spinx"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spinx)
        self.stat_j5_3 = QtGui.QLabel(Dialog)
        self.stat_j5_3.setObjectName(_fromUtf8("stat_j5_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.stat_j5_3)
        self.spiny = QtGui.QDoubleSpinBox(Dialog)
        self.spiny.setMinimum(-0.5)
        self.spiny.setMaximum(0.5)
        self.spiny.setSingleStep(0.1)
        self.spiny.setObjectName(_fromUtf8("spiny"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spiny)
        self.stat_j5_4 = QtGui.QLabel(Dialog)
        self.stat_j5_4.setObjectName(_fromUtf8("stat_j5_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.stat_j5_4)
        self.spinz = QtGui.QDoubleSpinBox(Dialog)
        self.spinz.setMinimum(-0.5)
        self.spinz.setMaximum(0.5)
        self.spinz.setSingleStep(0.1)
        self.spinz.setObjectName(_fromUtf8("spinz"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinz)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.pushButton_xyz = QtGui.QPushButton(Dialog)
        self.pushButton_xyz.setObjectName(_fromUtf8("pushButton_xyz"))
        self.verticalLayout_3.addWidget(self.pushButton_xyz)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.spinj1, self.spinj2)
        Dialog.setTabOrder(self.spinj2, self.spinj3)
        Dialog.setTabOrder(self.spinj3, self.spinj4)
        Dialog.setTabOrder(self.spinj4, self.pushButton_mjnts)
        Dialog.setTabOrder(self.pushButton_mjnts, self.spinx)
        Dialog.setTabOrder(self.spinx, self.spiny)
        Dialog.setTabOrder(self.spiny, self.spinz)
        Dialog.setTabOrder(self.spinz, self.pushButton_xyz)
        Dialog.setTabOrder(self.pushButton_xyz, self.pushButton_j1min)
        Dialog.setTabOrder(self.pushButton_j1min, self.pushButton_j1plus)
        Dialog.setTabOrder(self.pushButton_j1plus, self.pushButton_j2min)
        Dialog.setTabOrder(self.pushButton_j2min, self.pushButton_j2plus)
        Dialog.setTabOrder(self.pushButton_j2plus, self.pushButton_j3min)
        Dialog.setTabOrder(self.pushButton_j3min, self.pushButton_j3plus)
        Dialog.setTabOrder(self.pushButton_j3plus, self.pushButton_j4min)
        Dialog.setTabOrder(self.pushButton_j4min, self.pushButton_j4plus)
        Dialog.setTabOrder(self.pushButton_j4plus, self.pushButton_grab)
        Dialog.setTabOrder(self.pushButton_grab, self.slider_j1)
        Dialog.setTabOrder(self.slider_j1, self.slider_j2)
        Dialog.setTabOrder(self.slider_j2, self.slider_j3)
        Dialog.setTabOrder(self.slider_j3, self.slider_j4)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Smart Arm Controller Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "j1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "j3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "j2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "j4:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_mjnts.setText(QtGui.QApplication.translate("Dialog", "Move joints", None, QtGui.QApplication.UnicodeUTF8))
        self.label_j3.setText(QtGui.QApplication.translate("Dialog", "elbow_flex (Q/W)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j3min.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j3min.setShortcut(QtGui.QApplication.translate("Dialog", "Q", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j3plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j3plus.setShortcut(QtGui.QApplication.translate("Dialog", "W", None, QtGui.QApplication.UnicodeUTF8))
        self.label_j4.setText(QtGui.QApplication.translate("Dialog", "wrist_roll (1/2)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j4min.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j4min.setShortcut(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j4plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j4plus.setShortcut(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Angle increment:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_j2.setText(QtGui.QApplication.translate("Dialog", "shoulder_pitch (A/S)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j2min.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j2min.setShortcut(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j2plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j2plus.setShortcut(QtGui.QApplication.translate("Dialog", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.label_j1.setText(QtGui.QApplication.translate("Dialog", "shoulder_pan (Z/X)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j1min.setText(QtGui.QApplication.translate("Dialog", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j1min.setShortcut(QtGui.QApplication.translate("Dialog", "Z", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j1plus.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_j1plus.setShortcut(QtGui.QApplication.translate("Dialog", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j1.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j2.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j3.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j4.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j5.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_grab.setText(QtGui.QApplication.translate("Dialog", "Grab (G)", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_grab.setShortcut(QtGui.QApplication.translate("Dialog", "G", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "X :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Y :", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_y.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Z :", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_z.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_x.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j5_2.setText(QtGui.QApplication.translate("Dialog", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j5_3.setText(QtGui.QApplication.translate("Dialog", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.stat_j5_4.setText(QtGui.QApplication.translate("Dialog", "Z:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_xyz.setText(QtGui.QApplication.translate("Dialog", "Move xyz", None, QtGui.QApplication.UnicodeUTF8))

import interface_rc
