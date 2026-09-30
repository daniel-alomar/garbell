---
id: demo-guia
type: synthesis
status: draft
created: "2026-09-30"
updated: "2026-09-30"
tags: [demostracio, guia]
sources: []
source_notes: []
---

# Com llegir la demostració de Garbell

Guia sobre l'organització de l'exemple; no és evidència científica ni una
síntesi dels resultats dels articles.

| Peça | Què representa | Com explorar-la |
|---|---|---|
| `raw/` | Resums documentals propis de dos abstracts reals | Segueix DOI i URL cap als articles |
| `wiki/fonts/` | Metadades, versió i abast llegit | Consulta la procedència abans de reutilitzar una conclusió |
| `wiki/metodes/` | Notes sobre els mètodes dels documents seleccionats | Torna a la fitxa per veure el límit de lectura |
| `wiki/conceptes/` | Pauta analítica d'evidència, model i abast | Distingeix les propostes de l'agent dels resultats atribuïts |
| `wiki/autors/` | Navegació per autoria col·lectiva | No interpretis autoria com una puntuació de fiabilitat |
| `wiki/sintesis/` | Comparació provisional de dues preguntes | Segueix els localitzadors de cada afirmació |
| `wiki/preguntes/` | Qüestió encara no resolta | Consulta les lectures necessàries |
| `wiki/pendents.md` | Falta de lectura integral dels papers | No donis per completada la ingestió científica |

Comença per [[wiki/sintesis/comparacio|la comparació]], obre
[[wiki/fonts/lz-2023|la fitxa de LZ]] i torna al
[[raw/lz-2023#2. Resultat reportat|resum documental]]. La fitxa diferencia
l'article, el resum propi i el contingut efectivament consultat.

Les propietats `sources` i `source_notes` registren dependències; `read_scope`
explica abast. `status: draft` no indica revisió humana. El graf mostra
enllaços; llegir les notes explica el significat i els límits de les relacions.

## Colors suggerits

Als grups del graf d'Obsidian pots triar, per exemple, `path:wiki/fonts/`
en blau, `path:wiki/metodes/` en verd i `path:wiki/preguntes/` en taronja.
Són opcions de visualització que configures a l'aplicació, no propietats de
validesa científica. No s'inclouen preferències personals ni plugins.
[Ajuda oficial del graf](https://obsidian.md/help/plugins/graph).
