# Garbell: preguntes de recerca sobre matèria fosca

Demostració basada en dues publicacions reals. Els fitxers de `demo/raw/`
són **resums propis dels abstracts**, amb metadades i enllaços verificats
el 2026-09-30; no són els articles íntegres ni cites literals. El contingut
bibliogràfic no és fictici. L'organització de la volta i les preguntes són
propostes didàctiques, no una tesi ni una revisió exhaustiva de la literatura.

## Articles seleccionats

- Douglas Clowe et al. (2006), *A direct empirical proof of the existence of dark matter*.
  [arXiv v1](https://arxiv.org/abs/astro-ph/0608407v1),
  [DOI de la publicació](https://doi.org/10.1086/508162).
- J. Aalbers et al., LZ Collaboration (2023), *First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment*.
  Preprint inicial de 2022, [versió v4 de 2023](https://arxiv.org/abs/2207.03764v4),
  [DOI de la publicació](https://doi.org/10.1103/PhysRevLett.131.041002).

La selecció històrica serveix per comparar preguntes i mètodes. No pretén
mostrar els resultats més recents ni concloure l'estat actual de la recerca.

## Explorar el resultat

Obre **`demo/`** a Obsidian i entra a `wiki/index.md`. Hi trobaràs dues fitxes,
dues notes de mètode, una de concepte, una d'autoria col·lectiva, una síntesi
i una pregunta. Segueix síntesi → mètode → fitxa → resum documental → article.
[La guia de lectura](demo/wiki/guia.md) explica què representa cada peça i
com visualitzar-la. Consulta `wiki/pendents.md`: llegir el resum no completa la ingestió de l'article.

## Provar la skill

Copia `demo/raw/` a una carpeta temporal i demana:

> Utilitza $garbell per crear una volta de demostració sobre matèria fosca.
> Aquests fitxers contenen resums documentals d'abstracts, no articles complets.
> Conserva aquest límit, prepara fitxes amb DOI i versió, compara les preguntes
> dels estudis i identifica què queda pendent. Treballa sense Python.

La sortida pot adoptar una organització diferent. Per continuar amb articles
complets, aporta'ls a la còpia temporal i demana una lectura amb localitzadors
de pàgines, taules i figures. No donis per llegits els papers a partir de les
fitxes. L'exemple no s'incorpora automàticament a cap biblioteca personal.

## Retirar-lo

Elimina `examples/` quan ja no el necessitis. També pots generar un paquet
sense exemples amb `python3 scripts/distribute.py --without-examples`, o copiar
només `skills/garbell/`. Les publicacions mantenen els seus drets i llicències;
aquí s'inclouen resums propis breus amb atribució, no còpies dels articles.

La carpeta oculta `demo/.obsidian/` inclou únicament el perfil de graf de
la demostració. Conserva-la quan copiïs l'exemple si vols veure els colors
preparats. Aquesta ajuda visual és opcional i no forma part de la skill.

La demostració inclou també `wiki/revistes.md` i `wiki/tipus-documents.md`,
amb els treballs agrupats i la classificació explicada a les fitxes.
