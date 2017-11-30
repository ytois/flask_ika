from forbiddenfruit import curse
import re


def __classfy__(self):
    """some class_name => SomeClassName"""
    word = re.split(r'[ _]', self)
    return ''.join([w[0].upper() + w[1:] for w in word])


def __underscore__(self):
    return re.sub("([\sA-Z]+)", "_\\1", self).lower().lstrip("_").replace(' ', '')


curse(str, 'classfy', __classfy__)
curse(str, 'underscore', __underscore__)
