def lasit_datni():
    #pajautāsim ievadīt datnes nosakums
    datnes_nosaukums=input("Ievadi datnes nosaukumu:  ")
    try:
    # Kā ielādēt datnes saturu?
        with open(datnes_nosaukums, 'r') as ff:
            saturs=ff.read()
            #print(saturs) pārliecinājos, ka datnē ir skaitļi
            #izvadi simbolu skaitu virknē
            print(f"Simbolu skaits virknē ir {len(saturs)}")

            #Izvadīt pirmos 10 simbolus
            print(f"Pirmie 10 simboli ir: {saturs[:10]}")
            #Izvadīt pirmo un pēdējo simbolu
            print(f"Izvadīt pirmo un pēdējo simbolu: {saturs[0]} un {saturs[-1]}")
    

    except FileExistsError:
        print("Datne nav atrasta!!!")
    except ValueError:
        print("Datu kļūda!!!")



if __name__=="__main__":
    lasit_datni()