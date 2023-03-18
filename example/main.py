import sys
import platform
from pathlib import Path

from PySide6.QtCore import QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PySide6.QtGui import QIcon, QPixmap

from PySide6_DAW.Widgets import ApplicationWidget
from PySide6_DAW.Widgets import SideBarButton


class MainWindow(QMainWindow):
    """TODO
    """
    def __init__(self) -> None:
        """Constructor
        """
        super().__init__(parent=None)

        #self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("MenuButton Test")
        self.setWindowIcon(QIcon("settings.svg"))
        self.setStyleSheet("background-color: #2c313c")

        application_widget = ApplicationWidget(self)
        self.setCentralWidget(application_widget)

        icon = QPixmap(Path("./settings.svg"))

        # Page 1
        b1 = SideBarButton(icon, "Button 1")
        p1 = QWidget()
        p1_button = QPushButton(p1)
        p1_button.setGeometry(QRect(100, 100, 75, 24))
        p1_button.setText("Test 1")
        application_widget.addPage(b1, SideBarButton.Alignment.TOP, p1)

        # Page 2
        b2 = SideBarButton(icon, "Button 2")
        p2 = QWidget()
        p2_button = QPushButton(p2)
        p2_button.setGeometry(QRect(0, 0, 75, 24))
        p2_button.setText("Test 2")
        application_widget.addPage(b2, SideBarButton.Alignment.TOP, p2)

        # Page 3
        b3 = SideBarButton(icon, "Button 3")
        p3 = QWidget()
        p3_button = QPushButton(p3)
        p3_button.setGeometry(QRect(50, 50, 75, 24))
        p3_button.setText("Test 3")
        application_widget.addPage(b3, SideBarButton.Alignment.BOTTOM, p3)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


# TODO: Not working yet!
def change_window_title_bar_color():
    if platform.system() == "Windows":
        import ctypes
        from ctypes.wintypes import RGB
        from ctypes import byref, c_int
        
        color = RGB(255, 0, 0)
        print(ctypes.windll.user32.SetSysColors(2, byref(c_int(2)), byref(c_int(color))))


if __name__ == "__main__":
    main()
