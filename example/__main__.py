"""PySide6 example application demonstrating the use of PySide6-DAW."""

import sys
from pathlib import Path

from PySide6.QtCore import QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

from PySide6DAW.Widgets import DesktopApplication, SideBarButton


class MainWindow(QMainWindow):
    """TODO"""

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(parent=None)

        self.setWindowTitle("MenuButton Test")

        desktop_application = DesktopApplication(self)
        self.setCentralWidget(desktop_application)

        icon = QPixmap(Path("./settings.svg"))

        # Page 1
        btn_1 = SideBarButton(icon, "Button 1")
        page_1 = QWidget()
        page_1_btn = QPushButton(page_1)
        page_1_btn.setGeometry(QRect(100, 100, 75, 24))
        page_1_btn.setText("Test 1")
        desktop_application.addPage(btn_1, SideBarButton.Alignment.TOP, page_1)

        # Page 2
        btn_2 = SideBarButton(icon, "Button 2")
        page_2 = QWidget()
        page_2_btn = QPushButton(page_2)
        page_2_btn.setGeometry(QRect(0, 0, 75, 24))
        page_2_btn.setText("Test 2")
        desktop_application.addPage(btn_2, SideBarButton.Alignment.TOP, page_2)

        # Page 3
        btn_3 = SideBarButton(icon, "Button 3")
        page_3 = QWidget()
        page_3_btn = QPushButton(page_3)
        page_3_btn.setGeometry(QRect(50, 50, 75, 24))
        page_3_btn.setText("Test 3")
        desktop_application.addPage(btn_3, SideBarButton.Alignment.BOTTOM, page_3)


def main() -> None:
    """Main function"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Style sheet with the default color theme
    # with open("style.qss", "r", encoding="utf-8") as f:
    #    app.setStyleSheet(f.read())

    # Style sheet with custom color theme
    # with open("style2.qss", "r", encoding="utf-8") as style_sheet:
    #    app.setStyleSheet(style_sheet.read())

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
