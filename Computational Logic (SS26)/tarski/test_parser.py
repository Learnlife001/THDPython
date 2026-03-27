from predicate_parser import PredicateParser
from predicate_evaluator import PredicateEvaluator

# Create a simple mock world for testing
class MockTarskiWorld:
    def __init__(self):
        self.blocks = []
    
    def get_block_by_name(self, name):
        # For testing, assume all blocks are cubes
        return type('Block', (), {'name': name, 'shape': 'cube'})()
    
    def is_cube(self, name):
        return True  # All blocks are cubes for this test

parser = PredicateParser()
evaluator = PredicateEvaluator(MockTarskiWorld())

# Test the expression with syntax error
test_expr_error = "¬Medium(c) ∧ Smaller(c, a))"
print("Testing expression with syntax error:")
try:
    result = parser.parse(test_expr_error)
    print("Parsed result:", result)
except Exception as e:
    print("Error:", e)

print("\n" + "="*50 + "\n")

# Test the corrected expression
test_expr_correct = "¬Medium(c) ∧ Smaller(c, a)"
print("Testing corrected expression:")
try:
    result = parser.parse(test_expr_correct)
    print("Parsed result:", result)
    
    evaluation = evaluator.evaluate(result)
    print("Evaluation result:", evaluation)
    print("Success!")
except Exception as e:
    print("Error:", e) 