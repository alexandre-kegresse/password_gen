import hashlib
import json

user = input("Veuillez saisir un nom d'utilisateur : ")

while True:
    
    password = input("Veuillez saisir un mot de passe : ")

    # Vérifie si le mot de passe a moins de 8 caractères
    if len(password) < 8:
        print("Mot de passe invalide : doit contenir au moins 8 caractères.")
    else:
        # Vérifie si le mot de passe contient au moins une lettre majuscule, une minuscule, un int et un character special
        has_uppercase = False
        has_lowercase = False
        has_int = False
        has_spec = False

        for char in password:
            if 65 <= ord(char) <= 90:  # Vérifie si le caractère est une majuscule
                has_uppercase = True
            elif 97 <= ord(char) <= 122:  # Vérifie si le caractère est une minuscule
                has_lowercase = True
            elif 48 <= ord(char) <= 57:  # Vérifie si le mdp contient un int
                has_int = True
            elif 35 <= ord(char) <= 38 or 64 == ord(char) or 42 or 94:  # Vérifie si le mdp contient un character special
                has_spec = True

            # Si on a déjà trouvé une majuscule,une minuscule, un int et un character special pas besoin de continuer
            if has_uppercase and has_lowercase and has_int and has_spec:
                break

        if has_uppercase and has_lowercase and has_int and has_spec:
            print("Mot de passe valide, félicitations !")
            password = hashlib.sha256(password.encode()).hexdigest()
            print(password)
            with open("./password.json", "w") as f:
                data = [user, password]
                json.dump(data, f, indent=2)
            break
        else:
            print("Mot de passe invalide : doit contenir au moins une majuscule, une minuscule, un chiffre et un character special.")


