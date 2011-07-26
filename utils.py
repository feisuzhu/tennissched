#!/bin/false
import cPickle

class CheckFailed(Exception):
    pass

def check(exp, errstr = 'Generic error'):
    if not exp:
        raise CheckFailed(errstr)


def bean(*args):
    flist = args

    def bean_constrain_access(self, field, v):
        if not self.__dict__.has_key(field) and field not in flist and not field.startswith("_"):
            raise AttributeError("'%s' object has no attribute '%s'" % (str(self.__class__), field))
        self.__dict__[field] = v

    def f(klass):
        klass.__setattr__ = bean_constrain_access 
        return klass

    return f

def singleton(klass):
    '''
    Make a class singleton
    Create an instance and store as 'instance' attribute.
    Call '_static_' if decorated class has this function.
    '''
    def no_new(*args, **kwargs):
        raise Exception("%s is a singleton class, so don't create any instance of it" % str(klass))

    klass.instance = klass()
    klass.__init__ = no_new
    if klass.__dict__.has_key("_static_") and callable(klass._static_):
        klass._static_(klass)
    return klass


def nop(g):
    for i in g:
        pass
