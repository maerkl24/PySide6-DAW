from PySide6.QtWidgets import QHBoxLayout, QStackedWidget, QWidget

from PySide6_DAW.Widgets.SideBar import SideBar
from PySide6_DAW.Widgets.SideBarButton import SideBarButton


class ApplicationWidget(QWidget):
    """TODO"""

    def __init__(self, parent: QWidget) -> None:
        """Constructor

        Args:
            parent: TODO
            flags: TODO
        """
        super().__init__(parent)

        self.side_bar: SideBar
        self.stacked_widget: QStackedWidget

        self._setup_ui()

    def addPage(self, button: SideBarButton, button_alignment: SideBarButton.Alignment, page: QWidget) -> None:
        """TODO

        Args:
            button: TODO
            button_alignment: TODO
            page: TODO
        """
        button.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(page))
        self.side_bar.addButton(button, button_alignment)
        self.stacked_widget.addWidget(page)

    def _setup_ui(self):
        """TODO"""
        self.setStyleSheet("background-color: #2c313c")

        # Layout for this widget
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)

        # Menu bar
        self.side_bar = SideBar(self)
        self.side_bar.setFixedWidth(60)
        layout.addWidget(self.side_bar)

        # Stacked widget and its layout
        self.stacked_widget = QStackedWidget(self)
        self.stacked_widget.setStyleSheet("background-color: #FF00FF")
        layout.addWidget(self.stacked_widget)
