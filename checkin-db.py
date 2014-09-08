#!/usr/bin/python

import sqlite3 as lite
import sys, time

RegModus = 1
ANR = 0

con = None

con = lite.connect("checkin.db")
with con:
  cur = con.cursor()
  cur.execute("SELECT * FROM deltakere WHERE (RNR='"+sys.argv[1]+"') AND (DatoUt Is Null);")
  if len(cur.fetchall()) > 0:
    cur.execute("UPDATE deltakere SET DatoUt='"+str(int(time.time()))+"' WHERE (RNR='"+sys.argv[1]+"') AND (DatoUt Is Null);")
    print "UT"
  else:
    cur.execute("INSERT INTO deltakere(AID,RNR,DatoInn) VALUES (0,'"+sys.argv[1]+"','"+str(int(time.time()))+"');")
    #print cur.lastrowid
    print "INN"

#while True:
#try:
#  if RegModus == 0:
#    print "Normalmodus!"
#  elif RegModus == 1:
#    print "Aksjonsmodus!"

#  RNR = raw_input("Relasjonsnummer: ")
#  print RNR

#except KeyboardInterrupt:
#  con.close()


con.close()
