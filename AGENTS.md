# Projecte Garbell

L'entrada és `skills/garbell/SKILL.md`; context a `context/product.md`.
Mantén les regles científiques a `references/research.md` dins de la skill;
els rols d'agent hi remeten en lloc de duplicar-les.
El paquet funciona sense el projecte genèric. No hi incorporis la volta real,
articles personals ni converses. Els rols d'agents són opcionals i no activen
execucions. No atribueixis revisió humana a comprovacions de l'agent.

Proves: python3 -B -m unittest discover -s tests. Paquet: python3 scripts/distribute.py.
Els exemples són opcionals; no els utilitzis com a fonts reals.
