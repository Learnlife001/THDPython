# predicate_parser.py

import re
from typing import List, Union, Tuple
from predicate_registry import predicate_registry

class PredicateParser:
    def __init__(self):
        self.predicates = predicate_registry.get_predicates()

    def parse(self, input_string: str) -> Union[Tuple[str, List[str]], List[Union[str, List]]]:
        tokens = self._tokenize(input_string)
        return self._parse_expression(tokens, 0)

    def _tokenize(self, input_string: str) -> List[str]:
        return re.findall(r'\w+|\(|\)|\&|\||\!|\-\>|\<\-\>|∀|@|∃|€|∧|∨|¬|→|↔', input_string)

    def _parse_expression(self, tokens: List[str], precedence: int = 0):
        if not tokens:
            raise ValueError("Empty expression")

        # Define operator precedence (higher number = higher precedence)
        operator_precedence = {
            '!': 4, '¬': 4,
            '&': 3, '∧': 3,
            '|': 2, '∨': 2,
            '->': 1, '→': 1, '<->': 1, '↔': 1
        }

        if tokens[0] == '(':  # Parenthesized expression
            count = 1
            for i, token in enumerate(tokens[1:], 1):
                if token == '(': count += 1
                elif token == ')': count -= 1
                if count == 0: break
            if count != 0:
                raise ValueError("Mismatched parentheses")
            sub_expr = self._parse_expression(tokens[1:i], 0)
            rest = tokens[i+1:]
            if not rest:
                return sub_expr
            if rest[0] in operator_precedence and operator_precedence[rest[0]] >= precedence:
                return [rest[0], sub_expr, self._parse_expression(rest[1:], operator_precedence[rest[0]])]
            return sub_expr

        if tokens[0] in ['!', '¬']:
            return ['!', self._parse_expression(tokens[1:], 4)]

        if tokens[0] in ['∀', '@']:
            if len(tokens) < 3:
                raise ValueError(f"Invalid syntax for universal quantifier {tokens[0]}")
            variable = tokens[1]
            
            # Check if the next token is another quantifier (nested quantifiers)
            if len(tokens) > 2 and tokens[2] in ['∀', '@', '∃', '€']:
                # Parse the nested quantifier as the quantified formula
                quantified_formula = self._parse_expression(tokens[2:], 0)
                return ['∀', variable, quantified_formula]
            
            if len(tokens) > 2 and tokens[2] == '(':  # Quantified formula in parens
                count = 1
                for i, token in enumerate(tokens[3:], 3):
                    if token == '(': count += 1
                    elif token == ')': count -= 1
                    if count == 0: break
                if count != 0:
                    raise ValueError("Mismatched parentheses in universal quantifier")
                quantified_tokens = tokens[3:i]
                rest = tokens[i+1:]
            else:
                quantified_tokens = []
                rest = []
                for i, token in enumerate(tokens[2:], 2):
                    if token in operator_precedence:
                        rest = tokens[i:]
                        break
                    quantified_tokens.append(token)
            quantified_formula = self._parse_expression(quantified_tokens, 0)
            if not rest:
                return ['∀', variable, quantified_formula]
            if rest[0] in operator_precedence and operator_precedence[rest[0]] >= precedence:
                return [rest[0], ['∀', variable, quantified_formula], self._parse_expression(rest[1:], operator_precedence[rest[0]])]
            return ['∀', variable, quantified_formula]

        if tokens[0] in ['∃', '€']:
            if len(tokens) < 3:
                raise ValueError(f"Invalid syntax for existential quantifier {tokens[0]}")
            variable = tokens[1]
            
            # Check if the next token is another quantifier (nested quantifiers)
            if len(tokens) > 2 and tokens[2] in ['∀', '@', '∃', '€']:
                # Parse the nested quantifier as the quantified formula
                quantified_formula = self._parse_expression(tokens[2:], 0)
                return ['∃', variable, quantified_formula]
            
            if len(tokens) > 2 and tokens[2] == '(':  # Quantified formula in parens
                count = 1
                for i, token in enumerate(tokens[3:], 3):
                    if token == '(': count += 1
                    elif token == ')': count -= 1
                    if count == 0: break
                if count != 0:
                    raise ValueError("Mismatched parentheses in existential quantifier")
                quantified_tokens = tokens[3:i]
                rest = tokens[i+1:]
            else:
                quantified_tokens = []
                rest = []
                for i, token in enumerate(tokens[2:], 2):
                    if token in operator_precedence:
                        rest = tokens[i:]
                        break
                    quantified_tokens.append(token)
            quantified_formula = self._parse_expression(quantified_tokens, 0)
            if not rest:
                return ['∃', variable, quantified_formula]
            if rest[0] in operator_precedence and operator_precedence[rest[0]] >= precedence:
                return [rest[0], ['∃', variable, quantified_formula], self._parse_expression(rest[1:], operator_precedence[rest[0]])]
            return ['∃', variable, quantified_formula]

        if tokens[0] in self.predicates:
            predicate = tokens[0]
            if len(tokens) < 3 or tokens[1] != '(':  # Must have at least pred ( ... )
                raise ValueError(f"Invalid syntax for predicate {predicate}")
            # Find the matching closing parenthesis
            count = 1
            for i, token in enumerate(tokens[2:], 2):
                if token == '(': count += 1
                elif token == ')': count -= 1
                if count == 0:
                    closing_paren_index = i
                    break
            else:
                raise ValueError(f"Mismatched parentheses in predicate {predicate}")
            args = tokens[2:closing_paren_index]
            print(f"DEBUG: Parser - predicate {predicate}, tokens: {tokens}, args: {args}, closing_paren_index: {closing_paren_index}")  # DEBUG
            # Remove commas if present (not used in your grammar, but just in case)
            args = [arg for arg in args if arg != ',']
            rest = tokens[closing_paren_index+1:]
            expected_args = self.predicates[predicate]
            if len(args) != expected_args:
                raise ValueError(f"Predicate {predicate} expects {expected_args} arguments, got {len(args)}")
            if not rest:
                return (predicate, args)
            if rest[0] in operator_precedence and operator_precedence[rest[0]] >= precedence:
                return [rest[0], (predicate, args), self._parse_expression(rest[1:], operator_precedence[rest[0]])]
            return (predicate, args)

        raise ValueError(f"Unexpected token: {tokens[0]}")

if __name__ == "__main__":
    parser = PredicateParser()
    
    # Test cases
    test_cases = [
        "Cube(a)",
        "LeftOf(a,b)",
        "Cube(a) & LeftOf(a,b)",
        "!(Cube(a) & LeftOf(a,b))",
        "(Cube(a) | Tet(b)) & LeftOf(a,b)",
    ]

    for case in test_cases:
        try:
            result = parser.parse(case)
            print(f"Input: {case}")
            print(f"Parsed: {result}\n")
        except ValueError as e:
            print(f"Error parsing '{case}': {str(e)}\n")
