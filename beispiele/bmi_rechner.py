"""
BMI-Rechner (Body Mass Index Calculator)

Berechnet den Body Mass Index basierend auf Gewicht und Größe.
CC-BY Jan Eggers
"""

def berechne_bmi(gewicht_kg, groesse_m):
    """
    Berechnet den BMI.

    Args:
        gewicht_kg: Gewicht in Kilogramm
        groesse_m: Größe in Metern

    Returns:
        BMI-Wert (float)
    """
    return gewicht_kg / (groesse_m ** 2)


def bmi_kategorie(bmi):
    """
    Bestimmt die BMI-Kategorie nach WHO-Standard.

    Args:
        bmi: BMI-Wert

    Returns:
        Kategorie als String
    """
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


def main():
    """Hauptprogramm - fragt Daten ab und gibt BMI aus."""
    print("=== BMI-Rechner ===\n")

    try:
        # Eingabe von Gewicht und Größe
        gewicht = float(input("Gewicht in kg: "))
        groesse = float(input("Größe in m (z.B. 1.75): "))

        # Validierung
        if gewicht <= 0 or groesse <= 0:
            print("Fehler: Gewicht und Größe müssen positive Zahlen sein.")
            return

        # BMI berechnen
        bmi = berechne_bmi(gewicht, groesse)
        kategorie = bmi_kategorie(bmi)

        # Ergebnis ausgeben
        print(f"\nDein BMI: {bmi:.1f}")
        print(f"Kategorie: {kategorie}")

        # Zusätzliche Informationen
        print("\n--- BMI-Kategorien (WHO) ---")
        print("Untergewicht: < 18.5")
        print("Normalgewicht: 18.5 - 24.9")
        print("Übergewicht: 25 - 29.9")
        print("Adipositas: ≥ 30")

    except ValueError:
        print("Fehler: Bitte gib gültige Zahlen ein.")


if __name__ == "__main__":
    main()
