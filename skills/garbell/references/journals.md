# Revistes i tipus de document del corpus

Consulta aquesta guia en incorporar o actualitzar fonts. Mantén dues vies
complementàries de navegació: per revista i per tipus de document. L'agent
les actualitza amb Markdown i enllaços; no requereixen plugins d'Obsidian.

## Llistat de revistes

Crea `wiki/revistes.md` quan hi hagi documents amb revista identificada.
Agrupa pel títol normalitzat de la revista i enllaça totes les fitxes del
corpus que hi corresponen. La unitat del recompte és el treball bibliogràfic,
no cada còpia o versió. Conserva el nom original o l'abreviatura com a àlies
quan la correspondència estigui verificada. Un ISSN conegut ajuda a distingir
títols semblants; no fusionis revistes només per noms coincidents.

Una taula suficient: revista | treballs del corpus | fitxes. Si aporta context,
crea també una nota `type: journal` a `wiki/revistes/` amb títol, àlies, ISSN
si consta i documents relacionats. No cal una pàgina per revista amb poc contingut.
Les tesis, informes i documents sense revista continuen al catàleg documental;
no se'ls ha d'assignar una revista fictícia. Un repositori de preprints no és
la revista de publicació. No creïs llistats buits en una volta sense dades.

## Classificació de les fitxes

Mantén `type: source` per al tipus de nota de la wiki. Afegeix aquests camps
bibliogràfics quan es puguin determinar:

```yaml
document_type: null
editorial_format: null
publication_version: null
journal_title: null
venue_title: null
classification_evidence: []
```

| Camp | Què descriu | Valors orientatius |
|---|---|---|
| `document_type` | Naturalesa del treball | `research_article`, `review`, `conference_paper`, `thesis`, `report`, `book`, `book_chapter`, `dataset`, `editorial`, `correspondence`, `other` |
| `editorial_format` | Denominació editorial específica | `letter`, `short_communication`, `full_article`; conservar l'etiqueta original al cos |
| `publication_version` | Versió efectivament consultada | `preprint`, `accepted_manuscript`, `version_of_record` |
| `journal_title` | Revista on es publica el treball | Nom bibliogràfic verificat |
| `venue_title` | Altres llocs de publicació | Congrés, actes o sèrie, quan pertoqui |
| `classification_evidence` | Procedència de la classificació | Ruta/URL i pàgina, secció o camp de metadades |

Són categories inicials ampliables segons la disciplina. Una revisió sistemàtica
pot usar `document_type: review` amb el subtipus explicat al cos. «Paper» és
un terme general: no l'utilitzis com a categoria si es pot precisar. Una Letter
pot ser un article de recerca breu o una correspondència; decideix segons
la denominació editorial i el contingut, no pel nom de la revista ni pel
nombre de pàgines. «Physical Review Letters» és un títol de revista; no és
per si sol evidència del format de tots els seus documents.

Un preprint d'un article manté el tipus d'article; la versió és una altra dada.
Si hi ha diverses versions, descriu cadascuna amb el seu fitxer/URL i abast
llegit, sense duplicar el treball com si fossin estudis diferents. La lectura
d'un abstract es registra a `read_scope`, no com una versió editorial ni
com una lectura íntegra. Deixa `null` i explica el dubte si no es pot classificar.

## Catàleg per tipus

Crea `wiki/tipus-documents.md` amb els tipus presents, les fitxes corresponents
i, quan constin, format i versió. Les dues pàgines de catàleg són `type: map`,
amb els camps bàsics de l'esquema i dependències de les fonts que agrupen.
Enllaça-les des de `wiki/index.md`. Revisa-les si s'afegeix una font, es
corregeixen metadades o es resol la identitat entre versions. Preserva les
edicions humanes i proposa canvis separats si hi ha conflicte.

La classificació facilita recuperar materials; no implica haver-ne completat
la lectura ni haver verificat l'estat de revisió per parells. Les voltes
existents poden conservar metadades bibliomètriques aportades per l'usuari;
aquest flux no les esborra ni les actualitza automàticament.
