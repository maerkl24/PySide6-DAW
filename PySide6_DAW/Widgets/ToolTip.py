from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QWidget


class ToolTip(QLabel):
    """Tool tip"""

    def __init__(self, parent: QWidget, text: str) -> None:
        """Constructor

        Args:
            parent: The parent widget.
            text: The text of the tool tip.
        """
        super().__init__(parent)

        self.setStyleSheet(
            (
                "background-color: #1b1e23;"
                "color: #808080;"
                "padding-left: 10px;"
                "padding-right: 10px;"
                "border-radius: 17px;"
                "border: 0px solid transparent;"
                "border-left: 3px solid #568af2;"
                "font: 800 9pt Segoe UI;"
            )
        )
        self.setMinimumHeight(34)
        self.setText(text)
        self.adjustSize()

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 80))
        self.setGraphicsEffect(shadow)
