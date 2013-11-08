#! /usr/bin/python

from CouchDbWrapper import CouchDbWrapper
from UserDbOperations import UserOperations
from MessageDbOperations import MessageOperations
#from uuid import uuid4
from bottle import run
from Logger import ERROR, WARNING, INFO, Log
import Logger
#doc_id = uuid4().hex

class Backend():
       
    def __init__(self, DbWrapper=''):
        Log(INFO, "Start Backend")
        self.initDbs(DbWrapper)
        self.initReactors()
                
    def initDbs(self, DbWrapper):
        self.archiveDb = DbWrapper(dbname='message_archive')
        self.pendingDb = DbWrapper(dbname='message_pending')
        self.usersDb = DbWrapper(dbname='users_db')
        
    def initReactors(self):
        self.userOp = UserOperations(self.usersDb)
        self.messageOp = MessageOperations(self.pendingDb, self.archiveDb)     
        
def main():    
    Logger.openLogFile('/var/tmp/chat_server.log')
    Backend(CouchDbWrapper)
    run(host='localhost', port=8080, debug=True)   
 
if __name__ == "__main__":
    main()    
    
    