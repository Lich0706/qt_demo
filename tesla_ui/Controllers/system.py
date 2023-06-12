from PySide6 import QtCore
import time
import sys


class System(QtCore.QObject):
    def __init__(self, carLocked, outdoorTemp, userName):
        # carLocked, outdoorTemp, userName

        QtCore.QObject.__init__(self)
        self.carLocked = carLocked
        self.outdoorTemp = outdoorTemp
        self.userName = userName
        # self.carLocked = True
        # self.outdoorTemp = 54
        # self.userName = "lich"

        # self.currentTime = ''
        # self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.showTime)

    def printSelf(self):
        print("carlocked: " + str(self.carLocked) +
              " temp: " + str(self.outdoorTemp))

    # def showTime(self):
    #     time = QtCore.QDateTime.currentDateTime()
    #     timeDisplay = time.toString('yyyy-MM-dd hh:mm')
    #     self.currentTime = timeDisplay

    def carLocked(self):
        return self.carLocked

    def getOutdoorTemp(self):
        return self.outdoorTemp

    def getUserName(self):
        return self.userName

    carLockedChanged = QtCore.Signal(bool)

    @QtCore.Slot(bool)
    def setCarLocked(self, carLocked):
        if (self.carLocked == carLocked):
            return
        else:
            self.carLocked = carLocked
            self.carLockedChanged.emit(carLocked)

    outdoorTempChanged = QtCore.Signal(int)

    @QtCore.Slot(int)
    def setOutdoorTemp(self, outdoorTemp):
        if (self.outdoorTemp == outdoorTemp):
            return
        else:
            self.outdoorTemp = outdoorTemp
            self.outdoorTempChanged.emit(outdoorTemp)

    userNameChanged = QtCore.Signal(str)

    @QtCore.Slot(str)
    def setUserName(self, userName):
        if (self.userName == userName):
            return
        else:
            self.userName = userName
            self.userNameChanged.emit(userName)

    m_carLocked = QtCore.Property(bool, carLocked, notify=carLockedChanged)

    # @QtCore.Slot(str)
    # def currTimerTimeout(self, userName):
    #     if (self.userName == userName):
    #         return
    #     else:
    #         self.userName = userName
    #         self.userNameChanged.emit(userName)
