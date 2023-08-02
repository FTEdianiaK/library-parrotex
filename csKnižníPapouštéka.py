# Library Parrotex: A simple library index and card system.
# Copyright (C) 2023 Foxie EdianiaK a.k.a. F_TEK

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
import isbnlib as isbn
import PySimpleGUI as sg
import requests
import re
from time import sleep

# Papouščí ikona v Base64
ICON = "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".encode()

# Seznam globálních konstant
ROWS = []
FIELDS = []
IDS = {}
CARDS = {}
HELP = ""
SORT = 0
LAST_LOC = ""
VERSION = "2.0"

# Vytváří potřebné soubory při prvním startu
try:
    with open("knihy.csv", "x", encoding="utf-8") as f:
        _data = ["ID", "ISBN", "Autor", "Název", "Žánr", "Umístění", "Stav"]
        _wrt = cwrite(f)
        _wrt.writerow(_data)
        f.close()
except FileExistsError:
    pass

try:
    with open("kody.json", "x", encoding="utf-8") as f:
        _data = {"test": 0}
        jdump(_data, f)
        f.close()
except FileExistsError:
    pass

try:
    with open("karty.json", "x", encoding="utf-8") as f:
        _data = {"LIST": []}
        jdump(_data, f)
        f.close()
except FileExistsError:
    pass

try:
    with open("pomoc.txt", "x", encoding="utf-8") as f:
        f.close()
except FileExistsError:
    pass


def PopupAnoNe(msg: str) -> str:
    pLO = [[sg.T(msg)],
           [sg.B("Ano", k="Yes"),
            sg.B("Ne", k="No")]]
    pWin = sg.Window(msg, pLO, icon=ICON)
    pEv, pVal = pWin.read()
    pWin.close()
    return pEv


def load() -> sg.Window:
    """
    (Pře)Načítá všechny konstanty a Main Window.
    @ ROWS, FIELDS, IDS, CARDS, HELP
    > Main Window

    - Načítá data z knihy.csv, kody.json, karty.json a pomoc.txt
    - Seřazuje ROWS
    - Připravuje Main Window
    """
    global ROWS, FIELDS, IDS, CARDS, HELP
    ROWS = []
    FIELDS = []
    IDS = {}
    CARDS = {}
    HELP = ""

    with open("knihy.csv", "r", encoding="utf-8") as f:
        _raw = cread(f)
        FIELDS = next(_raw)
        for _row in _raw:
            ROWS.append(_row)
        f.close()

    while True:
        try:
            ROWS.remove([])
        except ValueError:
            break

    with open("kody.json", "r", encoding="utf-8") as f:
        IDS = jload(f)
        f.close()

    with open("karty.json", "r", encoding="utf-8") as f:
        CARDS = jload(f)
        f.close()

    with open("pomoc.txt", "r", encoding="utf-8") as f:
        HELP = f.read()
        f.close()

    for i in reversed((SORT, 0)):
        ROWS = sorted(ROWS, key=operator.itemgetter(i))

    mLO = [[sg.B("Přidat", k="Add"),
            sg.B("Hledat", k="Search"),
            sg.P(),
            sg.B("Výpůjční listy", k="Cards"),
            sg.B("Legenda", k="Help"),
            sg.B("Vrátit změnu", k="Undo")],
           [sg.Table(values=ROWS,
                     headings=FIELDS,
                     auto_size_columns=True,
                     max_col_width=50,
                     justification="center",
                     num_rows=30,
                     enable_click_events=True,
                     alternating_row_color="#a0ca6d",
                     k="Table")]]
    mWin = sg.Window("Knižní Papouštéka", mLO, icon=ICON)
    return mWin


def save(type: str) -> None:
    """
    Ukládá a Zálohuje vybrané soubory.
    < Soubory

    - Dostupné soubory:
      - b - knihy.csv + kody.json
      - c - karty.json
      - h - pomoc.txt
    """
    if "b" in type:
        _old_fields = []
        _old_rows = []

        with open("knihy.csv", "r", encoding="utf-8") as f:
            _raw = cread(f)
            _old_fields = next(_raw)
            for _row in _raw:
                _old_rows.append(_row)
            f.close()

        with open("knihy.csv.bak", "w", encoding="utf-8") as f:
            _wrt = cwrite(f)
            _wrt.writerow(_old_fields)
            _wrt.writerows(_old_rows)
            f.close()

        with open("knihy.csv", "w", encoding="utf-8") as f:
            _wrt = cwrite(f)
            _wrt.writerow(FIELDS)
            _wrt.writerows(ROWS)
            f.close()

        _old_ids = {}

        with open("kody.json", "r", encoding="utf-8") as f:
            _old_ids = jload(f)
            f.close()

        with open("kody.json.bak", "w", encoding="utf-8") as f:
            jdump(_old_ids, f)
            f.close()

        with open("kody.json", "w", encoding="utf-8") as f:
            jdump(IDS, f)
            f.close()
    if "c" in type:
        _old_cards = {}

        with open("karty.json", "r", encoding="utf-8") as f:
            _old_cards = jload(f)
            f.close()

        with open("karty.json.bak", "w", encoding="utf-8") as f:
            jdump(_old_cards, f)
            f.close()

        with open("karty.json", "w", encoding="utf-8") as f:
            jdump(CARDS, f)
            f.close()
    if "h" in type:
        _old_help = ""

        with open("pomoc.txt", "r", encoding="utf-8") as f:
            _old_help = f.read()
            f.close()

        with open("pomoc.txt.bak", "w", encoding="utf-8") as f:
            f.write(_old_help)
            f.close()

        with open("pomoc.txt", "w", encoding="utf-8") as f:
            f.write(HELP)
            f.close()


def undo(type: str) -> None:
    """
    Odvolává jednu změnu vybraného souboru.
    < Soubor

    - Dostupné soubory:
      - b - knihy.csv + kody.json
      - c - karty.json
      - h - pomoc.txt
    """
    try:
        if "b" in type:
            _new_fields = []
            _new_rows = []

            with open("knihy.csv.bak", "r", encoding="utf-8") as f:
                _raw = cread(f)
                _new_fields = next(_raw)
                for _row in _raw:
                    _new_rows.append(_row)
                f.close()

            with open("knihy.csv.bak", "w", encoding="utf-8") as f:
                _wrt = cwrite(f)
                _wrt.writerow(FIELDS)
                _wrt.writerows(ROWS)
                f.close()

            with open("knihy.csv", "w", encoding="utf-8") as f:
                _wrt = cwrite(f)
                _wrt.writerow(_new_fields)
                _wrt.writerows(_new_rows)
                f.close()

            _new_ids = {}

            with open("kody.json.bak", "r", encoding="utf-8") as f:
                _new_ids = jload(f)
                f.close()

            with open("kody.json.bak", "w", encoding="utf-8") as f:
                jdump(IDS, f)
                f.close()

            with open("kody.json", "w", encoding="utf-8") as f:
                jdump(_new_ids, f)
                f.close()
        if "c" in type:
            _new_cards = {}

            with open("karty.json.bak", "r", encoding="utf-8") as f:
                _new_cards = jload(f)
                f.close()

            with open("card.json.bak", "w", encoding="utf-8") as f:
                jdump(CARDS, f)
                f.close()

            with open("karty.json", "w", encoding="utf-8") as f:
                jdump(_new_cards, f)
                f.close()
        if "h" in type:
            _new_help = ""

            with open("pomoc.txt.bak", "r", encoding="utf-8") as f:
                _new_help = f.read()
                f.close()

            with open("pomoc.txt.bak", "w", encoding="utf-8") as f:
                f.write(HELP)
                f.close()

            with open("pomoc.txt", "w", encoding="utf-8") as f:
                f.write(_new_help)
                f.close()
    except FileNotFoundError:
        sg.PopupError("Žádná změna k zvrácení.")


def add() -> None:
    """
    Umožňuje přidávat nové knižní záznamy.
    @ LAST_LOC

    - Přednačítá data z ISBN kódu a záznamu z databazeknih.cz.
    - Umožňuje uživateli přidat ostatní data ručně.
    """
    global LAST_LOC

    con = False
    err = ""
    inISBN = ""
    r = {
        "ID": "",
        "ISBN": "",
        "Author": "",
        "Title": "",
        "Genre": "",
        "Location": LAST_LOC,
        "State": "K"
    }

    while True:
        aLO = [[sg.T("Zadejte ISBN knihy:")],
               [sg.I(inISBN, k="inISBN")],
               [sg.T(err)],
               [sg.B("Zrušit", k="Cancel"),
                sg.P(),
                sg.B("Přeskočit", k="Skip"),
                sg.B("OK", k="OK")]]
        aWin = sg.Window("Knižní Papouštéka: Přidat 1/2", aLO, icon=ICON)
        aEv, aVal = aWin.read()

        err = ""

        aWin.close()
        if aEv is None or aEv == "Cancel":
            break
        if aEv == "Skip":
            con = True
            break
        if aEv == "OK":
            inISBN = aVal["inISBN"]
            inISBN = inISBN.replace("-", "")
            if isbn.is_isbn10(inISBN) or isbn.is_isbn13(inISBN):
                _data = isbn.meta(inISBN)
                r["Title"] = _data["Title"]
                r["Author"] = "; ".join(author for author in _data["Authors"])
                r["ISBN"] = inISBN

                _a_tries = 0
                g = ""
                while _a_tries < 3:
                    try:
                        db = requests.get(url=("https://www.databazeknih.cz/"
                                               + "search?q=" + inISBN
                                               + "&hledat="),
                                          allow_redirects=True)
                    except requests.exceptions.ConnectionError:
                        _a_tries += 1
                        sleep(0.5)
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

                            _a_tries = 4
                        else:
                            _a_tries += 1
                            sleep(0.5)

                if _a_tries == 3:
                    sg.PopupError("Chyba: Nelze načíst databazeknih.cz")

                r["Genre"] = g

                con = True
                break
            else:
                err = "Chyba: Bylo zadáno neplatné ISBN."

    err = ""

    while con:
        aLO = [[sg.T("Vyplňte údaje knihy:")],
               [sg.T("ISBN:"), sg.I(r["ISBN"], disabled=True)],
               [sg.T("Autor:"), sg.I(r["Author"], k="author")],
               [sg.T("Název:"), sg.I(r["Title"], k="title"),
                sg.B("Vyhledat", k="Search")],
               [sg.T("Žánr:"), sg.I(r["Genre"], k="genre")],
               [sg.T("Umístění:"), sg.I(r["Location"], k="location")],
               [sg.T("Stav:"), sg.I("K", disabled=True)],
               [sg.T(err)],
               [sg.B("Zrušit", k="Cancel"), sg.P(), sg.B("Přidat", k="Add")]]
        aWin = sg.Window("Knižní Papouštéka: Přidat 2/2", aLO, icon=ICON)
        aEv, aVal = aWin.read()

        err = ""

        aWin.close()
        if aEv is None or aEv == "Cancel":
            break
        else:
            r["Author"] = aVal["author"].replace(",", ";")
            r["Title"] = aVal["title"].replace(",", ";")
            r["Genre"] = aVal["genre"].replace(",", ";")
            r["Location"] = aVal["location"].replace(",", ";")
            LAST_LOC = r["Location"]

        if aEv == "Search":
            webbrowser.open(url=("https://www.databazeknih.cz/search?q="
                                 + aVal["title"]
                                 + "&hledat="))
        if aEv == "Add":
            if (aVal["author"] != ""
                    and aVal["title"] != ""
                    and aVal["genre"] != ""
                    and aVal["location"] != ""):
                abbr = r["Location"][0]

                try:
                    int(abbr)
                except ValueError:
                    pass
                else:
                    err = "Chyba: Lokace nesmí začínat číslem."
                    continue

                if abbr not in IDS:
                    IDS[abbr] = 0

                IDS[abbr] += 1
                r["ID"] = abbr + str(IDS[abbr])

                ROWS.append([r["ID"],
                             r["ISBN"],
                             r["Author"],
                             r["Title"],
                             r["Genre"],
                             r["Location"],
                             r["State"]])
                save("b")

                break
            else:
                err = "Chyba: Všechny údaje musí být vyplněné."


def search() -> None:
    """
    Dovoluje prohledávání knižních záznamů.

    - Možné filtry:
      - Žánr
      - Autor
      - Název
    """
    par = ["", "", ""]
    res = []
    num = 0

    while True:
        sLO = [[sg.T("Zadejte vyhledávací parametry:")],
               [sg.T("1. Žánr:"), sg.I(par[0], k="zero")],
               [sg.T("2. Autor:"), sg.I(par[1], k="one")],
               [sg.T("3. Název:"), sg.I(par[2], k="two")],
               [sg.T("Celkem výsledků: " + str(num)),
                sg.P(),
                sg.B("Hledat", k="Search"),
                sg.B("Zavřít", k="Cancel")],
               [sg.Table(values=res,
                         headings=FIELDS,
                         auto_size_columns=True,
                         max_col_width=50,
                         justification="center",
                         num_rows=20,
                         alternating_row_color="#a0ca6d",
                         k="Table")]]
        sWin = sg.Window("Knižní Papouštéka: Hledat", sLO, icon=ICON)
        sEv, sVal = sWin.read()

        sWin.close()
        if sEv is None or sEv == "Cancel":
            break
        else:
            par = [sVal["zero"].lower(),
                   sVal["one"].lower(),
                   sVal["two"].lower()]

        if sEv == "Search":
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

            num = len(res)


def cards() -> None:
    """
    Rozhraní výpujčních karet.

    - Přidej a odstraň vypujčené knihy ze zvolené karty.
    - Podívej se kdy si zvolená karta pujčila jakou knihu.
    - Vytvoř a/nebo smaž výpujční karty.
    """
    vw = [[]]
    card = ""
    err = ""

    while True:
        cLO = [[sg.T("ID"),
                sg.I(k="id"),
                sg.P(),
                sg.DD(CARDS["LIST"], card, k="Card"),
                sg.B("Zobrazit", k="View")],
               [sg.B("Vypůjčit", k="Borrow"),
                sg.B("Vrátit", k="Return"),
                sg.P(),
                sg.B("Spravovat", k="Manage"),
                sg.B("Zavřít", k="Close")],
               [sg.T("Karta: " + card), sg.P(), sg.T(err), sg.P(), sg.P()],
               [sg.Table(values=vw,
                         headings=["ID", "Název", "Datum"],
                         auto_size_columns=True,
                         max_col_width=50,
                         justification="center",
                         num_rows=20,
                         alternating_row_color="#a0ca6d",
                         k="Table")]]
        cWin = sg.Window("Knižní Papouštéka: Výpůjčky", cLO, icon=ICON)
        cEv, cVal = cWin.read()

        err = ""

        cWin.close()
        if cEv is None or cEv == "Close":
            break
        else:
            card = cVal["Card"]

        if cEv == "View":
            if cVal["Card"] not in CARDS["LIST"]:
                card = ""
            else:
                vw = CARDS[card]
        if cEv == "Borrow":
            if card == "":
                err = "Chyba: Musíte zvolit kartu."
            elif cVal["id"] == "":
                err = "Chyba: Musíte zadat ID knihy."
            else:
                err = "Chyba: Zadané ID nebylo nalezeno."
                for row in ROWS:
                    if row[0] == cVal["id"]:
                        if row[6] != "K":
                            err = ("Chyba: Nelze si vypůjčit "
                                   + "již vypůjčenou knihu.")
                        else:
                            err = ""
                            CARDS[card].append([row[0],
                                                row[3],
                                                str(date.today())])
                            num = ROWS.index(row)
                            ROWS[num][6] = "V:" + card
                            save("bc")
        if cEv == "Return":
            if card == "":
                err = "Chyba: Musíte zvolit kartu."
            elif cVal["id"] == "":
                err = "Chyba: Musíte zadat ID knihy."
            else:
                err = "Chyba: Zadané ID nebylo nalezeno."
                for row in ROWS:
                    if row[0] == cVal["id"]:
                        if row[6] == "K":
                            err = "Chyba: Nelze vrátit nevypůjčenou knihu."
                        else:
                            err = ("Chyba: Daná karta neobsahuje "
                                   + "zadané ID knihy.")
                            for entry in CARDS[card]:
                                if entry[0] == cVal["id"]:
                                    err = ""
                                    num = CARDS[card].index(entry)
                                    CARDS[card].pop(num)
                                    num = ROWS.index(row)
                                    ROWS[num][6] = "K"
                                    save("bc")
        if cEv == "Manage":
            err = ""
            while True:
                mLO = [[sg.T("Jméno:"),
                        sg.I(k="name"),
                        sg.B("Přidat", k="Add"),
                        sg.B("Smazat", k="Delete")],
                       [sg.T(err), sg.P(), sg.B("Zavřít", k="Close")]]
                mWin = sg.Window("Knižní Papouštéka: Administrativa",
                                 mLO,
                                 icon=ICON)
                mEv, mVal = mWin.read()

                err = ""

                mWin.close()
                if mEv is None or mEv == "Close":
                    break
                else:
                    name = mVal["name"]

                if mEv == "Add":
                    if name == "":
                        err = "Chyba: Musíte zadat jméno karty."
                    elif name in CARDS["LIST"]:
                        err = "Chyba: Karta již existuje."
                    else:
                        CARDS["LIST"].append(name)
                        CARDS[name] = []
                        save("c")
                        break
                if mEv == "Delete":
                    if name == "":
                        err = "Chyba: Musíte zadat jméno karty."
                    elif name not in CARDS["LIST"]:
                        err = "Chyba: Karta neexistuje."
                    elif CARDS[name] != []:
                        err = ("Chyba: Nelze smazat kartu "
                               + "s vypůjčenými knihami.")
                    else:
                        ans = PopupAnoNe(("Chcete doopravdy smazat "
                                          + "danou kartu?"))
                        if ans == "Yes":
                            CARDS["LIST"].remove(name)
                            CARDS.pop(name)
                            save("c")
                            break


def help() -> None:
    """
    Jednoduché rozhraní textového souboru.

    - Umožňuje četbu a úpravu pomoc.txt
    """
    global HELP
    while True:
        hLO = [[sg.T("Legenda:")],
               [sg.Multiline(HELP, k="help", size=(60, 20))],
               [sg.B("Zavřít", k="Close"), sg.P(), sg.B("Uložit", k="Save")]]
        hWin = sg.Window("Knižní Papouštéka: Legenda", hLO, icon=ICON)
        hEv, hVal = hWin.read()

        hWin.close()
        if hEv is None or hEv == "Close":
            break
        if hEv == "Save":
            HELP = hVal["help"]
            save("h")


def edit(row: int) -> None:
    """
    Dovoluje upravovat knižní záznamy.

    - Můžete upravovat:
      - Autora(/-y)
      - Název
      - Žánr(/-y)
      - Umístění - což mění i ID
    """
    r = ROWS[row]
    loc = r[5]
    err = ""

    while True:
        eLO = [[sg.T("Upravujete knihu #" + r[0])],
               [sg.T("ISBN:"), sg.I(r[1], disabled=True)],
               [sg.T("Autor:"), sg.I(r[2], k="author")],
               [sg.T("Název:"),
                sg.I(r[3], k="title"),
                sg.B("Vyhledat", k="Search")],
               [sg.T("Žánr:"), sg.I(r[4], k="genre")],
               [sg.T("Umístění:"), sg.I(r[5], k="location")],
               [sg.T("Stav:"), sg.I(r[6], disabled=True)],
               [sg.T(err)],
               [sg.B("Zrušit", k="Cancel"),
                sg.P(),
                sg.B("Smazat", k="Delete"),
                sg.B("Upravit", k="Edit")]]
        eWin = sg.Window("Knižní Papouštéka: Upravit", eLO, icon=ICON)
        eEv, eVal = eWin.read()

        err = ""

        eWin.close()
        if eEv is None or eEv == "Cancel":
            break
        else:
            r[2] = eVal["author"].replace(",", ";")
            r[3] = eVal["title"].replace(",", ";")
            r[4] = eVal["genre"].replace(",", ";")
            r[5] = eVal["location"].replace(",", ";")

        if eEv == "Search":
            webbrowser.open(url=("https://www.databazeknih.cz/search?q="
                                 + eVal["title"]
                                 + "&hledat="))
        if eEv == "Delete":
            if r[6] == "K":
                ans = PopupAnoNe("Chcete doopravdy smazat tuto knihu?")
                if ans == "Yes":
                    ROWS.pop(row)
                    save("b")

                    break
            else:
                sg.PopupError("Chyba: Nelze smazat vypůjčenou knihu.")
        if eEv == "Edit":
            if r[2] != "" and r[3] != "" and r[4] != "" and r[5] != "":
                if r[5] != loc and r[6] != "K":
                    err = "Chyba: Nelze změnit lokaci vypůjčené knihy."
                else:
                    abbr = r[5][0]

                    try:
                        int(abbr)
                    except ValueError:
                        pass
                    else:
                        err = "Chyba: Lokace nesmí začínat číslem."
                        continue

                    if abbr not in IDS:
                        IDS[abbr] = 0

                    IDS[abbr] += 1
                    r[0] = abbr + str(IDS[abbr])

                    ROWS[row] = r
                    save("b")
                    break
            else:
                err = "Chyba: Všechny údaje musí být vyplněné."


# Nastavuje styl úvodního obrázku
sg.theme("DarkGreen4")

# Úvodní obrázek
spLO = [[sg.P(),
         sg.T("Knižní Papouštéka"),
         sg.P()],
        [sg.P(),
         sg.Image(ICON),
         sg.P()],
        [sg.T("v" + VERSION),
         sg.P(),
         sg.T("od F_TEK")]]
spWin = sg.Window("",
                  spLO,
                  no_titlebar=True,
                  disable_close=True,
                  disable_minimize=True,
                  keep_on_top=True)
spWin.read(1500)
spWin.close()

# Kontrola aktualizace
_up_tries = 0
while _up_tries < 3:
    try:
        _ver = requests.get("https://raw.githubusercontent.com/"
                            + "FTEdianiaK/library-parrotex/main/VERSION")
    except requests.exceptions.ConnectionError:
        _up_tries += 1
        sleep(0.5)
    else:
        if _ver.status_code == 200:
            if VERSION != _ver.text:
                ans = PopupAnoNe("Je k dispozici nová verze.\n"
                                 + "Chcete otevřít stránky vývojáře?")
                if ans == "Yes":
                    webbrowser.open("https://github.com/FTEdianiaK/"
                                    + "library-parrotex/releases/latest")

            _up_tries = 4
        else:
            _up_tries += 1
            sleep(0.5)

if _up_tries == 3:
    sg.PopupError("Chyba: Nelze načíst github.com")

# Nastavuje styl hlavního rozhraní
sg.theme("DarkGreen")

# Hlavní cyklus
while True:
    mWin = load()
    mEv, mVal = mWin.read()

    mWin.close()
    if mEv is None:
        break
    if mEv == "Add":
        add()
    if mEv == "Search":
        search()
    if mEv == "Cards":
        cards()
    if mEv == "Help":
        help()
    if mEv == "Undo":
        uEv, uVal = sg.Window("Knižní Papouštéka: Vrátit změnu",
                              [[sg.T("Změnu čeho byste rádi odvolali?")],
                               [sg.B("Knihy", k="b"),
                                sg.B("Karty", k="c"),
                                sg.B("Legendu", k="h"),
                                sg.P(),
                                sg.B("Zrušit", k="Cancel")]]).read()

        if uEv is None or uEv == "Cancel":
            continue
        else:
            undo(uEv)
    if type(mEv) == tuple:
        if mEv[2][0] == -1 and mEv[2][1] != -1:
            SORT = mEv[2][1]
        elif mEv[2][0] is not None:
            edit(mEv[2][0])
