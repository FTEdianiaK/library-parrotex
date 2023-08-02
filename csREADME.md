# Knižní Papouštéka

*Jednoduchý program pro tvorbu knihovní kartotéky a výpůjčních listů.*

![Obrázek programu](cs.png)

[English version](https://github.com/FTEdianiaK/library-parrotex/blob/main/README.md) | [Záznam změn](https://github.com/FTEdianiaK/library-parrotex/blob/main/csCHANGELOG.md) | [Licenční smlouva](https://github.com/FTEdianiaK/library-parrotex/blob/main/LICENSE)

### Vlastnosti
- Tabulka se všemi důležitými informacemi o knihách, kterou lze podle každé seřadit.
- Okno pro hledání a filtrování knih podle jejich názvu, autora nebo žánru.
- Knihy jsou uložené v souboru, který je kompatibilní s většinou tabulkových procesorů (.csv).
- Nápomocné přidávací okno, které dokáže najít informace pomocí ISBN nebo přesměrovat na stránky dané knihy z DatabázeKnih pomocí názvu.
- Upravovací funkce, která používá stejné okno jako přidávací.
- Jednoduché odvolání poslední změny pro případ, že byste udělali chybu.
- Soubor s legendou, který lze využít pro jakékoliv poznámky, např. co která zkratka umístění znamená

### Jak...
**Nainstalovat:**
- **Windows:** Stáhněte si .exe průvodce instalací, spusťte jej a vyberte složku, do které se má program stáhnout. Poté co instalace skončí, spusťte "csKnižníPapouštéka.exe".
- **Zdrojový kód:** Stáhněte si "csKnižníPapouštéka.py" a vložte jej do prázdné složky (při aktualizaci nahraďte starší verzi). Poté spusťte daný soubor.

**Aktualizovat:**
- Pro aktualizaci použijte stejné instrukce jako pro instalaci.
- Je doporučené zálohovat si datové soubory (knihy.csv, karty.json, kody.json, pomoc.txt) před aktualizací, poté je umísťete do stejné složky jako hlavní soubor.
- Aktualizace je pouze potřeba, když se nejnovější verze neshoduje s tou, kterou používáte (to můžete zkontrolovat v úvodním obrázku).
- **POZOR!** Pokud se první číslo nejnovější verze (v 1.4 je jím 1) neshoduje s tím, které používáte, je možné, že bude potřeba aktualizace i vašich datových souborů. Pro více informací o tomto nahlédněte do záznamu změn.

**Smazat:** Použijte "unins000.exe" (pokud jste použili .exe průvodce instalací), poté smažte složku, ve které byl program naninstalován, abyste smazali i datové soubory zanechané programem (knihy.csv, karty.json, kody.json, pomoc.txt), pokud si je neplánujete nechat.

### Známé chyby
**[#3](https://github.com/FTEdianiaK/library-parrotex/issues/3)**: Některé speciální znaky mohou být vloženy špatně když jsou napsány pomocí klávesnice. (např. ě -> ì)<br>
Zatím jsem nepřišel na důvod, proč se toto děje a budu více než vděčný za jakoukoliv pomoc s opravením tohoto problému.<br>
**Dočasné řešení**: Zdá se, že dané znaky lze zadat zkopírováním odjinud a ty jsou poté zpracovány správně.

### Zdroje
[Papouščí ikona od uživatele Lorc z game-icons.net](https://game-icons.net/1x1/lorc/parrot-head.html)

**Použité knihovny v kódu:**
- [operator, webbrowser, csv, datetime, json, re, time - ze Standardní Knihovny Python - PSF](https://docs.python.org/3/library/index.html)
- [isbnlib - od Alexandre Lima Conde - LGPLv3](https://pypi.org/project/isbnlib/)
- [PySimpleGui - od PySimpleGui - LGPLv3+](https://pypi.org/project/PySimpleGUI/)
- [requests - od Kenneth Reitz - Apache 2.0](https://pypi.org/project/requests/)

**Další použité knihovny:**
- [pyinstaller - od Hartmut Goebel, Giovanni Bajo, David Vierra, David Cortesi, Martin Zibricky - GPLv2](https://pypi.org/project/pyinstaller/)
- [pycodestyle - od Johann C. Rocholl - MIT](https://pypi.org/project/pycodestyle/)
