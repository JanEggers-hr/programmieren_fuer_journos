"""
BMI-Rechner Streamlit App mit Verlaufskurve

Eine interaktive Web-App zur Berechnung und Visualisierung
des Body Mass Index über die Zeit.

CC-BY Jan Eggers
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy import stats


def berechne_bmi(gewicht_kg, groesse_m):
    """Berechnet den BMI."""
    return gewicht_kg / (groesse_m ** 2)


def bmi_kategorie(bmi):
    """Bestimmt die BMI-Kategorie nach WHO-Standard."""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


def initialisiere_daten():
    """Initialisiert die Session State Daten."""
    if 'bmi_verlauf' not in st.session_state:
        st.session_state.bmi_verlauf = pd.DataFrame(
            columns=['Person', 'Datum', 'Gewicht', 'Größe', 'BMI', 'Kategorie']
        )


def generiere_beispieldaten(anzahl=50):
    """Generiert Beispieldaten für mehrere Personen mit realistischen BMI-Werten."""
    np.random.seed(42)
    daten = []

    for i in range(anzahl):
        # Realistische BMI-Verteilung (Mittelwert ~24, Standardabweichung ~4)
        bmi = np.random.normal(24, 4)
        bmi = max(15, min(45, bmi))  # Begrenzen auf realistische Werte

        # Zufällige Größe zwischen 1.50 und 2.00 m
        groesse = np.random.uniform(1.50, 2.00)

        # Gewicht basierend auf BMI und Größe berechnen
        gewicht = bmi * (groesse ** 2)

        kategorie = bmi_kategorie(bmi)

        daten.append({
            'Person': f'Person {i+1}',
            'Datum': datetime.now(),
            'Gewicht': round(gewicht, 1),
            'Größe': round(groesse, 2),
            'BMI': round(bmi, 1),
            'Kategorie': kategorie
        })

    return pd.DataFrame(daten)


def main():
    """Hauptfunktion der Streamlit App."""
    st.set_page_config(page_title="BMI-Rechner", page_icon="📊")

    # Initialisiere Daten
    initialisiere_daten()

    # Titel
    st.title("📊 BMI-Rechner mit Verlaufskurve")
    st.write("Berechne deinen Body Mass Index und verfolge deine Entwicklung.")

    # Beispieldaten generieren
    st.header("Beispieldaten")
    col_btn1, col_btn2 = st.columns(2)

    with col_btn1:
        if st.button("🎲 50 Beispielpersonen generieren", type="secondary"):
            beispieldaten = generiere_beispieldaten(50)
            st.session_state.bmi_verlauf = pd.concat(
                [st.session_state.bmi_verlauf, beispieldaten],
                ignore_index=True
            )
            st.success("✅ 50 Beispieldatensätze generiert!")
            st.rerun()

    with col_btn2:
        if st.button("🗑️ Alle Daten löschen"):
            st.session_state.bmi_verlauf = pd.DataFrame(
                columns=['Person', 'Datum', 'Gewicht', 'Größe', 'BMI', 'Kategorie']
            )
            st.rerun()

    # Eingabebereich
    st.header("Neue Messung eingeben")

    col1, col2, col3 = st.columns(3)

    with col1:
        person_name = st.text_input(
            "Name/ID",
            value=f"Person {len(st.session_state.bmi_verlauf) + 1}"
        )

    with col2:
        gewicht = st.number_input(
            "Gewicht (kg)",
            min_value=20.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )

    with col3:
        groesse = st.number_input(
            "Größe (m)",
            min_value=1.0,
            max_value=2.5,
            value=1.75,
            step=0.01
        )

    # Berechnen Button
    if st.button("BMI berechnen und speichern", type="primary"):
        bmi = berechne_bmi(gewicht, groesse)
        kategorie = bmi_kategorie(bmi)

        # Neuen Eintrag erstellen
        neuer_eintrag = pd.DataFrame({
            'Person': [person_name],
            'Datum': [datetime.now()],
            'Gewicht': [gewicht],
            'Größe': [groesse],
            'BMI': [bmi],
            'Kategorie': [kategorie]
        })

        # Zum Verlauf hinzufügen
        st.session_state.bmi_verlauf = pd.concat(
            [st.session_state.bmi_verlauf, neuer_eintrag],
            ignore_index=True
        )

        st.success(f"✅ BMI gespeichert: {bmi:.1f} ({kategorie})")

    # Aktueller BMI (wenn vorhanden)
    if not st.session_state.bmi_verlauf.empty:
        letzter_bmi = st.session_state.bmi_verlauf.iloc[-1]

        st.header("Aktueller BMI")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("BMI", f"{letzter_bmi['BMI']:.1f}")
        with col2:
            st.metric("Kategorie", letzter_bmi['Kategorie'])
        with col3:
            st.metric("Gewicht", f"{letzter_bmi['Gewicht']:.1f} kg")

    # Referenzbereiche
    st.header("BMI-Kategorien (WHO)")
    st.write("""
    - **Untergewicht**: < 18.5
    - **Normalgewicht**: 18.5 - 24.9
    - **Übergewicht**: 25 - 29.9
    - **Adipositas**: ≥ 30
    """)

    # BMI-Verteilung mit Gaußkurve
    if len(st.session_state.bmi_verlauf) > 0:
        st.header("BMI-Verteilung (Gaußkurve)")

        df = st.session_state.bmi_verlauf.copy()
        bmi_werte = df['BMI'].values

        # Statistiken berechnen
        mittelwert = np.mean(bmi_werte)
        std_abweichung = np.std(bmi_werte)

        # Erstelle die Grafik
        fig, ax = plt.subplots(figsize=(12, 6))

        # Histogramm der tatsächlichen Daten
        n, bins, patches = ax.hist(bmi_werte, bins=20, density=True,
                                    alpha=0.6, color='steelblue',
                                    edgecolor='black', label='Tatsächliche Daten')

        # Gaußkurve (Normalverteilung)
        x = np.linspace(min(bmi_werte) - 2, max(bmi_werte) + 2, 100)
        gaussian = stats.norm.pdf(x, mittelwert, std_abweichung)
        ax.plot(x, gaussian, 'r-', linewidth=3, label=f'Gaußkurve (μ={mittelwert:.1f}, σ={std_abweichung:.1f})')

        # Referenzlinien für BMI-Kategorien
        ax.axvline(x=18.5, color='lightblue', linestyle='--',
                   linewidth=2, alpha=0.8, label='Untergewicht-Grenze')
        ax.axvline(x=25, color='green', linestyle='--',
                   linewidth=2, alpha=0.8, label='Normalgewicht-Grenze')
        ax.axvline(x=30, color='orange', linestyle='--',
                   linewidth=2, alpha=0.8, label='Übergewicht-Grenze')

        # Mittelwert markieren
        ax.axvline(x=mittelwert, color='red', linestyle='-',
                   linewidth=2, alpha=0.8, label=f'Mittelwert ({mittelwert:.1f})')

        # Beschriftungen
        ax.set_xlabel('BMI', fontsize=12)
        ax.set_ylabel('Häufigkeitsdichte', fontsize=12)
        ax.set_title('BMI-Verteilung mit Normalverteilungskurve', fontsize=14, fontweight='bold')
        ax.legend(loc='best', fontsize=10)
        ax.grid(True, alpha=0.3)

        # Zeige die Grafik
        st.pyplot(fig)

        # Statistiken anzeigen
        st.subheader("Statistische Kennzahlen")
        stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

        with stat_col1:
            st.metric("Mittelwert", f"{mittelwert:.1f}")
        with stat_col2:
            st.metric("Standardabweichung", f"{std_abweichung:.1f}")
        with stat_col3:
            st.metric("Median", f"{np.median(bmi_werte):.1f}")
        with stat_col4:
            st.metric("Anzahl Personen", len(bmi_werte))

        # Daten-Tabelle
        st.header("Alle Messungen")

        # Formatiere die Anzeige
        df_anzeige = df.copy()
        df_anzeige['Datum'] = pd.to_datetime(df_anzeige['Datum']).dt.strftime('%d.%m.%Y %H:%M')
        df_anzeige['Gewicht'] = df_anzeige['Gewicht'].round(1).astype(str) + ' kg'
        df_anzeige['Größe'] = df_anzeige['Größe'].round(2).astype(str) + ' m'
        df_anzeige['BMI'] = df_anzeige['BMI'].round(1)

        # Zeige nur die ersten 20 Einträge in der Tabelle
        st.dataframe(df_anzeige.head(20), use_container_width=True)

        if len(df_anzeige) > 20:
            st.info(f"Zeige 20 von {len(df_anzeige)} Einträgen")

    else:
        st.info("ℹ️ Noch keine Messungen vorhanden. Gib deine ersten Werte ein!")


if __name__ == "__main__":
    main()
