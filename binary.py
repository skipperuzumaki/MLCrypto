# Helper functions to conbert various datatypes to binary data

def binary(data):
    if type(data) == type(list()):
        ends = str()
        for i in data:
            ends += ('\n' + str(i))
        return ends.encode('utf8')
    else:
        try:
            ends = str(data)
            return ends.encode('utf8')
        except:
            pass
