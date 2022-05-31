
# API dokumentace



## Funkce

- Přidání nového pacienta
- Přidání problému a návštěv k jednotlivým problémům.


## Pacient

#### Získání všech dat o pacientech

```http
  GET /api/patient/
```

Vrátí JSON soubor všech vašich pacientů.

#### Vytvoření nového pacienta

```http
  POST /api/patient/
```

| Parametr | Typ     | Popis                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | Jméno a Příjmení pacienta. |
| `dob`      | `string` | Datum narození pacienta. |

Vrátí JSON objekt s novým pacientem.

## Problém

#### Získání všech problémů konkrétního pacienta

```http
  GET /api/problem/<int:pid>/
```

Vrátí JSON objekt všech problémů, které jsem pacientovi zadal.

#### Vytvoření nového problému

```http
  POST /api/problem/<int:pid>/
```

| Parametr | Typ     | Popis                       |
| :-------- | :------- | :-------------------------------- |
| `problem`      | `string` | Název problému, který chceme uložit. |

Vrátí JSON objekt s novým problémem.

## Návštěva

#### Získání všech návštěv k jednomu problému

```http
  GET /api/appointment/<int:pid>/<int:PrId>/
```

Vrátí JSON objekt všech návštěv, které jsem pacientovi zadal.

#### Vytvoření nového problému

```http
  POST /api/appointment/<int:pid>/<int:PrId>/
```

| Parametr | Typ     | Popis                       |
| :-------- | :------- | :-------------------------------- |
| `date`      | `string` | Datum návštěvy. |
| `data`      | `string` | Všechny informace co chceme do návštěvy zapsat. |

Vrátí JSON objekt s novou návštěvou.
