"""PySide6 example application demonstrating the use of PySide6-DAW."""

import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget

from PySide6_DAW.Widgets import DesktopApplication, SideBarButton


class MainWindow(QMainWindow):
    """Main Window class."""

    def __init__(self) -> None:
        """Constructor"""
        super().__init__(parent=None)

        self.setWindowTitle("PySide6-DAW Example")
        self.setMinimumSize(800, 600)

        desktop_application = DesktopApplication(self)
        self.setCentralWidget(desktop_application)

        icon = QPixmap(Path(__file__).parent.joinpath("settings.svg"))

        # Page 1
        btn_1 = SideBarButton(icon, "Button 1")
        page_1 = QWidget()
        page_1_layout = QGridLayout(page_1)
        page_1_label = QLabel(page_1)
        page_1_label.setText("Page 1")
        page_1_label.setStyleSheet('color: rgb(255, 255, 255); font: 700 48pt "Segoe UI";')
        page_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_1_layout.addWidget(page_1_label)
        desktop_application.addPage(btn_1, SideBarButton.Alignment.TOP, page_1)

        # Page 2
        btn_2 = SideBarButton(icon, "Button 2")
        page_2 = QWidget()
        page_2_layout = QGridLayout(page_2)
        page_2_label = QLabel(page_2)
        page_2_label.setText("Page 2")
        page_2_label.setStyleSheet('color: rgb(255, 255, 255); font: 700 48pt "Segoe UI";')
        page_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_2_layout.addWidget(page_2_label)
        desktop_application.addPage(btn_2, SideBarButton.Alignment.TOP, page_2)

        # Page 3
        btn_3 = SideBarButton(icon, "Button 3")
        page_3 = QWidget()
        page_3_layout = QGridLayout(page_3)
        page_3_label = QLabel(page_3)
        page_3_label.setText("Page 3")
        page_3_label.setStyleSheet('color: rgb(255, 255, 255); font: 700 48pt "Segoe UI";')
        page_3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_3_layout.addWidget(page_3_label)
        desktop_application.addPage(btn_3, SideBarButton.Alignment.BOTTOM, page_3)


def main() -> None:
    """Main function"""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Style sheet with the default color theme
    # with open(Path(__file__).parent.joinpath("style.qss"), "r", encoding="utf-8") as f:
    #    app.setStyleSheet(f.read())

    # Style sheet with custom color theme
    # with open(Path(__file__).parent.joinpath("style2.qss"), "r", encoding="utf-8") as style_sheet:
    #    app.setStyleSheet(style_sheet.read())

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
