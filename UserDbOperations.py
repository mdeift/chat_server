#! /usr/bin/python

'''
Created on Nov 1, 2013

@author: home
'''

import json
from bottle import route, request, HTTPResponse
from Logger import ERROR, WARNING, INFO, Log

''' Handle Users Operations '''

class UserOperations:

    route_user = '/_user'
    route_connect = '/_user/connect'
    route_disconnect = '/_user/disconnect'
    route_get_connected_list = '/_user/get_connected_list'
    
    def __init__(self, db):
        self.db = db
        route(self.route_user, method='PUT')(self.registerUser)
        route(self.route_user, method='DELETE')(self.unregisterUser)
        route(self.route_connect, method='PUT')(self.connectUser)
        route(self.route_disconnect, method='PUT')(self.disconnectUser)
        route(self.route_get_connected_list, method='GET')(self.getConnectedUsers)
        
    #@route(route_user, method='POST', )
    def registerUser(self):      
        req = request.json
        name = req['name']
        
        Log(INFO, 'Received request = ' + str(req) )
              
        isExist, obj = self.isUserExistInDb('name', name)
        if isExist:
            Log(INFO, 'Already exists user \"name\"= ' + name )
            theBody = json.dumps({'reason': 'Already exist user '+ name})
            return HTTPResponse(status=405, body=theBody)
        
        if not self.addUserToDb(req):
            Log(ERROR, 'Failed to register user \"name\"= ' + name )
            theBody = json.dumps({'reason': 'Failed to register user '+name})
            return HTTPResponse(status=405, body=theBody)

        Log(INFO, 'Added new user \"name\"= ' + name )
        return { "success" : True, "Added user" : name }
    
    #@route(route_user, method='DELETE' )
    def unregisterUser(self):
        req = request.json
        name = req['name']
        
        Log(INFO, 'Received request = ' + str(req) )
        
        isExist, obj = self.isUserExistInDb('name', name)
        if not isExist:
            theBody = json.dumps({'reason': 'Not exist user '+name})
            return HTTPResponse(status=405, body=theBody)
        
        if not self.deleteUserFromDb(obj):
            theBody = json.dumps({'reason': 'Failed to remove user '+name})
            return HTTPResponse(status=405, body=theBody)          
            
        theBody = json.dumps({'reason': 'Deleted'})
        Log(INFO, 'Deleted user \"name\"= ' + name )
        return HTTPResponse(status=200, body=theBody)
    
    #@route(route_connect, method='PUT', )
    def connectUser(self):
        req = request.json
        Log(INFO, 'Received request = ' + str(req) )
                            
    #@route(route_disconnect, method='PUT', )
    def disconnectUser(self):
        req = request.json
        Log(INFO, 'Received request = ' + str(req) )
        
    #@route(route_get_connected_list, method='GET', )
    def getConnectedUsers(self):
        Log(INFO, 'Received request' )
        
    
    def isUserExistInDb(self, key, val):
        b, obj = self.db.find(key, val)
        return b, obj
    
    def addUserToDb(self, obj):
        return self.db.insert(obj)
    
    def deleteUserFromDb(self, key):
        return self.db.remove(key)
     
    
    
