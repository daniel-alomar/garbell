# Revistes i indicadors: context opcional de la recerca

Llegeix aquesta referència quan l'usuari demani contextualitzar revistes,
registrar quartils o explorar on publicar. No és un filtre d'ingestió ni una
llista universal de revistes prestigioses. Tria les revistes segons la
pregunta, disciplina i corpus; una revista generalista no substitueix una
revista especialitzada pertinent.

## Com interpretar les dades

Un quartil és una posició relativa dins una classificació. Registra sempre
el sistema, la mètrica, l'any de dades i la categoria. Una revista pot tenir
més d'una categoria i quartils diferents; conserva'ls, sense triar només el
més favorable. El JIF de JCR i l'SJR de SCImago són indicadors diferents;
no traslladis el quartil d'un a l'altre ni un valor actual a l'any de l'article.
Q1 representa el grup superior de la classificació corresponent, no una
certificació de la validesa dels articles. Respecta els quartils publicats
pel proveïdor, inclosos empats i casos sense classificació.

JCR és un informe anual i Clarivate desaconsella utilitzar el JIF per avaluar
articles individuals. La lectura de mètodes, evidències i limitacions continua
sent necessària. [JCR](https://clarivate.com/academia-government/scientific-and-academic-research/research-funding-analytics/journal-citation-reports/).
La classificació és per categoria i pot tenir empats:
[explicació de Clarivate](https://clarivate.com/academia-government/blog/a-primer-on-ties-in-the-jcr/).

## Registre verificable

Quan sigui útil, crea `wiki/revistes/` amb notes `type: journal` i el mateix
esquema bàsic que la resta de notes. Identifica títol i ISSN només si s'han
verificat, i enllaça els articles del corpus. Una entrada de mètrica pot
seguir aquest format; els valors nuls són pendents, no zeros:

```yaml
journal_title: null
issn: []
metrics:
  - system: null          # JCR o SCImago, segons la font realment consultada
    metric: null          # JIF, SJR o un altre indicador identificat
    data_year: null
    edition: null
    category: null
    quartile: null
    value: null
    source_url: null
    accessed_on: null
    verification_status: pending
```

Consulta la font autoritzada, registra l'accés i desa evidència o localitzador
segons els permisos disponibles. Declara aquesta evidència a `sources`,
separada dels articles publicats per la revista. Si només tens un catàleg
bibliogràfic, això verifica el nom de la revista, no el seu quartil.
JCR pot requerir accés institucional; no pressuposis que hi ha accés.
[SCImago Journal & Country Rank](https://www.scimagojr.com/) és un altre
recurs de consulta: indica explícitament sistema i indicador.

Si la dada no es pot consultar, deixa-la pendent amb el motiu. Si s'actualitza,
conserva l'any anterior com una observació diferent. No refresquis indicadors
ni iniciïs cerques recurrents sense que formin part de l'encàrrec.
No prioritzis, excloguis ni donis per fiable un article només pel quartil.

## Quan aporta valor

És útil per descriure el context editorial del corpus o preparar una selecció
de revistes candidates per publicar. En aquest últim cas també cal considerar
abast temàtic, tipus d'article, públic, polítiques i condicions vigents.
Per entendre què demostra un estudi, el registre de revistes és secundari.
