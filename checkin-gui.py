#!/usr/bin/python
# -*- coding: utf-8 -*-

import curses,re,os,subprocess

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(1)
stdscr.keypad(1)

rnr = ""

maxy, maxx = stdscr.getmaxyx()
#stdscr.hline("-", ((maxx - 23) / 2))
stdscr.addstr("R0DE KORS INNSJEKKING", curses.A_REVERSE)
stdscr.addstr(2, 4, "Tast inn ditt relasjonsnummer etterfulgt av enter.")
stdscr.addstr(4, 4, "Relasjonsnummer: ")

while True:
  event = stdscr.getch()
  if event == ord("q"): break
  elif event == 10:
    stdscr.move(4, 21)
    stdscr.clrtoeol()
    subprocess.call("./checkin-db.py "+rnr, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    #os.system("./checkin-db.py "+rnr+" > /dev/null")
    rnr = ""
    stdscr.move(4, 21)
    stdscr.clrtoeol()
    curses.flash()
  else:
    if re.search("[0-9]", chr(event)):
      if len(rnr) >= 7:
        rnr = rnr[1:]
      rnr = rnr+chr(event)
  stdscr.addstr(4, 21, rnr)

curses.endwin()
