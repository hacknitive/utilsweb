class SafeFormat(object):
    def __init__(self, **kw):
        self.__dict = kw

    def __getitem__(self, name):
        return self.__dict.get(name, '{%s}' % name)
