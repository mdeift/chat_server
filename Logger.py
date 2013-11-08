#! /usr/bin/python

'''
Created on Nov 8, 2013

@author: home
'''

from time import ctime
import inspect

ERROR =    'ERROR'
WARNING =  'WARNING'
INFO =     'INFO'

global logFile
    
def openLogFile(filename):
    global logFile 
    logFile = open(filename, "w")
        
def Log(level, text):
    global logFile
 
    callerframerecord = inspect.stack()[1]    # 0 represents this line                                            # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)

    out = ctime() + ':' + info.filename + ':' + info.function + ':' +  str(info.lineno)  + ':' + level + ':' + text + '\n'
    logFile.write(out)
    logFile.flush()
    
def closeLogFile():
    global logFile
    logFile.close()
        
    
        