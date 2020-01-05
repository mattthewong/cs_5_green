def countPattern(pattern, string):
    patterncounter = 0.0
    for i in range(0, len(string)+1):
        if pattern == string[i:len(pattern)+i]:
            patterncounter = patterncounter + 1
    return patterncounter
      