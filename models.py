#/bin/false
# -*- coding: utf-8 -*-
from utils import check, bean, singleton
import cPickle
import re

@bean('tldata')
class Timeline(object):
    '''
    Timeline class:
    Every char in tldata is 1 minute, total 1440 for a day
    ' ' for available
    'X' for non-available
    '''
    
    def __init__(self, tl=None):
        super(self.__class__, self).__init__()
        if tl is None:
            self.tldata = 'X' * 1440
        elif isinstance(tl, Timeline):
            self.tldata = tl.tldata[:]
        elif isinstance(tl, str):
            self.tldata = (tl * (int(1440/len(tl)) + 1))[:1440]
        else:
            check(False, "tl is nether a Timeline nor a string!")

    def __setslice__(self, f, t, v):
        '''
        Set time status
        '''
        check(0 <= f < t <= 1440, 'Timeline: f and t should satisfy 0 <= f < t <= 1440!')
        v = str(v)
        check(len(v) > 0, 'Timeline: len(v) == 0!')

        self.tldata = self.tldata[:f] + (v * (int((t - f)/len(v)) + 1))[:(t - f)] + self.tldata[t:]

    def __str__(self):
        return self.tldata;

    def __getitem__(self, v):
        '''
        Find free time of v minutes
        '''
        if isinstance(v, int):
            rst = re.search(' {%d,}' % int(v), self.tldata)
            return None if rst is None else rst.start()
        elif isinstance(v, tuple):
            s, l = v
            check(0 <= s <= 1440, "starttime not in range!")
            check(0 <= l and s + l <= 1440, "length not in range!")
            return s if self.tldata[s:s+l] == ' ' * l else None
     
        else:
            check(False, "v must be int or tuple!")

    def __and__(self, op):
        '''
        Calculate time intersection
        '''
        s = ''.join(
            ' ' if (self.tldata[i] == ' ' and op.tldata[i] == ' ') else 'X'
            for i in xrange(len(self.tldata))
        )
        return Timeline(s)

    def __or__(self, op):
        s = ''.join(
            ' ' if (self.tldata[i] == ' ' or op.tldata[i] == ' ') else 'X'
            for i in xrange(len(self.tldata))
        )
        return Timeline(s)
    
    def normalize(self):
        '''
        Make all special cases of unavailable time to the generic 'X'
        '''
        return Timeline(re.sub(r'[^ ]', 'X', self.tldata))

    @staticmethod
    def timetonum(s):
        '''
        convert '24:00' to 1440
        '''
        l = s.split(':')
        if len(l) == 2:
            return int(l[0])*60 + int(l[1])
        else:
            return int(l[0])*60

    @staticmethod
    def numtotime(n):
        '''
        convert 1440 to '24:00'
        '''
        return (str(n/60) + ':' + str(n%60).zfill(2)).decode("utf-8")

    @staticmethod
    def parse(s):
        '''
        convert '8:00-10:00, 15:00-17:00' to a Timeline
        '''
        if(len(s.strip()) == 0): return Timeline('X')

        a = bytearray('X' * 1440)
        for v in s.split(","):
            f, t = [Timeline.timetonum(i) for i in v.split('-')]
            check(0 <= f < t <= 1440, 'time not in range!')
            a[f:t] = ' ' * (t - f)

        return Timeline(str(a))

    def tostring(self):
        '''
        Return human readable Timeline represention
        '8:00-10:00, 15:00-17:00'
        '''
        return u', '.join(
            Timeline.numtotime(i.start()) + u"-" + Timeline.numtotime(i.end())
            for i in re.finditer(" +", self.tldata)
        )

    def freecount(self):
        return self.tldata.count(' ')

@bean('timelines')
class WeekTimeline(object):
    days = 2
    #days_represent = [u"星期一", u"星期二", u"星期三", u"星期四", u"星期五", u"星期六", u"星期日"]
    days_represent = [u"星期六", u"星期日"]
    def __init__(self, l=None):
        super(self.__class__, self).__init__()
        days = WeekTimeline.days
        if isinstance(l, list):
            check(isinstance(l, list), 'tl must be a list of %d Timelines!' % days)
            check(len(l) == days, 'l must be a list of %d Timelines!' % days)
            check(reduce(lambda x,y: x and isinstance(y, Timeline), [True] + l), 'l must be a list of %d Timelines!' % days)
            self.timelines = [Timeline(i) for i in l]
        elif isinstance(l, WeekTimeline):
            self.timelines = [Timeline(i) for i in l.timelines]
        else:
            self.timelines = [Timeline('X') for i in xrange(days)]

    def __or__(self, op):
        check(isinstance(op, WeekTimeline), 'op should be a WeekTimeline!')
        return WeekTimeline([
            self.timelines[i] | op.timelines[i]
            for i in xrange(WeekTimeline.days)
        ])

    def __and__(self, op):
        check(isinstance(op, WeekTimeline), 'op should be a WeekTimeline!')
        return WeekTimeline([
            self.timelines[i] & op.timelines[i]
            for i in xrange(WeekTimeline.days)
        ])

    def __getitem__(self, v):
        for i in xrange(WeekTimeline.days):
            r = self.timelines[i][v]
            if r:
                return (i, r)

        return None

    def __len__(self):
        return WeekTimelines.days

    def freecount(self):
        return sum(i.freecount() for i in self.timelines)

    def tostring(self):
        l = [i.tostring() for i in self.timelines]
        return u'; '.join(
            WeekTimeline.days_represent[i] + u": " + l[i]
            for i in xrange(len(l))
            if len(l[i])
        )

@bean('name', 'group', 'timeavail', 'comment')
class Person(object):
    '''
    Represent a person
    Fields:
        name str
        group Group
        timeavail WeekTimeline
    '''
    def __init__(self, name=u'<没有名字>'):
        super(self.__class__, self).__init__()
        self.name = unicode(name)
        self.group = None
        self.timeavail = WeekTimeline()
        self.comment = u""

    def __add__(self, op):
        return Match(self, op)

@bean('name', 'comment')
class Group(object):
    '''
    Represent a group
    Fields:
        name str
    '''
    def __init__(self, name=u'<未命名的小组>'):
        super(self.__class__, self).__init__()
        self.name = unicode(name)
        self.comment = u""

    def get_members(self):
        return [i for i in Data.instance.persons if i.group == self]
    
    def __mul__(self, op):
        l = []
        s = set()
        for i in self.get_members():
            for j in op.get_members():
                p = (max(i,j), min(i,j))
                if p not in s and i is not j:
                    s.add(p)
                    l.append(i + j)
        return l

@bean('name', 'timeavail', 'comment')
class Field(object):
    '''
    Represent a match field
    Fields:
        name str
        timeavail WeekTimeline
    '''
    def __init__(self, name=u'<未指定名字的场地>', tl=None):
        super(self.__class__, self).__init__()
        self.name = unicode(name)
        self.comment = u""
        if tl is not None:
            check(isinstance(tl, WeekTimeline), 'tl must be a WeekTimeline!')
            self.timeavail = tl
        else:
            self.timeavail = WeekTimeline()
    
@bean('player1', 'player2', 'timeavail', 'sched')
class Match(object):
    '''
    Represent a match
    Fields:
        player1 Person
        player2 Person
        timeavail WeekTimeline
    '''
    def __init__(self, p1=None, p2=None):
        super(self.__class__, self).__init__()
        self.player1 = p1
        self.player2 = p2
        self.timeavail = self.player1.timeavail & self.player2.timeavail


class Setting(object):
    pass
'''
    def __getattribute__(self, k):
        if not self.__dict__.has_key(k):
            return None
        else:
            return self.__dict__[k]
'''

@singleton
@bean('persons', 'fields', 'groups', 'settings')
class Data(object):
    '''
    Data holder, nothing else
    '''
    
    def save(self):
        f = open("save.dat", "wb")
        cPickle.dump(self.__dict__, f, 2)
        f.close()

    @staticmethod
    def _static_(klass):
        try:
            with open("save.dat", "rb") as f:
                klass.instance.__dict__.update(cPickle.load(f))

        except (IOError, EOFError):
            r = klass.instance
            r.persons = []
            r.fields = []
            r.groups = []
            r.settings = Setting()
            r.settings.matchtime = 60
