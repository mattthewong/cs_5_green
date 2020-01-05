def reverse(D):
    '''takes a dictionary D as input and returns a new dictionary that
    includes reversed definitions.'''
    Dict2 = {}
    for k,v in D.iteritems():
            Dict2.setdefault(v,[]).append(k)
    return Dict2

Dict = {'dude!' : 'hello', 'later' : 'goodbye', 'stoked' : 'happy', 'ciao' : 'goodbye'}
    