# predicate_registry.py

class PredicateRegistry:
    """Central registry for all supported predicates in Tarski's World"""
    
    def __init__(self):
        # Define all predicates with their arity (number of arguments)
        self._predicates = {
            'Cube': 1, 'Tet': 1, 'Dodec': 1,
            'Small': 1, 'Medium': 1, 'Large': 1,
            'LeftOf': 2, 'RightOf': 2, 'FrontOf': 2, 'BackOf': 2,
            'SameCol': 2, 'SameRow': 2, 'Between': 3, 'Adjoins': 2,
            'Smaller': 2, 'SameSize': 2, 'Larger': 2
        }
    
    def get_predicates(self):
        """Get all predicates as a dictionary {name: arity}"""
        return self._predicates.copy()
    
    def get_predicate_names(self):
        """Get list of all predicate names"""
        return list(self._predicates.keys())
    
    def get_predicate_arity(self, predicate_name):
        """Get the arity (number of arguments) for a predicate"""
        return self._predicates.get(predicate_name)
    
    def is_valid_predicate(self, predicate_name):
        """Check if a predicate name is valid"""
        return predicate_name in self._predicates
    
    def get_predicates_by_arity(self, arity):
        """Get all predicates with a specific arity"""
        return {name: arity for name, pred_arity in self._predicates.items() if pred_arity == arity}
    
    def get_unary_predicates(self):
        """Get all unary predicates (arity 1)"""
        return self.get_predicates_by_arity(1)
    
    def get_binary_predicates(self):
        """Get all binary predicates (arity 2)"""
        return self.get_predicates_by_arity(2)

# Global instance
predicate_registry = PredicateRegistry() 