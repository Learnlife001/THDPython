import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont, QPen
from PyQt5.QtCore import Qt, QRect, QPoint
from predicate_parser import PredicateParser
from predicate_evaluator import PredicateEvaluator
from predicate_registry import predicate_registry
import math
import json

"""
Tarski's World - A First-Order Logic Visualizer
===============================================

Author: [Your Name]
Date: [Current Date]
Version: 1.0

Description:
    A PyQt5-based application for visualizing and evaluating first-order logic
    sentences in a 2D grid world with blocks of different shapes, sizes, and colors.
    
    Features:
    - Visual block placement and manipulation
    - First-order logic sentence evaluation
    - Support for quantifiers (∀, ∃), logical operators, and geometric predicates
    - Real-time evaluation with visual feedback

License: MIT
"""

class Block:
    def __init__(self, x, y, size='medium', shape='cube', name=None):
        self.x = x
        self.y = y
        self.size = size
        self.shape = shape
        self.name = name

class TarskiWorld(QWidget):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.grid_size = 8
        self.selected_block = None
        self.dragging = False
        self.drag_block = None
        self.drag_start_pos = None
        self.initUI()

    def initUI(self):
        self.setMinimumSize(600, 450)  # Increased size by 50% (400*1.5=600, 300*1.5=450)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()  # Set focus to this widget


    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawCheckerboard(painter)
        self.drawBlocks(painter)


    def drawCheckerboard(self, painter):
        cell_size = min(self.width(), self.height()) // self.grid_size
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i + j) % 2 == 0:
                    painter.fillRect(i * cell_size, j * cell_size, cell_size, cell_size, Qt.lightGray)
                else:
                    painter.fillRect(i * cell_size, j * cell_size, cell_size, cell_size, Qt.white)


    def drawBlocks(self, painter):
        cell_size = min(self.width(), self.height()) // self.grid_size
        for block in self.blocks:
            x = block.x * cell_size
            y = block.y * cell_size
            
            if block.size == 'small':
                size = cell_size // 2
            elif block.size == 'medium':
                size = cell_size * 3 // 4
            else:
                size = cell_size

            if block == self.selected_block:
                painter.setPen(QPen(Qt.black, 2))
                painter.drawRect(x, y, cell_size, cell_size)
                painter.setPen(Qt.black)

            center_x = x + cell_size // 2
            center_y = y + cell_size // 2

            if block.shape == 'cube':
                painter.fillRect(center_x - size // 2, center_y - size // 2, size, size, Qt.blue)
            elif block.shape == 'tetrahedron':
                painter.setBrush(Qt.red)
                painter.drawPolygon([
                    QPoint(center_x, center_y - size // 2),
                    QPoint(center_x - size // 2, center_y + size // 2),
                    QPoint(center_x + size // 2, center_y + size // 2)
                ])
                painter.setBrush(Qt.NoBrush)
            else:  # dodecahedron
                painter.setBrush(Qt.yellow)
                # Draw a pentagon (dodecahedron in 2D)
                points = []
                for i in range(5):
                    angle = i * 2 * math.pi / 5 - math.pi / 2  # Start from top
                    x = center_x + int(size // 2 * math.cos(angle))
                    y = center_y + int(size // 2 * math.sin(angle))
                    points.append(QPoint(x, y))
                painter.drawPolygon(points)
                painter.setBrush(Qt.NoBrush)

            if block.name:
                painter.setFont(QFont('Arial', cell_size // 3))
                text_rect = QRect(x, y, cell_size, cell_size)
                painter.fillRect(text_rect, QColor(255, 255, 255, 180))
                painter.drawText(text_rect, Qt.AlignCenter, block.name)


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            cell_size = min(self.width(), self.height()) // self.grid_size
            x = event.x() // cell_size
            y = event.y() // cell_size

            clicked_block = None
            for block in self.blocks:
                if block.x == x and block.y == y:
                    clicked_block = block
                    break

            if clicked_block:
                self.selected_block = clicked_block
                # Start drag operation
                self.dragging = True
                self.drag_block = clicked_block
                self.drag_start_pos = (x, y)
            else:
                new_block = Block(x, y)
                self.blocks.append(new_block)
                self.selected_block = new_block

            self.update()
            self.setFocus()  # Ensure focus after mouse click

    def keyPressEvent(self, event):
        if self.hasFocus():
            if self.selected_block:
                if event.key() == Qt.Key_Delete:
                    self.blocks.remove(self.selected_block)
                    self.selected_block = None
                elif event.key() == Qt.Key_Left:
                    self.selected_block.x = max(0, self.selected_block.x - 1)
                elif event.key() == Qt.Key_Right:
                    self.selected_block.x = min(self.grid_size - 1, self.selected_block.x + 1)
                elif event.key() == Qt.Key_Up:
                    self.selected_block.y = max(0, self.selected_block.y - 1)
                elif event.key() == Qt.Key_Down:
                    self.selected_block.y = min(self.grid_size - 1, self.selected_block.y + 1)
                elif event.key() >= Qt.Key_A and event.key() <= Qt.Key_F:
                    self.selected_block.name = chr(event.key()).lower()
            self.update()
            if self.selected_block:
                print(f"Selected block: shape={self.selected_block.shape}, name={self.selected_block.name}")  # Debug print
            else:
                print("No block selected")  # Debug print
        else:
            super().keyPressEvent(event)

    def mouseMoveEvent(self, event):
        if self.dragging and self.drag_block:
            cell_size = min(self.width(), self.height()) // self.grid_size
            x = event.x() // cell_size
            y = event.y() // cell_size
            
            # Constrain to grid boundaries
            x = max(0, min(self.grid_size - 1, x))
            y = max(0, min(self.grid_size - 1, y))
            
            # Check if the target position is occupied by another block
            position_occupied = False
            for block in self.blocks:
                if block != self.drag_block and block.x == x and block.y == y:
                    position_occupied = True
                    break
            
            # Only move if the position is not occupied
            if not position_occupied:
                self.drag_block.x = x
                self.drag_block.y = y
                self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.dragging:
            self.dragging = False
            self.drag_block = None
            self.drag_start_pos = None

    def change_shape(self, shape):
        if self.selected_block:
            self.selected_block.shape = shape
            print(f"Changed shape to {shape}")  # Debug print
            self.update()

    def change_size(self, size):
        if self.selected_block:
            self.selected_block.size = size
            self.update()

    def get_block_by_name(self, name):
        # First check for named blocks
        for block in self.blocks:
            if block.name == name:
                return block
        
        # Check for block identifiers (for unnamed blocks)
        if name.startswith('block_'):
            try:
                index = int(name.split('_')[1])
                if 0 <= index < len(self.blocks):
                    return self.blocks[index]
            except (ValueError, IndexError):
                pass
        
        return None

    def is_cube(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.shape == 'cube'

    def is_tet(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.shape == 'tetrahedron'

    def is_dodec(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.shape == 'dodecahedron'

    def is_left_of(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.x < block2.x

    def is_right_of(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.x > block2.x

    def is_front_of(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.y > block2.y

    def is_back_of(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.y < block2.y

    def is_small(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.size == 'small'

    def is_medium(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.size == 'medium'

    def is_large(self, block_name):
        block = self.get_block_by_name(block_name)
        return block is not None and block.size == 'large'

    def is_same_col(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.x == block2.x

    def is_same_row(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.y == block2.y

    def is_between(self, block1_name, block2_name, block3_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        block3 = self.get_block_by_name(block3_name)
        if block1 is None or block2 is None or block3 is None:
            return False
        
        # Check if block1 is between block2 and block3 in the same row
        if block1.y == block2.y == block3.y:
            return (block2.x < block1.x < block3.x) or (block3.x < block1.x < block2.x)
        
        # Check if block1 is between block2 and block3 in the same column
        if block1.x == block2.x == block3.x:
            return (block2.y < block1.y < block3.y) or (block3.y < block1.y < block2.y)
        
        return False

    def is_adjoins(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        if block1 is None or block2 is None:
            return False
        
        # Check if blocks are adjacent horizontally or vertically
        x_diff = abs(block1.x - block2.x)
        y_diff = abs(block1.y - block2.y)
        return (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)

    def is_smaller(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        if block1 is None or block2 is None:
            return False
        
        size_order = {'small': 1, 'medium': 2, 'large': 3}
        return size_order.get(block1.size, 0) < size_order.get(block2.size, 0)

    def is_same_size(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        return block1 is not None and block2 is not None and block1.size == block2.size

    def is_larger(self, block1_name, block2_name):
        block1 = self.get_block_by_name(block1_name)
        block2 = self.get_block_by_name(block2_name)
        if block1 is None or block2 is None:
            return False
        
        size_order = {'small': 1, 'medium': 2, 'large': 3}
        return size_order.get(block1.size, 0) > size_order.get(block2.size, 0)

    def save_world(self, filename, sentences=None):
        """Save the current world state to a JSON file"""
        world_data = {
            "version": "1.0",
            "grid_size": self.grid_size,
            "blocks": []
        }
        
        for block in self.blocks:
            block_data = {
                "x": block.x,
                "y": block.y,
                "size": block.size,
                "shape": block.shape,
                "name": block.name
            }
            world_data["blocks"].append(block_data)
        
        # Add sentences if provided
        if sentences:
            world_data["sentences"] = sentences
        
        try:
            with open(filename, 'w') as f:
                json.dump(world_data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving world: {e}")
            return False

    def load_world(self, filename):
        """Load a world state from a JSON file"""
        try:
            with open(filename, 'r') as f:
                world_data = json.load(f)
            
            # Clear current world
            self.blocks.clear()
            self.selected_block = None
            
            # Load blocks
            for block_data in world_data.get("blocks", []):
                block = Block(
                    x=block_data["x"],
                    y=block_data["y"],
                    size=block_data["size"],
                    shape=block_data["shape"],
                    name=block_data["name"]
                )
                self.blocks.append(block)
            
            # Update grid size if specified
            if "grid_size" in world_data:
                self.grid_size = world_data["grid_size"]
            
            self.update()
            
            # Return sentences if they exist
            return world_data.get("sentences", None)
        except Exception as e:
            print(f"Error loading world: {e}")
            return None

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.edit_fields = []  # List to store all edit fields
        self.result_labels = []  # List to store all result labels
        self.max_fields = 8
        self.last_focused_field = None  # Track the last focused field
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Tarski's World")
        self.setGeometry(100, 100, 1200, 500)  # Reduced height for more compact layout

        # Set Inter font for the entire application
        app = QApplication.instance()
        if app:
            font = app.font()
            font.setFamily("Inter")
            font.setPointSize(9)
            app.setFont(font)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        main_layout.setSpacing(15)  # Reduced spacing between panels
        central_widget.setLayout(main_layout)

        # Left Panel: World Builder (reduced size to accommodate larger checkerboard)
        world_panel = QWidget()
        world_panel.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 6px;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
        """)
        world_layout = QVBoxLayout()
        world_layout.setSpacing(4)  # Reduced spacing between elements
        world_panel.setLayout(world_layout)

        # World Builder Header
        world_header = QLabel("🌍 World Builder")
        world_header.setStyleSheet("""
            QLabel {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                font-size: 14px;
                font-weight: bold;
                color: #495057;
                padding: 6px;
                background-color: #e9ecef;
                border-radius: 6px;
                margin-bottom: 6px;
            }
        """)
        world_layout.addWidget(world_header)

        # Controls section with better styling
        controls_widget = QWidget()
        controls_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 4px;
                margin: 2px;
            }
        """)
        controls_layout = QHBoxLayout()
        controls_layout.setSpacing(4)  # Reduced spacing
        controls_widget.setLayout(controls_layout)

        # Shapes section
        shapes_widget = QWidget()
        shapes_widget.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 3px;
            }
            QLabel {
                font-weight: bold;
                color: #495057;
                font-size: 10px;
            }
        """)
        shapes_layout = QVBoxLayout()
        shapes_layout.setSpacing(2)  # Reduced spacing
        shapes_widget.setLayout(shapes_layout)
        
        shape_label = QLabel("Shapes:")
        shape_label.setStyleSheet("font-size: 10px; font-weight: bold; color: #495057;")
        shapes_layout.addWidget(shape_label)

        shape_buttons = [
            ("Cube", "cube"),
            ("Tet", "tetrahedron"),
            ("Dodec", "dodecahedron")
        ]

        for button_text, shape in shape_buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("""
                QPushButton {
                    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 3px;
                    border-radius: 3px;
                    font-weight: bold;
                    font-size: 9px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
            button.clicked.connect(lambda checked, s=shape: self.tarski_world.change_shape(s))
            shapes_layout.addWidget(button)

        controls_layout.addWidget(shapes_widget)

        # Sizes section
        sizes_widget = QWidget()
        sizes_widget.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 4px;
                padding: 3px;
            }
            QLabel {
                font-weight: bold;
                color: #495057;
                font-size: 10px;
            }
        """)
        sizes_layout = QVBoxLayout()
        sizes_layout.setSpacing(2)  # Reduced spacing
        sizes_widget.setLayout(sizes_layout)
        
        size_label = QLabel("Sizes:")
        size_label.setStyleSheet("font-size: 10px; font-weight: bold; color: #495057;")
        sizes_layout.addWidget(size_label)

        size_buttons = [
            ("Small", "small"),
            ("Medium", "medium"),
            ("Large", "large")
        ]

        for button_text, size in size_buttons:
            button = QPushButton(button_text)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #28a745;
                    color: white;
                    border: none;
                    padding: 3px;
                    border-radius: 3px;
                    font-weight: bold;
                    font-size: 9px;
                }
                QPushButton:hover {
                    background-color: #1e7e34;
                }
            """)
            button.clicked.connect(lambda checked, s=size: self.tarski_world.change_size(s))
            sizes_layout.addWidget(button)

        controls_layout.addWidget(sizes_widget)

        world_layout.addWidget(controls_widget)

        # Add the TarskiWorld widget
        self.tarski_world = TarskiWorld()
        world_layout.addWidget(self.tarski_world)

        # File operations section
        file_widget = QWidget()
        file_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 4px;
                margin: 2px;
            }
        """)
        file_layout = QVBoxLayout()
        file_layout.setSpacing(3)  # Reduced spacing
        file_widget.setLayout(file_layout)

        file_header = QLabel("💾 File Operations")
        file_header.setStyleSheet("font-weight: bold; color: #495057; margin-bottom: 3px; font-size: 11px;")
        file_layout.addWidget(file_header)

        # World save/load buttons
        world_buttons_layout = QHBoxLayout()
        world_buttons_layout.setSpacing(3)  # Reduced spacing
        world_save_button = QPushButton("Save World")
        world_save_button.setStyleSheet("""
            QPushButton {
                background-color: #17a2b8;
                color: white;
                border: none;
                padding: 5px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #138496;
            }
        """)
        world_save_button.clicked.connect(self.save_world_only)
        world_buttons_layout.addWidget(world_save_button)

        world_load_button = QPushButton("Load World")
        world_load_button.setStyleSheet("""
            QPushButton {
                background-color: #6f42c1;
                color: white;
                border: none;
                padding: 5px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #5a32a3;
            }
        """)
        world_load_button.clicked.connect(self.load_world_only)
        world_buttons_layout.addWidget(world_load_button)

        file_layout.addLayout(world_buttons_layout)

        # Sentence save/load buttons
        sentence_buttons_layout = QHBoxLayout()
        sentence_buttons_layout.setSpacing(3)  # Reduced spacing
        sentence_save_button = QPushButton("Save Sentences")
        sentence_save_button.setStyleSheet("""
            QPushButton {
                background-color: #fd7e14;
                color: white;
                border: none;
                padding: 5px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #e8690b;
            }
        """)
        sentence_save_button.clicked.connect(self.save_sentences_only)
        sentence_buttons_layout.addWidget(sentence_save_button)

        sentence_load_button = QPushButton("Load Sentences")
        sentence_load_button.setStyleSheet("""
            QPushButton {
                background-color: #e83e8c;
                color: white;
                border: none;
                padding: 5px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #d63384;
            }
        """)
        sentence_load_button.clicked.connect(self.load_sentences_only)
        sentence_buttons_layout.addWidget(sentence_load_button)

        file_layout.addLayout(sentence_buttons_layout)

        # Clear button
        clear_button = QPushButton("🗑️ Clear World")
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border: none;
                padding: 5px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 9px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
        """)
        clear_button.clicked.connect(self.clearBoard)
        file_layout.addWidget(clear_button)

        world_layout.addWidget(file_widget)

        # Add world panel to main layout (reduced width to accommodate larger checkerboard)
        main_layout.addWidget(world_panel, 1)

        # Right Panel: Logic Palette (1/3 of width)
        logic_panel = QWidget()
        logic_panel.setStyleSheet("""
            QWidget {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                padding: 8px;
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            }
        """)
        self.right_layout = QVBoxLayout()
        logic_panel.setLayout(self.right_layout)

        # Logic Palette Header
        logic_header = QLabel("🧠 Logic Palette")
        logic_header.setStyleSheet("""
            QLabel {
                font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                font-size: 16px;
                font-weight: bold;
                color: #495057;
                padding: 8px;
                background-color: #e9ecef;
                border-radius: 6px;
                margin-bottom: 8px;
            }
        """)
        self.right_layout.addWidget(logic_header)

        # Naming instructions
        naming_label = QLabel("📝 Naming: Select a block and press A-F")
        naming_label.setStyleSheet("""
            QLabel {
                background-color: #fff3cd;
                border: 1px solid #ffeaa7;
                border-radius: 4px;
                padding: 6px;
                color: #856404;
                font-weight: bold;
                font-size: 11px;
            }
        """)
        self.right_layout.addWidget(naming_label)

        # Predicates section
        predicates_widget = QWidget()
        predicates_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 6px;
                margin: 3px;
            }
        """)
        predicates_layout = QVBoxLayout()
        predicates_widget.setLayout(predicates_layout)

        predicate_buttons_label = QLabel("🔍 Predicates:")
        predicate_buttons_label.setStyleSheet("font-weight: bold; color: #495057; margin-bottom: 5px;")
        predicates_layout.addWidget(predicate_buttons_label)

        # Create predicate buttons in a grid layout
        predicate_grid = QGridLayout()
        predicates_layout.addLayout(predicate_grid)

        # Get predicates from the centralized registry
        predicates = predicate_registry.get_predicates()

        # Create buttons in a 2-column grid (better for narrow panel)
        for i, (predicate, arity) in enumerate(predicates.items()):
            row = i // 2
            col = i % 2
            button = QPushButton(predicate)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #6c757d;
                    color: white;
                    border: none;
                    padding: 6px;
                    border-radius: 4px;
                    font-weight: bold;
                    font-size: 11px;
                }
                QPushButton:hover {
                    background-color: #545b62;
                }
            """)
            button.clicked.connect(lambda checked, p=predicate: self.insert_predicate(p))
            predicate_grid.addWidget(button, row, col)

        self.right_layout.addWidget(predicates_widget)

        # Logical operators section
        operators_widget = QWidget()
        operators_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 6px;
                margin: 3px;
            }
        """)
        operators_layout = QVBoxLayout()
        operators_widget.setLayout(operators_layout)

        logical_operators_label = QLabel("⚡ Logical Operators:")
        logical_operators_label.setStyleSheet("font-weight: bold; color: #495057; margin-bottom: 5px;")
        operators_layout.addWidget(logical_operators_label)

        logical_grid = QGridLayout()
        operators_layout.addLayout(logical_grid)

        logical_operators = ['∧', '∨', '¬', '→', '↔', '∀', '∃']
        operator_map = {'∧': '&', '∨': '|', '¬': '!', '→': '->', '↔': '<->', '∀': '@', '∃': '€'}
        for i, operator in enumerate(logical_operators):
            row = i // 3
            col = i % 3
            button = QPushButton(operator)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #ffc107;
                    color: #212529;
                    border: none;
                    padding: 8px;
                    border-radius: 4px;
                    font-weight: bold;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #e0a800;
                }
            """)
            button.clicked.connect(lambda checked, op=operator_map[operator]: self.insert_predicate(op))
            logical_grid.addWidget(button, row, col)

        self.right_layout.addWidget(operators_widget)

        # Sentence evaluation section
        evaluation_widget = QWidget()
        evaluation_widget.setStyleSheet("""
            QWidget {
                background-color: #ffffff;
                border: 1px solid #ced4da;
                border-radius: 6px;
                padding: 6px;
                margin: 3px;
            }
        """)
        evaluation_layout = QVBoxLayout()
        evaluation_widget.setLayout(evaluation_layout)

        predicate_label = QLabel("📝 Enter Sentences:")
        predicate_label.setStyleSheet("font-weight: bold; color: #495057; margin-bottom: 5px;")
        evaluation_layout.addWidget(predicate_label)

        # Container for edit fields
        self.edit_fields_container = QVBoxLayout()
        evaluation_layout.addLayout(self.edit_fields_container)

        # Create evaluate button first (but don't add to layout yet)
        evaluate_button = QPushButton("🔍 Evaluate All")
        evaluate_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 4px;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1e7e34;
            }
        """)
        evaluate_button.setFocusPolicy(Qt.StrongFocus)
        evaluate_button.clicked.connect(self.evaluate_all_predicates)
        self.evaluate_button = evaluate_button  # Store reference

        # Add initial edit fields
        self.add_edit_field()
        self.add_edit_field()

        # Add button to add more fields
        add_field_button = QPushButton("+")
        add_field_button.setFixedSize(35, 35)
        add_field_button.setToolTip("Add sentence field")
        add_field_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;
                border: black;
                border-radius: 15px;
                font-weight: bold;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: grey;
            }
        """)
        add_field_button.clicked.connect(self.add_edit_field)
        evaluation_layout.addWidget(add_field_button)

        # Add evaluate button to layout
        evaluation_layout.addWidget(evaluate_button)

        self.right_layout.addWidget(evaluation_widget)

        # Add logic panel to main layout (increased width since world panel is smaller)
        main_layout.addWidget(logic_panel, 2)

        # Set initial tab order
        self.update_tab_order()

        # Initialize parser and evaluator
        self.parser = PredicateParser()
        self.evaluator = PredicateEvaluator(self.tarski_world)

        # Set initial focus to the first input field
        if self.edit_fields:
            self.edit_fields[0].setFocus()


    def add_edit_field(self):
        """Add a new edit field with result label"""
        if len(self.edit_fields) >= self.max_fields:
            return
        
        # Create horizontal layout for this field
        row_layout = QHBoxLayout()
        self.edit_fields_container.addLayout(row_layout)
        
        # Create result label
        result_label = QLabel("X")
        result_label.setFixedSize(20, 20)
        result_label.setAlignment(Qt.AlignCenter)
        result_label.setStyleSheet("background-color: grey; color: white; border: 1px solid black; font-weight: bold;")
        row_layout.addWidget(result_label)
        self.result_labels.append(result_label)
        
        # Create edit field
        edit_field = QLineEdit()
        edit_field.setFocusPolicy(Qt.StrongFocus)
        edit_field.textChanged.connect(lambda: self.convert_logical_symbols_generic(edit_field))
        edit_field.focusInEvent = lambda event: self.on_field_focus(edit_field, event)
        row_layout.addWidget(edit_field)
        self.edit_fields.append(edit_field)
        
        # Create clear button for this field
        clear_button = QPushButton("X")
        clear_button.setFixedSize(30, 30)
        clear_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: black;                
                font-weight: bold;
                font-size: 10px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: grey;
            }
        """)
        clear_button.clicked.connect(lambda: self.clear_edit_field_content(edit_field, result_label))
        row_layout.addWidget(clear_button)
        
        # Update tab order
        self.update_tab_order()
        
        # Enable/disable add button based on field count
        self.update_add_button_state()

    def update_tab_order(self):
        """Update tab order for all edit fields"""
        # Clear existing tab order
        for i in range(len(self.edit_fields) - 1):
            self.setTabOrder(self.edit_fields[i], self.edit_fields[i + 1])
        
        # Set tab order from last field to evaluate button to tarski_world
        if self.edit_fields and hasattr(self, 'evaluate_button'):
            self.setTabOrder(self.edit_fields[-1], self.evaluate_button)
            self.setTabOrder(self.evaluate_button, self.tarski_world)

    def update_add_button_state(self):
        """Enable/disable add button based on field count"""
        # Find the add button (it's the last button in the right layout)
        for i in reversed(range(self.right_layout.count())):
            item = self.right_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                if isinstance(widget, QPushButton) and widget.text() == "+":
                    widget.setEnabled(len(self.edit_fields) < self.max_fields)
                    break

    def convert_logical_symbols_generic(self, edit_field):
        """Generic logical symbol converter for any edit field"""
        text = edit_field.text()
        if '|' in text or '&' in text or '!' in text or '->' in text or '<->' in text or '@' in text or '€' in text:
            # Temporarily disconnect the signal to prevent recursion
            edit_field.textChanged.disconnect()
            converted_text = text.replace('<->', '↔').replace('->', '→').replace('|', '∨').replace('&', '∧').replace('!', '¬').replace('@', '∀').replace('€', '∃')
            edit_field.setText(converted_text)
            # Reconnect the signal
            edit_field.textChanged.connect(lambda: self.convert_logical_symbols_generic(edit_field))

    def clear_edit_fields(self):
        """Clear all edit fields and result labels"""
        # Clear the container layout
        while self.edit_fields_container.count():
            child = self.edit_fields_container.takeAt(0)
            if child and child.widget():
                child.widget().deleteLater()
            elif child and child.layout():
                while child.layout().count():
                    subchild = child.layout().takeAt(0)
                    if subchild and subchild.widget():
                        subchild.widget().deleteLater()
        
        # Clear the lists
        self.edit_fields.clear()
        self.result_labels.clear()

    def on_field_focus(self, field, event):
        """Track which field has focus"""
        self.last_focused_field = field
        # Call the original focusInEvent if it exists
        if hasattr(field, '_original_focusInEvent'):
            field._original_focusInEvent(event)

    def clear_edit_field_content(self, edit_field, result_label):
        """Clear the content of a specific edit field and reset its result label"""
        edit_field.clear()
        self.update_result_label(result_label, None, is_error=True)



    def clearBoard(self):
        self.tarski_world.blocks.clear()
        self.tarski_world.selected_block = None
        self.tarski_world.update()

    def update_result_label(self, label, result, is_error=False):
        """Update a result label with the appropriate symbol and color"""
        if is_error:
            label.setText("X")
            label.setStyleSheet("background-color: grey; color: white; border: 1px solid black; font-weight: bold;")
        elif result is True:
            label.setText("T")
            label.setStyleSheet("background-color: green; color: white; border: 1px solid black; font-weight: bold;")
        elif result is False:
            label.setText("F")
            label.setStyleSheet("background-color: red; color: white; border: 1px solid black; font-weight: bold;")
        else:
            label.setText("X")
            label.setStyleSheet("background-color: grey; color: white; border: 1px solid black; font-weight: bold;")

    def evaluate_all_predicates(self):
        """Evaluate all edit fields"""
        for i, (edit_field, result_label) in enumerate(zip(self.edit_fields, self.result_labels)):
            input_string = edit_field.text().strip()
            if not input_string:
                self.update_result_label(result_label, None, is_error=True)
            else:
                try:
                    parsed_predicate = self.parser.parse(input_string)
                    result = self.evaluator.evaluate(parsed_predicate)
                    self.update_result_label(result_label, result)
                except ValueError as e:
                    self.update_result_label(result_label, None, is_error=True)

    def insert_predicate(self, predicate):
        """Insert predicate name into the focused text field at cursor position"""
        # Use the last focused field if available, otherwise find current focus
        focused_field = self.last_focused_field
        
        # If no last focused field, find which field currently has focus
        if not focused_field:
            for field in self.edit_fields:
                if field.hasFocus():
                    focused_field = field
                    break
        
        # If still no focused field, use the first one
        if not focused_field and self.edit_fields:
            focused_field = self.edit_fields[0]
        
        if focused_field:
            # Store current cursor position
            cursor_pos = focused_field.cursorPosition()
            current_text = focused_field.text()
            
            # Check if this is a predicate (not a logical operator)
            predicates = predicate_registry.get_predicates()
            if predicate in predicates:
                # Insert predicate with parentheses and position cursor between them
                predicate_with_parens = predicate + "()"
                new_text = current_text[:cursor_pos] + predicate_with_parens + current_text[cursor_pos:]
                focused_field.setText(new_text)
                
                # Move cursor between the parentheses
                new_cursor_pos = cursor_pos + len(predicate) + 1
                focused_field.setCursorPosition(new_cursor_pos)
            else:
                # For logical operators, just insert the symbol
                new_text = current_text[:cursor_pos] + predicate + current_text[cursor_pos:]
                focused_field.setText(new_text)
                
                # Move cursor to end of inserted text
                new_cursor_pos = cursor_pos + len(predicate)
                focused_field.setCursorPosition(new_cursor_pos)
            
            # Set focus back to the input field
            focused_field.setFocus()



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Tab:
            # Tab navigation is handled by Qt's tab order system
            super().keyPressEvent(event)
        elif event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Check if any edit field or evaluate button has focus
            focused_widget = self.focusWidget()
            if focused_widget in self.edit_fields or focused_widget == self.evaluate_button:
                self.evaluate_all_predicates()
        else:
            super().keyPressEvent(event)

    def save_world_only(self):
        """Save only the current world state to a file"""
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Save World Only", 
            "", 
            "Tarski World Files (*.tw);;JSON Files (*.json);;All Files (*)"
        )
        
        if filename:
            if not filename.endswith('.tw') and not filename.endswith('.json'):
                filename += '.tw'
            
            if self.tarski_world.save_world(filename):
                QMessageBox.information(self, "Success", f"World saved to {filename}")
            else:
                QMessageBox.critical(self, "Error", "Failed to save world")

    def load_world_only(self):
        """Load only the world state from a file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, 
            "Load World Only", 
            "", 
            "Tarski World Files (*.tw);;JSON Files (*.json);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    world_data = json.load(f)
                
                # Clear current world
                self.tarski_world.blocks.clear()
                self.tarski_world.selected_block = None
                
                # Load blocks
                for block_data in world_data.get("blocks", []):
                    block = Block(
                        x=block_data["x"],
                        y=block_data["y"],
                        size=block_data["size"],
                        shape=block_data["shape"],
                        name=block_data["name"]
                    )
                    self.tarski_world.blocks.append(block)
                
                # Update grid size if specified
                if "grid_size" in world_data:
                    self.tarski_world.grid_size = world_data["grid_size"]
                
                self.tarski_world.update()
                QMessageBox.information(self, "Success", f"World loaded from {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load world: {str(e)}")

    def save_sentences_only(self):
        """Save only the current sentences to a file"""
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Sentences Only", 
            "", 
            "Sentence Files (*.sent);;JSON Files (*.json);;All Files (*)"
        )
        
        if filename:
            if not filename.endswith('.sent') and not filename.endswith('.json'):
                filename += '.sent'
            
            # Collect current sentences from all fields
            sentences = {}
            for i, field in enumerate(self.edit_fields):
                sentences[f"sentence{i+1}"] = field.text()
            
            try:
                with open(filename, 'w') as f:
                    json.dump(sentences, f, indent=2)
                QMessageBox.information(self, "Success", f"Sentences saved to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save sentences: {str(e)}")

    def load_sentences_only(self):
        """Load only sentences from a file"""
        filename, _ = QFileDialog.getOpenFileName(
            self, 
            "Load Sentences Only", 
            "", 
            "Sentence Files (*.sent);;JSON Files (*.json);;All Files (*)"
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    sentences = json.load(f)
                
                # Clear existing fields and add new ones based on loaded sentences
                self.clear_edit_fields()
                for i in range(len(sentences)):
                    self.add_edit_field()
                    if i < len(self.edit_fields):
                        self.edit_fields[i].setText(sentences.get(f"sentence{i+1}", ""))
                
                QMessageBox.information(self, "Success", f"Sentences loaded from {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load sentences: {str(e)}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
