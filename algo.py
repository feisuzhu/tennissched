#!/bin/false
# -*- coding: utf-8 -*-

from models import *
from collections import defaultdict as ddict
from random import random, choice
from math import exp

s = Data.instance.settings

def arrange(matches, fields):
    '''
    Arrange matches to fields
    Both parameters should be list
    '''

    def list_split(l, f):
        l1 = []
        l2 = []
        for i in l:
            if f(i):
                l1.append(i)
            else:
                l2.append(i)

        return (l1, l2)

    def tag(o, d):
        o.__dict__.update(d)
        return o
    
    arr = []
    def add_week():
        l = [tag(WeekTimeline(i.timeavail), {'_field': i, '_nweek': len(arr)}) for i in fields]
        arr.append(l)
        return l

    def put(match, week):
        for ftl in week:
            t = match.timeavail & ftl
            a = t[s.matchtime] 
            if a:
                match.sched = {}
                match.sched["week"] = ftl._nweek
                match.sched["field"] = ftl._field
                match.sched["day"], m.sched["starttime"] = a
                daytl = ftl.timelines[a[0]]
                daytl[ a[1] : (s.matchtime + a[1]) ] = 'X'
                return True
        else:
            return False
    
    matches.sort(lambda x, y: 1 if x.timeavail.freecount() > y.timeavail.freecount() else -1)

    for m in matches:
        if m.__dict__.has_key("sched"):
            del m.sched

        for week in arr:
            if put(m, week):
                break
        else:
            nw = add_week()
            put(m, nw)

    matches, matches_notavail = list_split(matches, lambda x: x.__dict__.has_key('sched'))
    w = max(i.sched["week"] for i in matches) if len(matches) else 0
    return (matches, matches_notavail, arr[:w+1])
                    


# make it work, and then make it fast
def optimize(matches):
    '''
    Optimize arranges using simulated annealing
    '''

    if not len(matches):
        return 100

    lstat = ddict(list)
    
    def schedid(i):
        return i.sched["week"] * 1440 * 7 + i.sched["day"] * 1440 + i.sched["starttime"]
        
    for i in matches:
        t = schedid(i)
        lstat[i.player1].append(t)
        lstat[i.player2].append(t)

    def rate():
        s = 0.0
        for i in lstat.values():
            i.sort()
            for a, b in zip(i, [-99999999] + i):
                if a == b:
                    s += 99999999
                else:
                    s += 100/float(a - b)

        return s
    
    
    def canswap(a, b):
        if a.timeavail.timelines[b.sched["day"]][(b.sched["starttime"], s.matchtime)] and b.timeavail.timelines[a.sched["day"]][(a.sched["starttime"], s.matchtime)]:
            return True
        else:
            return False
           

    def swap(a, b):
        if a == b: return False
        
        if not canswap(a, b):
            return False
        
        sa = schedid(a)
        sb = schedid(b)
        la1 = lstat[a.player1]
        la2 = lstat[a.player2]
        lb1 = lstat[b.player1]
        lb2 = lstat[b.player2]
        
        del la1[la1.index(sa)]
        del la2[la2.index(sa)]
        del lb1[lb1.index(sb)]
        del lb2[lb2.index(sb)]

        la1.append(sb)
        la2.append(sb)
        lb1.append(sa)
        lb2.append(sa)

        a.sched, b.sched = b.sched, a.sched

        return True
    
    
    t = 1000.0
    cool = 0.999
    ev = rate()
    cnt = 0
    while t>0.000001:
        
        a = choice(matches)
        b = choice(matches)

        if swap(a, b):
            nev = rate()
            d = nev - ev
            if d<0 or (d>0 and exp(-d/t)>random()):
                cnt = 0
                ev = nev
            else:
                cnt += 1
                swap(a, b)
                
        if cnt >= 1000:
            break
        
        t *= cool
    
    return ev
    

