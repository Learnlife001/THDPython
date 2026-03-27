# predicate_evaluator.py

from typing import Union, List, Tuple
from predicate_registry import predicate_registry

class PredicateEvaluator:
    def __init__(self, tarski_world):
        self.world = tarski_world
        print(f"DEBUG: Predicate registry: {predicate_registry.get_predicates()}")  # DEBUG

    def evaluate(self, parsed_predicate: Union[Tuple[str, List[str]], List[Union[str, List]]]) -> bool:
        # If the top-level is a quantifier, use the distinct quantifier logic
        if isinstance(parsed_predicate, list) and parsed_predicate and parsed_predicate[0] in ['∀', '∃']:
            return self._evaluate_with_distinct_quantifiers(parsed_predicate, set())
        # Otherwise, use the original logic
        if isinstance(parsed_predicate, tuple):
            predicate, args = parsed_predicate
            return self._evaluate_simple_predicate(predicate, args)
        elif isinstance(parsed_predicate, list):
            if parsed_predicate[0] == '!':
                return not self.evaluate(parsed_predicate[1])
            elif parsed_predicate[0] in ['&', '∧']:
                return self.evaluate(parsed_predicate[1]) and self.evaluate(parsed_predicate[2])
            elif parsed_predicate[0] in ['|', '∨']:
                return self.evaluate(parsed_predicate[1]) or self.evaluate(parsed_predicate[2])
            elif parsed_predicate[0] in ['->', '→']:
                return (not self.evaluate(parsed_predicate[1])) or self.evaluate(parsed_predicate[2])
            elif parsed_predicate[0] in ['<->', '↔']:
                return (self.evaluate(parsed_predicate[1]) == self.evaluate(parsed_predicate[2]))
        raise ValueError(f"Invalid parsed predicate: {parsed_predicate}")

    def _flatten_args(self, args):
        flat = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                flat.extend(self._flatten_args(arg))
            else:
                flat.append(arg)
        return flat

    def _evaluate_simple_predicate(self, predicate: str, args: list) -> bool:
        # Validate predicate exists in registry
        if not predicate_registry.is_valid_predicate(predicate):
            raise ValueError(f"Unknown predicate: {predicate}")
        # Flatten arguments
        args = self._flatten_args(args)
        # Validate argument count
        expected_arity = predicate_registry.get_predicate_arity(predicate)
        print(f"DEBUG: Predicate {predicate}, expected arity: {expected_arity}, args: {args}")  # DEBUG
        if len(args) != expected_arity:
            raise ValueError(f"Predicate {predicate} expects {expected_arity} arguments, got {len(args)}")
        print(f"DEBUG: Evaluating predicate {predicate} with args {args}")  # DEBUG
        args = [arg.lower() for arg in args]

        if predicate == 'Cube':
            return self.world.is_cube(args[0])
        elif predicate == 'Tet':
            return self.world.is_tet(args[0])
        elif predicate == 'Dodec':
            return self.world.is_dodec(args[0])
        elif predicate == 'LeftOf':
            return self.world.is_left_of(args[0], args[1])
        elif predicate == 'RightOf':
            return self.world.is_right_of(args[0], args[1])
        elif predicate == 'FrontOf':
            return self.world.is_front_of(args[0], args[1])
        elif predicate == 'BackOf':
            return self.world.is_back_of(args[0], args[1])
        elif predicate == 'Small':
            return self.world.is_small(args[0])
        elif predicate == 'Medium':
            return self.world.is_medium(args[0])
        elif predicate == 'Large':
            return self.world.is_large(args[0])
        elif predicate == 'SameCol':
            return self.world.is_same_col(args[0], args[1])
        elif predicate == 'SameRow':
            return self.world.is_same_row(args[0], args[1])
        elif predicate == 'Between':
            return self.world.is_between(args[0], args[1], args[2])
        elif predicate == 'Adjoins':
            return self.world.is_adjoins(args[0], args[1])
        elif predicate == 'Smaller':
            return self.world.is_smaller(args[0], args[1])
        elif predicate == 'SameSize':
            return self.world.is_same_size(args[0], args[1])
        elif predicate == 'Larger':
            return self.world.is_larger(args[0], args[1])
        else:
            raise ValueError(f"Unknown predicate: {predicate}")

    def _evaluate_universal_quantifier(self, variable: str, quantified_formula) -> bool:
        """
        Evaluate universal quantifier ∀x(φ) - returns True if φ is true for all blocks (standard semantics)
        """
        all_blocks = []
        for i, block in enumerate(self.world.blocks):
            if block.name is not None:
                all_blocks.append(block.name)
            else:
                all_blocks.append(f"block_{i}")
        if not all_blocks:
            return True
        for block_identifier in all_blocks:
            substituted_formula = self._substitute_variable(quantified_formula, variable, block_identifier)
            if not self.evaluate(substituted_formula):
                return False
        return True

    def _evaluate_existential_quantifier(self, variable: str, quantified_formula) -> bool:
        """
        Evaluate existential quantifier ∃x(φ) - returns True if φ is true for at least one block (standard semantics)
        """
        all_blocks = []
        for i, block in enumerate(self.world.blocks):
            if block.name is not None:
                all_blocks.append(block.name)
            else:
                all_blocks.append(f"block_{i}")
        if not all_blocks:
            return False
        for block_identifier in all_blocks:
            substituted_formula = self._substitute_variable(quantified_formula, variable, block_identifier)
            if self.evaluate(substituted_formula):
                return True
        return False

    def _evaluate_with_distinct_quantifiers(self, parsed_predicate, used_blocks=None):
        # This is now just a wrapper for standard quantifier logic
        if isinstance(parsed_predicate, str):
            raise ValueError(f"Unexpected string in predicate evaluation: {parsed_predicate}")
        if isinstance(parsed_predicate, tuple):
            print(f"DEBUG: _evaluate_with_distinct_quantifiers received tuple: {parsed_predicate}")  # DEBUG
            predicate, args = parsed_predicate
            return self._evaluate_simple_predicate(predicate, args)
        if isinstance(parsed_predicate, list):
            print(f"DEBUG: _evaluate_with_distinct_quantifiers received list: {parsed_predicate}")  # DEBUG
            # If it's a quantifier or logical operator, handle as before
            if parsed_predicate and parsed_predicate[0] in ['∀', '∃', '!', '&', '∧', '|', '∨', '->', '→', '<->', '↔']:
                if parsed_predicate[0] == '∀':
                    variable = parsed_predicate[1]
                    quantified_formula = parsed_predicate[2]
                    return self._evaluate_universal_quantifier(variable, quantified_formula)
                elif parsed_predicate[0] == '∃':
                    variable = parsed_predicate[1]
                    quantified_formula = parsed_predicate[2]
                    return self._evaluate_existential_quantifier(variable, quantified_formula)
                elif parsed_predicate[0] == '!':
                    return not self._evaluate_with_distinct_quantifiers(parsed_predicate[1])
                elif parsed_predicate[0] in ['&', '∧']:
                    return self._evaluate_with_distinct_quantifiers(parsed_predicate[1]) and self._evaluate_with_distinct_quantifiers(parsed_predicate[2])
                elif parsed_predicate[0] in ['|', '∨']:
                    return self._evaluate_with_distinct_quantifiers(parsed_predicate[1]) or self._evaluate_with_distinct_quantifiers(parsed_predicate[2])
                elif parsed_predicate[0] in ['->', '→']:
                    return (not self._evaluate_with_distinct_quantifiers(parsed_predicate[1])) or self._evaluate_with_distinct_quantifiers(parsed_predicate[2])
                elif parsed_predicate[0] in ['<->', '↔']:
                    return self._evaluate_with_distinct_quantifiers(parsed_predicate[1]) == self._evaluate_with_distinct_quantifiers(parsed_predicate[2])
            # If it's a list and first element is a predicate name, treat as predicate tuple
            elif len(parsed_predicate) >= 1 and parsed_predicate[0] in predicate_registry.get_predicate_names():
                print(f"DEBUG: Treating list as predicate tuple: {parsed_predicate[0]}, {parsed_predicate[1:]}")  # DEBUG
                return self._evaluate_simple_predicate(parsed_predicate[0], parsed_predicate[1:])
            else:
                raise ValueError(f"Invalid list structure in predicate evaluation: {parsed_predicate}")
        raise ValueError(f"Invalid parsed predicate: {parsed_predicate}")

    def _substitute_variable(self, formula, variable: str, value: str):
        """
        Substitute a variable with a value in a formula
        """
        print(f"DEBUG: _substitute_variable called with formula={formula}, variable={variable}, value={value}")  # DEBUG
        if isinstance(formula, str):
            result = value if formula == variable else formula
            print(f"DEBUG: String substitution result: {result}")  # DEBUG
            return result
        if isinstance(formula, tuple):
            # Simple predicate: substitute in arguments
            predicate, args = formula
            # Recursively substitute in each argument
            new_args = [self._substitute_variable(arg, variable, value) for arg in args]
            result = (predicate, new_args)
            print(f"DEBUG: Tuple substitution result: {result}")  # DEBUG
            return result
        elif isinstance(formula, list):
            # Complex formula: recursively substitute
            if formula[0] in ['∀', '∃'] and len(formula) == 3:
                if formula[1] == variable:
                    # Shadowed variable: do not substitute inside
                    result = [formula[0], formula[1], formula[2]]
                else:
                    result = [formula[0], formula[1], self._substitute_variable(formula[2], variable, value)]
                print(f"DEBUG: Quantifier substitution result: {result}")  # DEBUG
                return result
            elif formula[0] == '!' and len(formula) == 2:
                # For '!', substitute in the operand (second element)
                result = [formula[0], self._substitute_variable(formula[1], variable, value)]
                print(f"DEBUG: Unary operator substitution result: {result}")  # DEBUG
                return result
            elif formula[0] in ['&', '|', '->', '<->', '∧', '∨', '→', '↔']:
                # Binary operators: substitute in both operands
                result = [
                    formula[0],
                    self._substitute_variable(formula[1], variable, value),
                    self._substitute_variable(formula[2], variable, value)
                ]
                print(f"DEBUG: Binary operator substitution result: {result}")  # DEBUG
                return result
        result = formula
        print(f"DEBUG: _substitute_variable({formula}, {variable}, {value}) => {result}")  # DEBUG
        return result

if __name__ == "__main__":
    # This is a mock TarskiWorld class for testing purposes
    class MockTarskiWorld:
        def is_cube(self, name):
            return name == 'a'
        def is_tet(self, name):
            return name == 'b'
        def is_left_of(self, name1, name2):
            return name1 == 'a' and name2 == 'b'
        # ... implement other methods as needed for testing

    mock_world = MockTarskiWorld()
    evaluator = PredicateEvaluator(mock_world)

    # Test cases
    test_cases = [
        (("Cube", ["a"]), True),
        (("Cube", ["b"]), False),
        (["&", ("Cube", ["a"]), ("LeftOf", ["a", "b"])], True),
        (["!", ("Cube", ["b"])], True),
        (["|", ("Cube", ["b"]), ("Tet", ["b"])], True),
    ]

    for parsed_predicate, expected_result in test_cases:
        result = evaluator.evaluate(parsed_predicate)
        print(f"Predicate: {parsed_predicate}")
        print(f"Result: {result}")
        print(f"Expected: {expected_result}")
        print(f"{'Passed' if result == expected_result else 'Failed'}\n")
