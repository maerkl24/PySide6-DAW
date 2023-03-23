"""Side bar button class implementation."""

from enum import Enum, auto
from typing import Optional

from PySide6.QtCore import Property, QRect, QSize, Qt
from PySide6.QtGui import QColor, QIcon, QPainter, QPaintEvent, QPixmap, QResizeEvent
from PySide6.QtWidgets import QPushButton, QWidget

from PySide6_DAW.Widgets.ToolTip import ToolTip


# pylint: disable=duplicate-code; Properties appear in several widgets.
class SideBarButton(QPushButton):
    """Side bar button widget"""

    class Alignment(Enum):
        """Side bar button alignment within side bar"""

        TOP = auto()
        BOTTOM = auto()

    def __init__(
        self, icon: QPixmap, tool_tip: Optional[str] = None, radius: int = 8, parent: Optional[QWidget] = None
    ) -> None:
        """Constructor

        Args:
            icon_path: Path to the icon for the button.
            tool_tip: Text for the tool tip.
            radius: Radius of shape.
            parent: The parent widget.
        """
        super().__init__(parent)

        # Set attributes from arguments
        self._icon = icon
        self._radius = radius
        self._tool_tip: Optional[ToolTip] = None
        if tool_tip:
            self._tool_tip = ToolTip(text=tool_tip)
            self._tool_tip.hide()

        # Define colors and set default values
        self._bg_color: QColor
        self._on_color: QColor
        self._hl_color: QColor
        self._icon_off_color: QColor
        self._icon_on_color: QColor
        self.bg_color = QColor("#191E23")  # type: ignore[assignment, method-assign]
        self.on_color = QColor("#282D32")  # type: ignore[assignment, method-assign]
        self.hl_color = QColor("#0066FF")  # type: ignore[assignment, method-assign]
        self.icon_off_color = QColor("#808080")  # type: ignore[assignment, method-assign]
        self.icon_on_color = QColor("#FFFFFF")  # type: ignore[assignment, method-assign]

        # Define areas for painting
        self.rect_background: QRect
        self.rect_icon: QRect
        self.rect_active_left: QRect
        self.rect_active_middle: QRect
        self.rect_active_right: QRect
        self.rect_active_right_corner_1: QRect
        self.rect_active_right_corner_2: QRect

        # Set QPushButton properties
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    @Property(QColor)
    def bg_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the background color for the button."""
        return self._bg_color

    @bg_color.setter  # type: ignore[no-redef]
    def bg_color(self, color: QColor) -> None:
        """Sets the background color for the button."""
        self._bg_color = color

    @Property(QColor)
    def on_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the background color for the button in active/hovered state."""
        return self._on_color

    @on_color.setter  # type: ignore[no-redef]
    def on_color(self, color: QColor) -> None:
        """Sets the background color for the button in active/hovered state."""
        self._on_color = color

    @Property(QColor)
    def hl_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the highlight color for the left edge of the button in active state."""
        return self._hl_color

    @hl_color.setter  # type: ignore[no-redef]
    def hl_color(self, color: QColor) -> None:
        """Sets the highlight color for the left edge of the button in active state.."""
        self._hl_color = color

    @Property(QColor)
    def icon_off_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the icon color for the button in inactive state."""
        return self._icon_off_color

    @icon_off_color.setter  # type: ignore[no-redef]
    def icon_off_color(self, color: QColor) -> None:
        """Sets the icon color for the button in inactive state."""
        self._icon_off_color = color

    @Property(QColor)
    def icon_on_color(self) -> QColor:  # pylint: disable=method-hidden; Method is a property and thus not hidden.
        """Returns the icon color for the button in active/hovered state."""
        return self._icon_on_color

    @icon_on_color.setter  # type: ignore[no-redef]
    def icon_on_color(self, color: QColor) -> None:
        """Returns the icon color for the button in active/hovered state."""
        self._icon_on_color = color

    def setParent(self, parent: QWidget) -> None:  # type: ignore[override]
        """Set parent widget.

        Args:
            parent: The parent widget.
        """
        super().setParent(parent)
        if self._tool_tip:
            self._tool_tip.setParent(self.window())

    def minimumSizeHint(self) -> QSize:
        """Return default size"""
        return QSize(40, 40)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """Resize event

        Args:
            event: The event.
        """
        super().resizeEvent(event)

        radius = self._radius
        width = self.width()
        height = self.height()
        self.rect_background = QRect(0, 0, width, height)
        # self.rect_icon = QRect(1.5*radius, 1.5*radius, width-3*radius, height-3*radius)
        self.rect_icon = QRect(width // 4, height // 4, width // 2, height // 2)
        self.rect_active_left = QRect(radius // 2, radius, 2 * radius, height - 2 * radius)
        self.rect_active_middle = QRect(radius, radius, width - 2 * radius, height - 2 * radius)
        self.rect_active_right = QRect(width - 2 * radius, 0, 2 * radius, height)
        self.rect_active_right_corner_1 = QRect(width - 3 * radius, -radius, 3 * radius, 2 * radius)
        self.rect_active_right_corner_2 = QRect(width - 3 * radius, height - radius, 3 * radius, 2 * radius)

    def paintEvent(self, event: QPaintEvent) -> None:
        """Paint event

        Args:
            event: The event.
        """
        super().paintEvent(event)

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)

        # Draw background
        painter.setBrush(self._bg_color)
        painter.drawRect(self.rect_background)

        if self.isChecked():
            # Draw left highlight area
            painter.setBrush(self._hl_color)
            painter.drawRoundedRect(self.rect_active_left, self._radius, self._radius)
            # Draw middle and right active area
            painter.setBrush(self._on_color)
            painter.drawRoundedRect(self.rect_active_middle, self._radius, self._radius)
            painter.setBrush(self._on_color)
            painter.drawRect(self.rect_active_right)
            # Draw right corners area (background)
            painter.setBrush(self._bg_color)
            painter.drawRoundedRect(self.rect_active_right_corner_1, self._radius, self._radius)
            painter.drawRoundedRect(self.rect_active_right_corner_2, self._radius, self._radius)
            # Draw icon
            self._drawIcon(painter, self.rect_icon, self._icon_on_color)
            # Hide tool tip
            if self._tool_tip:
                self._tool_tip.hide()
        elif self.underMouse():
            # Draw middle active area
            painter.setBrush(self._on_color)
            painter.drawRoundedRect(self.rect_active_middle, self._radius, self._radius)
            # Draw icon
            self._drawIcon(painter, self.rect_icon, self._icon_on_color)
            # Show tool tip
            if self._tool_tip:
                button_pos = self.window().mapFromGlobal(self.mapToGlobal(self.rect().topLeft()))
                tool_tip_x = button_pos.x() + self.width() + 5
                tool_tip_y = button_pos.y() + self.height() // 2 - self._tool_tip.height() // 2
                self._tool_tip.move(tool_tip_x, tool_tip_y)
                self._tool_tip.show()
        else:
            # Draw icon
            self._drawIcon(painter, self.rect_icon, self._icon_off_color)
            # Hide tool tip
            if self._tool_tip:
                self._tool_tip.hide()

        painter.end()

    def _drawIcon(self, painter: QPainter, rect: QRect, color: QColor) -> None:
        """Draw the side bar button icon

        Args:
            painter: The painter to paint the icon with.
            rect: The size of the icon.
            color: The color of the icon.
        """
        pixmap = QPixmap(self._icon)
        pixmap_painter = QPainter(pixmap)
        pixmap_painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        pixmap_painter.fillRect(pixmap.rect(), color)
        pixmap_painter.end()
        icon = QIcon(pixmap)
        icon.paint(painter, rect)
