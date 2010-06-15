


class Methodize(object):

    _dict = {}

    def __init__(self, dict_):
        object.__setattr__(self, '_dict', dict_)

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getitem__(self, item):
        response = self._dict[item]
        if type(response) in [dict, list]:
            return Methodize(response)
        else:
            return response

    def __setitem__(self, attr, value):
        self._dict[attr] = value
    
    def append(self, value):
        self._dict.append(value)
