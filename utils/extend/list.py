from forbiddenfruit import curse


def __flatten__(self):
    flat_list = []
    fringe = [self]

    while len(fringe) > 0:
        node = fringe.pop(0)
        if isinstance(node, list):
            fringe = node + fringe
        else:
            flat_list.append(node)

    return flat_list

curse(list, 'flatten', __flatten__)
