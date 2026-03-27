from predicate_parser import PredicateParser

parser = PredicateParser()

# Test the problematic expression
test_expr = "∃x∃y∃z(Between(x, y, z) ∧ Cube(x))"

print(f"Testing expression: {test_expr}")

# First, let's see what tokens are generated
tokens = parser._tokenize(test_expr)
print(f"Tokens: {tokens}")

# Now try to parse
try:
    result = parser.parse(test_expr)
    print(f"Parsed result: {result}")
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
    
    # Let's try parsing step by step
    print("\nTrying to parse step by step:")
    try:
        # Try parsing just the first quantifier
        first_part = "∃x(Between(x, y, z) ∧ Cube(x))"
        print(f"Parsing: {first_part}")
        result1 = parser.parse(first_part)
        print(f"Result: {result1}")
    except Exception as e1:
        print(f"Error with first part: {e1}") 