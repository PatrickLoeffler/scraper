#!/usr/bin/python
#<-Alles hinter Hashes/Rauten sind Kommentare.
# Hier importieren wir ein paar Bibliotheken, die nuetzliche Funktionen haben
# und die wir nicht selbst schreiben muessen.
import pdb # importiere den python debugger (brauchen wir hier allerdings nicht)
import urllib2 # importiere die Bibliothek um Daten aus dem Netz zu ziehen
import argparse # importiere Bibliothek um Kommandozeilenparameter lesen zu koennen
import re # importiere Bibliothek fuer regulaere Ausdruecke (Muster finden)

# Lese Kommandozeilenparameter
parser = argparse.ArgumentParser(description= \
					"Parse data from a website")
parser.add_argument("-u", "--url",help="path to URL",required=True) # Kommandozeilenparameter um URL zu uebergeben
parser.add_argument("-p", "--pattern",help="find this pattern",required=True) # KZP um Muster zu uebergeben
args = parser.parse_args() # Lese Kommandozeilenparameter

def parse_file_for_pattern (filehandle,pattern): # Funktion fuer die Suche in einer bestimmten Datei nach einem Muster
	for line in filehandle: # Fuer jede Zeile in dieser Datei
		m = re.search(pattern,line) # Suche nach dem Muster "pattern" in der aktuellen Zeile
		if(m != None): # Falls das Muster != (ungleich) nichts, also "etwas" gefunden
			return m.group(0) # Dann gebe die gematchte Gruppe zurueck

def main(): # Funktion main, hier startet das Skript ueber den Aufruf main() ganz unten
	#fh = open(args.purl,"r") # Oeffe die Datei args.purl (aus Konsole uebergebener Kommandozeilenparameter) im Lesemodus
	fh = urllib2.urlopen(args.url)
	#pattern = "(?<=Aktueller Kurs:) [0-9,]*" # 
	found = parse_file_for_pattern(fh,args.pattern) # Uebergebe Dateihandle und Muster an die Funktion parse_file_for_pattern
	if(found): # Falls etwas gefunden wurde, schreibe es raus/haenge es an eine Datei an.
		print ("I found the following:" + str(found)) # Dann gebe etwas aus
		fh = open("./data","a")
		fh.write(found + "\n")
		fh.close()
		return 0 # Erfolg zurueckgeben
	else: # Falls nichts gefunden wurde
		print("Could not find matching pattern")
		return 1 # Fehler zurueckgeben
		
retval = main() # Rufe die main-Funktion auf
exit(retval) # Verlasse das Skript

# Hey Leute, Valle war ja ganz interessiert an ein bischen Informatik und deswegen habe ich hier mal ein kleines python-skript geschrieben
# was man z.B. benutzen kann um jegliche Informationen aus dem Netz zu ziehen und automatisiert weiterzubenutzen.
# Im Prinzip relativ einfach, laden wir hier die HTML-Datei mit der noetigen Information aus dem Netz, lesen sie ein und suchen ueber Mustererkennung nach der benoetigten Information.
# Z.B koennte man damit Aktienkurse zu bestimmten Zeiten aus dem Netz ziehen und in eine Datei/Datenbank schreiben.
# Um die Info weiterzuverarbeiten koennte man z.B. den Windows scheduler (ich nehme mal an ihr nutzt kein Linux) hernehmen und das Skript beim Computerstart/Alle 60 Minuten oder so automatisch starten lassen.
# Wenn man die Infos jetzt weiterverarbeiten moechte gibt es natuerlich jede Menge Statistiksoftware und auch Tools fuer maschinelles Lernen um Muster in Daten erkennen zu koennen.
#
# Um das Skript aufzurufen muss man erst python installieren (pythonurl) und dann in der Windows-Kommandozeile das Skript starten:
# Python ist sehr anfaengerfreundlich, es gibt super Tutorials und ich kann euch bei Fragen gerne beistehen.
# Es gibt ausserdem tolle Tools im Netz, um eine Umgebung fuer die Kollaboration zu erstellen (d.h. jeder kann mitarbeiten und Code beiwirken), also wenn ihr eine tolle Idee habt koennen wir ja mal zusammen etwas umsetzen.
# 
# Auch wenn ihr jetzt denke, ok ist interessant aber brauch ich nicht, dann wuerde ichs euch trotzdem ans Herz legen, ihr werdet erstaunt sein, wie schnell man da etwas lernt und es ist sehr interessant wie schnell man einfache Dinge erledigen kann und wie komplex scheinbar einfache Sachen manchmal sind.