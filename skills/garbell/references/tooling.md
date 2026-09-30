# Treballar amb Python o sense

La síntesi i la revisió les fa l'agent amb les eines de lectura i escriptura
que tingui disponibles. Python és un auxiliar opcional, no el motor de la skill.

## Selecció del mode

Llegeix `tooling` a `knowledge.yaml`, una preferència interpretada per l'agent:

- `auto` (per defecte): usa el comprovador si hi ha Python 3.10+ i `fcntl`
  disponibles i autoritzats; altrament continua en mode manual i informa'n.
- `manual`: no executis Python ni per inventari ni per extracció. Usa els
  lectors disponibles; si un format requereix Python i no hi ha alternativa,
  deixa'l pendent amb el motiu. No instal·lis eines automàticament.
- `python`: usa les comprovacions amb empremtes. Si no es poden executar,
  explica la limitació abans d'actualitzar l'estat; no canviïs el mode en silenci.

Una petició explícita «treballa sense Python» preval sobre el valor desat.
Desa `tooling: manual` sense substituir la resta de la configuració. En una
volta nova, desa el mode acordat. Aquest camp no desactiva el programari
Obsidian ni modifica els scripts: és una instrucció per a l'agent.

## Equivalent manual del procediment

En mode manual, substitueix les operacions `scan`, `links` i `accept`:

1. Enumera les fonts amb les eines de fitxers i consulta `wiki/registre.md`
   i `wiki/pendents.md`. Compara el material amb les lectures documentades;
   una data o mida no prova que el contingut sigui igual. Si no pots demostrar
   que una font és igual, rellegeix-la abans de reutilitzar-ne conclusions.
2. Abans de canviar notes, consulta còpies prèvies i revisions disponibles.
   Sense una base fiable, tracta una nota existent com una possible edició
   humana: conserva-la i escriu la proposta separada. Treballa amb un únic
   escriptor i fes còpies de recuperació amb les eines disponibles.
3. Comprova els destins i localitzadors dels enllaços obrint els fitxers.
   Revisa també fonts, metadades i relacions; indica l'abast de la verificació.
4. Registra ruta de font, data de lectura, abast realment llegit, notes que
   en depenen, comprovacions i pendents a `wiki/registre.md`. No executis
   `accept`, no inventis empremtes i deixa `source_sha256: null`. Una lectura
   parcial continua pendent. L'estat editorial segueix sent `draft` fins
   a una revisió humana explícita.

Es conserven fitxes, cites, relacions, consultes i manteniment sota demanda.
Es perd la detecció automàtica per empremtes de duplicats, canvis d'originals
entre lectura i acceptació, i modificacions de notes. El manteniment pot
requerir més relectura; no presentis la revisió manual com a equivalent
criptogràfic del comprovador.

## Canvi de mode

En passar a manual, conserva `.wiki/state.json` si existeix i no el modifiquis;
indica al registre des de quan no s'actualitza. En tornar a Python, considera
el registre manual i revisa fonts i notes abans de donar-les per acceptades.
No importis dates com si fossin empremtes ni acceptis conflictes per establir
una base nova. Sense una base segura, proposa canvis separats.

## Què fa el comprovador

Consulta [l'esquema](schema.md) per a la sintaxi dels comandaments.
`scan` inventaria i compara empremtes; `links` comprova destins de wikilinks;
`accept` desa l'estat de fonts completades i notes dependents després de la
revisió. Cap d'aquestes operacions resumeix documents ni valida coneixement.

En manteniment periòdic manual, no afirmis «sense canvis» si només has
comparat dates o mides. Informa dels canvis realment verificats i de les
comprovacions que no s’han pogut fer; evita recomptes de duplicats no demostrats.
