import math
go = 0
while go < 1:
    C = int(input("C: "))/1000000000000 #pico
    L = int(input("L: "))/1000000 #micro
    F = 1 / (2*math.pi*math.sqrt(L*C))
    F = round(F, 3)
    print(f"{F} Hz")
