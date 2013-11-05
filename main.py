#! python

import couchdb
from CouchDbWrapper import CouchDbWrapper
from reactor import UserOperations
from uuid import uuid4
from bottle import run
#doc_id = uuid4().hex

'''
server = couchdb.Server()
del server['python-tests']

db = server.create('python-tests')

doc_id, doc_rev = db.save({'type': 'Person', 'name': 'John Doe'})

db['johndoe'] = dict(type='Person', name='John Doe')
'''
#map_fun = '''function(doc) {
#    if (doc.type == 'Person')
#    emit(doc.name, null);
#    }'''
#for row in db.query(map_fun):
#    print row.key

#for row in db.query(map_fun, descending=True):
#    print row.key
#for row in db.query(map_fun, key='John Doe'):
#    print row.key

class Backend():
       
    def __init__(self, DbWrapper=''):
        self.initDbs(DbWrapper)
        self.initReactors()
                
    def initDbs(self, DbWrapper):
        self.archiveDb = DbWrapper(dbname='message_archive')
        self.pendingDb = DbWrapper(dbname='message_pending')
        self.usersDb = DbWrapper(dbname='users_db')
        
    def initReactors(self):
        self.userOp = UserOperations(self.usersDb)        
        
def main():
    Backend(CouchDbWrapper)
    run(host='localhost', port=8080, debug=True)    
 
if __name__ == "__main__":
    main()    
    
    