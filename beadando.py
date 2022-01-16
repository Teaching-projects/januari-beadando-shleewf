jatekos = input("Elso jatekos: ko, papir, vagy ollo?: ")
jatekos2 = input("Masodik jatekos: ko, papir, vagy ollo?: ")

if jatekos == jatekos2:
    print("masodik jatekos: ",jatekos2)
    print("elso jatekos: ",jatekos)
    print("Dontetlen!")

elif jatekos == "ko":
    if jatekos2 == "papir":
        print("elso jatekos: ", jatekos)
        print("masodik jatekos: ", jatekos2)
        print("A masodik jatekos nyert ezzel: ", jatekos2)
    if jatekos2 == "ollo":
        print("elso jatekos: ", jatekos)
        print("masodik jatekos: ", jatekos2)        
        print("Az elso jatekos nyert ezzel: ", jatekos)

elif jatekos == "ollo":
    if jatekos2 == "ko":
        print("Elso jatekos: ", jatekos)
        print("Masodik jatekos: ", jatekos2)
        print("A masodik jatekos nyert ezzel: ", jatekos2)
    if jatekos2 == "papir":
        print("elso jatekos: ", jatekos)
        print("masodik jatekos: ", jatekos2)
        print("Az elso jatekos nyert ezzel: ", jatekos)

elif jatekos == "papir":
    if jatekos2 == "ollo":
        print("elso jatekos: ", jatekos)
        print("masodik jatekos: ", jatekos2)
        print("A masodik jatekos nyert ezzel: " ,jatekos2)
    if jatekos2 == "ko":
        print("elso jatekos: ", jatekos)
        print("masoik jatekos: ", jatekos2)
        print("Az elso jatekos nyert ezzel: ", jatekos)