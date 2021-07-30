class NotFound(Exception):
    def __repr__(self):
        return "value not found"
