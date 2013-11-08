#! /usr/bin/python

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
from bottle import route, request
from Logger import ERROR, WARNING, INFO, Log

''' Handle Users Operations '''

class MessageOperations:

    route_message_put = '/_message/'
    route_message_get = '/_message/<name>'
    
    def __init__(self, pendingDb, archiveDb):
        self.pendingDb = pendingDb
        self.archiveDb = archiveDb
        route(self.route_message_put, method='PUT')(self.pushMessage)
        route(self.route_message_get, method='GET')(self.pullMessage)        
        
    #@route(route_message, method='PUT', )
    def pushMessage(self):      
        req = request.json
        
        '''
        Perform Name validations
        '''
        
        Log(INFO, 'Received push request ' + str(req) )
        self.pendingDb.insert(req)
        return { "success" : True }
    
    #@route(route_message, method='GET' )
    def pullMessage(self, name):
        #req = request.json
        
        Log(INFO, 'Received pull request for \"name\"= ' + name )
        
        b, obj = self.pendingDb.find('To', name)
        
        if obj:
            self.pendingDb.remove(obj)
            self.archiveDb.insert(obj)           
            
            Log(INFO, 'Return message= ' + str(obj) )            
            return { "success" : True, "message" : obj }
        
        Log(INFO, 'Not Found message' )
        return { "success" : False }
    

     
    
    
