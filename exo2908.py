def menu():#menu principal

    list = []
    print("Bienvenue au zoo TSSR, vous disposez de plusieurs choix pour gérer vos animaux :")
    flag = True
    while flag:
        print(" 1 : Ajouter Animal")
        print(" 2 : Supprimer Animal")
        print(" 3 : Afficher liste")
        print(" 4 : Remplacer")
        print(" 5 : Modifier")
        print(" 6 : exit")

        choix = input()
        match choix:
            case "1":
                print("hello")
            case "2":
                print("hello")
            case "3":
                print("hello")
            case "4":
                print("hello")
            case "5":
                print("hello")
            case"6":
                flag = False
            case _:
                print("erreur de saisie")
                menu()

def main():
    menu()
if __name__ == '__main__':
    main()
    
    
    
    
    def menusupp(list):
    print("Quel animal voulez vous supprimer ?")
    nom = input()
    for i in range(len(list[i])):
        if list[i][0] == nom:
            confirmation(i)



def confirmation(i):
    print(list[i])
    print ("Confirmez la suppression y/n")
    choix = input()
    if choix == "y":
        del list[i]
        return list
    elif choix == "n":
        menu()

        
        
 def ajouterAnimeaux(nom, race, sexe, age, pays, list):
    list.append([nom, race, sexe, age, pays, list])
    afficherAnimeaux(list)
    return list




def menuAjoutAnimeaux(list):
    print("Quel est votre nom ?")
    nom = input()
    print("Quel est votre race ?")
    race = input()
    print("Quel est votre sexe ?")
    sexe = input()
    print("Quel est votre age")
    age = input()
    print("De quel pays venez-vous")
    pays = input()

    list = ajouterAnimeaux(nom, race, sexe, list)

    return list
