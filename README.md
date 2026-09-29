# Garbell

Passar pel sedàs: lectura crítica, atribució i comparació d’evidències per a la recerca.

Projecte independent: [repositori Garbell](https://github.com/daniel-alomar/garbell).
No necessita instal·lar l’altre projecte. Té les seves pròpies utilitats,
proves, exemples i historial.

## Començar

Copia `skills/garbell/` al directori personal de skills del teu agent, o
indica-li explícitament que llegeixi `skills/garbell/SKILL.md`.
La skill s’invoca com a `$garbell`. Indica la carpeta de fonts, la destinació
per a la volta i l’objectiu. No crea cap tasca periòdica automàticament.

Exemple de petició:

> Utilitza $garbell amb les fonts que t’indico. Crea una volta nova en català
> a la destinació que t’indico, conserva els originals i explica les relacions
> entre notes amb evidència i localitzadors.

## Exemples opcionals

[Guia de la demostració](examples/README.md): dues fonts fictícies i una
volta petita amb el resultat esperat. Pots obrir `examples/demo/` a Obsidian
per veure’n les connexions. Tot el contingut és sintètic, incloses les dades
numèriques; no s’ha d’utilitzar com a informació real.

Els exemples ajuden a entendre l’ús, però no són una estructura obligatòria
ni s’inclouen a la skill instal·lada. Es pot eliminar tota la carpeta
`examples/` sense afectar les eines. No els copiïs al `raw/` d’una volta real.
La prova de l’exemple s’omet si s’ha eliminat la carpeta.

## Carpetes

- `skills/garbell/`: skill autocontinguda i comprovador de canvis.
- `agents/`: rols opcionals de coordinació i revisió; no s’activen sols.
- `context/`: objectiu i decisions del producte.
- `memory/`: resums locals opcionals, exclosos de la distribució.
- `examples/`: demostració fictícia eliminable.
- `scripts/` i `tests/`: empaquetament i verificació independents.

## Verificar i empaquetar

Python 3.10 o superior en Linux/macOS (`fcntl`). La síntesi la fa l’agent;
l’OCR i la transcripció depenen de les eines disponibles.

```sh
python3 -B -m unittest discover -s tests
python3 scripts/distribute.py
python3 scripts/distribute.py --without-examples
```

Es generen un ZIP i un manifest a `dist/`. El manifest enumera exclusivament
els fitxers distribuïbles. Ni voltes personals, ni converses ni secrets
formen part del paquet. La llicència continua pendent de decisió.

## Projecte relacionat

[Farcell](https://github.com/daniel-alomar/farcell) és un projecte
separat: la base general per construir coneixement de qualsevol tema.
La relació és informativa; no hi ha dependència entre instal·lacions.
