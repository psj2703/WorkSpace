from typing import Sequence, Any

def bin_search(a: Sequence, key: Any):
    pl = 0
    pr = len(a)-1

    while True:
        pc = (pl+pr)//2
        if pc == key:
            return pc
        elif pc < key:
            pl = pc+1
        else:
            pr = pc-1
        
        if pr < pl:
            return -1



