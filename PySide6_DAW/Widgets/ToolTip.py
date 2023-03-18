"""Tool tip class implementation"""

from typing import Optional

from PySide6.QtWidgets import QLabel, QWidget


class ToolTip(QLabel):
    """Tool tip widget"""

    def __init__(self, text: str, parent: Optional[QWidget] = None) -> None:
        """Constructor

        Args:
            text: The text of the tool tip.
            parent: The parent widget.
        """
        super().__init__(parent)

        self.setColors()
        self.setMinimumHeight(30)
        self.setText(text)
        self.adjustSize()

    def setColors(self, color: str = "#A0A0A0", bg_color: str = "#191E23", hl_color: str = "#0066FF") -> None:
        """Set the colors for the tool tip

        Args:
            color: The text color.
            bg_color: The background color.
            hl_color: The highlight color.
        """
        self.setStyleSheet(
            (
                f"color: {color};"
                f"background-color: {bg_color};"
                "padding-left: 10px;"
                "padding-right: 10px;"
                "border-radius: 15px;"
                f"border-right: none;"
                f"border-left: 3px solid {hl_color};"
                "font: 800 9pt Segoe UI;"
            )
        )
