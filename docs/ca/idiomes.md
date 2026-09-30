# Documentació en català i anglès

## Estat actual

La documentació és en català. Aquesta pàgina defineix la proposta per a la
versió pública; la traducció anglesa completa encara no s'ha preparat.
Les guies actuals es troben a `docs/ca/`.

## Estructura proposada per a la publicació

Per facilitar l'arribada de lectors internacionals, proposem un README principal
en anglès amb un enllaç visible a la versió catalana, igualment completa:

```text
README.md                 Presentació i inici ràpid en anglès
README.ca.md              Presentació i inici ràpid en català
 docs/ca/                 Guies en català
 docs/en/                 Guies equivalents en anglès
 skills/                  Una sola implementació de cada skill
 examples/                Demostracions amb idioma i abast identificats
```

Cada pàgina traduïda ha de tenir un enllaç a la seva equivalent en l'altre
idioma, sense obligar a tornar a la portada. No s'han de publicar enllaços
a traduccions que encara no existeixen. Fins que es tradueixi, el README
actual continua en català. Aquesta organització és una decisió editorial
proposada per al projecte, no un requisit de GitHub.

## Evitar divergències

Mantindrem equivalència de contingut entre els dos idiomes. Quan canviï una
funció, actualitzarem les dues guies afectades en el mateix canvi o indicarem
explícitament quina traducció està pendent. Cada traducció llarga pot indicar
la revisió del text d'origen en què es basa i la data de revisió lingüística.
No s'ha de presentar una traducció automàtica sense revisar com a documentació
verificada. Per a la primera versió pública, cal revisar en ambdós idiomes
instal·lació, flux, requisits, límits i exemples de petició.

## Documentació, instruccions i contingut són coses diferents

Traduir les guies d'usuari no exigeix duplicar `SKILL.md`, scripts ni rols.
La skill manté una única versió operativa per evitar instruccions contradictòries;
les guies en català i anglès n'expliquen el mateix comportament. Si més endavant
es canvia la llengua interna de la skill, serà una edició de la mateixa
implementació, amb revisió de comportament.

La llengua de les voltes es decideix segons la petició i la configuració de
cada volta, no segons la llengua del README. Les convencions i noms de camps
no es tradueixen automàticament. Les cites i els títols bibliogràfics conserven
la llengua original. Abans de publicar cal revisar i explicar també els
valors d'idioma per defecte de cada skill.

Els exemples actuals poden conservar-se en català amb una guia anglesa.
Si volem una demostració íntegra en anglès, la prepararem com una còpia
identificada i revisarem enllaços i localitzadors; no traduirem fitxers en
una volta de l'usuari ni barrejarem idiomes dins la mateixa demostració.
