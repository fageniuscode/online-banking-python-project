import math
print("Bienvenue dans l'application de banque en ligne")

# La fonction 'signin' est utilisée pour créer un compte bancaire et connecter l'utilisateur.
def signin():
    global name  # nom d'utilisateur
    global pin  # mot de passe
    global cb  # solde courant
    name = str(input("Veuillez créer votre nom d'utilisateur : "))
    pin = str(input("Veuillez créer votre code PIN à 6 chiffres : "))

    if len(pin) == 6:
        pin = pin
    else:
        print("Le code PIN doit contenir 6 chiffres.")
        newpin = str(input("Veuillez créer votre code PIN à 6 chiffres : "))

        if len(newpin) != 6:
            print("Le code PIN doit contenir 6 chiffres.")
            signin()
        else:
            pin = newpin

    print("Merci d'avoir créé votre compte bancaire.")

# Appel de la fonction 'signin' pour commencer le processus de création de compte.
signin()

def forgotpin():
    # Demande à l'utilisateur de créer un nouveau code PIN composé de 6 chiffres
    recoverpin = str(input("Veuillez créer votre nouveau code PIN à 6 chiffres : "))

    # Vérifie si la longueur du code PIN est différente de 6
    if len(recoverpin) != 6:
        # Affiche un message d'erreur si le code PIN n'a pas 6 chiffres
        print("Le code PIN doit contenir 6 chiffres.")
        # Appelle à nouveau la fonction forgotpin pour permettre à l'utilisateur de réessayer
        forgotpin()
    else:
        # Affiche un message indiquant que le nouveau code PIN a été enregistré
        print("Le nouveau code PIN a été enregistré. Veuillez vous connecter.")
        # Stocke le nouveau code

import math

def depositinterest(p, r, t):    
    # Convertir les paramètres en nombres à virgule flottante
    p = float(p)
    r = float(r)
    t = float(t)
    
    # Calculer rt
    rt = r * t
    
    # Calculer e^(rt) en utilisant la fonction d'exponentielle de math
    e = math.exp(rt)
    
    # Calculer la valeur future de votre investissement (A)
    a = p * e
    
    # Retourner la valeur future de l'investissement
    return a

def login():
    # name1 représente le nom d'utilisateur
    # pin1 représente le NIP de l'utilisateur
    name1 = str(input("Veuillez entrer votre nom d'utilisateur : "))
    pin1 = str(input("Veuillez entrer votre NIP : "))
    
    # Vérifier si le nom et le NIP correspondent
    if name1 == name and pin1 == pin:
        print("Bienvenue dans l'application de banque en ligne, " + name)
        print("Veuillez choisir le menu ci-dessous :")
        
        listmenu = ["1-Dépôt", "2-Retrait", "3-Virement", "4-Vérifier le solde", "5-Taux d'intérêt des dépôts", "6-Calculer les intérêts composés"]
        
        for b in listmenu:
            print(b)
        
        choose = int(input("Veuillez entrer le numéro de votre choix : "))
        d = 0  # d représente le montant du dépôt
        w = 0  # w représente le montant du retrait
        cb = 0  # cb représente le solde actuel
        
        if choose == 1:
            d = int(input("Entrez le montant de votre dépôt : "))
            cb = d
            print("Votre solde actuel est de " + str(cb))
        
        elif choose == 2:
            w = int(input("Entrez le montant que vous souhaitez retirer : "))
            
            if w > cb:
                print("Votre solde actuel n'est pas suffisant pour cette transaction")
                login()
            else:
                cb = d - w
                print(str(w) + " a été retiré de votre compte. Votre solde actuel est de " + str(cb))
        
        elif choose == 3:
            dest = str(input("Veuillez entrer le numéro de compte de destination à 8 chiffres : "))
            
            if len(dest) == 8:
                amount = int(input("Veuillez entrer le montant que vous souhaitez transférer : "))
                
                if amount > cb:
                    print("Votre solde actuel n'est pas suffisant pour cette transaction")
                    login()
                else:
                    cb = d - amount
                    print("La transaction de " + str(amount) + " a été transférée vers " + str(dest) + ". Votre solde actuel est de " + str(cb))
            else:
                print("La transaction a été rejetée car le numéro de compte de destination est invalide")
                login()        
        elif choose == 4:
            print("Votre solde actuel est de " + str(cb))
        
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            print("Votre taux d'intérêt de dépôt actuel est de " + str(rate) + " %")
        
        elif choose == 6:
            listoption = ["1-Calculer les intérêts composés en fonction de votre solde actuel", "2-Calculer les intérêts composés en fonction du montant de votre dépôt"]
            
            for n in listoption:
                print(n)
            
            choice = int(input("Veuillez entrer votre choix parmi les options ci-dessus : "))
            
            if choice == 1:
                timing = str(input("Pendant combien d'années souhaitez-vous investir votre argent ? "))
                
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else: 
                    ratex = 1.5/100
                
                print("Votre solde actuel dans " + timing + " ans sera de : ")
                print(depositinterest(cb, ratex, timing))
            
            elif choice == 2:
                timing1 = str(input("Pendant combien d'années souhaitez-vous investir votre argent ? "))
                money = str(input("Veuillez entrer le montant d'argent que vous souhaitez déposer : "))
                money = int(money)
                
                if d > 50000:
                    ratex = 3/100
                elif d > 30000:
                    ratex = 2/100
                else: 
                    ratex = 1.5/100
                
                print("Votre solde actuel dans " + timing + " ans sera de : ")
                print(depositinterest(money, ratex, timing))
        
        else:
            print("Option non disponible, retour au menu principal")
            login()
        
    else:
        print("L'un de vos nom d'utilisateur ou NIP est incorrect, avez-vous créé votre compte ?")
        
        list1 = ["1-Oui", "2-Non"]
        
        for i in list1:
            print(i)
        
        inp = int(input("Veuillez entrer votre choix ci-dessous : "))
        
        if inp == 1:
            list2 = ["1-Voulez-vous essayer de vous connecter à nouveau ?", "2-Vous avez oublié votre NIP"]
            
            for e in list2:
                print(e)
            
            theanswer = str(input("Veuillez entrer votre choix : "))
            theanswer = int(theanswer)
            
            if theanswer == 1:
                login()
            
            elif theanswer == 2:
                forgotpin()
            
            else:
                print("Option non disponible")
                login()
        
        elif inp == 2:
            print("Veuillez créer votre compte")
            signin()
    
    exit()

def mainmenu():
    # Affiche le menu principal et demande à l'utilisateur de choisir une option
    optionone = int(input("Choisissez 1 pour vous inscrire et choisissez 2 pour vous connecter : "))
    
    # Vérifie l'option choisie par l'utilisateur
    if optionone == 1:
        signin()  # Appelle la fonction d'inscription
    elif optionone == 2:
        login()  # Appelle la fonction de connexion
    else:
        print("Option non disponible")  # Affiche un message d'erreur si l'option n'est pas valide
        mainmenu()  # Appelle à nouveau la fonction mainmenu pour permettre à l'utilisateur de choisir une autre option
    
    exit()  # Quitte le programme après avoir exécuté une des deux fonctions (inscription ou connexion)

def exit():
    # Demande à l'utilisateur s'il souhaite toujours effectuer une transaction
    answer = str(input("Voulez-vous toujours effectuer une transaction ? Oui ou Non"))
    if answer == "Oui":
        login()  # Appelle la fonction "login" si la réponse est "Oui"
    elif answer == "Non":
        print("Merci d'avoir utilisé cette application")  # Affiche un message de remerciement si la réponse est "Non"
    else: 
        print("Option non disponible")  # Affiche un message indiquant que l'option n'est pas disponible
        mainmenu()  # Appelle la fonction "mainmenu"
        
mainmenu()


