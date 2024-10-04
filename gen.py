import random
import string
from colorama import init, Fore, Style

init(autoreset=True)

def gen_mdp(longueur, difficulte):
    if difficulte == 'facile':
        caracteres = string.ascii_lowercase
    elif difficulte == 'moyen':
        caracteres = string.ascii_letters + string.digits
    elif difficulte == 'difficile':
        caracteres = string.ascii_letters + string.digits + string.punctuation 
    else:
        return "Réponse invalide. Choisis entre 'facile', 'moyen' ou 'difficile'."

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def gen_pseudo(longueur):
    caracteres = string.ascii_letters + string.digits
    pseudo = ''.join(random.choice(caracteres) for _ in range(longueur))
    return pseudo

def afficher_informations():
    info = f"""{Fore.BLUE}Informations:
- Mon github : {Fore.GREEN}https://github.com/Kyntex-Sys
- Mon discord : {Fore.GREEN}https://discord.com/users/1283916947586809898
- Mon telegram : {Fore.GREEN}https://telegram.org/
- Organisation : {Fore.YELLOW} Kyntex Industries  
"""
# merci de pas changer les informations svp ou de me fork sur vos projet 
    print(info)


def afficher_menu():
    menu = f"""{Fore.CYAN}Options disponible:
    1. Générateur de mots de passe
    2. Générateur de pseudonyme
    3. Afficher ces informations
"""
    print(menu)

def main():
    while True:
        afficher_menu()
        choix = input(f"{Fore.MAGENTA}Choisissez une option (1-3) ou 'q' pour quitter: ")

        if choix == '1':
            longueur = int(input("Longueur du mot de passe: "))
            difficulte = input("Niveau de difficulté (facile, moyen, difficile): ").lower()
            print(f"{Fore.YELLOW}Mot de passe généré:", gen_mdp(longueur, difficulte))
        elif choix == '2':
            longueur = int(input("Longueur du pseudonyme: "))
            print(f"{Fore.YELLOW}Pseudonyme généré:", gen_pseudo(longueur))
        elif choix == '3':
            afficher_informations()
        elif choix.lower() == 'q':
            break
        else:
            print(f"{Fore.RED}Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
