def card_conv(x: int , y: int) -> str:
    d = ""
    dchar = "0123456789abcdefghijklmnopqrstuvwxyz"

    while True:
        d += dchar[x%y]
        x=x//y
        if x < y:
            d+= dchar[x+1]
            break

    return d[::-1]