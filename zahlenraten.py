import random

def spiel_starten():
    geheime_zahl = random.randint(1, 20)
    versuche = 0
    
    print("Willkommen beim Zahlenraten!")
    print("Ich habe mir eine Zahl zwischen 1 und 20 ausgedacht.")

    while True:
        tipp = input("Dein Tipp: ")
        
        if not tipp.isdigit():
            print("Bitte gib eine gültige Zahl ein.")
            continue
            
        tipp = int(tipp)
        versuche += 1

        if tipp < geheime_zahl:
            print("Zu niedrig! Versuch es nochmal.")
        elif tipp > geheime_zahl:
            print("Zu hoch! Versuch es nochmal.")
        else:
            print(f"Richtig! Du hast die Zahl in {versuche} Versuchen erraten.")
            break

if __name__ == "__main__":
    spiel_starten()
