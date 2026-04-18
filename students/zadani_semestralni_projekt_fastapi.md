# Semestrální projekt – FastAPI

## Termín odevzdání

Projekt bude odevzdán **na cvičeních v zápočtovém týdnu od 11. 5. 2026 do 15. 5. 2026**.

## Obecné zadání

Pomocí frameworku **FastAPI** navrhněte a implementujte webovou aplikaci nebo službu, která bude představovat jeden logicky uzavřený informační systém dle zvoleného tématu.

Řešení musí splňovat následující obecné požadavky:

- aplikace bude obsahovat alespoň **4 datové modely**, které budou vzájemně provázány relacemi,
- pro práci s databází bude použito vhodné **ORM řešení**, např. SQLAlchemy
- aplikace bude obsahovat alespoň **10 endpointů**,
- endpointy budou pokrývat základní operace nad daty, tj. alespoň část operací typu **vytvoření, zobrazení, úprava a smazání**,
- vstupní a výstupní data budou validována pomocí **Pydantic modelů**,
- aplikace bude poskytovat **REST API** vracející data ve formátu **JSON**,
- součástí aplikace bude alespoň **6 vstupních scénářů**, ve kterých bude aplikace přijímat a zpracovávat data od uživatele,
- projekt bude rozdělen do více částí přehledným způsobem, např. na:
  - routery,
  - modely,
  - schémata,
  - databázovou vrstvu,
  - servisní logiku,
- aplikace bude obsahovat automaticky generovanou dokumentaci pomocí **OpenAPI / Swagger UI**,
- aplikace bude obsahovat ošetření chybových stavů a bude vracet vhodné **HTTP stavové kódy**,
- důraz bude kladen na **čitelnost kódu**, **smysluplnou strukturu projektu** a **logickou návaznost jednotlivých částí API**.

Autentizace a autorizace jsou volitelné, pokud není u konkrétního tématu uvedeno jinak.

## Varianty projektů

### Varianta 1: Rezervační systém pro sportovní centrum

#### Zadání

Navrhněte a implementujte REST API pro správu sportovního centra. Systém bude umožňovat evidenci zákazníků, sportovišť, sportovních aktivit, trenérů a rezervací. Aplikace musí umožnit vytváření rezervací, zobrazování obsazenosti a práci s vazbami mezi jednotlivými entitami.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- zákazník,
- sportoviště,
- sportovní aktivita,
- trenér,
- rezervace.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- evidovat zákazníky,
- evidovat sportoviště a jejich typy,
- evidovat aktivity, které lze na sportovištích provozovat,
- evidovat trenéry a jejich zaměření,
- vytvářet, zobrazovat, upravovat a rušit rezervace,
- vyhledávat rezervace podle data, zákazníka nebo sportoviště,
- zobrazit přehled rezervací konkrétního sportoviště.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- zákazník může mít více rezervací,
- sportoviště může být využito v mnoha rezervacích,
- trenér může být přiřazen k více rezervacím,
- aktivita může souviset s více sportovišti nebo rezervacemi.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- založení zákazníka pomocí dat v těle požadavku,
- založení rezervace pomocí JSON dat,
- filtrování rezervací přes query parametry,
- získání detailu rezervace pomocí path parametru,
- úprava rezervace,
- zrušení rezervace.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- rezervace na neexistující sportoviště,
- rezervace neexistujícím zákazníkem,
- kolize termínu rezervace,
- pokus o rezervaci v neplatném čase.

### Varianta 2: Školní informační systém pro evidenci předmětů a zápisů

#### Zadání

Navrhněte a implementujte REST API pro jednoduchý školní informační systém. Systém bude sloužit k evidenci studentů, vyučujících, předmětů, termínů výuky a zápisů studentů do jednotlivých termínů.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- student,
- vyučující,
- předmět,
- termín předmětu,
- zápis.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- evidovat studenty a vyučující,
- zakládat a spravovat předměty,
- evidovat jednotlivé termíny nebo vypsané skupiny předmětů,
- zapisovat studenty do termínů,
- zobrazovat seznam zapsaných studentů u předmětu nebo termínu,
- rušit zápisy,
- filtrovat nabídku předmětů a termínů.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- vyučující může vyučovat více předmětů,
- předmět může mít více termínů,
- student může být zapsán do více termínů,
- zápis propojuje konkrétního studenta s konkrétním termínem.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- registrace studenta,
- vytvoření předmětu,
- vytvoření termínu předmětu,
- zápis studenta do termínu,
- filtrování termínů podle semestru či vyučujícího,
- zobrazení detailu studenta nebo předmětu pomocí path parametru.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- zápis do neexistujícího termínu,
- překročení kapacity termínu,
- duplicitní zápis stejného studenta,
- zobrazení neexistujícího studenta nebo předmětu.

### Varianta 3: Systém pro správu týmových projektů a úkolů

#### Zadání

Navrhněte a implementujte REST API pro správu týmových projektů. Systém bude určen pro evidenci týmů, uživatelů, projektů, úkolů a komentářů k úkolům. Aplikace musí podporovat základní organizaci práce v týmu.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- uživatel,
- tým,
- projekt,
- úkol,
- komentář.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- zakládat a spravovat uživatele,
- zakládat a spravovat týmy,
- vytvářet projekty v rámci týmů,
- vytvářet, upravovat a mazat úkoly,
- přiřazovat úkoly uživatelům,
- přidávat komentáře k úkolům,
- filtrovat úkoly podle stavu, priority nebo projektu.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- tým obsahuje více uživatelů,
- tým může mít více projektů,
- projekt obsahuje více úkolů,
- úkol může být přiřazen konkrétnímu uživateli,
- úkol může mít více komentářů.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- vytvoření týmu,
- přidání uživatele do týmu,
- založení projektu,
- vytvoření úkolu,
- změna stavu úkolu,
- filtrování úkolů podle query parametrů,
- přidání komentáře k úkolu.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- přiřazení úkolu uživateli, který není členem týmu,
- vytvoření úkolu v neexistujícím projektu,
- úprava neexistujícího úkolu,
- pokus o smazání neexistujícího komentáře.

### Varianta 4: Jednoduchý e-shopový backend

#### Zadání

Navrhněte a implementujte REST API pro jednoduchý e-shopový backend. Systém bude sloužit k evidenci zákazníků, kategorií, produktů, objednávek a položek objednávek. Aplikace musí umožnit správu katalogu a zpracování objednávek.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- zákazník,
- kategorie,
- produkt,
- objednávka,
- položka objednávky.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- evidovat zákazníky,
- vytvářet a upravovat kategorie produktů,
- vytvářet, zobrazovat, upravovat a mazat produkty,
- vytvářet objednávky,
- přidávat položky do objednávek,
- zobrazovat detail objednávky včetně jejích položek,
- měnit stav objednávky,
- filtrovat produkty podle vybraných parametrů.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- kategorie obsahuje více produktů,
- zákazník může mít více objednávek,
- objednávka obsahuje více položek,
- každá položka objednávky odkazuje na konkrétní produkt.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- vytvoření produktu pomocí JSON dat,
- úprava produktu,
- vytvoření objednávky,
- vložení položek objednávky,
- filtrování produktů pomocí query parametrů,
- získání detailu objednávky pomocí path parametru.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- objednávka bez položek,
- odkaz na neexistující produkt,
- záporná cena nebo neplatné množství,
- změna stavu neexistující objednávky.

### Varianta 5: Systém pro správu akcí, registrací a vstupenek

#### Zadání

Navrhněte a implementujte REST API pro správu akcí. Systém bude evidovat pořadatele, akce, návštěvníky, registrace a vstupenky. Aplikace musí umožňovat registraci návštěvníků na akce a správu jejich vstupenek.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- pořadatel,
- akce,
- návštěvník,
- registrace,
- vstupenka.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- evidovat pořadatele a jimi spravované akce,
- evidovat návštěvníky,
- vytvářet registrace na akce,
- evidovat nebo generovat vstupenky,
- zobrazovat seznam registrací a vstupenek,
- označit vstupenku jako využitou při vstupu,
- filtrovat akce podle zvolených parametrů,
- zobrazovat registrace konkrétní akce nebo návštěvníka.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- pořadatel může pořádat více akcí,
- akce může mít více registrací,
- návštěvník může mít více registrací,
- registrace souvisí s konkrétní akcí a konkrétním návštěvníkem,
- registrace může mít přiřazenu vstupenku.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- vytvoření akce,
- registrace návštěvníka,
- filtrování akcí podle query parametrů,
- zobrazení detailu akce pomocí path parametru,
- zobrazení registrací konkrétní akce,
- změna stavu vstupenky při check-inu.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- registrace na neexistující akci,
- registrace po naplnění kapacity,
- duplicitní registrace stejného návštěvníka na stejnou akci,
- check-in neplatné nebo již použité vstupenky.

## Požadované výstupy k odevzdání

Každý student odevzdá:

- zdrojové kódy projektu,
- stručný popis struktury projektu,
- popis použitých datových modelů a jejich relací,
- stručný přehled endpointů,
- ukázku několika testovacích požadavků,
- funkční spuštění aplikace s dostupnou dokumentací Swagger UI.

## Hodnoticí kritéria

### Celkový princip hodnocení

Projekt je hodnocen podle:

- splnění povinných technických požadavků,
- kvality návrhu datového modelu,
- kvality implementace API,
- validace a ošetření chyb,
- struktury a čitelnosti kódu,
- praktické funkčnosti při předvedení.

Doporučené hodnocení v **procentech**. Získat můžete až **30 bodů**.

### Bodovací tabulka

| Oblast hodnocení                             | Max. procent |
| -------------------------------------------- | -----------: |
| 1. Splnění zadání a rozsahu projektu         |           15 |
| 2. Datový model a relace                     |           15 |
| 3. Návrh a implementace REST API             |           20 |
| 4. Validace vstupů a výstupů pomocí Pydantic |           10 |
| 5. Databázová vrstva a ORM                   |           10 |
| 6. Struktura projektu a kvalita kódu         |           10 |
| 7. Ošetření chybových stavů a HTTP kódy      |           10 |
| 8. Dokumentace API a prezentace projektu     |           10 |
| **Celkem**                                   |      **100** |

## Minimální podmínky pro uznání projektu

Projekt lze uznat pouze tehdy, pokud současně splní tyto minimální podmínky:

- obsahuje alespoň **4 datové modely**,
- obsahuje alespoň **10 endpointů**,
- používá **ORM**,
- používá **Pydantic** pro validaci,
- vrací data jako **JSON**,
- obsahuje funkční **Swagger UI / OpenAPI dokumentaci**,
- projekt je alespoň v základní míře spustitelný a předveditelný.

### Varianta pro diskusi na cvičení: Systém pro evidenci knihovny a výpůjček

#### Zadání

Navrhněte a implementujte REST API pro evidenci knihovny. Systém bude umožňovat správu autorů, knih, fyzických výtisků, čtenářů a výpůjček. Aplikace musí podporovat evidenci dostupnosti knih a proces vypůjčení a vrácení.

#### Minimální rozsah domény

Systém bude obsahovat alespoň následující entity:

- autor,
- kniha,
- výtisk,
- čtenář,
- výpůjčka.

#### Minimální požadovaná funkcionalita

Aplikace musí umožnit alespoň:

- evidovat autory a knihy,
- evidovat jednotlivé výtisky knih,
- evidovat čtenáře,
- vytvářet výpůjčky,
- vracet výpůjčky,
- zobrazovat dostupnost knih,
- zobrazovat aktivní výpůjčky konkrétního čtenáře,
- filtrovat výpůjčky podle stavu.

#### Povinné logické vazby

V návrhu musí být vhodně zachyceny alespoň tyto vztahy:

- autor může mít více knih,
- kniha může mít více výtisků,
- čtenář může mít více výpůjček,
- výpůjčka propojuje čtenáře s konkrétním výtiskem.

#### Příklady vstupních scénářů

Aplikace bude pracovat alespoň s těmito vstupy:

- založení knihy,
- přidání výtisku,
- registrace čtenáře,
- vytvoření výpůjčky,
- vrácení výpůjčky,
- filtrování aktivních výpůjček,
- získání detailu knihy nebo čtenáře.

#### Požadavky na validaci a chybové stavy

Aplikace musí ošetřit například tyto situace:

- pokus o vypůjčení již vypůjčeného výtisku,
- pokus o vrácení již vrácené výpůjčky,
- práce s neexistující knihou nebo čtenářem,
- neplatné datum výpůjčky nebo vrácení.
