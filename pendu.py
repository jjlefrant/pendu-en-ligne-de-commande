def pendu():
    """
    jeu du pendu en 6 tentatives
    """
    nb_lettres_trouvees = 0
    nb_essais=0

    tabMotATrouver=str(input("Entrez le mot à trouver : "))

    for i in range(25):
        print()

    l=len(tabMotATrouver)
    tabLettresTrouvees="_"*l
    
    print(tabLettresTrouvees)

    while nb_lettres_trouvees<l and nb_essais<6:
        lettre = str(input("Entrez une lettre : "))
        trouve=False
        for i in range(l):
            if tabMotATrouver[i]==lettre[0] and tabMotATrouver[i]!=tabLettresTrouvees[i]:
                tabLettresTrouvees=tabLettresTrouvees[:i]+tabMotATrouver[i]+tabLettresTrouvees[i+1:]
                nb_lettres_trouvees+=1
                trouve=True
                if nb_lettres_trouvees==l:
                    print("Gagné (^.^)")
                    break
        print(tabLettresTrouvees)
        if not trouve:
            nb_essais+=1
        print("Il vous reste : ", 6-nb_essais," tentatives")

    if not trouve:
        print("Perdu :(")
        print("Le mot était :", tabMotATrouver)
    return trouve

pendu()

