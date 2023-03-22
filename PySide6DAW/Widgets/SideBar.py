"""Side bar class implementation."""

from typing import List, Optional

from PySide6.QtCore import Property
from PySide6.QtGui import QColor, QResizeEvent
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from PySide6DAW.Widgets.SideBarButton import SideBarButton


class SideBar(QWidget):  # pylint: disable=duplicate-code; Property bg_color also appears in DesktopApplication.
    """Side bar widget"""

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """Constructor

        Args:
            parent: The parent widget.
        """
        super().__init__(parent)
        self._first_button = True
        self._top_buttons: List[SideBarButton] = []
        self._bottom_buttons: List[SideBarButton] = []

        self._layout: QVBoxLayout
        self._bg_frame: QFrame
        self._bg_layout: QVBoxLayout
        self._top_frame: QFrame
        self._top_frame_layout: QVBoxLayout
        self._vertical_spacer: QSpacerItem
        self._bottom_frame: QFrame
        self._bottom_frame_layout: QVBoxLayout
        self._setupUi()

        self._bg_color: QColor
        self.bg_color = QColor("#191E23")  # type: ignore[assignment, method-assign]

    @Property(QColor)
    def bg_color(self) -> QColor:  # pylint: disable=method-hidden; Method is not hidden, as it is a property.
        """Returns the background color for the side bar."""
        return self._bg_color

    @bg_color.setter  # type: ignore[no-redef]
    def bg_color(self, color: QColor) -> None:
        """Sets the background color for the side bar."""
        self._bg_color = color
        self._bg_frame.setStyleSheet(
            f"""\
QFrame#side_bar_bg_frame {{
    background-color: {self._bg_color.name()};
    border: none;
    border-radius: 8px;
}}
"""
        )
        self.update()

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Resize event

        Args:
            event: The event.
        """
        super().resizeEvent(event)

        buttons: List[SideBarButton] = self.findChildren(SideBarButton)
        for button in buttons:
            button.setFixedSize(self.width(), self.width())

    def addButton(self, button: SideBarButton, alignment: SideBarButton.Alignment) -> None:
        """Add a new side bar button the the side bar.

        Args:
            button: TODO
            alignment: TODO

        Raises:
            ValueError: If the alignment value is invalid.
        """
        button.setParent(self)
        button.clicked.connect(self._buttonCallback)  # type: ignore[attr-defined]

        if alignment == SideBarButton.Alignment.TOP:
            self._top_buttons.append(button)
            self._top_frame_layout.addWidget(button)
        elif alignment == SideBarButton.Alignment.BOTTOM:
            self._bottom_buttons.append(button)
            self._bottom_frame_layout.addWidget(button)
        else:
            raise ValueError(
                "Invalid value for 'alignment'!"
                "Supported values are 'SideBarButton.Alignment.TOP' and 'SideBarButton.Alignment.BOTTOM'."
            )

        # Select the first button as default
        if self._first_button:
            button.click()
            self._first_button = False

    def _buttonCallback(self):
        """Menu button callback

        Select the checked side bar button and unselect all others.
        """
        buttons: List[SideBarButton] = self.findChildren(SideBarButton)
        for button in buttons:
            if button == self.sender():
                button.setChecked(True)
            else:
                button.setChecked(False)

    def _setupUi(self):
        """TODO"""
        # Layout for this widget
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        # Background frame and its layout
        self._bg_frame = QFrame(self)
        self._bg_frame.setObjectName("side_bar_bg_frame")
        self._bg_layout = QVBoxLayout(self._bg_frame)
        self._bg_layout.setContentsMargins(0, 20, 0, 20)
        self._bg_layout.setSpacing(0)
        self._layout.addWidget(self._bg_frame)

        # Top side bar buttons frame and its layout
        self._top_frame = QFrame(self._bg_frame)
        self._top_frame_layout = QVBoxLayout(self._top_frame)
        self._top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._top_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._top_frame)

        # Vertical spacer between top and bottom bar
        self._vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self._bg_layout.addItem(self._vertical_spacer)

        # Bottom side bar buttons frame and its layout
        self._bottom_frame = QFrame(self._bg_frame)
        self._bottom_frame_layout = QVBoxLayout(self._bottom_frame)
        self._bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        self._bottom_frame_layout.setSpacing(0)
        self._bg_layout.addWidget(self._bottom_frame)
