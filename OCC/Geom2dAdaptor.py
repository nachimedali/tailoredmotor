# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _Geom2dAdaptor.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Geom2dAdaptor', [dirname(__file__)])
        except ImportError:
            import _Geom2dAdaptor
            return _Geom2dAdaptor
        if fp is not None:
            try:
                _mod = imp.load_module('_Geom2dAdaptor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Geom2dAdaptor = swig_import_helper()
    del swig_import_helper
else:
    import _Geom2dAdaptor
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
    __swig_destroy__ = _Geom2dAdaptor.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _Geom2dAdaptor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Adaptor2d
import OCC.Standard
import OCC.GeomAbs
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.gp
import OCC.Geom2d
import OCC.TColgp

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

class geom2dadaptor(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def MakeCurve(*args):
        """
        * Inherited from GHCurve. Provides a curve handled by reference. Creates a 2d curve from a HCurve2d. This cannot process the OtherCurves.

        :param HC:
        :type HC: Adaptor2d_Curve2d &
        :rtype: Handle_Geom2d_Curve

        """
        return _Geom2dAdaptor.geom2dadaptor_MakeCurve(*args)

    MakeCurve = staticmethod(MakeCurve)

    def __init__(self):
        _Geom2dAdaptor.geom2dadaptor_swiginit(self, _Geom2dAdaptor.new_geom2dadaptor())
    __swig_destroy__ = _Geom2dAdaptor.delete_geom2dadaptor
geom2dadaptor_swigregister = _Geom2dAdaptor.geom2dadaptor_swigregister
geom2dadaptor_swigregister(geom2dadaptor)

def geom2dadaptor_MakeCurve(*args):
    """
    * Inherited from GHCurve. Provides a curve handled by reference. Creates a 2d curve from a HCurve2d. This cannot process the OtherCurves.

    :param HC:
    :type HC: Adaptor2d_Curve2d &
    :rtype: Handle_Geom2d_Curve

    """
    return _Geom2dAdaptor.geom2dadaptor_MakeCurve(*args)

class Geom2dAdaptor_Curve(OCC.Adaptor2d.Adaptor2d_Curve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_Curve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_Curve(*args))

    def Load(self, *args):
        """
        :param C:
        :type C: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        return _Geom2dAdaptor.Geom2dAdaptor_Curve_Load(self, *args)


    def Curve(self, *args):
        """
        :rtype: Handle_Geom2d_Curve

        """
        return _Geom2dAdaptor.Geom2dAdaptor_Curve_Curve(self, *args)

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_Curve
Geom2dAdaptor_Curve.Load = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_Curve_Load, None, Geom2dAdaptor_Curve)
Geom2dAdaptor_Curve.Curve = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_Curve_Curve, None, Geom2dAdaptor_Curve)
Geom2dAdaptor_Curve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_Curve_swigregister
Geom2dAdaptor_Curve_swigregister(Geom2dAdaptor_Curve)

class Geom2dAdaptor_GHCurve(OCC.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: Geom2dAdaptor_Curve &
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_GHCurve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_GHCurve(*args))

    def Set(self, *args):
        """
        :param C:
        :type C: Geom2dAdaptor_Curve &
        :rtype: None

        """
        return _Geom2dAdaptor.Geom2dAdaptor_GHCurve_Set(self, *args)


    def ChangeCurve2d(self, *args):
        """
        :rtype: Geom2dAdaptor_Curve

        """
        return _Geom2dAdaptor.Geom2dAdaptor_GHCurve_ChangeCurve2d(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Geom2dAdaptor_GHCurve(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_GHCurve
Geom2dAdaptor_GHCurve.Set = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_GHCurve_Set, None, Geom2dAdaptor_GHCurve)
Geom2dAdaptor_GHCurve.ChangeCurve2d = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_GHCurve_ChangeCurve2d, None, Geom2dAdaptor_GHCurve)
Geom2dAdaptor_GHCurve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_GHCurve_swigregister
Geom2dAdaptor_GHCurve_swigregister(Geom2dAdaptor_GHCurve)

class Handle_Geom2dAdaptor_GHCurve(OCC.Adaptor2d.Handle_Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_swiginit(self, _Geom2dAdaptor.new_Handle_Geom2dAdaptor_GHCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast)
    __swig_destroy__ = _Geom2dAdaptor.delete_Handle_Geom2dAdaptor_GHCurve
Handle_Geom2dAdaptor_GHCurve.Nullify = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_Nullify, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve.IsNull = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_IsNull, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve.GetObject = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_GetObject, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve_swigregister = _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_swigregister
Handle_Geom2dAdaptor_GHCurve_swigregister(Handle_Geom2dAdaptor_GHCurve)

def Handle_Geom2dAdaptor_GHCurve_DownCast(AnObject):
    return _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast(AnObject)
Handle_Geom2dAdaptor_GHCurve_DownCast = _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast

class Geom2dAdaptor_HCurve(Geom2dAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param AS:
        :type AS: Geom2dAdaptor_Curve &
        :rtype: None

        :param S:
        :type S: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_HCurve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_HCurve(*args))

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Geom2dAdaptor_HCurve(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_HCurve
Geom2dAdaptor_HCurve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_HCurve_swigregister
Geom2dAdaptor_HCurve_swigregister(Geom2dAdaptor_HCurve)

class Handle_Geom2dAdaptor_HCurve(Handle_Geom2dAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_swiginit(self, _Geom2dAdaptor.new_Handle_Geom2dAdaptor_HCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast)
    __swig_destroy__ = _Geom2dAdaptor.delete_Handle_Geom2dAdaptor_HCurve
Handle_Geom2dAdaptor_HCurve.Nullify = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_Nullify, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve.IsNull = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_IsNull, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve.GetObject = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_GetObject, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve_swigregister = _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_swigregister
Handle_Geom2dAdaptor_HCurve_swigregister(Handle_Geom2dAdaptor_HCurve)

def Handle_Geom2dAdaptor_HCurve_DownCast(AnObject):
    return _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast(AnObject)
Handle_Geom2dAdaptor_HCurve_DownCast = _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast


