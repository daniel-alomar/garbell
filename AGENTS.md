# Projecte Garbell

L'entrada és `skills/garbell/SKILL.md`; context a `context/product.md`.
Mantén les regles científiques a `references/research.md` dins de la skill;
els rols d'agent hi remeten en lloc de duplicar-les.
No hi incorporis la volta real,
articles personals ni converses. Els rols d'agents són opcionals i no activen
execucions. No atribueixis revisió humana a comprovacions de l'agent.

Proves: python3 -B -m unittest discover -s tests. Paquet: python3 scripts/distribute.py.
Els exemples són opcionals i no són el corpus de l’usuari. Quan es basen
en articles reals, identifica procedència, versió i abast llegit; no inventis
evidència ni presentis un abstract com una lectura completa.
