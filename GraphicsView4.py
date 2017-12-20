# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:23:29 2017

@author: Rowan
"""

import wx
import os
from ToxinGraphicsMain import PhyloGraph
from Bio.Graphics import GenomeDiagram

### TODO
### Atm the on Open/View Sequence structure only works on image files which we cannot retroactively change
### need to accept in .fa or .gb files and then create the GenomeDiagram for a given fa file once it is selected
### The img of the GD needs to be saved in memory, so that when we call the add or remove feature capabilities
### it will be called on the SequenceRecord File, recreating the image in memory again and thus replacing the current image

class PhyloIslandWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname = ''
        wx.Frame.__init__(self, parent, title=title, size = (1400, 700))
        # At the moment using a text control to handle the files in the profile
        self.CreateStatusBar()       
        
        # Menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to place in profile")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EDIT, "E&xit", "Terminate the program")
        
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        
        # Menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        
        # Sequence List
        
        self.panel = Panel1(self)
        self.imagelist = []
        
        
    def OnAbout(self,e):
        # Create a message dialog box
        dlg = wx.MessageDialog(self, " Graphical toolkit for PhyloIsland profiles" , "About PhyloIsland Graphical Toolkit", wx.OK)
        dlg.ShowModal() # Shows it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self,e):
        self.Close(True)  # Close the frame.

    def OnOpen(self,e):
        """ Open a file"""
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.panel.seqList.append(self.filename)
            self.panel.editprofile.Append(self.filename)
            self.imagelist.append(self.filename)
            f.close()
        dlg.Destroy()
        


class Panel1(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.parent = parent
        # Sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainGrid = wx.GridBagSizer(hgap=5, vgap = 5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        grid = wx.GridBagSizer(hgap = 5, vgap = 5)
        self.seqList = ["No Sequence"]
        # GenomeDiagrams take up the left side of the grid
        
        self.seqImage = wx.StaticText(self, label = "Open a Sequence and it will appear here", size = (600, 600), style= wx.ALIGN_CENTER)
        #self.seqImage = wx.StaticBitmap(self, -1, wx.Bitmap("ppt_sample.png", wx.BITMAP_TYPE_ANY))
        self.mainGrid.Add(self.seqImage, pos = (0,0))
        
    
                
        self.mainGrid.Add(grid, pos = (0,1))
        hSizer.Add(self.mainGrid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        
        self.lblprofiles = wx.StaticText(self, label = 'Open a Sequence: ')
        grid.Add(self.lblprofiles, pos = (0,0))
        self.editprofile = wx.ComboBox(self, size = (95, -1), choices = self.seqList, style = wx.CB_READONLY)
        self.editprofile.SetValue(self.seqList[0])
        grid.Add(self.editprofile, pos = (0,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editprofile)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editprofile)
        
        # Add A1
        self.lbladdA1 = wx.StaticText(self, label = 'Add Feature: ')
        self.textInput = wx.TextCtrl(self, size = (95, -1), value = "Name")
        self.textInput2 = wx.TextCtrl(self, size = (95,-1), value = "Start location")
        self.textInput3 = wx.TextCtrl(self, size = (95,-1), value = "End Location")
        self.confirmbutton = wx.Button(self, label = "Confirm")
        grid.Add(self.lbladdA1, pos = (1, 0))
        grid.Add(self.textInput, pos =(1, 1))
        grid.Add(self.textInput2, pos = (1, 2))
        grid.Add(self.textInput3, pos = (1, 3))
        grid.Add(self.confirmbutton, pos = (1,4))
        
        
        # Remove Feature
        
        self.featureList = ['A1', 'A2']
        self.lblremove = wx.StaticText(self, label = 'Remove Feature: ')
        grid.Add(self.lblremove, pos = (2,0))
        self.removefeature = wx.TextCtrl(self, size = (95, -1), value = "Name")
        self.removebutton = wx.Button(self, label = "Confirm")
        grid.Add(self.removefeature, pos = (2, 1))
        grid.Add(self.removebutton, pos = (2, 2))
        
               
    # Event handlers
        
    def EvtComboBox(self, event):
        # Atm only works on list indexes
        if event.GetString() == "No Sequence":
             self.seqImage2 = wx.StaticText(self, label = "Open a Sequence and it will appear here", size = (600, 600), style= (wx.ALIGN_CENTER))   
        else:
            self.seqImage2 = wx.StaticBitmap(self, -1, wx.Bitmap(event.GetString(), wx.BITMAP_TYPE_ANY))
        self.seqImage.Destroy()
        self.mainGrid.Add(self.seqImage2, pos = (0,0)   )
        self.Layout()
        self.seqImage = self.seqImage2
        
        return None
    def EvtText(self, event):
        return None

    def GetSeqList(self):
        return self.seqList
        
app = wx.App(False)
frame = PhyloIslandWindow(None, "PhyloIsland Graphical Toolkit")
#nb = wx.Notebook(frame)
#nb.AddPage(Panel1(nb),"Panel 1")
frame.Show()
app.MainLoop()
        


        
        