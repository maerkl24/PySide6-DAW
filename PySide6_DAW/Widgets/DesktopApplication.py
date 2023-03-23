"""Application widget class implementation."""

from PySide6.QtCore import Property, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QHBoxLayout, QStackedWidget, QWidget

from PySide6_DAW.Widgets.SideBar import SideBar
from PySide6_DAW.Widgets.SideBarButton import SideBarButton


class DesktopApplication(QWidget):  # pylint: disable=duplicate-code; Property bg_color also appears in SideBar.
    """Desktop application widget"""

    def __init__(self, parent: QWidget) -> None:
        """Constructor

        Args:
            parent: TODO
            flags: TODO
        """
        super().__init__(parent)

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self._layout: QHBoxLayout
        self._side_bar: SideBar
        self._stacked_widget: QStackedWidget
        self._setupUi()

        self._bg_color: QColor
        self.bg_color = QColor("#282D32")  # type: ignore[assignment, method-assign]

    @Property(QColor)
    def bg_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the background color for the desktop application."""
        return self._bg_color

    @bg_color.setter  # type: ignore[no-redef]
    def bg_color(self, color: QColor) -> None:
        """Sets the background color for the desktop application."""
        self._bg_color = color
        self._bg_frame.setStyleSheet(
            f"""\
QFrame#desktop_application_bg_frame {{
    background-color: {self._bg_color.name()};
}}
"""
        )
        self.update()

    def addPage(self, button: SideBarButton, button_alignment: SideBarButton.Alignment, page: QWidget) -> None:
        """TODO

        Args:
            button: TODO
            button_alignment: TODO
            page: TODO
        """
        self._side_bar.addButton(button, button_alignment)
        self._stacked_widget.addWidget(page)
        button.clicked.connect(lambda: self._stacked_widget.setCurrentWidget(page))  # type: ignore[attr-defined]

    def _setupUi(self):
        """TODO"""
        # Layout for this widget
        self._layout = QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)
        self._bg_frame.setObjectName("desktop_application_bg_frame")
        self._bg_frame_layout = QHBoxLayout(self._bg_frame)
        self._bg_frame_layout.setContentsMargins(10, 10, 10, 10)
        self._bg_frame_layout.setSpacing(10)
        self._layout.addWidget(self._bg_frame)

        # Menu bar
        self._side_bar = SideBar(self)
        self._side_bar.setFixedWidth(60)
        self._bg_frame_layout.addWidget(self._side_bar)

        # Stacked widget and its layout
        self._stacked_widget = QStackedWidget(self)
        self._bg_frame_layout.addWidget(self._stacked_widget)
