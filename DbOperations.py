'''
Created on Nov 1, 2013

@author: home
'''

def pushMsg(msg):
    dbPending.save(msg)
    
def pullFirstMsg(toUser):
    msg = dbPending.findFirstMsg(toUser)
    if (msg):
        buildJsonRep(msg)
        moveMsgToArchive(msg)
        returnToUser
    else:
        return 'Not Found'

def registerUser(user):
    isExist = isExistUser(user)
    if isExist:
        return 'Already Exist'
    else:
        dbUsers.save(user)
        return 'Added'
    
def unregisterUser(user):
    isExist = isExistUser(user)
    if not isExist:
        return 'Not Found'
    else:
        dbUsers.remove(user)
        return 'Deleted'

    
    