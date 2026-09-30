# Garbell

Garbell ajuda a construir i mantenir una volta d'Obsidian per a una recerca
o un doctorat. L'agent prepara fitxes bibliogràfiques, relaciona conceptes i
mètodes, i compara resultats sense perdre autoria, context ni limitacions.
Les afirmacions remeten a fonts i localitzadors verificables; les síntesis
distingeixen els resultats dels articles de les interpretacions i hipòtesis
pròpies. La volta facilita escriure, recuperar evidències i detectar buits o
desacords que cal revisar.

Un **garbell** és un sedàs: permet destriar el gra de la palla. El nom expressa
una manera crítica de llegir i ordenar informació, preguntant què sosté cada
conclusió i fins on arriba l'evidència. Garbell conserva també els resultats
negatius, les contradiccions i les incerteses quan són rellevants per a la
recerca; una síntesi útil ha de permetre revisar com s'ha arribat a ella.

[Repositori Garbell](https://github.com/daniel-alomar/garbell).

## Com està plantejat

Garbell conté una skill que utilitza l'agent d'IA amb què treballes.
En l'ús habitual, un únic agent llegeix les fonts, crea notes, les connecta
i revisa el resultat seguint passos. No cal executar dos agents.

- `agents/` conté guies de rols opcionals: coordinador i revisor.
- `skills/garbell/agents/openai.yaml` conté metadades de presentació per a Codex;
  no és un altre agent.
- `AGENTS.md` conté instruccions contextuals per treballar al projecte.

[Funcionament, operacions i procés pas a pas](docs/ca/funcionament.md).

## Començar

Copia `skills/garbell/` al directori de skills del teu agent, o demana-li que
llegeixi `skills/garbell/SKILL.md`. Necessites un agent capaç de llegir les
fonts i escriure fitxers. La skill s'invoca com a `$garbell`; la lectura i
síntesi les fa l'agent. Obsidian permet navegar i editar el resultat.

Exemple de petició (substitueix les rutes per les teves):

> Utilitza $garbell. Organitza els articles de `/ruta/articles` en una volta a
> `/ruta/volta-recerca`. Conserva els originals i crea fitxes
> bibliogràfiques amb cites verificables. Compara resultats i mètodes,
> distingeix evidència i interpretació, i assenyala lectures pendents.

Obre la carpeta de la volta a Obsidian: contindrà `raw/` i `wiki/`.
El punt d'entrada és `wiki/index.md`. Obrir només `wiki/` deixa fora les fonts
que necessiten els enllaços de la demostració. La skill treballa sota demanda;
una execució periòdica requereix acordar el calendari i les carpetes.

## Ús amb Python o sense

**Python és opcional.** Pots crear, consultar i mantenir la volta amb l'agent
i Obsidian, sempre que l'agent disposi de les eines necessàries per llegir
els formats aportats. Per prescindir de Python, afegeix a la petició:

> Treballa sense Python i desa `tooling: manual` a `knowledge.yaml`.

La configuració la interpreta l'agent. En aquest mode comprova fonts i
enllaços amb els lectors disponibles i documenta les lectures al registre.
Es conserven les fitxes, les cites i les connexions. Es perd la detecció
automàtica per empremtes de duplicats, modificacions de notes i canvis de
fonts durant el procés; el manteniment pot requerir més relectures. Si no
pot llegir un format sense Python, el deixa pendent i explica el motiu.

**Qui executa Python?** L'agent, si disposa d'una eina per executar
comandaments i accés als fitxers. L'usuari demana la tasca en llenguatge natural;
no ha de copiar comandaments durant l'ús habitual. Tenir Python instal·lat
no és suficient si l'entorn de l'agent no permet executar-lo. Els comandaments
de més avall són documentació per al manteniment i la diagnosi.

| Mode | Avantatges | Costos i limitacions |
|---|---|---|
| Amb Python | Comprovacions repetibles d'enllaços; detecció per empremtes de canvis i duplicats; protecció davant canvis de la font entre lectura i acceptació | Requereix Python 3.10+, `fcntl` i execució de comandaments; llegir fitxers per calcular empremtes consumeix temps en corpus grans; cal mantenir l'estat local |
| Sense Python | Menys requisits d'execució; útil en entorns amb lectors i edició de fitxers però sense intèrpret | Més relectura i revisió per l'agent; menys detecció automàtica de canvis i duplicats; alguns formats poden quedar pendents |

En tots dos modes, l'agent fa la síntesi i revisa les evidències. Python
no valida la veritat dels continguts ni substitueix la revisió humana.
Recomanació: `auto` per a l'ús habitual; `manual` quan no vulguis executar
Python o l'entorn no ho permeti. «Manual» vol dir que l'agent fa les
comprovacions amb les altres eines, no que l'usuari hagi de fer-les totes.

Per defecte `tooling: auto` utilitza el comprovador quan és disponible; si
no ho és, aplica el procediment manual. `tooling: python` demana explícitament
les comprovacions automàtiques. [Detall dels modes](skills/garbell/references/tooling.md).

## Exemples opcionals

[Guia de la demostració](examples/README.md): recerca sobre matèria fosca basada en dos articles reals, amb DOI, versions
i referències verificables. Inclou fitxes, mètodes, una comparació d’evidències
i preguntes de recerca. Parteix de resums propis dels abstracts, amb la
lectura íntegra dels articles identificada com a pendent.

Obre **`examples/demo/`** com a volta a Obsidian i entra a `wiki/index.md`.
Els exemples estan identificats, no es carreguen automàticament i no formen
part de la skill instal·lada. Pots eliminar `examples/` sense afectar l'ús;
la prova de la demostració s'omet si s'ha eliminat. No els barregis amb les
fonts de la teva volta real. La demostració és una possibilitat d'organització,
no una plantilla obligatòria.

## Recomanació opcional: graf de colors

Els colors són una ajuda de navegació d'Obsidian. La skill pot treballar sense
ells i no configura automàticament el graf de les voltes personals.
La demostració inclou un perfil de colors preparat; la seva guia explica
com obrir el graf, interpretar la llegenda i canviar-la o retirar-la.

## Carpetes

- `skills/garbell/`: instruccions, referències i comprovador opcional.
- `agents/`: guies de rols opcionals, no agents executables.
- `docs/ca/`: explicació del funcionament i preparació de la documentació bilingüe.
- `context/`: objectiu i decisions del producte.
- `memory/`: resums locals opcionals, exclosos de la distribució.
- `examples/`: demostració eliminable.
- `scripts/` i `tests/`: eines de distribució i proves del projecte.

## Comprovacions auxiliars de la volta

L'eina `skills/garbell/scripts/vault_state.py` requereix Python 3.10 o superior
en Linux/macOS (`fcntl`) i només biblioteca estàndard. Aquests comandaments
s'executen des de `skills/garbell/`, habitualment per l'agent:

| Funció | Objectiu | Efecte |
|---|---|---|
| `scan` | Comparar fonts i notes amb l'estat desat; assenyalar canvis, absències i duplicats | Només lectura |
| `links` | Detectar destins de wikilinks inexistents o ambigus | Només lectura |
| `accept` | Registrar la font revisada i les empremtes de les notes dependents | Escriu `.wiki/state.json` |

```sh
python3 scripts/vault_state.py scan /ruta/volta
python3 scripts/vault_state.py links /ruta/volta
```

La sintaxi d'`accept` i els criteris previs són a [l'esquema](skills/garbell/references/schema.md).
L'eina no resumeix documents, no valida cites ni coneixement i no comprova
àncores, enllaços Markdown o metadades. La revisió de contingut continua
sent necessària. L'OCR i la transcripció depenen dels lectors disponibles.

## Provar el projecte i preparar-ne una distribució

Aquest apartat és per a qui modifica o comparteix el projecte. **No cal
executar-lo per utilitzar la skill ni per obrir una volta a Obsidian.**
Amb Python, des de l'arrel del projecte:

```sh
python3 -B -m unittest discover -s tests
python3 scripts/distribute.py
python3 scripts/distribute.py --without-examples
```

El primer comandament comprova les utilitats, la protecció d'edicions humanes
i els enllaços de la demostració. El segon genera un ZIP i un manifest de
fitxers distribuïbles a `dist/`. El tercer prepara una versió sense exemples;
**no és una opció per desactivar Python**. Sense Python, pots copiar la carpeta
`skills/garbell/` directament i compartir els fitxers seleccionats sense generar
el paquet automàtic. Memòria local, voltes personals, converses i secrets
queden fora de la distribució automàtica. La llicència continua pendent de decisió.

## Revistes i quartils: suport opcional

Garbell pot mantenir un registre de les revistes rellevants per al corpus,
amb indicadors verificats per sistema, any i categoria. Pot ajudar a entendre
el context editorial o explorar on publicar. No inclou una llista fixa de
«les millors revistes»: la pertinència depèn de la disciplina i els indicadors
canvien. El quartil tampoc substitueix l'avaluació de cada estudi.

[Guia i plantilla de registre](skills/garbell/references/journals.md).
Les dades no consultades queden pendents; no s'assignen quartils per reputació.

## Idiomes de la documentació

La documentació actual és en català. Per a la versió pública, es proposa
mantenir guies completes en català i anglès amb enllaços entre versions,
conservant una sola implementació de la skill.
[Organització i manteniment de les traduccions](docs/ca/idiomes.md).
La traducció anglesa completa queda pendent de preparar.

## Projecte relacionat

[Farcell](https://github.com/daniel-alomar/farcell) organitza documents i informació de qualsevol
tema en coneixement connectat, amb perfils adaptables a cada ús.
