h24r_tm = float(input("Type a random time (using 24 hour system (use . not: ex: 6.00 not 6:00)) "))
h12r_tm = "nothing"
if h24r_tm >= 12.00:
    h12r_tm = "{:0.2f}PM".format(h24r_tm-12)
else:
    h12r_tm = "{:0.2f}AM".format(h24r_tm)
print(h12r_tm)
