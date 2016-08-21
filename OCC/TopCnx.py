# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _TopCnx.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TopCnx', [dirname(__file__)])
        except ImportError:
            import _TopCnx
            return _TopCnx
        if fp is not None:
            try:
                _mod = imp.load_module('_TopCnx', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TopCnx = swig_import_helper()
    del swig_import_helper
else:
    import _TopCnx
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _TopCnx.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_TopCnx.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_TopCnx.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_TopCnx.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_TopCnx.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_TopCnx.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_TopCnx.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_TopCnx.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_TopCnx.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_TopCnx.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_TopCnx.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_TopCnx.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_TopCnx.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_TopCnx.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_TopCnx.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_TopCnx.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_TopCnx.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _TopCnx.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.gp
import OCC.Standard
import OCC.TopAbs

def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass

class TopCnx_EdgeFaceTransition(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an empty algorithm.

        :rtype: None

        """
        _TopCnx.TopCnx_EdgeFaceTransition_swiginit(self, _TopCnx.new_TopCnx_EdgeFaceTransition(*args))

    def Reset(self, *args):
        """
        * Initialize the algorithm with the local description of the edge.

        :param Tgt:
        :type Tgt: gp_Dir
        :param Norm:
        :type Norm: gp_Dir
        :param Curv:
        :type Curv: float
        :rtype: None

        * Initialize the algorithm with a linear Edge.

        :param Tgt:
        :type Tgt: gp_Dir
        :rtype: None

        """
        return _TopCnx.TopCnx_EdgeFaceTransition_Reset(self, *args)


    def AddInterference(self, *args):
        """
        * Add a curve element to the boundary. Or is the orientation of the interference on the boundary curve. Tr is the transition of the interference. BTr is the boundary transition of the interference.

        :param Tole:
        :type Tole: float
        :param Tang:
        :type Tang: gp_Dir
        :param Norm:
        :type Norm: gp_Dir
        :param Curv:
        :type Curv: float
        :param Or:
        :type Or: TopAbs_Orientation
        :param Tr:
        :type Tr: TopAbs_Orientation
        :param BTr:
        :type BTr: TopAbs_Orientation
        :rtype: None

        """
        return _TopCnx.TopCnx_EdgeFaceTransition_AddInterference(self, *args)


    def Transition(self, *args):
        """
        * Returns the current cumulated transition.

        :rtype: TopAbs_Orientation

        """
        return _TopCnx.TopCnx_EdgeFaceTransition_Transition(self, *args)


    def BoundaryTransition(self, *args):
        """
        * Returns the current cumulated BoundaryTransition.

        :rtype: TopAbs_Orientation

        """
        return _TopCnx.TopCnx_EdgeFaceTransition_BoundaryTransition(self, *args)

    __swig_destroy__ = _TopCnx.delete_TopCnx_EdgeFaceTransition
TopCnx_EdgeFaceTransition.Reset = new_instancemethod(_TopCnx.TopCnx_EdgeFaceTransition_Reset, None, TopCnx_EdgeFaceTransition)
TopCnx_EdgeFaceTransition.AddInterference = new_instancemethod(_TopCnx.TopCnx_EdgeFaceTransition_AddInterference, None, TopCnx_EdgeFaceTransition)
TopCnx_EdgeFaceTransition.Transition = new_instancemethod(_TopCnx.TopCnx_EdgeFaceTransition_Transition, None, TopCnx_EdgeFaceTransition)
TopCnx_EdgeFaceTransition.BoundaryTransition = new_instancemethod(_TopCnx.TopCnx_EdgeFaceTransition_BoundaryTransition, None, TopCnx_EdgeFaceTransition)
TopCnx_EdgeFaceTransition_swigregister = _TopCnx.TopCnx_EdgeFaceTransition_swigregister
TopCnx_EdgeFaceTransition_swigregister(TopCnx_EdgeFaceTransition)



