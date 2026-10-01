# Prova Garbell com a suport a una recerca

Aquest exemple és un resultat preparat per explorar el flux, no una prova
que qualsevol agent faci una revisió científica correcta. Parteix d'abstracts
reals i resums propis; utilitza una còpia temporal per provar incorporacions.

## 1. Recuperar informació amb procedència

Situació: has començat a recollir lectures sobre matèria fosca i vols preparar
una reunió. Obre `demo/` a Obsidian. Pots demanar a l'agent:

> Quines vies d'estudi hi ha al corpus? Compara les preguntes dels documents
> i enllaça cada afirmació amb el passatge consultat. Indica l'abast de lectura.

El resultat esperat separa observació de cúmuls, cerca experimental i inferència
cosmològica. La [matriu de tres vies](demo/wiki/sintesis/tres-vies.md) mostra
una organització possible. L'agent no hauria de presentar tres nombres com
si mesuressin el mateix ni sumar les evidències sense revisar-ne dependències.

## 2. Preparar una síntesi i identificar què falta

> Prepara un esquema breu de discussió amb el que podem dir, el que és
> interpretació i el que necessitem llegir abans de defensar una conclusió.

Una resposta útil remet a fonts, distingeix la proposta d'organització de les
conclusions dels autors i acaba amb tasques concretes de lectura. El
[pla de lectura](demo/wiki/preguntes/pla-lectura.md) és una possible sortida.
No inventa una pregunta de tesi ni pressuposa llegits els papers complets.

Prova també: «El resultat de LZ contradiu automàticament els altres dos?». La
comparació ha d'explicar que les preguntes i hipòtesis són diferents i que
caldria un model explícit per establir una incompatibilitat. Els abstracts
no permeten resoldre aquesta qüestió general. La resposta s'ha de poder rastrejar
fins a les fitxes, no recolzar només en la reputació d'una revista.

## 3. Navegar pel que tens

> Quins treballs hi ha per revista? Quin format té el de LZ? Quines versions
> i quines parts s'han consultat?

Els [catàlegs](demo/wiki/revistes.md) permeten recuperar treballs per revista;
els [tipus documentals](demo/wiki/tipus-documents.md) separen tipus i format.
La fitxa de LZ conserva l'evidència del format Letter. La lectura de metadades
i abstract no es converteix en lectura completa d'una versió publicada.

## 4. Veure com s'amplia el coneixement

Per reproduir una incorporació, copia primer només els resums de Clowe i LZ
a una entrada temporal i crea una volta nova amb Garbell. Després afegeix
`planck-2020.md` a aquella entrada i demana:

> Incorpora aquesta nova font. Amplia la comparació quan aporti una perspectiva
> útil, actualitza els catàlegs i registra què no s'ha pogut verificar.

La tercera font ha d'afegir una via a la comparació, una fitxa i dependències
traçables. La comparació prèvia entre dos estudis pot continuar sent vàlida
amb el seu abast. La nota de metadades sobre una correcció ha de generar una
lectura pendent, no una afirmació que l'agent ja ha avaluat els seus efectes.

## 5. Passar a documents complets

Quan disposis dels papers complets, aporta'ls a la còpia temporal i demana
lectura detallada, amb pàgines i figures. L'agent ha de distingir aquest nou
abast del dels resums, reutilitzar la identitat del treball i revisar les
síntesis afectades. Aquest pas requereix els documents; no està simulat com
a completat a la demostració inclosa.

La utilitat pràctica és poder passar d'una pregunta a les evidències i als
buits de lectura, i mantenir aquesta relació quan el corpus creix. El graf
ajuda a explorar; les afirmacions i els localitzadors permeten revisar el resultat.
