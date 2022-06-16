# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 373)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_main = QtWidgets.QVBoxLayout()
        self.verticalLayout_main.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_main.setObjectName("verticalLayout_main")
        self.horizontalLayout_device = QtWidgets.QHBoxLayout()
        self.horizontalLayout_device.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout_device.setObjectName("horizontalLayout_device")
        self.label_device = QtWidgets.QLabel(self.centralwidget)
        self.label_device.setObjectName("label_device")
        self.horizontalLayout_device.addWidget(self.label_device)
        self.comboBox_device_list = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_device_list.sizePolicy().hasHeightForWidth())
        self.comboBox_device_list.setSizePolicy(sizePolicy)
        self.comboBox_device_list.setObjectName("comboBox_device_list")
        self.horizontalLayout_device.addWidget(self.comboBox_device_list)
        self.pushButton_root = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_root.setObjectName("pushButton_root")
        self.horizontalLayout_device.addWidget(self.pushButton_root)
        self.pushButton_kill_cam = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_kill_cam.setObjectName("pushButton_kill_cam")
        self.horizontalLayout_device.addWidget(self.pushButton_kill_cam)
        self.verticalLayout_main.addLayout(self.horizontalLayout_device)
        self.gridLayout.addLayout(self.verticalLayout_main, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_main.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_main.setObjectName("tabWidget_main")
        self.tab_log_pull = QtWidgets.QWidget()
        self.tab_log_pull.setObjectName("tab_log_pull")
        self.tabWidget_main.addTab(self.tab_log_pull, "")
        self.tab_log_level = QtWidgets.QWidget()
        self.tab_log_level.setObjectName("tab_log_level")
        self.tabWidget_main.addTab(self.tab_log_level, "")
        self.horizontalLayout.addWidget(self.tabWidget_main)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 23))
        self.menubar.setObjectName("menubar")
        self.menu_others = QtWidgets.QMenu(self.menubar)
        self.menu_others.setObjectName("menu_others")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_log_level_settings = QtWidgets.QAction(MainWindow)
        self.action_log_level_settings.setObjectName("action_log_level_settings")
        self.action_refresh_device_list = QtWidgets.QAction(MainWindow)
        self.action_refresh_device_list.setObjectName("action_refresh_device_list")
        self.action_check_upgrade = QtWidgets.QAction(MainWindow)
        self.action_check_upgrade.setObjectName("action_check_upgrade")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu_others.addAction(self.action_refresh_device_list)
        self.menu_others.addAction(self.action_check_upgrade)
        self.menu_others.addSeparator()
        self.menu_others.addAction(self.action_about)
        self.menu_settings.addAction(self.action_log_level_settings)
        self.menubar.addAction(self.menu_settings.menuAction())
        self.menubar.addAction(self.menu_others.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AndroidLogs"))
        self.label_device.setText(_translate("MainWindow", "设备列表"))
        self.pushButton_root.setText(_translate("MainWindow", "remount"))
        self.pushButton_kill_cam.setText(_translate("MainWindow", "kill Camera server"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_log_pull), _translate("MainWindow", "日志拉取"))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_log_level), _translate("MainWindow", "日志设置"))
        self.menu_others.setTitle(_translate("MainWindow", "其它"))
        self.menu_settings.setTitle(_translate("MainWindow", "设置"))
        self.action_log_level_settings.setText(_translate("MainWindow", "日志分组设置"))
        self.action_refresh_device_list.setText(_translate("MainWindow", "刷新设备列表"))
        self.action_check_upgrade.setText(_translate("MainWindow", "检查更新"))
        self.action_about.setText(_translate("MainWindow", "关于"))