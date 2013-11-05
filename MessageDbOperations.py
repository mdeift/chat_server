'''
Created on Nov 5, 2013

@author: home
'''

'''
push_message = 
{
   From : "NAME"
   To : "NAME"
   Time : "Unix Time"
   Payload : "DATA"
}
'''

'''
pull_message = 
{
    To : "NAME"
}
'''


import json
from urllib2 import HTTPError
from bottle import route, run, request, HTTPResponse

''' Handle Users Operations '''

class MessageOperations:

    route_message = '/_message'
    
    def __init__(self, pendingDb, archiveDb):
        self.pendingDb = pendingDb
        self.archiveDb = archiveDb
        route(self.route_message, method='PUT')(self.pushMessage)
        route(self.route_message, method='GET')(self.pullMessage)        
        
    #@route(route_message, method='PUT', )
    def pushMessage(self):      
        req = request.json
        
        '''
        Perform Name validations
        '''
        
        self.pendingDb.insert(req)
        return { "success" : True }
    
    #@route(route_message, method='GET' )
    def pullMessage(self):
        req = request.json
        
        b, obj = self.pendingDb.find('To', req['To'])
        
        if obj:
            self.pendingDb.remove(obj)
            self.archiveDb.insert(obj)                       
            return { "success" : True, "message" : obj }
        return { "success" : False }
    

     
    
    
