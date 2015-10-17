#!/usr/bin/env python
# coding: utf-8
import mechanize

def attendManaba(user_name,user_password,attend_num):
    br = mechanize.Browser()
    attend_url = "https://atmnb.tsukuba.ac.jp/attend/tsukuba"
    login_url = "https://manaba.tsukuba.ac.jp/ct/login"
    
    br.open(login_url)
    br.select_form(nr = 0)
    
    br["j_username"] = user_name
    br["j_password"] = user_password
    br.submit()
    
