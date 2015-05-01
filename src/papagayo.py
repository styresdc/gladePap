#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# generated by wxGlade 0.3.5.1 on Thu Apr 21 12:10:56 2005

# Papagayo, a lip-sync tool for use with Lost Marble's Moho
# Copyright (C) 2005 Mike Clifton
# Contact information at http://www.lostmarble.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import wx
from LipsyncFrame import LipsyncFrame

class LipsyncApp(wx.App):
	def OnInit(self):
		wx.InitAllImageHandlers()
		self.mainFrame = LipsyncFrame(None, -1, "")
		self.SetTopWindow(self.mainFrame)
		self.mainFrame.Show()
		return 1

# end of class LipsyncApp

if __name__ == "__main__":
	papagayo = LipsyncApp(0)
	papagayo.mainFrame.TheApp = papagayo
	papagayo.mainFrame.waveformView.TheApp = papagayo
	papagayo.MainLoop()
