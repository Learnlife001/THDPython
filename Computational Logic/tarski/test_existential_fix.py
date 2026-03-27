#!/usr/bin/env python3

from predicate_parser import PredicateParser
from predicate_evaluator import PredicateEvaluator

# Mock TarskiWorld class for testing
class MockTarskiWorld:
    def __init__(self):
        # Create mock blocks
        self.blocks = [
            MockBlock(1, 1, name='a'),
            MockBlock(3, 1, name='b')
        ]
    
    def get_block_by_name(self, name):
        for block in self.blocks:
            if block.name == name:
                return block
        return None
    
    def is_cube(self, name):
        block = self.get_block_by_name(name)
        return block is not None and block.shape == 'cube'
    
    def is_right_of(self, name1, name2):
        block1 = self.get_block_by_name(name1)
        block2 = self.get_block_by_name(name2)
        return block1 is not None and block2 is not None and block1.x > block2.x
    
    def is_left_of(self, name1, name2):
        block1 = self.get_block_by_name(name1)
        block2 = self.get_block_by_name(name2)
        return block1 is not None and block2 is not None and block1.x < block2.x

class MockBlock:
    def __init__(self, x, y, shape='cube', name=None):
        self.x = x
        self.y = y
        self.shape = shape
        self.name = name

def test_existential_quantifier():
    # Create a mock TarskiWorld with two blocks on the same row
    world = MockTarskiWorld()
    
    # Create parser and evaluator
    parser = PredicateParser()
    evaluator = PredicateEvaluator(world)
    
    # Test cases
    test_cases = [
        "∃x∃y(RightOf(x, y))",
        "∃x∃y(LeftOf(x, y))",
        "∃x(Cube(x))",
        "∀x(Cube(x))"
    ]
    
    print("Testing existential quantifier fix:")
    print(f"Blocks: {[(b.name, b.x, b.y) for b in world.blocks]}")
    print()
    
    for formula in test_cases:
        try:
            parsed = parser.parse(formula)
            print(f"Parsed structure for {formula}: {parsed}")  # DEBUG
            result = evaluator.evaluate(parsed)
            print(f"Formula: {formula}")
            print(f"Result: {result}")
            print()
        except Exception as e:
            print(f"Error with {formula}: {e}")
            print()

if __name__ == "__main__":
    test_existential_quantifier() 