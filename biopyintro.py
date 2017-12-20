# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:27:37 2017

@author: Rowan
"""

import Bio as bio
import numpy as np
from Bio import SeqIO
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram

record = SeqIO.read("NC_005816.gb","genbank")

#Top Down Approach - create an empty diagram, then add stuff to the 

gd_diagram = GenomeDiagram.Diagram("Yersinia pestis biovar Microtus plasmid pPCP1")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue
    gd_feature_set.add_feature(feature, color=color, label = True)
    
gd_diagram.draw(format = "linear",orientation="landscape",pagesize='A4', fragments=4, start=0,end=len(record))
gd_diagram.write("plasmid_linear3.pdf","PDF")
gd_diagram.write("plasmid_linear.eps","EPS")
gd_diagram.write("plasmid_linear.svg","SVG")

#Bottom Down Approach - Create objects then combine them

#Create the feature set and its feature objects
gd_feature_set2 = GenomeDiagram.FeatureSet()
for feature in  record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set2) % 2 == 0:
        color = colors.blue
    else:
        color = colors.lightblue
    gd_feature_set2.add_feature(feature, color=color, label = True)
    
#Create a track, and a diagram
gd_track_for_features = GenomeDiagram.Track(name="Annotated Features")
gd_diagram = GenomeDiagram.Diagram("Yersinia pestis biovar Microtus plasmid pPCP1")

#Now have to glue the bits together...

gd_track_for_features.add_set(gd_feature_set)
gd_diagram.add_track(gd_track_for_features,1)
gd_diagram.draw(format = "linear",orientation="landscape",pagesize='A4', fragments=1, start=0,end=len(record))
gd_diagram.write("plasmid_linear4.pdf","PDF")

