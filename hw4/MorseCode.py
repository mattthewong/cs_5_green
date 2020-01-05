morsecode =  {'a': '.-' ,
              'b': '-...', 
              'c':'-.-.',
              'd':'-..',
              'e':'.',
              'f':'..-.',
              'g':'--.',  
              'h':'....',
              'i':'..',
              'j':'.---',
              'k':'-.-',
              'l':'.-..',
              'm':'--',
              'n':'-.',
              'o':'---',
              'p':'.--.',  
              'q':'--.-',
              'r':'.-.',
              's':'...',
              't':'-',
              'u':'..-',
              'v':'...-',
              'w':'.--',
              'x':'-..-',
              'y':'-.--',  
              'z':'--..',
              ' ': ' '}
def morse(mystring,code):
    '''takes as input a string and a dictionary 
    (e.g., the Morse code dictionary above), and returns
    the Morse code version of that string.'''
    if mystring == '':
       return ''
    else:
        return morsecode[mystring[0]] +' ' + morse(mystring[1:], code)

    
        
        
