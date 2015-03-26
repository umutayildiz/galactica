#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This handy little script converts Turkish characters in a file to LaTeX format
"""


import os,sys
from chardet import detect
import codecs

# Just checking the encoding
encoding = lambda x: detect(x)['encoding']

print "-----------------------------------------------------------------"
print "Please enter the name of the text file with Turkish characters..."
print "-----------------------------------------------------------------"
newtext = raw_input()
if (newtext == ''):
	print "No value entered, program exists!"
	sys.exit()


f=codecs.open(newtext,"r",encoding='utf-8')
mytext=f.read()

f=open("corr_"+newtext,"w")
f.write(mytext.encode('utf-8').replace('ı', '{\i}').replace('İ','\\.{I}').replace('ğ','\\u{g}').replace('Ğ','\\u{G}').replace('ç','\\c{c}').replace('Ç','\\c{C}').replace('ş','\\c{s}').replace('Ş','\\c{S}').replace('ü','\\"{u}').replace('Ü','\\"{U}').replace('ö','\\"{o}').replace('Ö','\\"{O}'))
f.close

print "-----------------------------------------------------------------------"
print '>>> SUCCESS! LaTeX version of the text is now called "corr_'+newtext+'"'
print "-----------------------------------------------------------------------"
