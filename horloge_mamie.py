import time
from datetime import datetime

def afficher_heure(t, format_heure):
    """Affiche l'heure sous la forme choisie : HH:MM:SS en 12h ou 24h avec strftime."""
    now = datetime(2025, 1, 1, t[0], t[1], t[2])  
    
    if format_heure == '24':
        # Format 24 heures
        print(f"{t[0]:02}:{t[1]:02}:{t[2]:02}", end="\r")
    elif format_heure == '12':
        # Format 12 heures (AM/PM)
        print(now.strftime("%I:%M:%S %p"), end="\r")

def regler_alarme():
    """Permet de régler l'alarme et retourne l'heure et les minutes de l'alarme."""
    while True:
        try:
            alarme_heure = int(input("Entrez l'heure de l'alarme (0-23) : "))
            if alarme_heure < 0 or alarme_heure > 23:
                raise ValueError("L'heure doit être comprise entre 0 et 23.")
            break
        except ValueError as e:
            print(f"Entrée invalide : {e}. Veuillez réessayer.")

    while True:
        try:
            alarme_minute = int(input("Entrez les minutes de l'alarme (0-59) : "))
            if alarme_minute < 0 or alarme_minute > 59:
                raise ValueError("Les minutes doivent être comprises entre 0 et 59.")
            break
        except ValueError as e:
            print(f"Entrée invalide : {e}. Veuillez réessayer.")

    return alarme_heure, alarme_minute

def alerte_alarme():
    """Affiche le message d'alerte lorsque l'alarme sonne."""
    print("\nALERTE ! bip bip bip !!!")

def main():
    """Affiche l'heure en temps réel et alerte quand l'alarme sonne."""
    # Choisir le format de l'heure uniquement si on choisit le réglage auto
    while True:
        reglage_heure = input("Appuyez sur 1 si vous voulez régler vous-même l'heure ou 2 pour le réglage auto : ")
        if reglage_heure in ['1', '2']:
            break
        else:
            print("Entrée invalide. Veuillez entrer '1' pour réglage manuel ou '2' pour réglage automatique.")

    if reglage_heure == '1':  # Réglage manuel de l'heure (format 24h)
        while True:
            try:
                H = int(input("Entrez l'heure actuelle (format 24h) : "))
                if H < 0 or H > 23:
                    raise ValueError("L'heure doit être comprise entre 0 et 23.")
                break
            except ValueError as e:
                print(f"Entrée invalide : {e}. Veuillez réessayer.")

        while True:
            try:
                M = int(input("Entrez les minutes : "))
                if M < 0 or M > 59:
                    raise ValueError("Les minutes doivent être comprises entre 0 et 59.")
                break
            except ValueError as e:
                print(f"Entrée invalide : {e}. Veuillez réessayer.")

        while True:
            try:
                S = int(input("Entrez les secondes : "))
                if S < 0 or S > 59:
                    raise ValueError("Les secondes doivent être comprises entre 0 et 59.")
                break
            except ValueError as e:
                print(f"Entrée invalide : {e}. Veuillez réessayer.")

        t = (H, M, S)
        format_heure = '24'  # Forcer le format 24h
    elif reglage_heure == '2':  # Réglage automatique de l'heure
        now = datetime.now()
        t = (now.hour, now.minute, now.second)
        while True:
            format_heure = input("Choisissez le format de l'heure (24 pour 24h, 12 pour 12h): ")
            if format_heure in ['24', '12']:
                break
            else:
                print("Format invalide. Choisissez '24' pour le format 24h ou '12' pour le format 12h.")

    # Réglage de l'alarme
    alarme_heure, alarme_minute = regler_alarme()

    alarme_sonnee = False 

    while True:
        # Incrémentation des secondes
        t = (t[0], t[1], t[2] + 1)

        # Gérer le passage d'une minute à l'autre
        if t[2] == 60:
            t = (t[0], t[1] + 1, 0)

        # Gérer le passage d'une heure à l'autre
        if t[1] == 60:
            t = (t[0] + 1, 0, 0)

        # Réinitialisation de l'heure si elle dépasse 23 heures
        if t[0] == 24:
            t = (0, 0, 0)

        # Affichage de l'heure avec le format choisi
        afficher_heure(t, format_heure)

        # Vérification si l'heure actuelle correspond à l'heure de l'alarme
        if t[0] == alarme_heure and t[1] == alarme_minute and not alarme_sonnee:
            alerte_alarme()  # Affichage de l'alerte
            alarme_sonnee = True  # Marquer que l'alarme a sonné une fois

        # Attendre 1 seconde avant de mettre à jour l'heure
        time.sleep(1)

main()
