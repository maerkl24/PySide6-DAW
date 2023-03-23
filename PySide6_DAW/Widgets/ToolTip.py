"""Tool tip class implementation"""

from typing import Optional

from PySide6.QtCore import Property, Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGridLayout, QLabel, QWidget

#: Template for label stylesheet
_LABEL_STYLESHEET = """\
QLabel {{
    color: {text_color};
    background-color: {bg_color};
    padding-left: 10px;
    padding-right: 10px;
    border-radius: 15px;
    border: none;
    border-left: 3px solid {hl_color};
    font: 800 9pt Segoe UI;
}}
"""


# pylint: disable=duplicate-code; Properties appear in several widgets.
class ToolTip(QWidget):
    """Tool tip widget"""

    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        """Constructor

        Args:
            text: The text of the tool tip.
            parent: The parent widget.
        """
        super().__init__(parent)

        self._layout = QGridLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._label = QLabel(self)
        self._layout.addWidget(self._label)

        # Define colors and set default values
        self._bg_color = QColor("#191E23")
        self._hl_color = QColor("#0066FF")
        self._text_color = QColor("#A0A0A0")
        self._setStyle()

        self._label.setMinimumHeight(30)
        self._label.setText(text)
        self._label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._label.adjustSize()
        self.setFixedSize(self._label.size())

    def _setStyle(self) -> None:
        """Apply stylesheet."""
        self._label.setStyleSheet(
            _LABEL_STYLESHEET.format(
                text_color=self._text_color.name(), bg_color=self._bg_color.name(), hl_color=self._hl_color.name()
            )
        )

    @Property(QColor)
    def bg_color(self) -> QColor:  # pylint: disable=method-hidden; Method is not hidden, as it is a property.
        """Returns the background color for the side bar."""
        return self._bg_color

    @bg_color.setter  # type: ignore[no-redef]
    def bg_color(self, color: QColor) -> None:
        """Sets the background color for the side bar."""
        self._bg_color = color
        self._setStyle()

    @Property(QColor)
    def hl_color(self) -> QColor:  # pylint: disable=method-hidden; Method is not hidden, as it is a property.
        """Returns the background color for the side bar."""
        return self._hl_color

    @hl_color.setter  # type: ignore[no-redef]
    def hl_color(self, color: QColor) -> None:
        """Sets the background color for the side bar."""
        self._hl_color = color
        self._setStyle()

    @Property(QColor)
    def text_color(self) -> QColor:  # pylint: disable=method-hidden; Method is not hidden, as it is a property.
        """Returns the background color for the side bar."""
        return self._text_color

    @text_color.setter  # type: ignore[no-redef]
    def text_color(self, color: QColor) -> None:
        """Sets the background color for the side bar."""
        self._text_color = color
        self._setStyle()
