from forbiddenfruit import curse


def __slice__(self, keys):
    return {k: self[k] for k in keys if k in self}


def __exclude__(self, keys):
    return {k: self[k] for k in self.keys() if k not in keys}

curse(dict, 'slice', __slice__)
curse(dict, 'exclude', __exclude__)
