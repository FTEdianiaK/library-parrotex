### v2.1.1
- Opraveno zůstávání údajů v Přidávacím okně i po úspěšném přidání knihy

### v2.1

**Vylepšení:**

- Naprosté předělání programu
  - Uživatelské prostředí přepracováno - nyní obsahuje záložky místo složitého systému oken
  - Jazyky přepracovány - místo dvou různých edicí nyní je pouze jedna, která se Vás při prvním startu zeptá, jakou jazykovou edici chcete používat
- Přidána funkce vycpávání čísel, takže když řadíte tabulku podle ID, tak se doopravdy řadí podle ID
- Vylepšení pohodlnosti užívání, některá tlačítka (většina ve stylu OK) mají nyní k sobě připoutaný Enter
- Přidávací okno nyní ukazuje ID přidané knihy
- Hlavní okno nyní používá stránkování, takže i větší papouštéky nebudou mít problém na starších zařízeních
- Nyní lze spustit Upravovací okno z Hledání
- Místo toho, aby program zmizel, když zpracovává Váš požadavek (např. načtení dat ISBN), se objeví načítací okno

**Opravy:**

- Opraveny ISBN chyby - žádné připojení k internetu a platné, ale prázdné ISBN
- Velikost okna je nyní menší a neměla by tedy přetékat
- Změna ID byla opravena (znovu), nyní by měla nastat pouze pokud změníte první písmenko lokace, které je to co určuje ID
- Přidána chybová hláška, když spustíte program v chráněné/systémové složce

### v2.0

- Opravena chyba, kdy program spadnul, když nebylo k dispozici internetové přiopojení (viz Issue [#1](https://github.com/FTEdianiaK/library-parrotex/issues/1))
- Opravena chyba, kdy se ID měnilo s každou změnou, ne pouze při změně umístění
- CS: Přeloženy názvy souborů do češtiny, aby nevznikla neshoda s anglickou verzí (viz Issue [#2](https://github.com/FTEdianiaK/library-parrotex/issues/2))
- CS: Opravena mírná chyba v překladu z angličtiny
- CS: Přeloženy docstring-y do češtiny
- CS: Opraveno nezavírání potvrzovacích oken

### v1.1

- Přidáno zapamatování umístení pro přidávací okno - Už není potřeba pokaždé přepisovat lokaci zatímco pracujete na stejné poličce/sekci
- Přepracováno hledací okno, aby parametrům nezáleželo na velikosti písmen
- Přidán úvodní obrázek, který uvádí současnou verzi programu
- Přidána funkce, která při spuštění kontroluje, zda je dostupná aktualizace
- Potvrzovací okna byla změněna tak, aby lépe seděla na své otázkya
- CS: Potvrzovací okna přeložena do češtiny

### v1.0

- První stabilní verze