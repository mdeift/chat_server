'''
Created on Nov 1, 2013

@author: home
'''
import couchdb

class CouchDbWrapper:
    
    def __init__(self, servername='', dbname=''):
        self.connect(servername)
        self.create(dbname)
        
    def connect(self, servername=""):
        self.server = couchdb.Server()
    
    def create(self, dbname):
        if self.server[dbname] != '':
            self.db = self.server[dbname]
        else:
            self.db = self.create(dbname)
        
    def delete(self, dbname):
        del self.server[dbname]
              
    def createMapFunction(self, key):
        map_fun = "function(doc) {\n\
        if (doc." + key + ")\n\
        emit(doc." + key + ", doc.id);\n\
        }" 
        return map_fun 
          
    def find(self, key, value):
        map_fun = self.createMapFunction(key) 
        
        for row in self.db.query(map_fun):
            if row.key == value:
                return True, self.db.get(row.id)
        return False, 0
    
    def insert(self, obj):
        id = self.db.save(obj)
        if id == 0:
            return False
        return True
        
    def remove(self, obj):
        self.db.delete(obj)
        return True
            
    
    
    
        
        