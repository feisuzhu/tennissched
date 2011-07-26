#!/usr/bin/python
import wx
from forms import MainFrame
from models import Data

app = wx.App(0)
f = MainFrame(None)
f.Show()
app.MainLoop()
Data.instance.save()

