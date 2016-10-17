class AssignOnce:
    forbidden = 1
    def __init__(self, initial_val):
        self.forbidden = initial_val

    def __setattr__(self, name, value):
        if hasattr(self, name):
            import pdb;pdb.set_trace()
            raise AttributeError("Undefined attribute %s" % name)
        super().__setattr__(name, value)

fw = AssignOnce(2)
fw.ok = 3


fw.forbidden = 3
fw.ok = 4