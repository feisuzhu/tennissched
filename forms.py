#!/bin/false
# -*- coding:utf-8 -*-
import forms_design as raw
from utils import nop
from models import *
from algo import arrange, optimize
import wx
import images

__all__ = ['MainFrame', 'EditPersonDialog', 'EditFieldDialog', 'EditGroupDialog']

dt = Data.instance

def timeline_validator(self, e):
    ctl = e.GetEventObject()
    try:
        tl = Timeline.parse(ctl.GetValue())
        ctl.SetValue(tl.tostring())
    except Exception:
        wx.MessageBox(u"输入有误！请按照如下格式输入：\n8:00-12:30, 13:00-15:00", u"网球场次安排", wx.ICON_ERROR)
        ctl.SetFocus()

class EditPersonDialog(raw.EditPersonDialog):
    tlvalidator = timeline_validator
    
    def __del__(self):
        pass

    def ShowModal(self):
        p = self.data
        
        cho = self.chogroup
        cho.Clear()
        cho.Append(u"[未分组]", None)
        for i in dt.groups:
            cho.Append(i.name, i)

        if p is not None:
            self.txtname.SetValue(p.name)
            self.txtcomment.SetValue(p.comment)
            cho.SetSelection(([None] + dt.groups).index(p.group))
            self.txttlsaturday.SetValue(p.timeavail.timelines[0].tostring())
            self.txttlsunday.SetValue(p.timeavail.timelines[1].tostring())

        else:
            cho.SetSelection(0)

        ret = super(self.__class__, self).ShowModal()
        if ret == wx.ID_OK:
            p.name = self.txtname.GetValue()
            p.group = cho.GetClientData(cho.GetSelection())
            p.comment = self.txtcomment.GetValue()
            for i, ctl in zip([0, 1], [self.txttlsaturday, self.txttlsunday]):
                try:
                    p.timeavail.timelines[i] = Timeline.parse(ctl.GetValue())
                except:
                    p.timeavail.timelines[i] = Timeline('X')

        return ret


class EditGroupDialog(raw.EditGroupDialog):

    def __del__(self):
        pass

    def ShowModal(self):
        g = self.data
        if g is not None:
            self.txtname.SetValue(g.name)
            self.txtcomment.SetValue(g.comment)

        ret = super(self.__class__, self).ShowModal()
        if ret == wx.ID_OK:
            g.name = self.txtname.GetValue()
            g.comment = self.txtcomment.GetValue()

        return ret
            

class EditFieldDialog(raw.EditFieldDialog):
    tlvalidator = timeline_validator
    
    def __del__(self):
        pass

    def ShowModal(self):
        f = self.data
        if f is not None:
            self.txtname.SetValue(f.name)
            self.txtcomment.SetValue(f.comment)
            self.txttlsaturday.SetValue(f.timeavail.timelines[0].tostring())
            self.txttlsunday.SetValue(f.timeavail.timelines[1].tostring())

        ret = super(self.__class__, self).ShowModal()
        if ret == wx.ID_OK:
            f.name = self.txtname.GetValue()
            f.comment = self.txtcomment.GetValue()
            for i, ctl in zip([0, 1], [self.txttlsaturday, self.txttlsunday]):
                try:
                    f.timeavail.timelines[i] = Timeline.parse(ctl.GetValue())
                except:
                    f.timeavail.timelines[i] = Timeline('X')
        
        return ret

class ArrangeOutputDialog(raw.ArrangeOutputDialog):
    def OnSave(self, e):
        dlg = wx.FileDialog(self, style=wx.FD_SAVE, message=u"保存结果", wildcard=u"文本文件(*.txt)|*.txt", defaultFile=u"场次安排.txt")
        dlg.ShowModal()
        p = dlg.GetPath()
        with open(p, "w") as f:
            f.write(self.txtoutput.GetValue().encode("utf-8"))

class MainFrame(raw.MainFrame):
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        
        self.imglist = wx.ImageList(16, 16)
        self.imglist.Add(images.person.GetBitmap())
        self.imglist.Add(images.group.GetBitmap())
        self.imglist.Add(images.field.GetBitmap())
        
        self.notebook.SetSelection(0) 
        self.refresh_person_listview()

    def OnExecPython(self, e):
        code = self.txtpythoncode.GetValue()
        try:
            exec code
            self.statusbar.SetStatusText(u"指定的代码已经执行")
        except Exception, e:
            import traceback
            wx.MessageBox(u"代码未成功执行！\n错误原因：\n%s" % str(traceback.format_exc()), u"网球场次安排", wx.OK | wx.ICON_ERROR)
            self.statusbar.SetStatusText(u"代码未成功执行！错误原因：%s" % str(e))
    
    def refresh_person_listview(self):
        lv = self.personlistview
        lv.ClearAll()
        lv.SetImageList(self.imglist, wx.IMAGE_LIST_SMALL)
        nop(lv.InsertColumn(*i) for i in zip(xrange(4), [u"姓名", u"所在小组", u"可用时间", u"备注"]))
        for i, v in enumerate(dt.persons):
            n = lv.Append([v.name, u"[未分组]" if v.group is None else v.group.name, v.timeavail.tostring(), v.comment])
            lv.SetItemData(n, i)
            lv.SetItemImage(n, 0)

        lv.SetColumnWidth(0, 80)
        nop(lv.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER) for i in xrange(1,4))

    def refresh_group_listview(self):
        lv = self.grouplistview
        lv.ClearAll()
        lv.SetImageList(self.imglist, wx.IMAGE_LIST_SMALL)
        nop(lv.InsertColumn(*i) for i in zip(xrange(3), [u"小组名称", u"小组成员", u"备注"]))
        for i, v in enumerate(dt.groups):
            n = lv.Append([v.name, ', '.join(m.name for m in v.get_members()), v.comment])
            lv.SetItemData(n, i)
            lv.SetItemImage(n, 1)

        lv.SetColumnWidth(0, 80)
        nop(lv.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER) for i in xrange(1,3))

    def refresh_field_listview(self):
        lv = self.fieldlistview
        lv.ClearAll()
        lv.SetImageList(self.imglist, wx.IMAGE_LIST_SMALL)
        nop(lv.InsertColumn(*i) for i in zip(xrange(3), [u"场地名称", u"可用时间", u"备注"]))
        for i, v in enumerate(dt.fields):
            n = lv.Append([v.name, v.timeavail.tostring(), v.comment])
            lv.SetItemData(n, i)
            lv.SetItemImage(n, 2)

        lv.SetColumnWidth(0, 120)
        nop(lv.SetColumnWidth(i, wx.LIST_AUTOSIZE_USEHEADER) for i in xrange(1,3))
    
    def OnModifyRecord(dlgclass, data, refresh):
        def evt_handler(self, e):   
            i = e.GetItem().GetData()
            dlg = dlgclass(self)
            dlg.data = data[i]
            dlg.ShowModal()
            refresh(self)
            dt.save()
            self.statusbar.SetStatusText(u"数据已保存")

        return evt_handler
    
    personlistviewOnDblClick = OnModifyRecord(EditPersonDialog, dt.persons, refresh_person_listview)
    grouplistviewOnDblClick = OnModifyRecord(EditGroupDialog, dt.groups, refresh_group_listview)
    fieldlistviewOnDblClick = OnModifyRecord(EditFieldDialog, dt.fields, refresh_field_listview)

    def OnNewRecord(dlgclass, klass, data, refresh):
        def evt_handler(self, e):
            dlg = dlgclass(self)
            dlg.data = klass()
            if dlg.ShowModal() == wx.ID_OK:
                data.append(dlg.data)
                refresh(self)
            dt.save()
            self.statusbar.SetStatusText(u"数据已保存")

        return evt_handler
    
    personlistviewOnNewRecord = OnNewRecord(EditPersonDialog, Person, dt.persons, refresh_person_listview)
    grouplistviewOnNewRecord = OnNewRecord(EditGroupDialog, Group, dt.groups, refresh_group_listview)
    fieldlistviewOnNewRecord = OnNewRecord(EditFieldDialog, Field, dt.fields, refresh_field_listview)

    def OnDelRecord(ctl, data, refresh, cb=None):
        def evt_handler(self, e):
            i = self.__getattribute__(ctl).GetFirstSelected()
            if i == -1: return
            if cb:
                cb(data[i])
            del data[i]
            refresh(self)
            dt.save()
            self.statusbar.SetStatusText(u"数据已保存")

        return evt_handler

    def _gdel_cb(o):
        for i in dt.persons:
            if i.group is o:
                i.group = None

    personlistviewOnDelRecord = OnDelRecord('personlistview', dt.persons, refresh_person_listview)
    grouplistviewOnDelRecord = OnDelRecord('grouplistview', dt.groups, refresh_group_listview, _gdel_cb)
    fieldlistviewOnDelRecord = OnDelRecord('fieldlistview', dt.fields, refresh_field_listview)

    def refresh_arrange_panel(self):
        gl = self.lstarrgroups
        fl = self.lstarrfields
        
        gl.Clear()
        nop(gl.Append(i.name) for i in dt.groups)

        fl.Clear()
        nop(fl.Append(i.name) for i in dt.fields)

    def refresh_settings_panel(self):
        self.txtsetmatchtime.SetValue(str(dt.settings.matchtime))

    def matchtime_handler(self, e):
        try:
            i = int(float(self.txtsetmatchtime.GetValue()))
            i = i if 0 < i <= 1440 else 60
            dt.settings.matchtime = i
            self.txtsetmatchtime.SetValue(unicode(i))
        except:
            self.txtsetmatchtime.SetValue(u"60")
            dt.settings.matchtime = 60
    
    def OnPageChange(self, e):
        e.Skip()
        pg = e.GetSelection()
        if pg in xrange(5):
            [
                self.refresh_person_listview,
                self.refresh_group_listview,
                self.refresh_field_listview,
                self.refresh_arrange_panel,
                self.refresh_settings_panel
            ][pg]()

        if e.GetOldSelection() in [4]:
            dt.save()
            self.statusbar.SetStatusText(u"数据已保存")

    def OnArrange(self, e):
        gl = self.lstarrgroups
        fl = self.lstarrfields

        g = [dt.groups[i] for i in gl.GetChecked()]
        f = [dt.fields[i] for i in fl.GetChecked()]

        m = []
        for i in g:
            m.extend(i * i)

        m, m_na, arrtl = arrange(m, f)
        rate = optimize(m)
        
        def match_sort(a, b):
            t1 = (a.sched["week"], a.sched["day"], a.sched["starttime"], a.sched["field"])
            t2 = (b.sched["week"], b.sched["day"], b.sched["starttime"], b.sched["field"])
            return 1 if t1 > t2 else -1

        m.sort(match_sort)
        
        dlg = ArrangeOutputDialog(self)
        
        s1 = u"比赛安排：\n" + u"\n".join(
            u"第%d周 比赛： %s VS %s 时间：%s %s 场地：%s " % (
                v.sched["week"] + 1, 
                u"%s(%s)" % (v.player1.name, v.player1.group.name),
                u"%s(%s)" % (v.player2.name, v.player2.group.name),
                WeekTimeline.days_represent[v.sched["day"]], 
                u"%s-%s" % (Timeline.numtotime(v.sched["starttime"]), Timeline.numtotime(v.sched["starttime"] + dt.settings.matchtime)),
                v.sched["field"].name, 
            )
            for v in m
        )

        s2 = u"无法安排的比赛：\n" + u"\n".join(
            u"%s VS %s, 可用时间： %s" % (
                u"%s(%s)" % (v.player1.name, v.player1.group.name),
                u"%s(%s)" % (v.player2.name, v.player2.group.name),
                v.timeavail.tostring()
            )
            for v in m_na
        )

        l = []
        for iw, w in enumerate(arrtl):
            for ftl in w:
                t = ftl.tostring()
                if len(t):
                    l.append(u"第%d周 场地：%s 空闲时间：%s" % (iw + 1, ftl._field.name, t))
        
        s3 = u"场地的剩余空闲时间：\n" + u"\n".join(l)
        
        s = (u"\n" + u"-" * 60 + u"\n").join([s1, s2, s3])
        dlg.txtoutput.SetValue(s)
        dlg.ShowModal()
    


