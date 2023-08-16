# Library Parrotex: A simple library index and card system.
# Copyright (C) 2023  Foxie EdianiaK a.k.a. F_TEK

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import operator
import webbrowser
from csv import reader as cread
from csv import writer as cwrite
from datetime import date
from json import dump as jdump
from json import load as jload
from json import loads as jloads
import isbnlib as isbn
import PySimpleGUI as sg
import requests
import re
from time import sleep
from math import ceil


# Parrot icon in Base64
ICON = "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".encode()


# Sets opening GUI theme
sg.theme("DarkGreen4")


# Language dictionary
LANGUAGES = {
    "cs": {"name": "Knižní Papouštéka",
           "by": "od",
           "y": "Ano",
           "n": "Ne",
           "ok": "OK",
           "del": "Smazat",
           "err": "Chyba",
           "errFP": "Není doporučeno používat tento program v "
           + "zabezpečených/systémových složkách.\nPokud jej i přesto "
           + "chcete zde spustit, spusťte jej s administrátorskými právy.",
           "errG": "Nelze načíst github.com",
           "up": "Je k dispozici nová verze.\n"
           + "Chcete otevřít stránky vývojáře?",
           "l": "Vyčkejte, prosím...\nVáš požadavek se právě zpracovává.",
           "fB": "knihy",
           "fBD": ["ID", "ISBN", "Autor", "Název", "Žánr", "Umístění", "Stav"],
           "fBS": ["K", "V"],
           "fI": "kody",
           "fC": "karty",
           "fH": "pomoc",
           "m": "Domov",
           "mV": "Zobrazit:",
           "mA": "Vše",
           "a": "Přidat",
           "aQ": "Vyplňte údaje knihy:",
           "aL": "Načíst",
           "aF": "Vyhledat",
           "aS": "Úspěch! Kniha přidána jako #",
           "errA1": "Nelze navázat spojení s ISBN databází.",
           "errA2": "Nelze načíst databazeknih.cz",
           "errA3": "Bylo zadáno neplatné ISBN.",
           "errA4": "Lokace nesmí začínat číslem.",
           "errA5": "Všechny údaje musí být vyplněné.",
           "s": "Hledat",
           "sP": "Zadejte vyhledávací parametry:",
           "sT": "Celkem výsledků: ",
           "c": "Výpujční listy",
           "cV": "Zobrazit",
           "cB": "Vypůjčit",
           "cR": "Vrátit",
           "cM": "Spravovat",
           "cC": "Karta: ",
           "cH": ["ID", "Název", "Datum"],
           "errC1": "Musíte zvolit kartu.",
           "errC2": "Musíte zadat ID knihy.",
           "errC3": "Zadané ID nebylo nalezeno.",
           "errC4": "Nelze si vypůjčit již vypůjčenou knihu.",
           "errC5": "Nelze vrátit nevypůjčenou knihu.",
           "errC6": "Daná karta neobsahuje zadané ID knihy.",
           "cm": "Administrativa",
           "cmN": "Jméno:",
           "cmC": "Zavřít",
           "cmY": "Chcete doopravdy smazat danou kartu?",
           "errCM1": "Musíte zadat jméno karty.",
           "errCM2": "Karta již existuje.",
           "errCM3": "Karta neexistuje.",
           "errCM4": "Nelze smazat kartu s vypůjčenými knihami.",
           "h": "Legenda",
           "hS": "Uložit",
           "u": "Vrátit změnu",
           "uQ": "Změnu čeho byste rádi odvolali?",
           "errU": "Žádná změna k zvrácení.",
           "e": "Upravit",
           "eT": "Upravujete knihu #",
           "eE": "Upravit",
           "eC": "Zrušit",
           "eDQ": "Chcete doopravdy smazat tuto knihu?",
           "errE1": "Nelze smazat vypůjčenou knihu.",
           "errE2": "Nelze změnit lokaci vypůjčené knihy.",
           "errE3": "Lokace nesmí začínat číslem.",
           "errE4": "Všechny údaje musí být vyplněné."},
    "en": {"name": "Library Parrotex",
           "by": "by",
           "y": "Yes",
           "n": "No",
           "ok": "OK",
           "del": "Delete",
           "err": "Error",
           "errFP": "It's not recommended to use this software in "
           + "protected/system folders.\nIf you still want to launch "
           + "it here, launch it with administrator privileges.",
           "errG": "Couldn't load github.com",
           "up": "New version is available.\n"
           + "Would you like to open the developer's website?",
           "l": "Please, wait...\nYour request is being processed right now.",
           "fB": "books",
           "fBD": ["ID", "ISBN", "Author", "Title",
                   "Subject", "Location", "State"],
           "fBS": ["L", "B"],
           "fI": "ids",
           "fC": "cards",
           "fH": "help",
           "m": "Home",
           "mV": "View:",
           "mA": "All",
           "a": "Add",
           "aQ": "Enter book details:",
           "aL": "Load",
           "aF": "Find",
           "aS": "Success! Book added as #",
           "errA1": "Couldn't reach ISBN database.",
           "errA2": "Couldn't load openlibrary.org",
           "errA3": "Invalid ISBN has been entered.",
           "errA4": "Location can't begin with a number.",
           "errA5": "Location can't begin with a number.",
           "s": "Search",
           "sP": "Enter search parameters:",
           "sT": "Number of results: ",
           "c": "Library cards",
           "cV": "View",
           "cB": "Borrow",
           "cR": "Return",
           "cM": "Manage",
           "cC": "Card: ",
           "cH": ["ID", "Title", "Date"],
           "errC1": "You have to select a card.",
           "errC2": "You have to enter the book ID.",
           "errC3": "Entered ID couldn't be found.",
           "errC4": "You can't borrow an already borrowed book.",
           "errC5": "You can't return an already returned book.",
           "errC6": "Selected card doesn't contain entered book ID.",
           "cm": "Administration",
           "cmN": "Name:",
           "cmC": "Close",
           "cmY": "Are you sure you want to delete the selected card?",
           "errCM1": "You have to enter the card name.",
           "errCM2": "This card already exists.",
           "errCM3": "This card doesn't exist.",
           "errCM4": "You can't delete a card with borrowed books.",
           "h": "Key",
           "hS": "Save",
           "u": "Undo",
           "uQ": "Which one would you like to undo?",
           "errU": "Nothing to undo.",
           "e": "Edit",
           "eT": "Editing book #",
           "eC": "Cancel",
           "eDQ": "Are you sure you want to delete this book?",
           "errE1": "You can't delete a borrowed book.",
           "errE2": "You can't change a location of a borrowed book.",
           "errE3": "Location can't begin with a number.",
           "errE4": "All details must be filled in."}
    }


# Language check and selector (+ folder write check)
try:
    with open("lang.txt", "x", encoding="utf-8") as f:
        LNG = ""
        f.close()
except FileExistsError:
    with open("lang.txt", "r", encoding="utf-8") as f:
        LNG = f.read()
        f.close()
except PermissionError:
    msg = LANGUAGES["cs"]["err"] + " #FP: " + LANGUAGES["cs"]["errFP"] + "\n"
    + LANGUAGES["en"]["err"] + " #FP: " + LANGUAGES["en"]["errFP"]
    pLO = [[sg.T(msg)],
           [sg.P(),
            sg.B("OK", k="OK")]]
    title = msg[0:(msg.find(":"))]
    pWin = sg.Window(title, pLO, icon=ICON)
    pEv, pVal = pWin.read()
    pWin.close()

if LNG == "":
    lLO = [[sg.P(), sg.T("Jazyk / Language"), sg.P()],
           [sg.T("Vítá vás, Knižní Papouštéka!"),
            sg.P(), sg.B("Čeština", k="cs")],
           [sg.T("Welcome to the Library Parrotex!"),
            sg.P(), sg.B("English", k="en")]]
    lWin = sg.Window("Library Parrotex", lLO, icon=ICON)
    lEv, lVal = lWin.read()

    lWin.close()
    if lEv is None:
        pass
    else:
        LNG = lEv
        with open("lang.txt", "w", encoding="utf-8") as f:
            f.write(LNG)
            f.close()


# List of global constants
LANG = LANGUAGES[LNG]
ROWS = []
FIELDS = []
IDS = {}
CARDS = {}
HELP = ""
SORT = 0
LAST_LOC = ""
VERSION = "v2.2.1"
WINDOW = "m"
CHANGED = True


# Defines pop-up windows
def Popups(tip: str, msg: str) -> str:
    title = ""
    pLO = [[]]

    if tip == "yn":
        pLO = [[sg.T(msg)],
               [sg.P(),
                sg.B(LANG["y"], k="Yes"),
                sg.B(LANG["n"], k="No")]]
        title = msg
    elif tip == "e":
        pLO = [[sg.T(msg)],
               [sg.P(),
                sg.B(LANG["ok"], k="OK")]]
        title = msg[0:(msg.find(":"))]

    pWin = sg.Window(title, pLO, icon=ICON)
    pEv, pVal = pWin.read()
    pWin.close()
    return pEv


def Loading() -> sg.Window:
    pLO = [[sg.T(LANG["l"])]]
    pWin = sg.Window("",
                     pLO,
                     disable_close=True,
                     no_titlebar=True,
                     finalize=True)
    pWin.read(0)
    sleep(0.1)
    return pWin


# Creates necessary files on first launch
try:
    with open((LANG["fB"] + ".csv"), "x", encoding="utf-8") as f:
        _data = LANG["fBD"]
        _wrt = cwrite(f)
        _wrt.writerow(_data)
        f.close()
except FileExistsError:
    pass

try:
    with open((LANG["fI"] + ".json"), "x", encoding="utf-8") as f:
        _data = {"test": 0}
        jdump(_data, f)
        f.close()
except FileExistsError:
    pass

try:
    with open((LANG["fC"] + ".json"), "x", encoding="utf-8") as f:
        _data = {"LIST": []}
        jdump(_data, f)
        f.close()
except FileExistsError:
    pass

try:
    with open((LANG["fH"] + ".txt"), "x", encoding="utf-8") as f:
        f.close()
except FileExistsError:
    pass


def load() -> None:
    """
    (Re)Loads all constants.
    @ ROWS, FIELDS, IDS, CARDS, HELP

    - Loads data from books.csv, ids.json, cards.json and help.txt
    - Sorts ROWS
    """
    global ROWS, FIELDS, IDS, CARDS, HELP
    ROWS = []
    FIELDS = []
    IDS = {}
    CARDS = {}
    HELP = ""

    with open((LANG["fB"] + ".csv"), "r", encoding="utf-8") as f:
        _raw = cread(f)
        FIELDS = next(_raw)
        for _row in _raw:
            if _row != []:
                ROWS.append(_row)
        f.close()

    with open((LANG["fI"] + ".json"), "r", encoding="utf-8") as f:
        IDS = jload(f)
        f.close()

    with open((LANG["fC"] + ".json"), "r", encoding="utf-8") as f:
        CARDS = jload(f)
        f.close()

    with open((LANG["fH"] + ".txt"), "r", encoding="utf-8") as f:
        HELP = f.read()
        f.close()

    for i in reversed((SORT, 0)):
        ROWS = sorted(ROWS, key=operator.itemgetter(i))


def main() -> None:
    """
    The Main Window.
    @ WINDOW, SORT, CHANGED
    # page, num

    - Prepares Main Window
    """
    global WINDOW, SORT, CHANGED, page, num

    if CHANGED:
        page = 0
        num = 30
        CHANGED = False

    if num == -1:
        start = 0
        end = len(ROWS)
        final = 0
    else:
        start = 0 + (num * page)
        end = num + (num * page)
        final = ceil(len(ROWS)/num)-1

    mLO = [[sg.P(),
            sg.B("[" + LANG["m"] + "]"),
            sg.B(LANG["a"], k="Add"),
            sg.B(LANG["s"], k="Search"),
            sg.B(LANG["c"], k="Cards"),
            sg.B(LANG["h"], k="Help"),
            sg.B(LANG["u"], k="Undo"),
            sg.P()],
           [sg.P(),
            sg.T(LANG["mV"]),
            sg.DD([30, 60, 90, 120, LANG["mA"]],
                  num,
                  k="Num",
                  enable_events=True)],
           [sg.Table(values=ROWS[start:end],
                     headings=FIELDS,
                     auto_size_columns=True,
                     max_col_width=30,
                     justification="center",
                     num_rows=30,
                     enable_click_events=True,
                     alternating_row_color="#a0ca6d",
                     k="Table")],
           [sg.B("<<", k="Start"),
            sg.B("<", k="Prev"),
            sg.P(),
            sg.B("[" + str(page+1) + "/" + str(final+1) + "]"),
            sg.P(),
            sg.B(">", k="Next"),
            sg.B(">>", k="End")]]
    mWin = sg.Window(LANG["name"], mLO, icon=ICON)
    mEv, mVal = mWin.read()

    mWin.close()
    if mEv is None:
        WINDOW = ""
    else:
        if mVal["Num"] != num:
            page = 0

        if mVal["Num"] == LANG["mA"]:
            num = -1
        else:
            try:
                num = int(mVal["Num"])
            except TypeError:
                pass
            except ValueError:
                pass

    if mEv == "Add":
        WINDOW = "a"
        CHANGED = True
    if mEv == "Search":
        WINDOW = "s"
        CHANGED = True
    if mEv == "Cards":
        WINDOW = "c"
        CHANGED = True
    if mEv == "Help":
        WINDOW = "h"
    if mEv == "Undo":
        WINDOW = "u"
    if mEv == "Start":
        page = 0
    if mEv == "Prev" and page != 0:
        page -= 1
    if mEv == "Next" and page != final:
        page += 1
    if mEv == "End":
        page = final
    if type(mEv) == tuple:
        if mEv[2][0] == -1 and mEv[2][1] != -1:
            SORT = mEv[2][1]
        elif mEv[2][0] is not None:
            if num == -1:
                edit(mEv[2][0])
            else:
                _row = mEv[2][0] + (num * page)
                edit(_row)


def save(files: str) -> None:
    """
    Saves and Backups selected files.
    < Files

    - Available files:
      - b - LANG["fB"].csv + LANG["fI"].json
      - c - LANG["fC"].json
      - h - LANG["fH"].txt
    """
    if "b" in files:
        _old_fields = []
        _old_rows = []

        with open((LANG["fB"] + ".csv"), "r", encoding="utf-8") as f:
            _raw = cread(f)
            _old_fields = next(_raw)
            for _row in _raw:
                _old_rows.append(_row)
            f.close()

        with open((LANG["fB"] + ".csv.bak"), "w", encoding="utf-8") as f:
            _wrt = cwrite(f)
            _wrt.writerow(_old_fields)
            _wrt.writerows(_old_rows)
            f.close()

        with open((LANG["fB"] + ".csv"), "w", encoding="utf-8") as f:
            _wrt = cwrite(f)
            _wrt.writerow(FIELDS)
            _wrt.writerows(ROWS)
            f.close()

        _old_ids = {}

        with open((LANG["fI"] + ".json"), "r", encoding="utf-8") as f:
            _old_ids = jload(f)
            f.close()

        with open((LANG["fI"] + ".json.bak"), "w", encoding="utf-8") as f:
            jdump(_old_ids, f)
            f.close()

        with open((LANG["fI"] + ".json"), "w", encoding="utf-8") as f:
            jdump(IDS, f)
            f.close()
    if "c" in files:
        _old_cards = {}

        with open((LANG["fC"] + ".json"), "r", encoding="utf-8") as f:
            _old_cards = jload(f)
            f.close()

        with open((LANG["fC"] + ".json.bak"), "w", encoding="utf-8") as f:
            jdump(_old_cards, f)
            f.close()

        with open((LANG["fC"] + ".json"), "w", encoding="utf-8") as f:
            jdump(CARDS, f)
            f.close()
    if "h" in files:
        _old_help = ""

        with open((LANG["fH"] + ".txt"), "r", encoding="utf-8") as f:
            _old_help = f.read()
            f.close()

        with open((LANG["fH"] + ".txt.bak"), "w", encoding="utf-8") as f:
            f.write(_old_help)
            f.close()

        with open((LANG["fH"] + ".txt"), "w", encoding="utf-8") as f:
            f.write(HELP)
            f.close()


def undo() -> None:
    """
    Undoes one modification to selected file.
    @ WINDOW, CHANGED

    - Available files:
      - b - books.csv + ids.json
      - c - cards.json
      - h - help.txt
    """
    global WINDOW, CHANGED

    uLO = [[sg.P(),
            sg.B(LANG["m"], k="Main"),
            sg.B(LANG["a"], k="Add"),
            sg.B(LANG["s"], k="Search"),
            sg.B(LANG["c"], k="Cards"),
            sg.B(LANG["h"], k="Help"),
            sg.B("[" + LANG["u"] + "]"),
            sg.P()],
           [sg.T(LANG["uQ"]),
            sg.P(),
            sg.B(LANG["fB"].capitalize(), k="b"),
            sg.B(LANG["fC"].capitalize(), k="c"),
            sg.B(LANG["h"], k="h")]]
    uWin = sg.Window(LANG["name"], uLO, icon=ICON)
    uEv, uVal = uWin.read()

    uWin.close()
    if uEv is None:
        WINDOW = ""
    elif uEv == "Main":
        WINDOW = "m"
        CHANGED = True
    elif uEv == "Add":
        WINDOW = "a"
        CHANGED = True
    elif uEv == "Search":
        WINDOW = "s"
        CHANGED = True
    elif uEv == "Cards":
        WINDOW = "c"
        CHANGED = True
    elif uEv == "Help":
        WINDOW = "h"
    else:
        file = uEv
        pWin = Loading()

        try:
            if file == "b":
                _new_fields = []
                _new_rows = []

                with open((LANG["fB"] + ".csv.bak"),
                          "r", encoding="utf-8") as f:
                    _raw = cread(f)
                    _new_fields = next(_raw)
                    for _row in _raw:
                        _new_rows.append(_row)
                    f.close()

                with open((LANG["fB"] + ".csv.bak"),
                          "w", encoding="utf-8") as f:
                    _wrt = cwrite(f)
                    _wrt.writerow(FIELDS)
                    _wrt.writerows(ROWS)
                    f.close()

                with open((LANG["fB"] + ".csv"),
                          "w", encoding="utf-8") as f:
                    _wrt = cwrite(f)
                    _wrt.writerow(_new_fields)
                    _wrt.writerows(_new_rows)
                    f.close()

                _new_ids = {}

                with open((LANG["fI"] + ".json.bak"),
                          "r", encoding="utf-8") as f:
                    _new_ids = jload(f)
                    f.close()

                with open((LANG["fI"] + ".json.bak"),
                          "w", encoding="utf-8") as f:
                    jdump(IDS, f)
                    f.close()

                with open((LANG["fI"] + ".json"),
                          "w", encoding="utf-8") as f:
                    jdump(_new_ids, f)
                    f.close()
            if file == "c":
                _new_cards = {}

                with open((LANG["fC"] + ".json.bak"),
                          "r", encoding="utf-8") as f:
                    _new_cards = jload(f)
                    f.close()

                with open((LANG["fC"] + ".json.bak"),
                          "w", encoding="utf-8") as f:
                    jdump(CARDS, f)
                    f.close()

                with open((LANG["fC"] + ".json"),
                          "w", encoding="utf-8") as f:
                    jdump(_new_cards, f)
                    f.close()
            if file == "h":
                _new_help = ""

                with open((LANG["fH"] + ".txt.bak"),
                          "r", encoding="utf-8") as f:
                    _new_help = f.read()
                    f.close()

                with open((LANG["fH"] + ".txt.bak"),
                          "w", encoding="utf-8") as f:
                    f.write(HELP)
                    f.close()

                with open((LANG["fH"] + ".txt"),
                          "w", encoding="utf-8") as f:
                    f.write(_new_help)
                    f.close()

            pWin.close()
        except FileNotFoundError:
            pWin.close()
            Popups("e", LANG["err"] + " #U: " + LANG["errU"])


def expander(abbr: str) -> None:
    global ROWS

    for i in range(0, len(ROWS)):
        _id = ROWS[i][0]
        if _id[0] == abbr:
            if len(_id[1:]) != len(str(IDS[abbr])):
                ROWS[i][0] = abbr + _id[1:].rjust(len(str(IDS[abbr])), "0")
                if ROWS[i][6] != LANG["fBS"][0]:
                    card = CARDS[ROWS[i][6][2:]]
                    for j in range(0, len(card)):
                        if card[j][0] == _id:
                            CARDS[ROWS[i][6][2:]][j][0] = ROWS[i][0]
                    save("c")


def add() -> None:
    """
    Makes it possible to add new book records.
    @ LAST_LOC, WINDOW, CHANGED
    # err, _inISBN, r

    - Preloads data from ISBN code and openlibrary.org record.
    - Lets the user add other data manually.
    """
    global LAST_LOC, WINDOW, CHANGED, err, _inISBN, r

    if CHANGED:
        err = ""
        _inISBN = ""
        r = {
             "ID": "",
             "ISBN": "",
             "Author": "",
             "Title": "",
             "Genre": "",
             "Location": LAST_LOC,
             "State": LANG["fBS"][0]
        }
        CHANGED = False

    aLO = [[sg.P(),
            sg.B(LANG["m"], k="Main"),
            sg.B("[" + LANG["a"] + "]"),
            sg.B(LANG["s"], k="Search"),
            sg.B(LANG["c"], k="Cards"),
            sg.B(LANG["h"], k="Help"),
            sg.B(LANG["u"], k="Undo"),
            sg.P()],
           [sg.T(LANG["aQ"])],
           [sg.T(LANG["fBD"][1] + ":"), sg.I(r["ISBN"], k="inISBN"),
            sg.B(LANG["aL"], k="Load")],
           [sg.T(LANG["fBD"][2] + ":"), sg.I(r["Author"], k="author")],
           [sg.T(LANG["fBD"][3] + ":"), sg.I(r["Title"], k="title"),
            sg.B(LANG["aF"], k="Find")],
           [sg.T(LANG["fBD"][4] + ":"), sg.I(r["Genre"], k="genre")],
           [sg.T(LANG["fBD"][5] + ":"), sg.I(r["Location"], k="location")],
           [sg.T(LANG["fBD"][6] + ":"), sg.I(LANG["fBS"][0], disabled=True)],
           [sg.T(err)],
           [sg.P(), sg.B(LANG["a"], k="Add", bind_return_key=True)]]
    aWin = sg.Window(LANG["name"], aLO, icon=ICON)
    aEv, aVal = aWin.read()

    err = ""

    aWin.close()
    if aEv is None:
        WINDOW = ""
    else:
        r["Author"] = aVal["author"].replace(",", ";")
        r["Title"] = aVal["title"].replace(",", ";")
        r["Genre"] = aVal["genre"].replace(",", ";")
        r["Location"] = aVal["location"].replace(",", ";")
        LAST_LOC = r["Location"]

    if aEv == "Main":
        WINDOW = "m"
        CHANGED = True
    if aEv == "Search":
        WINDOW = "s"
        CHANGED = True
    if aEv == "Cards":
        WINDOW = "c"
        CHANGED = True
    if aEv == "Help":
        WINDOW = "h"
    if aEv == "Undo":
        WINDOW = "u"
    if aEv == "Load":
        pWin = Loading()

        _inISBN = aVal["inISBN"]
        _inISBN = _inISBN.replace("-", "")
        if isbn.is_isbn10(_inISBN) or isbn.is_isbn13(_inISBN):
            r["ISBN"] = _inISBN

            try:
                _data = isbn.meta(_inISBN)
            except isbn.dev._exceptions.ISBNLibURLError:
                pWin.close()
                Popups("e", LANG["err"] + " #A1: " + LANG["errA1"])
                pWin = Loading()
            finally:
                try:
                    r["Title"] = _data["Title"]
                except KeyError:
                    pass

                try:
                    r["Author"] = "; ".join(author
                                            for author
                                            in _data["Authors"])
                except KeyError:
                    pass

            g = ""
            if LNG == "cs":
                try:
                    db = requests.get(url=("https://www.databazeknih.cz/"
                                           + "search?q=" + _inISBN
                                           + "&hledat="),
                                      allow_redirects=True)
                except requests.exceptions.ConnectionError:
                    pWin.close()
                    Popups("e", LANG["err"] + " #A2: " + LANG["errA2"])
                    pWin = Loading()
                else:
                    if db.status_code == 200:
                        db = db.text

                        start = db.find("<h5 itemprop='genre'>") + 21
                        end = start + db[start:].find("</h5>")
                        db = db[start:end]
                        db = db.replace("</a>, ", "\n")
                        db = db.replace("</a>", "")
                        db = re.split("<.*'>", db)

                        db.pop(0)

                        for i in db:
                            g += i + "; "

                        g = g[:-2]
                        g = g.replace("\n", "")
                        g = g.replace(",", ";")
                    else:
                        pWin.close()
                        Popups("e", LANG["err"] + " #A2: " + LANG["errA2"])
                        pWin = Loading()
            elif LNG == "en":
                try:
                    db = requests.get(url=("https://openlibrary.org/isbn/"
                                           + _inISBN),
                                      allow_redirects=True)
                except requests.exceptions.ConnectionError:
                    pWin.close()
                    Popups("e", LANG["err"] + " #A2: " + LANG["errA2"])
                    pWin = Loading()
                else:
                    if db.status_code == 200:
                        db = db.text

                        start = db.find("<h6>Subjects</h6>") + 18
                        end = start + db[start:].find("</span>")
                        db = db[start:end]
                        db = db.replace("</a>,", "")
                        db = db.replace("</a>", "")
                        db = re.split(' *<.*">', db)

                        db.pop(0)

                        for i in db:
                            g += i + "; "

                        g = g[:-2]
                        g = g.replace("&amp;", "&")
                        g = g.replace("\n", "")
                        g = g.replace(",", ";")
                    else:
                        pWin.close()
                        Popups("e", LANG["err"] + " #A2: " + LANG["errA2"])
                        pWin = Loading()

            r["Genre"] = g
            pWin.close()
        else:
            Popups("e", LANG["err"] + " #A3: " + LANG["errA3"])
            pWin.close()
    if aEv == "Find":
        if LNG == "cs":
            webbrowser.open(url=("https://www.databazeknih.cz/search?q="
                                 + aVal["title"]
                                 + "&hledat="))
        elif LNG == "en":
            webbrowser.open(url=("https://openlibrary.org/search?q="
                                 + aVal["title"]
                                 + "&mode=everything"))
    if aEv == "Add":
        if (aVal["author"] != ""
                and aVal["title"] != ""
                and aVal["genre"] != ""
                and aVal["location"] != ""):
            abbr = r["Location"][0]

            try:
                int(abbr)
            except ValueError:
                pWin = Loading()
                if abbr not in IDS:
                    IDS[abbr] = 0

                IDS[abbr] += 1

                if len(str(IDS[abbr] - 1)) != len(str(IDS[abbr])):
                    expander(abbr)

                r["ID"] = abbr + str(IDS[abbr])

                ROWS.append([r["ID"],
                             r["ISBN"],
                             r["Author"],
                             r["Title"],
                             r["Genre"],
                             r["Location"],
                             r["State"]])
                save("b")
                pWin.close()
                err = LANG["aS"] + r["ID"]
                _inISBN = ""
                r = {
                    "ID": "",
                    "ISBN": "",
                    "Author": "",
                    "Title": "",
                    "Genre": "",
                    "Location": LAST_LOC,
                    "State": LANG["fBS"][0]
                }
            else:
                err = LANG["err"] + " #A4: " + LANG["errA4"]
        else:
            err = LANG["err"] + " #A5: " + LANG["errA5"]


def search() -> None:
    """
    Allows the search of book records.
    @ WINDOW, CHANGED
    # par, res, num

    - Possible filters:
      - Genre
      - Author
      - Title
    """
    global WINDOW, CHANGED, par, res, num
    if CHANGED:
        par = ["", "", ""]
        res = []
        num = 0
        CHANGED = False

    sLO = [[sg.P(),
            sg.B(LANG["m"], k="Main"),
            sg.B(LANG["a"], k="Add"),
            sg.B("[" + LANG["s"] + "]"),
            sg.B(LANG["c"], k="Cards"),
            sg.B(LANG["h"], k="Help"),
            sg.B(LANG["u"], k="Undo"),
            sg.P()],
           [sg.T(LANG["sP"])],
           [sg.T("1. " + LANG["fBD"][4] + ":"), sg.I(par[0], k="zero")],
           [sg.T("2. " + LANG["fBD"][2] + ":"), sg.I(par[1], k="one")],
           [sg.T("3. " + LANG["fBD"][3] + ":"), sg.I(par[2], k="two")],
           [sg.T(LANG["sT"] + str(num)),
            sg.P(),
            sg.B(LANG["s"], k="Search", bind_return_key=True)],
           [sg.Table(values=res,
                     headings=FIELDS,
                     auto_size_columns=True,
                     max_col_width=30,
                     justification="center",
                     num_rows=30,
                     enable_click_events=True,
                     alternating_row_color="#a0ca6d",
                     k="Table")]]
    sWin = sg.Window(LANG["name"], sLO, icon=ICON)
    sEv, sVal = sWin.read()

    sWin.close()
    if sEv is None:
        WINDOW = ""
    else:
        par = [sVal["zero"].lower(),
               sVal["one"].lower(),
               sVal["two"].lower()]

    if sEv == "Main":
        WINDOW = "m"
        CHANGED = True
    if sEv == "Add":
        WINDOW = "a"
        CHANGED = True
    if sEv == "Cards":
        WINDOW = "c"
        CHANGED = True
    if sEv == "Help":
        WINDOW = "h"
    if sEv == "Undo":
        WINDOW = "u"
    if type(sEv) == tuple:
        if (sEv[2][0] != -1
                and sEv[2][1] != -1
                and sEv[2][0] is not None):
            pWin = Loading()
            id = res[sEv[2][0]][0]

            for i in range(0, len(ROWS)):
                if ROWS[i][0] == id:
                    pWin.close()
                    edit(i)
    if sEv == "Search":
        pWin = Loading()
        res = []

        if par[0] != "":
            for i in ROWS:
                if par[0] in i[4].lower():
                    res.append(i)
        if par[1] != "":
            if res != []:
                for i in res:
                    if par[1] not in i[2].lower():
                        res.pop(i)
            else:
                for i in ROWS:
                    if par[1] in i[2].lower():
                        res.append(i)
        if par[2] != "":
            if res != []:
                for i in res:
                    if par[2] not in i[3].lower():
                        res.pop(i)
            else:
                for i in ROWS:
                    if par[2] in i[3].lower():
                        res.append(i)

        pWin.close()
        num = len(res)


def cards() -> None:
    """
    The library card interface.
    @ WINDOW, CHANGED
    # vw, card, err

    - Add and remove borrowed books from selected card.
    - See when selected card borrowed which book.
    - Create and/or delete library cards.
    """
    global WINDOW, CHANGED, vw, card, err
    if CHANGED:
        vw = [[]]
        card = ""
        err = ""
        CHANGED = False

    if card != "" and card in CARDS["LIST"]:
        vw = CARDS[card]

    cLO = [[sg.P(),
            sg.B(LANG["m"], k="Main"),
            sg.B(LANG["a"], k="Add"),
            sg.B(LANG["s"], k="Search"),
            sg.B("[" + LANG["c"] + "]"),
            sg.B(LANG["h"], k="Help"),
            sg.B(LANG["u"], k="Undo"),
            sg.P()],
           [sg.T("ID"),
            sg.I(k="id"),
            sg.P(),
            sg.DD(CARDS["LIST"], card, k="Card"),
            sg.B(LANG["cV"], k="View")],
           [sg.B(LANG["cB"], k="Borrow"),
            sg.B(LANG["cR"], k="Return"),
            sg.P(),
            sg.B(LANG["cM"], k="Manage")],
           [sg.T(LANG["cC"] + card), sg.P(), sg.T(err), sg.P(), sg.P()],
           [sg.Table(values=vw,
                     headings=LANG["cH"],
                     auto_size_columns=True,
                     max_col_width=30,
                     justification="center",
                     num_rows=30,
                     alternating_row_color="#a0ca6d",
                     k="Table")]]
    cWin = sg.Window(LANG["name"], cLO, icon=ICON)
    cEv, cVal = cWin.read()

    err = ""

    cWin.close()
    if cEv is None:
        WINDOW = ""
    else:
        card = cVal["Card"]

    if cEv == "Main":
        WINDOW = "m"
        CHANGED = True
    if cEv == "Add":
        WINDOW = "a"
        CHANGED = True
    if cEv == "Search":
        WINDOW = "s"
        CHANGED = True
    if cEv == "Help":
        WINDOW = "h"
    if cEv == "Undo":
        WINDOW = "u"
    if cEv == "View":
        if cVal["Card"] not in CARDS["LIST"]:
            card = ""
        else:
            vw = CARDS[card]
    if cEv == "Borrow":
        if card == "":
            err = LANG["err"] + " #C1: " + LANG["errC1"]
        elif cVal["id"] == "":
            err = LANG["err"] + " #C2: " + LANG["errC2"]
        else:
            pWin = Loading()
            err = LANG["err"] + " #C3: " + LANG["errC3"]
            for row in ROWS:
                if row[0] == cVal["id"]:
                    if row[6] != LANG["fBS"][0]:
                        err = LANG["err"] + " #C4: " + LANG["errC4"]
                    else:
                        err = ""
                        CARDS[card].append([row[0],
                                            row[3],
                                            str(date.today())])
                        num = ROWS.index(row)
                        ROWS[num][6] = LANG["fBS"][1] + ":" + card
                        save("bc")
            pWin.close()
    if cEv == "Return":
        if card == "":
            err = LANG["err"] + " #C1: " + LANG["errC1"]
        elif cVal["id"] == "":
            err = LANG["err"] + " #C2: " + LANG["errC2"]
        else:
            pWin = Loading()
            err = LANG["err"] + " #C3: " + LANG["errC3"]
            for row in ROWS:
                if row[0] == cVal["id"]:
                    if row[6] == LANG["fBS"][0]:
                        err = LANG["err"] + " #C5: " + LANG["errC5"]
                    else:
                        err = LANG["err"] + " #C6: " + LANG["errC6"]
                        for entry in CARDS[card]:
                            if entry[0] == cVal["id"]:
                                err = ""
                                num = CARDS[card].index(entry)
                                CARDS[card].pop(num)
                                num = ROWS.index(row)
                                ROWS[num][6] = LANG["fBS"][0]
                                save("bc")
            pWin.close()
    if cEv == "Manage":
        err = ""
        while True:
            cmLO = [[sg.T(LANG["cmN"]),
                    sg.I(k="name"),
                    sg.B(LANG["a"], k="Add"),
                    sg.B(LANG["del"], k="Delete")],
                    [sg.T(err), sg.P(), sg.B(LANG["cmC"], k="Close")]]
            cmWin = sg.Window((LANG["name"] + ": " + LANG["cm"]),
                              cmLO,
                              icon=ICON)
            cmEv, cmVal = cmWin.read()

            err = ""

            cmWin.close()
            if cmEv is None or cmEv == "Close":
                break
            else:
                name = cmVal["name"]

            if cmEv == "Add":
                if name == "":
                    err = LANG["err"] + " #CM1: " + LANG["errCM1"]
                elif name in CARDS["LIST"]:
                    err = LANG["err"] + " #CM2: " + LANG["errCM2"]
                else:
                    pWin = Loading()
                    CARDS["LIST"].append(name)
                    CARDS[name] = []
                    save("c")
                    pWin.close()
                    break
            if cmEv == "Delete":
                if name == "":
                    err = LANG["err"] + " #CM1: " + LANG["errCM1"]
                elif name not in CARDS["LIST"]:
                    err = LANG["err"] + " #CM3: " + LANG["errCM3"]
                elif CARDS[name] != []:
                    err = LANG["err"] + " #CM4: " + LANG["errCM4"]
                else:
                    ans = Popups("yn", LANG["cmY"])
                    if ans == "Yes":
                        pWin = Loading()
                        CARDS["LIST"].remove(name)
                        CARDS.pop(name)
                        save("c")
                        pWin.close()
                        break


def help() -> None:
    """
    A simple text file interface.
    @ HELP, WINDOW, CHANGED

    - Allows reading and editing help.txt
    """
    global HELP, WINDOW, CHANGED
    hLO = [[sg.P(),
            sg.B(LANG["m"], k="Main"),
            sg.B(LANG["a"], k="Add"),
            sg.B(LANG["s"], k="Search"),
            sg.B(LANG["c"], k="Cards"),
            sg.B("[" + LANG["h"] + "]"),
            sg.B(LANG["u"], k="Undo"),
            sg.P()],
           [sg.T(LANG["h"] + ":")],
           [sg.Multiline(HELP, k="help", size=(60, 20))],
           [sg.P(), sg.B(LANG["hS"], k="Save")]]
    hWin = sg.Window(LANG["name"], hLO, icon=ICON)
    hEv, hVal = hWin.read()

    hWin.close()
    if hEv is None:
        WINDOW = ""
    if hEv == "Main":
        WINDOW = "m"
        CHANGED = True
    if hEv == "Add":
        WINDOW = "a"
        CHANGED = True
    if hEv == "Search":
        WINDOW = "s"
        CHANGED = True
    if hEv == "Cards":
        WINDOW = "c"
        CHANGED = True
    if hEv == "Undo":
        WINDOW = "u"
    if hEv == "Save":
        pWin = Loading()
        HELP = hVal["help"]
        save("h")
        pWin.close()


def edit(row: int) -> None:
    """
    Makes editing book records possible.
    @ CHANGED

    - You can edit:
      - Author(s)
      - Title
      - Genre(s)
      - Location - also changes the ID
    """
    global CHANGED

    CHANGED = True
    r = ROWS[row]
    loc = r[5]
    err = ""

    while True:
        eLO = [[sg.T(LANG["eT"] + r[0])],
               [sg.T(LANG["fBD"][1] + ":"), sg.I(r[1], k="inISBN")],
               [sg.T(LANG["fBD"][2] + ":"), sg.I(r[2], k="author")],
               [sg.T(LANG["fBD"][3] + ":"),
                sg.I(r[3], k="title"),
                sg.B(LANG["aF"], k="Search")],
               [sg.T(LANG["fBD"][4] + ":"), sg.I(r[4], k="genre")],
               [sg.T(LANG["fBD"][5] + ":"), sg.I(r[5], k="location")],
               [sg.T(LANG["fBD"][6] + ":"), sg.I(r[6], disabled=True)],
               [sg.T(err)],
               [sg.B(LANG["eC"], k="Cancel"),
                sg.P(),
                sg.B(LANG["del"], k="Delete"),
                sg.B(LANG["e"], k="Edit", bind_return_key=True)]]
        eWin = sg.Window(LANG["name"] + ": " + LANG["e"], eLO, icon=ICON)
        eEv, eVal = eWin.read()

        err = ""

        eWin.close()
        if eEv is None or eEv == "Cancel":
            break
        else:
            r[1] = eVal["inISBN"].replace("-", "")
            r[2] = eVal["author"].replace(",", ";")
            r[3] = eVal["title"].replace(",", ";")
            r[4] = eVal["genre"].replace(",", ";")
            r[5] = eVal["location"].replace(",", ";")

        if eEv == "Search":
            if LNG == "cs":
                webbrowser.open(url=("https://www.databazeknih.cz/search?q="
                                     + eVal["title"]
                                     + "&hledat="))
            elif LNG == "en":
                webbrowser.open(url=("https://openlibrary.org/search?q="
                                     + eVal["title"]
                                     + "&mode=everything"))
        if eEv == "Delete":
            if r[6] == LANG["fBS"][0]:
                ans = Popups("yn", LANG["eDQ"])
                if ans == "Yes":
                    ROWS.pop(row)
                    pWin = Loading()
                    save("b")
                    pWin.close()

                    break
            else:
                Popups("e", LANG["err"] + " #E1: " + LANG["errE1"])
        if eEv == "Edit":
            if r[2] != "" and r[3] != "" and r[4] != "" and r[5] != "":
                if r[5] != loc and r[6] != LANG["fBS"][0]:
                    err = LANG["err"] + " #E2: " + LANG["errE2"]
                else:
                    pWin = Loading()
                    if r[5][0] != loc[0]:
                        abbr = r[5][0]

                        try:
                            int(abbr)
                        except ValueError:
                            pass
                        else:
                            err = LANG["err"] + " #E3: " + LANG["errE3"]
                            continue

                        if abbr not in IDS:
                            IDS[abbr] = 0

                        IDS[abbr] += 1

                        if len(str(IDS[abbr] - 1)) != len(str(IDS[abbr])):
                            expander(abbr)

                        r[0] = abbr + str(IDS[abbr])

                    ROWS[row] = r
                    save("b")
                    pWin.close()
                    break
            else:
                err = LANG["err"] + " #E4: " + LANG["errE4"]


# Splash image
spLO = [[sg.P(),
         sg.T(LANG["name"]),
         sg.P()],
        [sg.P(),
         sg.Image(ICON),
         sg.P()],
        [sg.T(VERSION),
         sg.P(),
         sg.T(LANG["by"] + " F_TEK")]]
spWin = sg.Window("",
                  spLO,
                  no_titlebar=True,
                  disable_close=True,
                  disable_minimize=True,
                  keep_on_top=True)
spWin.read(1500)
spWin.close()

LICENSE = """Library Parrotex  Copyright (C) 2023  Foxie EdianiaK a.k.a. F_TEK
- This program comes with ABSOLUTELY NO WARRANTY.
- This is free software, and you are welcome to
  redistribute it under certain conditions.
- For more details refer to the attached README.txt file
  or to the LICENSE file in the GitHub repository."""

spLO = [[sg.T(LICENSE)]]
spWin = sg.Window("",
                  spLO,
                  no_titlebar=True,
                  disable_close=True,
                  disable_minimize=True,
                  keep_on_top=True)
spWin.read(3000)
spWin.close()

# Update check
try:
    _ver = requests.get("https://api.github.com/repos/ftedianiak/"
                        + "library-parrotex/releases")
except requests.exceptions.ConnectionError:
    Popups("e", LANG["err"] + " #G: " + LANG["errG"])
else:
    if _ver.status_code == 200:
        _chk = jloads(_ver.text)[0]["name"]
        if VERSION != _chk:
            ans = Popups("yn", LANG["up"])
            if ans == "Yes":
                webbrowser.open("https://github.com/FTEdianiaK/"
                                + "library-parrotex/releases/latest")
    else:
        Popups("e", LANG["err"] + " #G: " + LANG["errG"])

# Sets main GUI theme
sg.theme("DarkGreen")

# Main loop
while True:
    load()

    if WINDOW == "":
        break
    elif WINDOW == "m":
        main()
    elif WINDOW == "a":
        add()
    elif WINDOW == "s":
        search()
    elif WINDOW == "c":
        cards()
    elif WINDOW == "h":
        help()
    elif WINDOW == "u":
        undo()
