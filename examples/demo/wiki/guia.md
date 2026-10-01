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
| `raw/` | Resums documentals propis de tres abstracts reals | Segueix DOI i URL cap als articles |
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

## Recomanació opcional: colors

Als grups del graf d'Obsidian pots triar, per exemple, `path:wiki/fonts/`
en blau, `path:wiki/metodes/` en verd i `path:wiki/preguntes/` en taronja.
La demostració inclou aquests grups a `.obsidian/graph.json`, amb les síntesis
en violeta. Són ajudes de navegació, no propietats de validesa científica.
[Ajuda oficial del graf](https://obsidian.md/help/plugins/graph).

### Veure els colors de la demostració

Obre la carpeta completa `examples/demo/` com a volta i després la vista de
graf global. No n'hi ha prou amb copiar només `wiki/`: la carpeta oculta
`.obsidian/` conté el perfil. Si ja tenies aquesta volta oberta quan s'ha
afegit el fitxer, tanca-la i torna-la a obrir. La demostració filtra el graf
per les notes de `wiki/`; pots canviar aquest filtre.

Els colors són opcionals i es poden modificar a Grups o restablir des de la
configuració del graf. No copiïs el perfil sobre les preferències d'una volta
personal sense revisar-lo. El graf local pot tenir opcions pròpies.
El format del perfil s'ha comprovat com a JSON; la visualització no s'ha
validat en una sessió gràfica d'Obsidian en aquesta revisió.

## Navegar pel corpus bibliogràfic

[[wiki/revistes|Revistes]] agrupa els treballs per publicació;
[[wiki/tipus-documents|tipus de document]] distingeix naturalesa, format
i material consultat. Els dos catàlegs remeten a les fitxes i no impliquen
lectura completa dels papers.

L'ampliació amb [[wiki/fonts/planck-2020|Planck]] ofereix una
[[wiki/sintesis/tres-vies|matriu de comparació]] i un
[[wiki/preguntes/pla-lectura|pla de lectura]]: permet recuperar fonts i ordenar
les comprovacions necessàries abans d'escriure conclusions.
