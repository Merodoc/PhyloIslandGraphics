# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:50:44 2017

@author: Rowan
"""

from ToxinGraphicsMain import PhyloGraph, MultiplePhyloGraph

YenTC = PhyloGraph("PPT Example")
YenTC.read_from_file("sequence(2).gb", "genbank")
YenTC.create_feature("A1", 798388, 801882, 1)
YenTC.tdraw()
YenTC.write_to_file("newtest2.png","png", fragments = 10)

