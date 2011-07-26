# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"网球场次安排", pos = wx.DefaultPosition, size = wx.Size( 598,497 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		mainsizer = wx.BoxSizer( wx.VERTICAL )
		
		self.notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.personpanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.personlistview = wx.ListCtrl( self.personpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer4.Add( self.personlistview, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer35 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnstuadd = wx.Button( self.personpanel, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.btnstuadd, 0, wx.ALL, 5 )
		
		self.btnstudel = wx.Button( self.personpanel, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.btnstudel, 0, wx.ALL, 5 )
		
		bSizer4.Add( bSizer35, 0, wx.ALIGN_RIGHT, 5 )
		
		self.personpanel.SetSizer( bSizer4 )
		self.personpanel.Layout()
		bSizer4.Fit( self.personpanel )
		self.notebook.AddPage( self.personpanel, u"学生管理", False )
		self.grouppanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.grouplistview = wx.ListCtrl( self.grouppanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer7.Add( self.grouplistview, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer351 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnstuadd1 = wx.Button( self.grouppanel, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer351.Add( self.btnstuadd1, 0, wx.ALL, 5 )
		
		self.btngroupdel = wx.Button( self.grouppanel, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer351.Add( self.btngroupdel, 0, wx.ALL, 5 )
		
		bSizer7.Add( bSizer351, 0, wx.ALIGN_RIGHT, 5 )
		
		self.grouppanel.SetSizer( bSizer7 )
		self.grouppanel.Layout()
		bSizer7.Fit( self.grouppanel )
		self.notebook.AddPage( self.grouppanel, u"小组管理", False )
		self.fieldpanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		self.fieldlistview = wx.ListCtrl( self.fieldpanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_SORT_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL|wx.LC_VRULES )
		bSizer9.Add( self.fieldlistview, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer352 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnfieldadd = wx.Button( self.fieldpanel, wx.ID_ANY, u"添加", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer352.Add( self.btnfieldadd, 0, wx.ALL, 5 )
		
		self.btnfielddel = wx.Button( self.fieldpanel, wx.ID_ANY, u"删除", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer352.Add( self.btnfielddel, 0, wx.ALL, 5 )
		
		bSizer9.Add( bSizer352, 0, wx.ALIGN_RIGHT, 5 )
		
		self.fieldpanel.SetSizer( bSizer9 )
		self.fieldpanel.Layout()
		bSizer9.Fit( self.fieldpanel )
		self.notebook.AddPage( self.fieldpanel, u"场地管理", False )
		self.arrangepanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer27 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer28 = wx.BoxSizer( wx.HORIZONTAL )
		
		sbSizer13 = wx.StaticBoxSizer( wx.StaticBox( self.arrangepanel, wx.ID_ANY, u"比赛小组" ), wx.VERTICAL )
		
		lstarrgroupsChoices = [ u"1", u"2", u"3" ];
		self.lstarrgroups = wx.CheckListBox( self.arrangepanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstarrgroupsChoices, 0 )
		self.lstarrgroups.SetMinSize( wx.Size( -1,200 ) )
		
		sbSizer13.Add( self.lstarrgroups, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer28.Add( sbSizer13, 1, wx.ALL|wx.EXPAND, 5 )
		
		sbSizer15 = wx.StaticBoxSizer( wx.StaticBox( self.arrangepanel, wx.ID_ANY, u"可用场地" ), wx.VERTICAL )
		
		lstarrfieldsChoices = [ u"1", u"2", u"3" ];
		self.lstarrfields = wx.CheckListBox( self.arrangepanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, lstarrfieldsChoices, 0 )
		self.lstarrfields.SetMinSize( wx.Size( -1,200 ) )
		
		sbSizer15.Add( self.lstarrfields, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer28.Add( sbSizer15, 1, wx.TOP|wx.BOTTOM|wx.RIGHT|wx.EXPAND, 5 )
		
		bSizer27.Add( bSizer28, 1, wx.EXPAND, 5 )
		
		self.btnarrange = wx.Button( self.arrangepanel, wx.ID_ANY, u"安排场次", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer27.Add( self.btnarrange, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.arrangepanel.SetSizer( bSizer27 )
		self.arrangepanel.Layout()
		bSizer27.Fit( self.arrangepanel )
		self.notebook.AddPage( self.arrangepanel, u"比赛安排", False )
		self.settingspanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer71 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.settingspanel, wx.ID_ANY, u"算法设置" ), wx.VERTICAL )
		
		bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self.settingspanel, wx.ID_ANY, u"每场比赛时间：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer91.Add( self.m_staticText71, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtsetmatchtime = wx.TextCtrl( self.settingspanel, wx.ID_ANY, u"60", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer91.Add( self.txtsetmatchtime, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.settingspanel, wx.ID_ANY, u"单位：分钟", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer91.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		sbSizer3.Add( bSizer91, 1, wx.EXPAND, 5 )
		
		bSizer71.Add( sbSizer3, 0, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.settingspanel, wx.ID_ANY, u"执行Python代码" ), wx.VERTICAL )
		
		self.txtpythoncode = wx.TextCtrl( self.settingspanel, wx.ID_ANY, u"# 请不要在这里随便写东西\n# 如果有批量的操作，自己操作觉得麻烦\n# 或者有什么临时需要的功能\n# 可以给我说下要求，我来帮你写段代码，贴在这里执行就可以\n\nimport wx\nwx.MessageBox(u\"这是一段样例代码\",u\"样例代码\", wx.OK)\nd = Data.instance\np = d.persons[0]\n\nwx.MessageBox(u\"列表里第一个学生的名字是：%s\" % p.name,u\"样例代码\", wx.OK)", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		sbSizer9.Add( self.txtpythoncode, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.btnexecpython = wx.Button( self.settingspanel, wx.ID_ANY, u"执行", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.btnexecpython, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		bSizer71.Add( sbSizer9, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.settingspanel.SetSizer( bSizer71 )
		self.settingspanel.Layout()
		bSizer71.Fit( self.settingspanel )
		self.notebook.AddPage( self.settingspanel, u"设置", True )
		self.aboutpanel = wx.Panel( self.notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, 0, 5 )
		
		self.m_staticText3 = wx.StaticText( self.aboutpanel, wx.ID_ANY, u"Proton制作", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 8 )
		
		self.m_staticText4 = wx.StaticText( self.aboutpanel, wx.ID_ANY, u"QQ:84065234", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer2.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 8 )
		
		self.m_staticText5 = wx.StaticText( self.aboutpanel, wx.ID_ANY, u"邮箱：feisuzhu@163.com", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		bSizer2.Add( self.m_staticText5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 8 )
		
		self.m_staticText6 = wx.StaticText( self.aboutpanel, wx.ID_ANY, u"Project starts at 2011-3-24", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer2.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 8 )
		
		self.m_staticText7 = wx.StaticText( self.aboutpanel, wx.ID_ANY, u"在GPL许可证下发布", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer2.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 8 )
		
		
		bSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.aboutpanel.SetSizer( bSizer2 )
		self.aboutpanel.Layout()
		bSizer2.Fit( self.aboutpanel )
		self.notebook.AddPage( self.aboutpanel, u"关于", False )
		
		mainsizer.Add( self.notebook, 1, wx.EXPAND, 5 )
		
		self.SetSizer( mainsizer )
		self.Layout()
		self.statusbar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.notebook.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChange )
		self.personlistview.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.personlistviewOnDblClick )
		self.btnstuadd.Bind( wx.EVT_BUTTON, self.personlistviewOnNewRecord )
		self.btnstudel.Bind( wx.EVT_BUTTON, self.personlistviewOnDelRecord )
		self.grouplistview.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.grouplistviewOnDblClick )
		self.btnstuadd1.Bind( wx.EVT_BUTTON, self.grouplistviewOnNewRecord )
		self.btngroupdel.Bind( wx.EVT_BUTTON, self.grouplistviewOnDelRecord )
		self.fieldlistview.Bind( wx.EVT_LIST_ITEM_ACTIVATED, self.fieldlistviewOnDblClick )
		self.btnfieldadd.Bind( wx.EVT_BUTTON, self.fieldlistviewOnNewRecord )
		self.btnfielddel.Bind( wx.EVT_BUTTON, self.fieldlistviewOnDelRecord )
		self.btnarrange.Bind( wx.EVT_BUTTON, self.OnArrange )
		self.txtsetmatchtime.Bind( wx.EVT_KILL_FOCUS, self.matchtime_handler )
		self.btnexecpython.Bind( wx.EVT_BUTTON, self.OnExecPython )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPageChange( self, event ):
		pass
	
	def personlistviewOnDblClick( self, event ):
		pass
	
	def personlistviewOnNewRecord( self, event ):
		pass
	
	def personlistviewOnDelRecord( self, event ):
		pass
	
	def grouplistviewOnDblClick( self, event ):
		pass
	
	def grouplistviewOnNewRecord( self, event ):
		pass
	
	def grouplistviewOnDelRecord( self, event ):
		pass
	
	def fieldlistviewOnDblClick( self, event ):
		pass
	
	def fieldlistviewOnNewRecord( self, event ):
		pass
	
	def fieldlistviewOnDelRecord( self, event ):
		pass
	
	def OnArrange( self, event ):
		pass
	
	def matchtime_handler( self, event ):
		pass
	
	def OnExecPython( self, event ):
		pass
	

###########################################################################
## Class EditPersonDialog
###########################################################################

class EditPersonDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"编辑学生信息", pos = wx.DefaultPosition, size = wx.Size( 484,271 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"基本信息" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"姓名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer19.Add( self.m_staticText30, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.txtname, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		gSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer191 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"所在小组：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )
		bSizer191.Add( self.m_staticText301, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		chogroupChoices = [ u"1", u"2", u"3" ]
		self.chogroup = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, chogroupChoices, 0 )
		self.chogroup.SetSelection( 2 )
		bSizer191.Add( self.chogroup, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 5 )
		
		gSizer2.Add( bSizer191, 1, wx.EXPAND, 5 )
		
		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText302 = wx.StaticText( self, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText302.Wrap( -1 )
		bSizer192.Add( self.m_staticText302, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtcomment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.txtcomment, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		gSizer2.Add( bSizer192, 1, wx.EXPAND, 5 )
		
		sbSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		bSizer10.Add( sbSizer4, 0, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"可用时间" ), wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"星期六", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer17.Add( self.m_staticText28, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txttlsaturday = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.txttlsaturday, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer5.Add( bSizer17, 0, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"星期日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer18.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txttlsunday = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.txttlsunday, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sbSizer5.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer10.Add( sbSizer5, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		bSizer10.Add( m_sdbSizer4, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txttlsaturday.Bind( wx.EVT_KILL_FOCUS, self.tlvalidator )
		self.txttlsunday.Bind( wx.EVT_KILL_FOCUS, self.tlvalidator )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def tlvalidator( self, event ):
		pass
	
	

###########################################################################
## Class EditGroupDialog
###########################################################################

class EditGroupDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"编辑小组信息", pos = wx.DefaultPosition, size = wx.Size( 345,174 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"基本信息" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 1, 0, 0 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"小组名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer19.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		self.txtname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.txtname, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		gSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText302 = wx.StaticText( self, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText302.Wrap( -1 )
		bSizer192.Add( self.m_staticText302, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txtcomment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.txtcomment, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		gSizer2.Add( bSizer192, 1, wx.EXPAND, 5 )
		
		sbSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		bSizer10.Add( sbSizer4, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		m_sdbSizer4.Realize();
		bSizer10.Add( m_sdbSizer4, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EditFieldDialog
###########################################################################

class EditFieldDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"编辑场地信息", pos = wx.DefaultPosition, size = wx.Size( 407,222 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer10 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"基本信息" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 2, 0, 0 )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"场地名：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		bSizer19.Add( self.m_staticText30, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.txtname, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		gSizer2.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		bSizer192 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText302 = wx.StaticText( self, wx.ID_ANY, u"备注：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText302.Wrap( -1 )
		bSizer192.Add( self.m_staticText302, 0, wx.RIGHT|wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtcomment = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer192.Add( self.txtcomment, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )
		
		gSizer2.Add( bSizer192, 1, wx.EXPAND, 5 )
		
		sbSizer4.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		bSizer10.Add( sbSizer4, 0, wx.EXPAND|wx.ALL, 5 )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"可用时间" ), wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText28 = wx.StaticText( self, wx.ID_ANY, u"星期六", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		bSizer17.Add( self.m_staticText28, 0, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		self.txttlsaturday = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.txttlsaturday, 1, wx.ALIGN_CENTER_VERTICAL|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		sbSizer5.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"星期日", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		bSizer18.Add( self.m_staticText29, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.txttlsunday = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.txttlsunday, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		sbSizer5.Add( bSizer18, 0, wx.EXPAND, 5 )
		
		bSizer10.Add( sbSizer5, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		
		
		bSizer10.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		m_sdbSizer4 = wx.StdDialogButtonSizer()
		self.m_sdbSizer4OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer4.AddButton( self.m_sdbSizer4OK )
		self.m_sdbSizer4Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer4.AddButton( self.m_sdbSizer4Cancel )
		m_sdbSizer4.Realize();
		bSizer10.Add( m_sdbSizer4, 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5 )
		
		self.SetSizer( bSizer10 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.txttlsaturday.Bind( wx.EVT_KILL_FOCUS, self.tlvalidator )
		self.txttlsunday.Bind( wx.EVT_KILL_FOCUS, self.tlvalidator )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def tlvalidator( self, event ):
		pass
	
	

###########################################################################
## Class ArrangeOutputDialog
###########################################################################

class ArrangeOutputDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"安排结果", pos = wx.DefaultPosition, size = wx.Size( 575,493 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer29 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnsave = wx.Button( self, wx.ID_ANY, u"保存", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.btnsave, 0, wx.ALL, 5 )
		
		bSizer29.Add( bSizer30, 0, wx.ALIGN_RIGHT, 5 )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		self.txtoutput = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer31.Add( self.txtoutput, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer29.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer29 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnsave.Bind( wx.EVT_BUTTON, self.OnSave )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnSave( self, event ):
		pass
	

