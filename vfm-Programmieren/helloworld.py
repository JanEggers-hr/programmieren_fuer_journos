print("Hello World!")
print("Irgendwas anderes")
print(1 + 1)

# Eingabe einer ganzen Zahl
n = int(input("Geben Sie eine ganze Zahl ein: "))

# Sieb des Eratosthenes
if n < 2:
    print("Keine Primzahlen bis", n)
else:
    # Liste aller Zahlen von 2 bis n erstellen
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 und 1 sind keine Primzahlen
    
    # Sieb des Eratosthenes anwenden
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            # Alle Vielfachen von i markieren
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    # Primzahlen sammeln
    # Eine leere Liste erstellen, um alle gefundenen Primzahlen zu speichern
    primzahlen = []
    
    # Hier erstellt das Programm aus dem Sieb eine Python-Programmstruktur:
    # eine Liste, die die Primzahlen enthält.
    # Durch alle Zahlen von 2 bis n iterieren
    for i in range(2, n + 1):
        # Prüfen, ob die aktuelle Zahl i eine Primzahl ist
        # (im Sieb als True markiert)
        if sieve[i]:
            # Wenn i eine Primzahl ist, zur Liste hinzufügen
            primzahlen.append(i)
    
    # Primzahlen in umgekehrter Reihenfolge ausgeben
    print(f"Primzahlen bis {n} (umgekehrt):")
    count = 0
    for p in reversed(primzahlen):
        if count % 2 == 0:
            # Schwarz auf weiß (normal)
            print(p, end=" ")
        else:
            # Weiß auf schwarz (invertiert)
            print(f"\033[7m{p}\033[0m", end=" ")
        count += 1
    print()  # Neue Zeile am Ende