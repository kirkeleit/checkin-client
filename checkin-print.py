#!/usr/bin/python

import sqlite3 as lite
import sys, time

RegModus = 1
ANR = 0

con = lite.connect("checkin.db")
cur = con.cursor()
cur.execute("INSERT INTO aksjoner VALUES ("+str(time.time())+",0);")
print time.time()

while True:
#  try:
    if RegModus == 0:
      print "Normalmodus!"
    elif RegModus == 1:
      print "Aksjonsmodus!"

    RNR = raw_input("Relasjonsnummer: ")
    print RNR

#  except KeyboardInterrupt:
