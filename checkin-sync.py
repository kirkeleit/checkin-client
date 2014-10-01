#!/usr/bin/python

import sqlite3 as lite
import sys, time

def getserial():
  # Extract serial from cpuinfo file
  cpuserial = "0000000000000000"
  try:
    f = open('/proc/cpuinfo','r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial = line[10:26]
    f.close()
  except:
    cpuserial = "ERROR000000000"

  return cpuserial


import httplib, urllib
con = None

SerieNummer = getserial()

headers = {"Content-type": "application/x-www-form-urlencoded",
          "Accept": "text/plain"}
conn = httplib.HTTPConnection("checkin.sarlog.net")

con = lite.connect("/root/checkin-client/checkin.db")
with con:
  cur = con.cursor()
  cur.execute("SELECT rowid,* FROM registreringer WHERE SynkStatus=0")
  rows = cur.fetchall()
  for row in rows:
    print row

    params = urllib.urlencode({'serienummer': SerieNummer, 'identifikator': row[1], 'tidspunkt': row[2]})
    conn.request("POST", "/index.php/api/registrere/", params, headers)
    response = conn.getresponse()
    print response.status, response.reason

    if response.status == 200:
      cur.execute("UPDATE registreringer SET SynkStatus=1 WHERE rowid=? LIMIT 1;",str(row[0]))
    data = response.read()
    print data
    conn.close()

con.close()
