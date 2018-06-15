

class State:

    def __init__(self, name=None, matrix=[]):
        self.name = name
        self.matrix = matrix
        self.parent = None
        self.g = 2*10000

    def get_name(self):
        return self.name

    def get_matrix(self):
        return self.matrix

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent
