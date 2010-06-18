


class Methodize(object):

    _element = None
    
    _numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    
    def __init__(self, dict_):
        object.__setattr__(self, '_element', dict_)

    def __getattr__(self, attr):

        if type(self._element) is list:
            if attr in dir(list):
                return list.__getattribute__(self._element, attr)
            if attr in self._numbers:
                return self[self._numbers.index(attr)]
            if attr == 'first':
                return self[0]
            if attr == 'last':
                return self[-1]
        if type(self._element) is dict and attr in dir(dict):
            return dict.__getattribute__(self._element, attr)
        
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

    def __getitem__(self, item):
        response = self._element[item]
        if type(response) in [dict, list]:
            return Methodize(response)
        else:
            return response

    def __setitem__(self, attr, value):
        self._element[attr] = value
