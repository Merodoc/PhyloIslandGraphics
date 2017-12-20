# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:02:14 2017

@author: Rowan
"""

class ToxinGraphics:
    """ Class containing elements for the graphical representation of toxin genomes """
    def __init__(self,name):
        self.name = name
        self.record = None
        self.gd_diagram = GenomeDiagram.Diagram(name)
        self.gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
        self.gd_feature_set = gd_track_for_feature.new_set()
        
    def read_from_file(self, filename, filetype):
        self.record = SeqIO.read(filename, filetype)
        
    def add_features(self):
        for feature in self.record.features:
            if feature.type != "gene":
                continue
            if len(gd_feature_set) % 2 ==0:
                color = colors.blue
            else: 
                color = colors.lightblue
            self.gd_feature_set.add_feature(feature, color=color, label = True)
            
    def tdraw(self, style, fragments):
        self.gd_diagram.draw(format = style, orientation = "landscape", pagesize = "A4",fragments = fragments, start = 0, end = len(record))
    
    def write_to_file(self,filename, filetype, style, fragments):
        self.tdraw(style, fragments)
        self.gd_diagram.write(filename, filetype)
        
        