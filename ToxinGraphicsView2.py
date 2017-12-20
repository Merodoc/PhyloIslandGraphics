# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:23:29 2017

@author: Rowan
"""

import wx
import os
from ToxinGraphicsMain import PhyloGraph
from Bio.Graphics import GenomeDiagram


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
        self.seqList = []
        
        
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
            self.seqList.append(self.filename)
            f.close()
        dlg.Destroy()
        
    def GetSeqList(self):
        return self.seqList

class Panel1(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        self.parent = parent
        self.seqList = parent.GetSeqList()
        # Sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainGrid = wx.GridBagSizer(hgap=5, vgap = 5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        grid = wx.GridBagSizer(hgap = 5, vgap = 5)
        # GenomeDiagrams take up the left side of the grid
        
        #self.seqImage = wx.StaticText(self, label = "Open a Sequence and it will appear here", size = (600, 600), style= wx.ALIGN_CENTER)
        self.seqImage = wx.StaticBitmap(self, -1, wx.Bitmap("ppt_sample.png", wx.BITMAP_TYPE_ANY))
        mainGrid.Add(self.seqImage, pos = (0,0))
        
    
                
        mainGrid.Add(grid, pos = (0,1))
        hSizer.Add(mainGrid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
        self.profileList = frame.GetSeqList()
        
        self.lblprofiles = wx.StaticText(self, label = 'Open a Sequence: ')
        grid.Add(self.lblprofiles, pos = (0,0))
        self.editprofile = wx.ComboBox(self, size = (95, -1), choices = self.profileList, style = wx.CB_DROPDOWN)
        grid.Add(self.editprofile, pos = (0,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.editprofile)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editprofile)
        
        # Add A1
        self.lbladdA1 = wx.StaticText(self, label = 'Add A1: ')
        self.textInput = wx.TextCtrl(self, size = (95,-1), value = "Start location")
        self.textInput2 = wx.TextCtrl(self, size = (95,-1), value = "End Location")
        self.confirmbutton = wx.Button(self, label = "Confirm")
        grid.Add(self.lbladdA1, pos = (1, 0))
        grid.Add(self.textInput, pos =(1, 1))
        grid.Add(self.textInput2, pos = (1, 2))
        grid.Add(self.confirmbutton, pos = (1,3))
        
        # Add A2

        self.lbladdA2 = wx.StaticText(self, label = 'Add A2: ')
        self.textInput3 = wx.TextCtrl(self, size = (95,-1), value = "Start location")
        self.textInput4 = wx.TextCtrl(self, size = (95,-1), value = "End Location")
        self.confirmbutton2 = wx.Button(self, label = "Confirm")
        grid.Add(self.lbladdA2, pos = (2, 0))
        grid.Add(self.textInput3, pos =(2, 1))
        grid.Add(self.textInput4, pos = (2, 2))
        grid.Add(self.confirmbutton2, pos = (2,3))
        
        # Remove Feature
        
        self.featureList = ['A1', 'A2']
        self.lblremove = wx.StaticText(self, label = 'Remove Feature: ')
        grid.Add(self.lblremove, pos = (3,0))
        self.removefeature = wx.ComboBox(self, size = (95, -1), choices = self.featureList, style = wx.CB_DROPDOWN)
        grid.Add(self.removefeature, pos = (3, 1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.removefeature)
        self.Bind(wx.EVT_TEXT, self.EvtText, self.removefeature)
        
               
    # Event handlers
        
    def EvtComboBox(self, event):
        return None
    def EvtText(self, event):
        return None

        
app = wx.App(False)
frame = PhyloIslandWindow(None, "PhyloIsland Graphical Toolkit")
#nb = wx.Notebook(frame)
#nb.AddPage(Panel1(nb),"Panel 1")
panel = Panel1(frame)
frame.Show()
app.MainLoop()
        
        
        