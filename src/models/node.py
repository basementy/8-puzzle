class Node:
    """
    A class representing an Solver node
    - 'puzzle' is a Puzzle instance
    - 'parent' is the preceding node generated by the solver, if any
    - 'action' is the action taken to produce puzzle, if any
    """
    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action

        if (self.parent != None):
            self.score_g = parent.score_g + 1
        else:
            self.score_g = 0

    @property
    def score(self):
        return (self.score_g + self.score_h)

    @property
    def state(self):
        """
        Return a hashable representation of self
        """
        return str(self)

    @property
    def path(self):
        """
        Reconstruct a path from to the root 'parent'
        """
        node, parent = self, []

        while node:
            parent.append(node)
            node = node.parent

        yield from reversed(parent)

    @property
    def solved(self):
        """ Wrapper to check if 'puzzle' is solved """
        return self.puzzle.solved

    @property
    def actions(self):
        """ Wrapper for 'actions' accessible at current state """
        return self.puzzle.actions

    @property
    def score_h(self):
        """"Score H"""
        return self.puzzle.manhattan

    @property
    def score_f(self):
        """"Score F"""
        return self.score_h + self.score_g

    def __str__(self):
        return str(self.puzzle)