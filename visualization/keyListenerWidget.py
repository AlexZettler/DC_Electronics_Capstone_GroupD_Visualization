from PyQt5.QtWidgets import QPushButton, QTabWidget, QLineEdit, QLabel, QWidget
from PyQt5 import QtCore
from PyQt5 import QtGui


class iKeyListenerWidget(QWidget):
    keyPressed = QtCore.pyqtSignal(int)
    keyReleased = QtCore.pyqtSignal(int)

    def keyPressEvent(self, event: QtGui.QKeyEvent):
        print("Key pressed")
        super(iKeyListenerWidget, self).keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def keyReleaseEvent(self, event: QtGui.QKeyEvent):
        super(iKeyListenerWidget, self).keyReleaseEvent(event)
        self.keyReleased.emit(event.key())
