# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:23:29 2017

@author: Rowan
"""

import wx
import os
import ToxinGraphicsMain

        
class PhyloIslandWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = (1050, 600))
        # At the moment using a text control to handle the files in the profile
        self.CreateStatusBar()


class Panel1(wx.Panel):
    
    def __init__(self, parent):
        self.dirname = ''
        wx.Panel.__init__(self, parent)
        
        # Menu
        filemenu = wx.Menu()
        filemenu.Append(wx.ID_OPEN, "&Open"," Open a file to place in profile")
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.Append(wx.ID_EDIT, "E&xit", "Terminate the program")
        
        # Menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")
        self.SetMenuBar(menuBar)
        
        # Sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainGrid = wx.GridBagSizer(hgap=5, vgap = 5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)
        grid = wx.GridBagSizer(hgap = 5, vgap = 5)
        # GenomeDiagrams take up the left side of the grid
        
        self.seqImage = wx.StaticText(self, label = "Open a Sequence and it will appear here", size = (600, 600), style= wx.ALIGN_CENTER)
        # self.png = wx.StaticBitmap(self, -1, wx.Bitmap("ppt_sample.png", wx.BITMAP_TYPE_ANY))
        mainGrid.Add(self.seqImage, pos = (0,0))
        
        # Multiline TextCtrl which will store all open Sequences (may change to like a dropdown or something eventually, mostly just proof of concept atm)
        #self.profile = wx.TextCtrl(self, size = (200, -1), style = wx.TE_MULTILINE | wx.TE_READONLY)
        
        # Button/s
        
        # ComboBox
        self.profileList = ['seq1', 'seq2', 'seq3', 'seq4']
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
        
        
        mainGrid.Add(grid, pos = (0,1))
        hSizer.Add(mainGrid, 0, wx.ALL, 5)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        self.SetSizerAndFit(mainSizer)
               
    # Event handlers
        
    def EvtComboBox(self, event):
        return None
    def EvtText(self, event):
        return None

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
        
app22 = wx.App(False)
frame = PhyloIslandWindow(None, "PhyloIsland Graphical Interface")
nb = wx.Notebook(frame)

nb.AddPage(Panel1(nb),"Panel 1")
frame.Show()
app22.MainLoop()
        
        
        