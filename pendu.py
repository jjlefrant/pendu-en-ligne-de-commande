def pendu():
    """
    jeu du pendu en 8 tentatives
    """
    nb_lettres_trouvees = 0
    nb_essais=0

    tabMotATrouver=str(input("Entrez le mot à trouver : "))

    for i in range(25):
        print()

    tabLettresTrouvees="_"*len(tabMotATrouver)
    
    print(tabLettresTrouvees)

    while nb_lettres_trouvees<len(tabMotATrouver) and nb_essais<=7:
        lettre = str(input("Entrez une lettre : "))
        trouve=False
        for i in range(len(tabMotATrouver)):
            if tabMotATrouver[i]==lettre[0]:
                tabLettresTrouvees=tabLettresTrouvees[:i]+tabMotATrouver[i]+tabLettresTrouvees[i+1:]
                nb_lettres_trouvees+=1
                trouve=True
                if nb_lettres_trouvees==len(tabMotATrouver):
                    print("Gagné !!!")
                    break
        print(tabLettresTrouvees)
        if not trouve:
            nb_essais+=1
        print("Il vous reste : ", 7-nb_essais," tentatives")

    if not trouve:
        print("Perdu !")
    return trouve

pendu()

