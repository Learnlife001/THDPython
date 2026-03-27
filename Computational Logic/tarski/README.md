# Tarski's World - First-Order Logic Visualizer

A PyQt5-based application for visualizing and evaluating first-order logic sentences in a 2D grid world.

## Author
**[Thomas Ewender]**  
Email: [thomas.ewender@th-deg.de]  
GitHub: [your-github-username]

## Description
This application allows users to:
- Place and manipulate blocks of different shapes (cube, tetrahedron, dodecahedron)
- Set block properties (size, color, name)
- Write and evaluate first-order logic sentences
- Use quantifiers (∀, ∃), logical operators (∧, ∨, ¬, →, ↔), and geometric predicates
- Get real-time evaluation results with visual feedback

## Features
- **Visual Interface**: 8x8 grid world with drag-and-drop block placement
- **Block Properties**: Three shapes, three sizes, named blocks (A-F)
- **Logic Evaluation**: Support for complex first-order logic sentences
- **Predicates**: Geometric (LeftOf, RightOf, Between, etc.) and property predicates
- **Keyboard Navigation**: Tab navigation and Enter key evaluation

## Installation
```bash
pip install PyQt5
python TarskiWorld.py
```

## Usage
1. Click on the grid to place blocks
2. Select blocks and use shape/size buttons to modify them
3. Press A-F to name blocks
4. Enter logical sentences in the input field
5. Press Enter or click Evaluate to see results

## License
[MIT]

## Version
1.0 