def snail(snail_map):
    res = []
    
    while len(snail_map) > 0:
        res += snail_map[0]    
        del snail_map[0]
        
        if len(snail_map) > 0:
            for i in snail_map:
                res += [i[-1]]
                del i[-1]
            
            if snail_map[-1]:
                res += snail_map[-1][::-1]
                del snail_map[-1]
            
            for i in reversed(snail_map):
                res += [i[0]]
                del i[0]
    return res
