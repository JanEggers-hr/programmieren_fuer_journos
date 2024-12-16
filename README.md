# programmieren_fuer_journos

Material zum 2-Tages-Programmier-Kurs für Journalistinnen und Journalisten


## Die Lektionen

* [Hallo Welt: Wir bringen ein Colab zum Laufen](00_gude_welt.ipynb)
* [Übung 01: Das erste Colab-Notebook zum Laufen bringen](01_erste_schritte.ipynb)
* [Übung 02: Bibliotheken einbauen](02_python_erweitern.ipynb)
* [Übung 03: Eine App mit ipywidgets](03_interaktive_widgets.ipynb)
* [Übung 04: Svelte - Javascript, aber einfach](04_svelte.ipynb)
* [Übung 05: Ein KI-Chatbot in Streamlit - dem Svelte für Python](05_python_streamlit.ipynb)

## Die Software

* [Download-Seite Python-Umgebung "Miniconda"](https://docs.anaconda.com/free/miniconda/)
* [Download-Seite Programmier-Editor VSC](https://code.visualstudio.com/download)
* [KI-Sprachmodell-Betriebsprogramm Ollama](https://ollama.com/download)
* Nur zur Info: [KI-Erweiterung "Continue" für VSC](https://marketplace.visualstudio.com/items?itemName=Continue.continue) - holen wir direkt über den VSC-Marketplace

### Mini-Tutorial: Software installieren

(Setzt voraus, dass ich auf meinem Computer Programme installieren darf - Rechner in Firmennetzen sind damit außen vor, weil sie in der
Regel nicht erlauben, dass man eine Skriptsprache wie Python nutzt - weil die ein potenzielles Sicherheitsproblem in Firmennetzen ist. 
Auch ein Programm wie ollama, das die KI-Sprachmodelle über einen eigenen kleinen Server bereitstellt, wird Misstrauen von Firmen-Admins erregen. 
**Das heißt aber nicht, dass diese Programme allein für den eigenen Rechner ein Sicherheitsrisiko darstellen** - auch wenn das Misstrauen der
Admins vernünftig ist: Lokale Server verraten oft, dass ein Schadprogramm versucht, Daten nach außen zu transferieren, und Skriptsprachen 
können genutzt werden, um schädliche Programme auszuführen - was wir aber nicht tun werden.) 

#### Vorbereitung: Programmiersprache Python installieren, falls nötig

Vielleicht hat unser Rechner längst Python? Um das herauszufinden, müssen wir eine Kommandozeile, bzw. ein Terminal öffnen - auf Windows-Rechnern geht das durch die Windows-Start-Taste und Eintippen
von "cmd" und Return, auf Macs durch Öffnen des Programms "Terminal". (Linuxer wissen sowieso, wie sie zu einer bash kommen.) Es öffnet sich eins dieser Fenster, das aussieht, wie ein Computer-Terminal
aus grauer Vorzeit - ein schwarzes Fenster mit grüner oder weißer Schrift, in das wir unsere Befehle eintippen können. Hier probieren wir jetzt mal Folgendes aus: 

```python --version```

Wenn Python schon installiert ist, bekommen wir als Antwort die Versionsnummer der installierten Python-Umgebung.
![Mac-Terminal](./shell.png)

Wenn der Computer sich beschwert, dass er den Befehl "python" nicht finden kann, oder die Python-Version recht alt ist (3.7 oder früher): 

- [Download: "Miniconda"](https://docs.anaconda.com/free/miniconda/) - das  ist ein Paket mit der Skriptsprache
Python und einigen nützlichen Tools wie der Umgebungs-Verwaltung ```conda```. (Wir kommen dorthin!)

Das Paket für Windows, MacOs, Linux herunterladen und ausführen. Python wird installiert. 

Auf Windows-Rechnern zeigt sich dann übrigens beim Eintippen des "cmd" eine neue Kommandozeile - die "Anaconda Shell".

- Die **Kommandozeile** ausführen: 
    - Auf Mac: Das Programm "terminal" suchen und starten
    - Auf Windows: Startfläche links unten anklicken, "CMD" anklicken (bzw.: nach dem Installieren von Miniconda das "Anaconda Prompt")
    - Auf Linux: Hey, wer Linux hat, kann das auch selbst.
  - Ein wenig zwischen den Ordnern herumnavigieren, mit diesen Befehlen: 
    - ```mkdir name``` legt im augenblicklichen Ordner einen Unterordner ```name``` an
    - ```cd name``` wechselt in den Unterordner
    - ```cd ..``` wechselt zurück in den übergeordneten. 
    - Inhalt des augenblicklichen Ordners anzeigen lassen: ```dir``` (Windows) bzw. ```ls -l``` (Mac und Linux)
  - Auf der Kommandozeile eingeben: ```python``` - wir kriegen ```>>>``` als Eingabeaufforderung
  - In Python rechnen: z.B. ```15 * 5```

#### Programmier-Umgebung VSC installieren und aufrüsten

VSC ist ein kostenloses Programm von Microsoft: ein Editor für Programmcode und eine Umgebung, in der man die Programme ausführen und testen kann. Mit Erweiterungsmodulen kann VSC für alle 
möglichen Zwecke aufgerüstet werden - für uns zum Beispiel um Python-Programme zu nutzen und uns von KI dabei helfen zu lassen. 

* [Download-Seite Programmier-Editor VSC](https://code.visualstudio.com/download)

#### In VSC die Plugins nachrüsten

- Installieren und das erste Mal starten - und Erweiterungen installieren: Am linken Rand ist ein Symbol mit vier kleinen Quadraten, das wie ein Puzzle aussieht - für die Erweiterungen. 
- Darauf klicken, in die Suche "Python" eingeben und die Erweiterungen **Python** und **Python Debugger** installieren. Stammen beide von Microsoft, wie die nächste, deren Namen wir auch erstwieder in die Suche eingeben müssen: "jupyter" - die **juPyter**-Erweiterung ermöglicht uns, so genannte Notebooks zu nutzen, in denen wir Programmcode, Dokumentation und Ausgaben speichern können. 
- Jetzt: "**Continue**" eingeben - das ist die Erweiterung, über die wir KI beim Programmieren direkt in VSC nutzen können. Auch sie installieren. 

#### KI in Continue einklinken

Nach der Installation von Continue und einem evtl. Neustart erscheint am linken Fensterrand das Continue-Symbol - ein Sechseck mit einer Art Rahmen darum. 

Draufklicken - und beim ersten Fenster auf den Reiter "Best" umschalten: Die vorgegebene KI-Einbindung wollen wir nicht nutzen, sondern einen eigenen API-Key verwenden (wer keinen gespendeten verwenden kann: hier kriegt man ihn für[OpenAI](https://platform.openai.com/settings/organization/api-keys) , hier für [Anthropic](https://console.anthropic.com/settings/keys); jeweils sind Kreditkartendaten bzw. Credits vonnöten). Alternativ kann man auch Ollama als KI einbinden. 

- Wer will, kann das "Continue"-Symbol auf den linken oder rechten Sidebar ziehen - dann wird der Chat immer dort angezeigt. 
- Aufruf: Ctrl-L (bzw. Cmd-L auf dem Mac), um eine allgemeine Frage zu stellen bzw. den markierten Code in die Frage zu übernehmen; Ctrl-I (bzw. Cmd-I), um zu beschreiben, welchen Code man sich am Cursor schreiben lassen möchte, Tab, um vorgeschlagenen Code zu übernehmen. 




- VSC star