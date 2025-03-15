def tickt():
    ticket = 10
    root={1:"CHENNAI CENTRAL",2:"PERAMBUR",3:"ARAKKONAM",4:"TIRUTTANI",5:"PUTTUR",6:"RENIGUNTA JN",7:"RAZAMPETA",8:"CUDDAPAH",9:"YERRAGUNTLA",10:"TADIPATRI",11:"GOOTY JN",12:"GUNTAKAL JN",13:"ADONI",14:"MANTHRALAYAM RD",15:"RAICHUR",16:"SAIDAPUR",17:"YADGIR",18:"WADI",19:"KALABURAGI JN",20:"PUNE JN"}
    id1=[d for d in root.keys()]
    place=[o for o in root.values()]
    print("""\t*******TRAIN ROOT******
        1 CHENNAI CENTRAL
        2 PERAMBUR
        3 ARAKKONAM
        4 TIRUTTANI
        5 PUTTUR
        6 RENIGUNTA JN
        7 RAZAMPETA
        8 CUDDAPAH
        9 YERRAGUNTLA
        10 TADIPATRI
        11 GOOTY JN
        12 GUNTAKAL JN
        13 ADONI
        14 MANTHRALAYAM RD
        15 RAICHUR
        16 SAIDAPUR
        17 YADGIR
        18 WADI
        19 KALABURAGI JN
        20 PUNE JN""")
    print("*" * 30)
    try:
        while(True):
            e =input("SELECT FROM STATION :")
            if(e.isdigit() and 21>int(e)>0):break
        while(True):
            r = input("SELECT TO STATION :")
            if(r.isdigit() and 21>int(r)>0):break
        total_amt = abs(int(r) - int(e)) * ticket
    except :
        print("""DON'T ENTER STRINT
        1 string
        2 special symbole
        3 exceeded value""")
    else:
        print("*" * 30)
        print("\t\tTICKET DETAILS")
        print("*" * 30)
        print("\tFROM :", root.get(int(e)))
        print("\tTO :", root.get(int(r)))
        print("*" * 30)
        print("\tTECKET AMOUNT :", total_amt)
        print("*" * 30)
    finally:
        print("\tMAKE A SAFE JURNY WEL COME")
    return root,id1,place
with open("vicky","a") as tick:
    k=tickt()
    tick.write(str(k))
print("data returned")
