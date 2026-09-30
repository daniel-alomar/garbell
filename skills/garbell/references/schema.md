# Esquema i estat

## Notes generades

YAML al principi de cada fitxa o pàgina temàtica (índex, registre, pendents i
propostes queden exempts). Camps obligatoris:

```yaml
---
id: "src-identificador-estable"
type: "source"
status: "draft"
created: "2026-09-29"
updated: "2026-09-29"
tags: [recerca]
sources: ["raw/article.pdf"]
source_notes: []
---
```

L'exemple mostra el format, no una font real. `type`: source, concept, method,
synthesis, question, author; `journal` per al registre opcional de revistes. Les notes d'autor són opcionals i segueixen
[els criteris de recerca](research.md). `status`: draft, reviewed, needs-review. `reviewed` es
reserva a una revisió humana explícita; la verificació de l'agent no l'atorga.
`id` ha de ser únic i estable encara que canviï el títol. Dates ISO reals.
`sources` enumera TOTES les fonts originals directes; `source_notes` conté els
camins de les fitxes de font sense `.md`. En fitxes, pot quedar buit.

Per a fonts afegeix, quan constin: `title`, `authors`, `year`, `doi`, `url`,
`citekey`, `source_sha256`, `read_scope`, `extraction_notes`. Valors desconeguts:
`null` o llista buida; mai deduccions presentades com a metadades verificades.
La citekey és opcional per facilitar una futura connexió bibliogràfica.

## Cos de la fitxa

- Referència i enllaç a l'original.
- Pregunta o objectiu, context i mètode, resultats, limitacions.
- Evidències: afirmació o cita curta + localitzador precís. Exemple de sintaxi
  d'un original PDF: `[[raw/article.pdf#page=7|Original, pàgina PDF 7]]`.
- Utilitat per al doctorat: diferenciada de les conclusions de l'autor.
- Relacions justificades amb conceptes, mètodes i altres fonts existents.

Si només hi ha abstract o falten pàgines, indica explícitament l'abast; la font
queda pendent d'ingestió completa. No extrapolis resultats no llegits.

## Cos de les síntesis

Organitza afirmacions per pregunta, amb atribució i localitzador al costat de
cadascuna. Afegeix desacords, condicions en què els resultats són aplicables i
buits de coneixement. Les fonts d'una revisió no es converteixen en fonts
primàries llegides: si no les has llegit, indica la citació secundària.

## Eina d'estat opcional (Python 3.10+, biblioteca estàndard)

Aquests comandaments només s'utilitzen en mode amb Python. En mode manual
aplica [el procediment alternatiu](tooling.md); `source_sha256` queda a `null`.
El comprovador requereix `fcntl` (Linux/macOS).

Des de la carpeta de la skill:

```sh
python3 scripts/vault_state.py scan /ruta/vault
python3 scripts/vault_state.py links /ruta/vault
python3 scripts/vault_state.py accept /ruta/vault --source raw/article.pdf --sha256 EMPREMTA_LLEGIDA --outputs wiki/fonts/article.md wiki/conceptes/concepte.md
```

`accept` registra una font completada i les empremtes dels fitxers generats.
Passa TOTS els fitxers temàtics que depenen d'aquesta font, encara que en aquest
lot només n'hagis modificat alguns. L'índex i el registre no són dependències.
`accept` comprova existència, ubicació i hash original; no avalua la fidelitat
del resum. És responsabilitat de l'agent revisar-lo abans d'acceptar.

`scan` no modifica res. Compara originals i notes amb `.wiki/state.json`,
mostra còpies amb contingut idèntic i fonts amb notes modificades o absents.
Les baixes continuen visibles fins que l'usuari resol la incidència; mai
eliminen automàticament contingut. Les fonts no acceptades tornen a aparèixer
com a noves: consulta `wiki/pendents.md` per saber si ja es van intentar.

`links` valida destins de wikilinks del cos de `wiki/**/*.md`, inclosos adjunts;
ignora blocs de codi. No valida àncores, enllaços Markdown, YAML, idioma ni
cites. La skill exigeix revisar aquests aspectes per separat. Un retorn 1
indica enllaços inexistents o ambigus. No presenta aquesta prova com un lint
complet de la volta.
