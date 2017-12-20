# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 16:34:10 2017

@author: Rowan
"""

from Bio import GenBank
from Bio.Graphics import GenomeDiagram
gdd = GenomeDiagram.Diagram('NC_002703.gbk')
gdt1 =  gdd.new_track(2, greytrack =1, name = 'CDS features')
gdt2 = gdd.new_track(4, greytrack = 1, name = 'GC Content')
gdfs = gdt1.new_set('feature')
gdgs = gdt2.new_set('graph')

parser = GenBank.FeatureParser()
fhandle = open('Yersinia_entomophaga_protein.faa','r')
genbank_entry = parser.parse(fhandle)
for feature in genbank_entry.features:
    if feature.type == 'CDS':
        gdfs.add_feature(feature)

gdd.draw(format = 'linear', orientation = 'landscape', tracklines = 0, pagesize = 'A5', fragments = 5, circular = 0)
gdd.write('NC_005213.png','PNG')
