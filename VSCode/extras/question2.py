a = False
ta = int(input())
tb = int(input())
if ta>tb:
    print ("Team A is the winner")
elif ta<tb:
    print ("Team B is the winner")
else:
    print ("the match is a tie")
    tap = int(input(""))
    tbp = int(input(""))
    if tap>tbp:
        print ("Team A is the winner after penalties")
    elif tap<tbp:
        print ("Team B is the winner after penalties")
    else: print("It's still a tie after penalties!")