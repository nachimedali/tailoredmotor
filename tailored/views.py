from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from OCC.STEPControl import STEPControl_Reader, STEPControl_Writer, STEPControl_AsIs
from OCC.Display.WebGl import x3dom_renderer
from wsgiref.util import FileWrapper
from django.http import HttpResponse
from OCC.BRepAlgoAPI import BRepAlgoAPI_Fuse, BRepAlgoAPI_Cut
from OCC.AIS import AIS_MultipleConnectedInteractive, AIS_Shape
from OCC.TopoDS import TopoDS_Shape
from OCC.Display.SimpleGui import *
from OCC.gp import gp_Ax1, gp_Pnt, gp_Dir, gp_Trsf, gp_Vec
from OCC.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Interface import Interface_Static_SetCVal
from OCC.IFSelect import IFSelect_RetDone
from OCC.BRepPrimAPI import BRepPrimAPI_MakeCylinder

import json
from math import pi

from .models import updat

# Create your views here.

def home(request):
		
	context = {}
	template = "index.html"
	return render(request, template, context)

# Dm: Diameter Motor in [4,20]
# Lm: Length Motor in [0,5*Dm, 4*Dm]
# Ds: Diameter Shaft in [4, 10]
# Dt: Diamater thread M2 = 2 
# Dc: Diamater centering in [4*Ds, Dm- 3Dt]
# Dp: Diamater pitch in [Dc + 2Dt, Dm - 2Dt]
# Ls : Length shaft in [10, Lm]
# Lc = 5

def build_solid(Dm, Lm, Ds, Dt, Dc, Dp, Ls, Lc):
	my_renderer = x3dom_renderer.X3DomRenderer()

	center = BRepPrimAPI_MakeCylinder(Dm/2, Lm).Shape()

	trou = BRepPrimAPI_MakeCylinder(Dt/2, 5).Shape()
	tr = gp_Trsf()
	tr.SetTranslation(gp_Vec(0,Dm/2 -4,-2))
	gen_3 = BRepBuilderAPI_Transform(trou, tr).Shape()
	result = BRepAlgoAPI_Cut(center, gen_3).Shape()

	tr.SetTranslation(gp_Vec(Dm/2 -4,0,-2))
	gen_3 = BRepBuilderAPI_Transform(trou, tr).Shape()
	result = BRepAlgoAPI_Cut(result, gen_3).Shape()
	tr.SetTranslation(gp_Vec(-Dm/2 +4,0,-2))
	gen_3 = BRepBuilderAPI_Transform(trou, tr).Shape()
	result = BRepAlgoAPI_Cut(result, gen_3).Shape()
	tr.SetTranslation(gp_Vec(0,-Dm/2 +4,-2))
	gen_3 = BRepBuilderAPI_Transform(trou, tr).Shape()
	result = BRepAlgoAPI_Cut(result, gen_3).Shape()

	cyl_2 = BRepPrimAPI_MakeCylinder(Dc/ 2, Lc).Shape()
	trns = gp_Trsf()
	trns.SetTranslation(gp_Vec(0,0,-Lc))
		
	gen_2 = BRepBuilderAPI_Transform(cyl_2, trns).Shape()
	result = BRepAlgoAPI_Fuse(result, gen_2).Shape()


	rou = BRepPrimAPI_MakeCylinder(Ds / 2, Ls).Shape()
	trns = gp_Trsf()
	trns.SetTranslation(gp_Vec(0,0,-Ls))

	gen_3 = BRepBuilderAPI_Transform(rou, trns).Shape()

	result = BRepAlgoAPI_Fuse(result, gen_3).Shape()

	dis = my_renderer.DisplayShape(result)
	return dis

def design(request):
	if request.method == 'POST':
		Dm = int(request.POST.get("Dm"))
		Lm = int(request.POST.get("Lm"))
		Ds = int(request.POST.get("Ds"))
		Dt = int(request.POST.get("Dt"))
		Dc = int(request.POST.get("Dc"))
		Dp = int(request.POST.get("Dp"))
		Ls = int(request.POST.get("Ls"))
		Lc = 5
		dis = build_solid(Dm, Lm, Ds, Dt, Dc, Dp, Ls, Lc)
		form = updat()
		data = {'Dm': Dm, 'Lm':Lm, 'Ds': Ds, 'Dt':Dt, 'Dc':Dc, 'Dp':Dp, 'Ls':Ls, 'Lc':Lc}
		context = {"dis": dis,"form" : form, "data":data,}
		template = "design.html"
		return render(request, template, context)
	else:
		# Diameter Motor in [4,20]
		Dm = 120
		# Length Motor in [0,5*Dm, 4*Dm]
		Lm = 270
		# Diameter Shaft in [4, 10]
		Ds = 7
		# Diamater thread M2 = 2 
		Dt = 2
		# Diamater centering in [4*Ds, Dm- 3Dt]
		Dc = (4*Ds + Dm- 3*Dt) / 2
		# Diamater pitch in [Dc + 2Dt, Dm - 2Dt]
		Dp = (Dc + 2*Dt + Dm - 2*Dt) / 2
		# Length shaft in [10, Lm]
		Ls = (10 + Lm) / 2
		Lc = 5

		dis = build_solid(Dm, Lm, Ds, Dt, Dc, Dp, Ls, Lc)
		form = updat()
		data = {'Dm': Dm, 'Lm':Lm, 'Ds': Ds, 'Dt':Dt, 'Dc':Dc, 'Dp':Dp, 'Ls':Ls, 'Lc':Lc}
		context = {"dis": dis,"form" : form, "data":data,}
		template = "design.html"
		return render(request, template, context)
