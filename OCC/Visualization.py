# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _Visualization.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Visualization', [dirname(__file__)])
        except ImportError:
            import _Visualization
            return _Visualization
        if fp is not None:
            try:
                _mod = imp.load_module('_Visualization', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Visualization = swig_import_helper()
    del swig_import_helper
else:
    import _Visualization
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



_Visualization.atCube_swigconstant(_Visualization)
atCube = _Visualization.atCube

_Visualization.atNormal_swigconstant(_Visualization)
atNormal = _Visualization.atNormal

_Visualization.atNormalAutoScale_swigconstant(_Visualization)
atNormalAutoScale = _Visualization.atNormalAutoScale
class Tesselator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Visualization.Tesselator_swiginit(self, _Visualization.new_Tesselator(*args))
    __swig_destroy__ = _Visualization.delete_Tesselator
Tesselator.GetVertex = new_instancemethod(_Visualization.Tesselator_GetVertex, None, Tesselator)
Tesselator.GetNormal = new_instancemethod(_Visualization.Tesselator_GetNormal, None, Tesselator)
Tesselator.GetTriangleIndex = new_instancemethod(_Visualization.Tesselator_GetTriangleIndex, None, Tesselator)
Tesselator.GetEdgeVertex = new_instancemethod(_Visualization.Tesselator_GetEdgeVertex, None, Tesselator)
Tesselator.VerticesList = new_instancemethod(_Visualization.Tesselator_VerticesList, None, Tesselator)
Tesselator.ObjGetTriangleCount = new_instancemethod(_Visualization.Tesselator_ObjGetTriangleCount, None, Tesselator)
Tesselator.ObjGetVertexCount = new_instancemethod(_Visualization.Tesselator_ObjGetVertexCount, None, Tesselator)
Tesselator.ObjGetNormalCount = new_instancemethod(_Visualization.Tesselator_ObjGetNormalCount, None, Tesselator)
Tesselator.ObjGetEdgeCount = new_instancemethod(_Visualization.Tesselator_ObjGetEdgeCount, None, Tesselator)
Tesselator.ObjEdgeGetVertexCount = new_instancemethod(_Visualization.Tesselator_ObjEdgeGetVertexCount, None, Tesselator)
Tesselator.ExportShapeToX3DIndexedFaceSet = new_instancemethod(_Visualization.Tesselator_ExportShapeToX3DIndexedFaceSet, None, Tesselator)
Tesselator.ExportShapeToThreejs = new_instancemethod(_Visualization.Tesselator_ExportShapeToThreejs, None, Tesselator)
Tesselator.ExportShapeToX3D = new_instancemethod(_Visualization.Tesselator_ExportShapeToX3D, None, Tesselator)
Tesselator.SetDeviation = new_instancemethod(_Visualization.Tesselator_SetDeviation, None, Tesselator)
Tesselator_swigregister = _Visualization.Tesselator_swigregister
Tesselator_swigregister(Tesselator)

class Display3d(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(Display3d self) -> Display3d"""
        _Visualization.Display3d_swiginit(self, _Visualization.new_Display3d())
    __swig_destroy__ = _Visualization.delete_Display3d

    def Init(self, handle):
        """Init(Display3d self, long const handle)"""
        return _Visualization.Display3d_Init(self, handle)


    def GetView(self):
        """GetView(Display3d self) -> Handle_V3d_View &"""
        return _Visualization.Display3d_GetView(self)


    def GetViewer(self):
        """GetViewer(Display3d self) -> Handle_V3d_Viewer &"""
        return _Visualization.Display3d_GetViewer(self)


    def GetContext(self):
        """GetContext(Display3d self) -> Handle_AIS_InteractiveContext"""
        return _Visualization.Display3d_GetContext(self)


    def Test(self):
        """Test(Display3d self)"""
        return _Visualization.Display3d_Test(self)

Display3d.Init = new_instancemethod(_Visualization.Display3d_Init, None, Display3d)
Display3d.GetView = new_instancemethod(_Visualization.Display3d_GetView, None, Display3d)
Display3d.GetViewer = new_instancemethod(_Visualization.Display3d_GetViewer, None, Display3d)
Display3d.GetContext = new_instancemethod(_Visualization.Display3d_GetContext, None, Display3d)
Display3d.Test = new_instancemethod(_Visualization.Display3d_Test, None, Display3d)
Display3d_swigregister = _Visualization.Display3d_swigregister
Display3d_swigregister(Display3d)


