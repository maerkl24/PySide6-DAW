from typing import List

from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QFrame, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from PySide6_DAW.Widgets.SideBarButton import SideBarButton


# TODO: Set default button as first button. There must be always on button enabled!
class SideBar(QWidget):
    """Menu bar

    Menu bar for desktop applications.
    """

    def __init__(self, parent: QWidget) -> None:
        """Constructor

        Args:
            parent: TODO
        """
        super().__init__(parent)

        self._first_button = True

        self.setStyleSheet("background-color: #1b1e23; border: none; border-radius: 8px;")
        self._setupUi()

    def resizeEvent(self, event: QResizeEvent) -> None:  # pylint: disable=invalid-name; PySide6 API
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
        button.clicked.connect(self._buttonCallback)

        if alignment == SideBarButton.Alignment.TOP:
            self.top_frame_layout.addWidget(button)
        elif alignment == SideBarButton.Alignment.BOTTOM:
            self.bottom_frame_layout.addWidget(button)
        else:
            raise ValueError(
                "Invalid value for 'alignment'! Implemented values are 'SideBarButton.Alignment.TOP' and 'SideBarButton.Alignment.BOTTOM'."
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
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Background frame and its layout
        bg_frame = QFrame(self)
        bg_frame.setStyleSheet("background-color: #1b1e23; border: none; border-radius: 8px;")
        bg_layout = QVBoxLayout(bg_frame)
        bg_layout.setContentsMargins(0, 20, 0, 20)
        bg_layout.setSpacing(0)
        layout.addWidget(bg_frame)

        # Top side bar buttons frame and its layout
        top_frame = QFrame(bg_frame)
        self.top_frame_layout = QVBoxLayout(top_frame)
        self.top_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.top_frame_layout.setSpacing(0)
        # bg_layout.addWidget(top_frame, 0, Qt.AlignmentFlag.AlignTop)
        bg_layout.addWidget(top_frame)

        # Vertical spacer between top and bottom bar
        vertical_spacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        bg_layout.addItem(vertical_spacer)

        # Bottom side bar buttons frame and its layout
        bottom_frame = QFrame(bg_frame)
        self.bottom_frame_layout = QVBoxLayout(bottom_frame)
        self.bottom_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.bottom_frame_layout.setSpacing(0)
        # bg_layout.addWidget(bottom_frame, 0, Qt.AlignmentFlag.AlignBottom)
        bg_layout.addWidget(bottom_frame)
