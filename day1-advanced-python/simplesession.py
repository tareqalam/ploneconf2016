import uuid


class SimpleSession:

    def __init__(self, manager_inst):
        self.id = None
        self.data = {}
        self.manager = manager_inst

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]

    def make_session_id(self):
        return str(uuid.uuid4())

    def get(self, key, default=None):
        pass

    def load(self, id):
        if id in self.manager:
            self.data = self.manager[id]
            self.id = id
        else:
            self.data = {}
            self.id - uuid.uuid4().hex

    def save(self):
        self.manager[self.id] = self.data
        return self.id


class DictBasedSessionManager:
    sessions = {}

    def __setitem__(self, id, data):
        pass

    def __getitem__(self, id):
        return self.sessions[id]

    def __contains__(self, id):
        return id in self.sessions
