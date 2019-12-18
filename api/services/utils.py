def isEmpty(value):
    if(value == None or value == ''):
        return True
    else:
        return False

def generateError(status, msg, error = {}):
    return {
        'status': status,
        'message': msg,
        'error': error
    }

def successAction(status, msg):
    return {
        'status': status,
        'message': msg
    }

def isNumber(value):
    try:
        val = int(value)
        return True
    except ValueError:
        return False