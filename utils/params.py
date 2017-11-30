from flask import request


class Params:
    def __init__(self):
        self.params = {}
        for p, v in request.args.items():
            self.params[p] = v
            # setattr(self, p, v)

    def __getattr__(self, name):
        if name in self.params:
            return self.params[name]

    def get(self, key, default=None):
        return request.args.get(key, default)
