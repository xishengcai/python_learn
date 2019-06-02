class Dict(dict):
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("Dict' object has no attribute {}".format(key))

    def __setattr__(self, key, value):
        self[key] = value

