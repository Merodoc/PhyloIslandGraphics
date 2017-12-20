# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:23:29 2017

@author: Rowan
"""

import wx
import os
from ToxinGraphicsMain import PhyloGraph, MultiplePhyloGraph

class PhyloIslandWindow(wx.Frame):
    def __init__(self, parent, title):
        self.dirname =''
        wx.Frame.__init__(self, parent, title=title, size = (-1, -1))
        # At the moment using a text control to handle the files in the profile
        self.profile = wx.StaticText(self, -1, label = "Current Profile", size = (-1, -1),style = wx.TE_MULTILINE)
        self.CreateStatusBar()
        
        # Menu
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to place in profile")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        menuExit = filemenu.Append(wx.ID_EDIT, "E&xit", "Terminate the program")
        
        # Menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        
        # Images to allow representation of GenomeDiagrams
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("ppt_sample.png", wx.BITMAP_TYPE_ANY))
        # Events 
        
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        
        self.sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.buttons = []
        for i in range(0, 6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1)

        # Use some sizers to see layout options
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.png, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.sizer.Add(self.profile, 1, wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

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
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

phylo5 = wx.App(False)
frame = PhyloIslandWindow(None, "PhyloIsland Graphical Toolkit")
phylo5.MainLoop()
        
        
        