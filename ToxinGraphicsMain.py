# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:02:14 2017

@author: Rowan
"""


from Bio.SeqFeature import SeqFeature, FeatureLocation
import numpy as np
from Bio import SeqIO
from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram

class PhyloGraph:
    """ Class containing elements for the graphical representation of toxin genomes """
    
    def __init__(self,name):
        """ Creates a new ToxinGraphics object containing a new GenomeDiagram with a single track and feature set """
        ### May be worth just creating an object and then applying the methods to it within event handlers etc
        self.name = name
        self.record = None
        self.gd_diagram = GenomeDiagram.Diagram(name)
        self.gd_track_for_features = self.gd_diagram.new_track(1, name="Annotated Features")
        self.gd_feature_set = self.gd_track_for_features.new_set()

        
    def read_from_file(self, filename, filetype):
        """ Reads a SeqRecord object from a given file """
        self.record = SeqIO.read(filename, filetype)
                              
    ### Add a read_from_database function etc
        
    def add_features(self):
        """ Annotates the existing features in the SeqRecord object """
        ### Again may be worth changing for better functionality given the ability to view one or more GenomeDiagrams
        for feature in self.record.features:
            if feature.type != "CDS":
                continue
            if len(self.gd_feature_set) % 2 ==0:
                color = colors.blue
            else: 
                color = colors.lightblue
            self.gd_feature_set.add_feature(feature, color=color, label = True)
            
    def tdraw(self, style = "linear", fragments = 1):
        """ 
        Draws the Genome Diagram with given fragments works with both single and mutliple genomes 
        takes default values for linear genomes depending on how many are currently stored in the genome set
        can change to be circular
        """

        if style == "linear":
            self.gd_diagram.draw(format = style, orientation = "landscape", pagesize = "A4",fragments = fragments, start = 0, end = len(self.record))
        else:
            self.gd_diagram.draw(format = style, circular = True, pagesize = (20*cm,20*cm), start = 0, end = len(self.record), circle_core = 0.7)
            
    def write_to_file(self,filename, filetype, style = "linear", fragments = 1):
        """ Writes the GenomeDiagram to a file """
        self.tdraw(style, fragments)
        self.gd_diagram.write(filename, filetype)
        
    def create_feature(self, name, start, end, strand):
        """ adds a feature to the existing genome diagram """
        ### does not have any functionality for the multiple genome diagrams
        seq_feature = SeqFeature(FeatureLocation(start, end), strand = strand)
        self.gd_feature_set.add_feature(seq_feature, name = name, label = True)      
        
    def remove_feature(self, featureid):
        """ removes a feature from the existing genome diagram """
        ### does not have any functionality for the multiple genome diagrams
        self.gd_feature_set.del_feature(featureid)
    
    def get_features(self):
        """ returns a list of all feature names in order of ids"""
        featurelst = []
        for c in self.gd_feature_set.get_ids():
            featurelst.append(self.gd_feature_set.__getitem__(c).name)
        return featurelst
    
            
class MultiplePhyloGraph(PhyloGraph):
    
    """ Subclass of PhyloGraph that handles multiple genomes """
    
    def __init__(self, name):
        
        super(PhyloGraph,self).__init__()
        self.name = name
        self.genome_set = []
        self.max_len = 0
        self.gd_diagram = GenomeDiagram.Diagram(name)
        self.features = []
        
    def read_from_file(self, filename, filetype):
            rec = SeqIO.read(filename, filetype)
            self.genome_set.append(rec)
            self.add_features()
            
    def add_features(self):
        self.features = []
        for record in self.genome_set:
            self.max_len = max(self.max_len, len(record))
            self.gd_track_for_features = self.gd_diagram.new_track(1, name = record.name, greytrack = True, start = 0, end = len(record))
            self.gd_feature_set = self.gd_track_for_features.new_set()
            i = 0
            
            for feature in record.features:
                if feature.type != "gene":
                    continue
                self.gd_feature_set.add_feature(feature,sigil = "ARROW", label = True, name = str(i+1),label_position = "start", label_size = 6, label_angle = 0)
                i += 1
              
            self.features.append(self.gd_feature_set)
            print(len(self.features))
            
    def remove_from_multiple(self, index, featureid):
        """ removes a feature from the existing multiple genome diagram """
        #### Note, could integrate handling into remove_feature to handle all cases, or keep separate cases
        self.features[index].del_feature(featureid)

    
    def create_from_multiple(self, index, name, start, end, strand):
        """ adds a feature to the existing multiple genome diagram """
        ### Note, could integrate handling into create_feature to handle all cases, or keep separate cases
        seq_feature = SeqFeature(FeatureLocation(start, end), strand = strand)
        self.features[index].add_feature(seq_feature, name = name, label = True)     
    
    def tdraw(self, style = "linear", fragments = 1):
        self.gd_diagram = GenomeDiagram.Diagram(self.name)
        i = 0
        
        for record in self.genome_set:
            self.max_len = max(self.max_len, len(record))
            self.gd_track_for_features = self.gd_diagram.new_track(1, name = record.name, greytrack = True, start = 0, end = len(record))
            self.gd_feature_set = self.gd_track_for_features.new_set()
            for c in self.features[i].get_ids():
                j = 0
                self.gd_feature_set.add_feature(self.features[i].__getitem__(c), sigil = "ARROW", label = True, name = str(j+1), label_position = "start", label_size = 6, label_angle = 0)                
                j += 1
            i += 1
            
        self.gd_diagram.draw(format = "linear", pagesize = "A4", fragments = fragments, start = 0, end = self.max_len)
    
    def get_features(self):
        """ returns a list of all feature names in order of ids"""
        featurelst = []
        i = 0
        while i < len(self.features):
            feature_sub_list = []
            for c in self.features[i].get_ids():
                feature_sub_list.append(self.features[i].__getitem__(c).name)
            featurelst.append(feature_sub_list)
            i += 1
        return featurelst