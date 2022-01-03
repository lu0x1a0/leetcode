def solution(message):
    #print(len(message))
    if len(message) == 0:
        return 1
    import numpy as np
    store = np.zeros((len(message),2))
    store[0,:] = (1 if message[0] != '0' else 0 ,0)
    for i in range(1,len(message)):
        store[i,:] = (
            (message[i]!='0')*np.sum(store[i-1,:])% (1e9+7),
            validity(message[i-1:i+1])*store[i-1,0]
        ) 
    #print(store)
    return sum(store[len(message)-1,:])# % (1e9+7),store


def validity(s):
    if int(s)<=26: 
        return 1
    else:
        return 0


x = "1221112111122221211221221212212212111221222212122221222112122212121212221212122221211112212212211211"
pred,store = solution(x)
print(pred)
print(store)