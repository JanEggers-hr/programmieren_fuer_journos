print ('Hello, World!')
i <- 1
cat(i)
library(tidyr)
library(dplyr)
library(openxlsx)
library(stringr)
library(ggplot2)
daten <- read.xlsx('/Users/halynakubiv/Downloads/BU-TV-22-T62-TV-Staatsangehoerigkeiten_xls.xlsx',
                   colNames = TRUE, startRow = 5)
#Das ist der Schritt vier: Wir haben den Kolumten aussagekräftige Namen vergeben, die sich aus der Zeile vier ergeben)
#daten <- read.csv('/Users/halynakubiv/Downloads/BU-TV-22-T62-TV-Staatsangehoerigkeiten_csv.csv')
#Wir vergeben den Spalten aussagekräftige Namen
daten_neu_df <- daten %>% 
  select(Kategorie = 1, 
         Daten = 2) %>% 
  filter(str_detect(Kategorie, '\\d\\d\\d\\d\\d\\d')) %>% 
  mutate(Kategorie = as.integer(Kategorie))
#Wir haben in der Tabelle in der Spalte "Kategorie" nur die Zellen mit Zahlen ausgewählt (Zeilen 17 und 18)
daten_komplett_df <- daten %>%
  rename(Kategorie = 1) %>% 
  filter(str_detect(Kategorie, '\\d\\d\\d\\d\\d\\d'))
str(daten)
#In der Zeile 23 haben wir überprüft, welche Formate die einzelnen Spalten haben. Wir müssen nun die Spalten 3 bis 201 in die Zahlen umwandeln
daten <- daten %>% 
  mutate(across(3:201, as.numeric))
#Noch mal überprüfen, ob in entsprechenden Spalten tatsächlich numerische Werte vorhanden sind
str(daten)
#Wir versuchen, etwas zu visualisieren
barplot(rbind(daten$Deutschland, daten$Nichtdeutsche.insgesamt),
        names.arg = daten$Straftat)
#Manche Balken schlagen auffalend nach oben hoch, dazu ist die Grafik nicht aussagekräftig genug, wir probieren was anderes, indem wir das Tool für Visualisierung ändern und dafür die Daten präparieren. Dafür brauchen wir erstmal nur drei Spalten. Aus diesen drei Spalten machen wir eine neue Tabelle und bereiten Sie zum Download vor. 
daten_download_df <- daten %>% 
  select(Straftat, Deutschland, Nichtdeutsche.insgesamt)
write.xlsx(daten_download_df, file = 'Polizeistatistik_download')
#Das Diagramm ist trotzdem nicht besonders aussagekräftig, wir wollen eine Gegenüberstellung der Anzahl der Straftaten von Deutschen und Nicht-Deutschen. Die Werte in einer Spalte, beispielsweise in "Nicht Deutsch insegamt" sollen mit einem Minuszeichen versehen werden. 
daten_download_df$Nichtdeutsche.insgesamt <- daten_download_df$Nichtdeutsche.insgesamt*-1
write.xlsx(daten_download_df, file = 'Polizeistatistik_download')
#Die Grafik ist immer noch unübersichtlich, weil unsere Tabelle 1137 Zeilen hat. Wir werden versuchen, diese zu kürzen, indem wir nur die Zeilen ausfiltern, die in der Spalte "Deutsche" und "Nicht-Deutsche" Werte größer als Null haben.
daten_gefiltert_df <- daten_download_df %>% 
  filter((Deutschland > 1000) | (Nichtdeutsche.insgesamt < -1000))

