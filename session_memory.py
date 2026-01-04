class SessionMemory:
    def __init__(self):
        self.history = []

    def add(self, user, bot):
        self.history.append((user, bot))

    def last(self, n=5):
        return self.history[-n:]
