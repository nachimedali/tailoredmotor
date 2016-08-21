# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _BRepAdaptor.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BRepAdaptor', [dirname(__file__)])
        except ImportError:
            import _BRepAdaptor
            return _BRepAdaptor
        if fp is not None:
            try:
                _mod = imp.load_module('_BRepAdaptor', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _BRepAdaptor = swig_import_helper()
    del swig_import_helper
else:
    import _BRepAdaptor
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
    __swig_destroy__ = _BRepAdaptor.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_BRepAdaptor.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_BRepAdaptor.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_BRepAdaptor.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_BRepAdaptor.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_BRepAdaptor.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_BRepAdaptor.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_BRepAdaptor.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_BRepAdaptor.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_BRepAdaptor.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_BRepAdaptor.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _BRepAdaptor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import OCC.Standard
import OCC.Adaptor3d
import OCC.GeomAbs
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.gp
import OCC.Geom
import OCC.TColgp
import OCC.Adaptor2d
import OCC.Geom2d
import OCC.TopAbs
import OCC.math
import OCC.TopoDS
import OCC.TopLoc
import OCC.GeomAdaptor
import OCC.Geom2dAdaptor

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

class BRepAdaptor_Array1OfCurve(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :param Low:
        :type Low: int
        :param Up:
        :type Up: int
        :rtype: None

        :param Item:
        :type Item: BRepAdaptor_Curve &
        :param Low:
        :type Low: int
        :param Up:
        :type Up: int
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_Array1OfCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Array1OfCurve(*args))

    def Init(self, *args):
        """
        :param V:
        :type V: BRepAdaptor_Curve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Init(self, *args)


    def Destroy(self, *args):
        """
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Destroy(self, *args)


    def IsAllocated(self, *args):
        """
        :rtype: bool

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_IsAllocated(self, *args)


    def Assign(self, *args):
        """
        :param Other:
        :type Other: BRepAdaptor_Array1OfCurve &
        :rtype: BRepAdaptor_Array1OfCurve

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Assign(self, *args)


    def Set(self, *args):
        """
        :param Other:
        :type Other: BRepAdaptor_Array1OfCurve &
        :rtype: BRepAdaptor_Array1OfCurve

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Set(self, *args)


    def Length(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Length(self, *args)


    def Lower(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Lower(self, *args)


    def Upper(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Upper(self, *args)


    def SetValue(self, *args):
        """
        :param Index:
        :type Index: int
        :param Value:
        :type Value: BRepAdaptor_Curve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_SetValue(self, *args)


    def Value(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: BRepAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_Value(self, *args)


    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: BRepAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_Array1OfCurve_ChangeValue(self, *args)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Array1OfCurve
BRepAdaptor_Array1OfCurve.Init = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Init, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Destroy = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Destroy, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.IsAllocated = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_IsAllocated, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Assign = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Assign, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Set = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Set, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Length = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Length, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Lower = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Lower, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Upper = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Upper, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.SetValue = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_SetValue, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.Value = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_Value, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve.ChangeValue = new_instancemethod(_BRepAdaptor.BRepAdaptor_Array1OfCurve_ChangeValue, None, BRepAdaptor_Array1OfCurve)
BRepAdaptor_Array1OfCurve_swigregister = _BRepAdaptor.BRepAdaptor_Array1OfCurve_swigregister
BRepAdaptor_Array1OfCurve_swigregister(BRepAdaptor_Array1OfCurve)

class BRepAdaptor_CompCurve(OCC.Adaptor3d.Adaptor3d_Curve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an undefined Curve with no Wire loaded.

        :rtype: None

        :param W:
        :type W: TopoDS_Wire &
        :param KnotByCurvilinearAbcissa: default value is Standard_False
        :type KnotByCurvilinearAbcissa: bool
        :rtype: None

        * Creates a Curve to acces to the geometry of edge <W>.

        :param W:
        :type W: TopoDS_Wire &
        :param KnotByCurvilinearAbcissa:
        :type KnotByCurvilinearAbcissa: bool
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Tol:
        :type Tol: float
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_CompCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_CompCurve(*args))

    def Initialize(self, *args):
        """
        * Sets the wire <W>.

        :param W:
        :type W: TopoDS_Wire &
        :param KnotByCurvilinearAbcissa:
        :type KnotByCurvilinearAbcissa: bool
        :rtype: None

        * Sets wire <W> and trimmed parameter.

        :param W:
        :type W: TopoDS_Wire &
        :param KnotByCurvilinearAbcissa:
        :type KnotByCurvilinearAbcissa: bool
        :param First:
        :type First: float
        :param Last:
        :type Last: float
        :param Tol:
        :type Tol: float
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_CompCurve_Initialize(self, *args)


    def SetPeriodic(self, *args):
        """
        * Set the flag Periodic. Warning: This method has no effect if the wire is not closed

        :param Periodic:
        :type Periodic: bool
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_CompCurve_SetPeriodic(self, *args)


    def Wire(self, *args):
        """
        * Returns the wire.

        :rtype: TopoDS_Wire

        """
        return _BRepAdaptor.BRepAdaptor_CompCurve_Wire(self, *args)


    def Edge(self, *args):
        """
        * returns an edge and one parameter on them corresponding to the parameter U.

        :param U:
        :type U: float
        :param E:
        :type E: TopoDS_Edge &
        :param UonE:
        :type UonE: float &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_CompCurve_Edge(self, *args)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_CompCurve
BRepAdaptor_CompCurve.Initialize = new_instancemethod(_BRepAdaptor.BRepAdaptor_CompCurve_Initialize, None, BRepAdaptor_CompCurve)
BRepAdaptor_CompCurve.SetPeriodic = new_instancemethod(_BRepAdaptor.BRepAdaptor_CompCurve_SetPeriodic, None, BRepAdaptor_CompCurve)
BRepAdaptor_CompCurve.Wire = new_instancemethod(_BRepAdaptor.BRepAdaptor_CompCurve_Wire, None, BRepAdaptor_CompCurve)
BRepAdaptor_CompCurve.Edge = new_instancemethod(_BRepAdaptor.BRepAdaptor_CompCurve_Edge, None, BRepAdaptor_CompCurve)
BRepAdaptor_CompCurve_swigregister = _BRepAdaptor.BRepAdaptor_CompCurve_swigregister
BRepAdaptor_CompCurve_swigregister(BRepAdaptor_CompCurve)

class BRepAdaptor_Curve(OCC.Adaptor3d.Adaptor3d_Curve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an undefined Curve with no Edge loaded.

        :rtype: None

        * Creates a Curve to acces to the geometry of edge <E>.

        :param E:
        :type E: TopoDS_Edge &
        :rtype: None

        * Creates a Curve to acces to the geometry of edge <E>. The geometry will be computed using the parametric curve of <E> on the face <F>. An Error is raised if the edge does not have a pcurve on the face.

        :param E:
        :type E: TopoDS_Edge &
        :param F:
        :type F: TopoDS_Face &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_Curve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Curve(*args))

    def Initialize(self, *args):
        """
        * Sets the Curve <self> to acces to the geometry of edge <E>.

        :param E:
        :type E: TopoDS_Edge &
        :rtype: None

        * Sets the Curve <self> to acces to the geometry of edge <E>. The geometry will be computed using the parametric curve of <E> on the face <F>. An Error is raised if the edge does not have a pcurve on the face.

        :param E:
        :type E: TopoDS_Edge &
        :param F:
        :type F: TopoDS_Face &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Initialize(self, *args)


    def Trsf(self, *args):
        """
        * Returns the coordinate system of the curve.

        :rtype: gp_Trsf

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Trsf(self, *args)


    def Is3DCurve(self, *args):
        """
        * Returns True if the edge geometry is computed from a 3D curve.

        :rtype: bool

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Is3DCurve(self, *args)


    def IsCurveOnSurface(self, *args):
        """
        * Returns True if the edge geometry is computed from a pcurve on a surface.

        :rtype: bool

        """
        return _BRepAdaptor.BRepAdaptor_Curve_IsCurveOnSurface(self, *args)


    def Curve(self, *args):
        """
        * Returns the Curve of the edge.

        :rtype: GeomAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Curve(self, *args)


    def CurveOnSurface(self, *args):
        """
        * Returns the CurveOnSurface of the edge.

        :rtype: Adaptor3d_CurveOnSurface

        """
        return _BRepAdaptor.BRepAdaptor_Curve_CurveOnSurface(self, *args)


    def Edge(self, *args):
        """
        * Returns the edge.

        :rtype: TopoDS_Edge

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Edge(self, *args)


    def Tolerance(self, *args):
        """
        * Returns the edge tolerance.

        :rtype: float

        """
        return _BRepAdaptor.BRepAdaptor_Curve_Tolerance(self, *args)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Curve
BRepAdaptor_Curve.Initialize = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Initialize, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.Trsf = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Trsf, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.Is3DCurve = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Is3DCurve, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.IsCurveOnSurface = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_IsCurveOnSurface, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.Curve = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Curve, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.CurveOnSurface = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_CurveOnSurface, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.Edge = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Edge, None, BRepAdaptor_Curve)
BRepAdaptor_Curve.Tolerance = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve_Tolerance, None, BRepAdaptor_Curve)
BRepAdaptor_Curve_swigregister = _BRepAdaptor.BRepAdaptor_Curve_swigregister
BRepAdaptor_Curve_swigregister(BRepAdaptor_Curve)

class BRepAdaptor_Curve2d(OCC.Geom2dAdaptor.Geom2dAdaptor_Curve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an uninitialized curve2d.

        :rtype: None

        * Creates with the pcurve of <E> on <F>.

        :param E:
        :type E: TopoDS_Edge &
        :param F:
        :type F: TopoDS_Face &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_Curve2d_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Curve2d(*args))

    def Initialize(self, *args):
        """
        * Initialize with the pcurve of <E> on <F>.

        :param E:
        :type E: TopoDS_Edge &
        :param F:
        :type F: TopoDS_Face &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Curve2d_Initialize(self, *args)


    def Edge(self, *args):
        """
        * Returns the Edge.

        :rtype: TopoDS_Edge

        """
        return _BRepAdaptor.BRepAdaptor_Curve2d_Edge(self, *args)


    def Face(self, *args):
        """
        * Returns the Face.

        :rtype: TopoDS_Face

        """
        return _BRepAdaptor.BRepAdaptor_Curve2d_Face(self, *args)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Curve2d
BRepAdaptor_Curve2d.Initialize = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve2d_Initialize, None, BRepAdaptor_Curve2d)
BRepAdaptor_Curve2d.Edge = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve2d_Edge, None, BRepAdaptor_Curve2d)
BRepAdaptor_Curve2d.Face = new_instancemethod(_BRepAdaptor.BRepAdaptor_Curve2d_Face, None, BRepAdaptor_Curve2d)
BRepAdaptor_Curve2d_swigregister = _BRepAdaptor.BRepAdaptor_Curve2d_swigregister
BRepAdaptor_Curve2d_swigregister(BRepAdaptor_Curve2d)

class BRepAdaptor_HArray1OfCurve(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :param Low:
        :type Low: int
        :param Up:
        :type Up: int
        :rtype: None

        :param Low:
        :type Low: int
        :param Up:
        :type Up: int
        :param V:
        :type V: BRepAdaptor_Curve &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_HArray1OfCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HArray1OfCurve(*args))

    def Init(self, *args):
        """
        :param V:
        :type V: BRepAdaptor_Curve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Init(self, *args)


    def Length(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Length(self, *args)


    def Lower(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Lower(self, *args)


    def Upper(self, *args):
        """
        :rtype: int

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Upper(self, *args)


    def SetValue(self, *args):
        """
        :param Index:
        :type Index: int
        :param Value:
        :type Value: BRepAdaptor_Curve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_SetValue(self, *args)


    def Value(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: BRepAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Value(self, *args)


    def ChangeValue(self, *args):
        """
        :param Index:
        :type Index: int
        :rtype: BRepAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_ChangeValue(self, *args)


    def Array1(self, *args):
        """
        :rtype: BRepAdaptor_Array1OfCurve

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_Array1(self, *args)


    def ChangeArray1(self, *args):
        """
        :rtype: BRepAdaptor_Array1OfCurve

        """
        return _BRepAdaptor.BRepAdaptor_HArray1OfCurve_ChangeArray1(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_BRepAdaptor_HArray1OfCurve(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HArray1OfCurve
BRepAdaptor_HArray1OfCurve.Init = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Init, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.Length = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Length, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.Lower = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Lower, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.Upper = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Upper, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.SetValue = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_SetValue, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.Value = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Value, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.ChangeValue = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_ChangeValue, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.Array1 = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_Array1, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve.ChangeArray1 = new_instancemethod(_BRepAdaptor.BRepAdaptor_HArray1OfCurve_ChangeArray1, None, BRepAdaptor_HArray1OfCurve)
BRepAdaptor_HArray1OfCurve_swigregister = _BRepAdaptor.BRepAdaptor_HArray1OfCurve_swigregister
BRepAdaptor_HArray1OfCurve_swigregister(BRepAdaptor_HArray1OfCurve)

class Handle_BRepAdaptor_HArray1OfCurve(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_swiginit(self, _BRepAdaptor.new_Handle_BRepAdaptor_HArray1OfCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_DownCast)
    __swig_destroy__ = _BRepAdaptor.delete_Handle_BRepAdaptor_HArray1OfCurve
Handle_BRepAdaptor_HArray1OfCurve.Nullify = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_Nullify, None, Handle_BRepAdaptor_HArray1OfCurve)
Handle_BRepAdaptor_HArray1OfCurve.IsNull = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_IsNull, None, Handle_BRepAdaptor_HArray1OfCurve)
Handle_BRepAdaptor_HArray1OfCurve.GetObject = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_GetObject, None, Handle_BRepAdaptor_HArray1OfCurve)
Handle_BRepAdaptor_HArray1OfCurve_swigregister = _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_swigregister
Handle_BRepAdaptor_HArray1OfCurve_swigregister(Handle_BRepAdaptor_HArray1OfCurve)

def Handle_BRepAdaptor_HArray1OfCurve_DownCast(AnObject):
    return _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_DownCast(AnObject)
Handle_BRepAdaptor_HArray1OfCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HArray1OfCurve_DownCast

class BRepAdaptor_HCompCurve(OCC.Adaptor3d.Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: BRepAdaptor_CompCurve &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_HCompCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCompCurve(*args))

    def Set(self, *args):
        """
        :param C:
        :type C: BRepAdaptor_CompCurve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HCompCurve_Set(self, *args)


    def ChangeCurve(self, *args):
        """
        :rtype: BRepAdaptor_CompCurve

        """
        return _BRepAdaptor.BRepAdaptor_HCompCurve_ChangeCurve(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_BRepAdaptor_HCompCurve(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCompCurve
BRepAdaptor_HCompCurve.Set = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCompCurve_Set, None, BRepAdaptor_HCompCurve)
BRepAdaptor_HCompCurve.ChangeCurve = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCompCurve_ChangeCurve, None, BRepAdaptor_HCompCurve)
BRepAdaptor_HCompCurve_swigregister = _BRepAdaptor.BRepAdaptor_HCompCurve_swigregister
BRepAdaptor_HCompCurve_swigregister(BRepAdaptor_HCompCurve)

class Handle_BRepAdaptor_HCompCurve(OCC.Adaptor3d.Handle_Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_swiginit(self, _BRepAdaptor.new_Handle_BRepAdaptor_HCompCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_BRepAdaptor.Handle_BRepAdaptor_HCompCurve_DownCast)
    __swig_destroy__ = _BRepAdaptor.delete_Handle_BRepAdaptor_HCompCurve
Handle_BRepAdaptor_HCompCurve.Nullify = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCompCurve_Nullify, None, Handle_BRepAdaptor_HCompCurve)
Handle_BRepAdaptor_HCompCurve.IsNull = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCompCurve_IsNull, None, Handle_BRepAdaptor_HCompCurve)
Handle_BRepAdaptor_HCompCurve.GetObject = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCompCurve_GetObject, None, Handle_BRepAdaptor_HCompCurve)
Handle_BRepAdaptor_HCompCurve_swigregister = _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_swigregister
Handle_BRepAdaptor_HCompCurve_swigregister(Handle_BRepAdaptor_HCompCurve)

def Handle_BRepAdaptor_HCompCurve_DownCast(AnObject):
    return _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_DownCast(AnObject)
Handle_BRepAdaptor_HCompCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCompCurve_DownCast

class BRepAdaptor_HCurve(OCC.Adaptor3d.Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: BRepAdaptor_Curve &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_HCurve_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCurve(*args))

    def Set(self, *args):
        """
        :param C:
        :type C: BRepAdaptor_Curve &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HCurve_Set(self, *args)


    def ChangeCurve(self, *args):
        """
        :rtype: BRepAdaptor_Curve

        """
        return _BRepAdaptor.BRepAdaptor_HCurve_ChangeCurve(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_BRepAdaptor_HCurve(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCurve
BRepAdaptor_HCurve.Set = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCurve_Set, None, BRepAdaptor_HCurve)
BRepAdaptor_HCurve.ChangeCurve = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCurve_ChangeCurve, None, BRepAdaptor_HCurve)
BRepAdaptor_HCurve_swigregister = _BRepAdaptor.BRepAdaptor_HCurve_swigregister
BRepAdaptor_HCurve_swigregister(BRepAdaptor_HCurve)

class Handle_BRepAdaptor_HCurve(OCC.Adaptor3d.Handle_Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.Handle_BRepAdaptor_HCurve_swiginit(self, _BRepAdaptor.new_Handle_BRepAdaptor_HCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve_DownCast)
    __swig_destroy__ = _BRepAdaptor.delete_Handle_BRepAdaptor_HCurve
Handle_BRepAdaptor_HCurve.Nullify = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve_Nullify, None, Handle_BRepAdaptor_HCurve)
Handle_BRepAdaptor_HCurve.IsNull = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve_IsNull, None, Handle_BRepAdaptor_HCurve)
Handle_BRepAdaptor_HCurve.GetObject = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve_GetObject, None, Handle_BRepAdaptor_HCurve)
Handle_BRepAdaptor_HCurve_swigregister = _BRepAdaptor.Handle_BRepAdaptor_HCurve_swigregister
Handle_BRepAdaptor_HCurve_swigregister(Handle_BRepAdaptor_HCurve)

def Handle_BRepAdaptor_HCurve_DownCast(AnObject):
    return _BRepAdaptor.Handle_BRepAdaptor_HCurve_DownCast(AnObject)
Handle_BRepAdaptor_HCurve_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCurve_DownCast

class BRepAdaptor_HCurve2d(OCC.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: BRepAdaptor_Curve2d &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_HCurve2d_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HCurve2d(*args))

    def Set(self, *args):
        """
        :param C:
        :type C: BRepAdaptor_Curve2d &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HCurve2d_Set(self, *args)


    def ChangeCurve2d(self, *args):
        """
        :rtype: BRepAdaptor_Curve2d

        """
        return _BRepAdaptor.BRepAdaptor_HCurve2d_ChangeCurve2d(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_BRepAdaptor_HCurve2d(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HCurve2d
BRepAdaptor_HCurve2d.Set = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCurve2d_Set, None, BRepAdaptor_HCurve2d)
BRepAdaptor_HCurve2d.ChangeCurve2d = new_instancemethod(_BRepAdaptor.BRepAdaptor_HCurve2d_ChangeCurve2d, None, BRepAdaptor_HCurve2d)
BRepAdaptor_HCurve2d_swigregister = _BRepAdaptor.BRepAdaptor_HCurve2d_swigregister
BRepAdaptor_HCurve2d_swigregister(BRepAdaptor_HCurve2d)

class Handle_BRepAdaptor_HCurve2d(OCC.Adaptor2d.Handle_Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_swiginit(self, _BRepAdaptor.new_Handle_BRepAdaptor_HCurve2d(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve2d_DownCast)
    __swig_destroy__ = _BRepAdaptor.delete_Handle_BRepAdaptor_HCurve2d
Handle_BRepAdaptor_HCurve2d.Nullify = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve2d_Nullify, None, Handle_BRepAdaptor_HCurve2d)
Handle_BRepAdaptor_HCurve2d.IsNull = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve2d_IsNull, None, Handle_BRepAdaptor_HCurve2d)
Handle_BRepAdaptor_HCurve2d.GetObject = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HCurve2d_GetObject, None, Handle_BRepAdaptor_HCurve2d)
Handle_BRepAdaptor_HCurve2d_swigregister = _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_swigregister
Handle_BRepAdaptor_HCurve2d_swigregister(Handle_BRepAdaptor_HCurve2d)

def Handle_BRepAdaptor_HCurve2d_DownCast(AnObject):
    return _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_DownCast(AnObject)
Handle_BRepAdaptor_HCurve2d_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HCurve2d_DownCast

class BRepAdaptor_HSurface(OCC.Adaptor3d.Adaptor3d_HSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param S:
        :type S: BRepAdaptor_Surface &
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_HSurface_swiginit(self, _BRepAdaptor.new_BRepAdaptor_HSurface(*args))

    def Set(self, *args):
        """
        :param S:
        :type S: BRepAdaptor_Surface &
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_HSurface_Set(self, *args)


    def ChangeSurface(self, *args):
        """
        :rtype: BRepAdaptor_Surface

        """
        return _BRepAdaptor.BRepAdaptor_HSurface_ChangeSurface(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_BRepAdaptor_HSurface(self)
            self.thisown = False
            return self.thisHandle

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_HSurface
BRepAdaptor_HSurface.Set = new_instancemethod(_BRepAdaptor.BRepAdaptor_HSurface_Set, None, BRepAdaptor_HSurface)
BRepAdaptor_HSurface.ChangeSurface = new_instancemethod(_BRepAdaptor.BRepAdaptor_HSurface_ChangeSurface, None, BRepAdaptor_HSurface)
BRepAdaptor_HSurface_swigregister = _BRepAdaptor.BRepAdaptor_HSurface_swigregister
BRepAdaptor_HSurface_swigregister(BRepAdaptor_HSurface)

class Handle_BRepAdaptor_HSurface(OCC.Adaptor3d.Handle_Adaptor3d_HSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _BRepAdaptor.Handle_BRepAdaptor_HSurface_swiginit(self, _BRepAdaptor.new_Handle_BRepAdaptor_HSurface(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_BRepAdaptor.Handle_BRepAdaptor_HSurface_DownCast)
    __swig_destroy__ = _BRepAdaptor.delete_Handle_BRepAdaptor_HSurface
Handle_BRepAdaptor_HSurface.Nullify = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HSurface_Nullify, None, Handle_BRepAdaptor_HSurface)
Handle_BRepAdaptor_HSurface.IsNull = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HSurface_IsNull, None, Handle_BRepAdaptor_HSurface)
Handle_BRepAdaptor_HSurface.GetObject = new_instancemethod(_BRepAdaptor.Handle_BRepAdaptor_HSurface_GetObject, None, Handle_BRepAdaptor_HSurface)
Handle_BRepAdaptor_HSurface_swigregister = _BRepAdaptor.Handle_BRepAdaptor_HSurface_swigregister
Handle_BRepAdaptor_HSurface_swigregister(Handle_BRepAdaptor_HSurface)

def Handle_BRepAdaptor_HSurface_DownCast(AnObject):
    return _BRepAdaptor.Handle_BRepAdaptor_HSurface_DownCast(AnObject)
Handle_BRepAdaptor_HSurface_DownCast = _BRepAdaptor.Handle_BRepAdaptor_HSurface_DownCast

class BRepAdaptor_Surface(OCC.Adaptor3d.Adaptor3d_Surface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an undefined surface with no face loaded.

        :rtype: None

        * Creates a surface to access the geometry of <F>. If <Restriction> is true the parameter range is the parameter range in the UV space of the restriction.

        :param F:
        :type F: TopoDS_Face &
        :param R: default value is Standard_True
        :type R: bool
        :rtype: None

        """
        _BRepAdaptor.BRepAdaptor_Surface_swiginit(self, _BRepAdaptor.new_BRepAdaptor_Surface(*args))

    def Initialize(self, *args):
        """
        * Sets the surface to the geometry of <F>.

        :param F:
        :type F: TopoDS_Face &
        :param Restriction: default value is Standard_True
        :type Restriction: bool
        :rtype: None

        """
        return _BRepAdaptor.BRepAdaptor_Surface_Initialize(self, *args)


    def Surface(self, *args):
        """
        * Returns the surface.

        :rtype: GeomAdaptor_Surface

        """
        return _BRepAdaptor.BRepAdaptor_Surface_Surface(self, *args)


    def ChangeSurface(self, *args):
        """
        * Returns the surface.

        :rtype: GeomAdaptor_Surface

        """
        return _BRepAdaptor.BRepAdaptor_Surface_ChangeSurface(self, *args)


    def Trsf(self, *args):
        """
        * Returns the surface coordinate system.

        :rtype: gp_Trsf

        """
        return _BRepAdaptor.BRepAdaptor_Surface_Trsf(self, *args)


    def Face(self, *args):
        """
        * Returns the face.

        :rtype: TopoDS_Face

        """
        return _BRepAdaptor.BRepAdaptor_Surface_Face(self, *args)


    def Tolerance(self, *args):
        """
        * Returns the face tolerance.

        :rtype: float

        """
        return _BRepAdaptor.BRepAdaptor_Surface_Tolerance(self, *args)

    __swig_destroy__ = _BRepAdaptor.delete_BRepAdaptor_Surface
BRepAdaptor_Surface.Initialize = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_Initialize, None, BRepAdaptor_Surface)
BRepAdaptor_Surface.Surface = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_Surface, None, BRepAdaptor_Surface)
BRepAdaptor_Surface.ChangeSurface = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_ChangeSurface, None, BRepAdaptor_Surface)
BRepAdaptor_Surface.Trsf = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_Trsf, None, BRepAdaptor_Surface)
BRepAdaptor_Surface.Face = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_Face, None, BRepAdaptor_Surface)
BRepAdaptor_Surface.Tolerance = new_instancemethod(_BRepAdaptor.BRepAdaptor_Surface_Tolerance, None, BRepAdaptor_Surface)
BRepAdaptor_Surface_swigregister = _BRepAdaptor.BRepAdaptor_Surface_swigregister
BRepAdaptor_Surface_swigregister(BRepAdaptor_Surface)



