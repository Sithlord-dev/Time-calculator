#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:50:38 2020

@author: sithlord-dev
"""

def add_time(stime,dtime,day_unf=None) :
    week = {'Monday':0, 'Tuesday':1 , 'Wednesday':2 , 'Thursday':3 , 'Friday':4 , 'Saturday':5 , 'Sunday':6 }
    terms_s=((stime.split()[0]).split(':')[0],(stime.split()[0]).split(':')[1],stime.split()[1])
    #print(terms_s)
    terms_d=dtime.split(':')
    #print(terms_d)
    msom = (int(terms_s[1]) + int(terms_d[1])) % 60
    if len(str(msom)) == 1 :
        m = f"{msom:02d}"
    else :
        m = msom
    rm = (int(terms_s[1]) + int(terms_d[1])) // 60
    #print('minutes: ',msom)
    #print('rest: ',rm)
    
    if terms_s[2] in ('PM','pM','Pm','pm') :
        h_cvt = int(terms_s[0]) +12
        #print(h_cvt,'cvt')
    else :
        h_cvt = int(terms_s[0])
        #print(h_cvt,'non cvt')
    hsom = ( h_cvt + int(terms_d[0]) + rm ) % 24
    #print('heures: ',hsom)
    
    d = ( h_cvt + int(terms_d[0]) + rm ) // 24
    #print('day: ',d)
    
    if (hsom // 12) > 0 :
        if hsom == 12 :
            att = 'PM'
            h = hsom
        else :
            att = 'PM'
            h = hsom - 12
    else :
        if hsom == 0 :
            att = 'AM'
            h = 12
        else :    
            att = 'AM'
            h = hsom
    if d == 0 :
        fut = ''
    elif d == 1 :
        fut = "(next day)"
    else : 
        fut = '('+str(d)+" days later)"
    
    if (len(fut) > 0) :
        if day_unf is not None :
            day_f = (day_unf.casefold()).capitalize()
            key= week[day_f]
            day =  [ k for k,v in week.items() ][(d+key) % 7]
            return print(h,':', m, att+', '+day,fut)
        else :
            return print(h,':', m, att,fut)
    else :
        return print(h,':', m, att)
    