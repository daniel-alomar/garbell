# Reading and visualizing the Garbell demonstration

[English](demo-guide.md) · [Català](../../examples/demo/wiki/guia.md)

This guide describes the example’s organization, not a source for its subject matter. The vault notes and original documents are in Catalan.

## The pieces

| Piece | Meaning | How to explore |
|---|---|---|
| `raw/` | Original documentary summaries of three real abstracts | Follow DOI and URL to the papers |
| `wiki/fonts/` | Metadata, version and reading scope | Check provenance before reusing conclusions |
| `wiki/metodes/` | Notes on selected methods | Return to the source note for reading limitations |
| `wiki/conceptes/` | Analytical guidance on evidence, model and scope | Separate agent proposals from attributed findings |
| `wiki/autors/` | Collective authorship navigation | Do not treat authorship as a reliability score |
| `wiki/sintesis/` | Provisional comparisons | Follow each claim's locators |
| `wiki/preguntes/` | Open questions and reading plan | Check what reading is required |
| `wiki/pendents.md` | Full papers still unread | Do not treat scientific ingestion as complete |

Start at the [comparison](../../examples/demo/wiki/sintesis/comparacio.md), open
[LZ's source note](../../examples/demo/wiki/fonts/lz-2023.md), then return to the
[documentary summary](../../examples/demo/raw/lz-2023.md), section 2. The source
note distinguishes the paper, our summary and the content actually consulted.
`read_scope` records the scope of reading.

## Navigate the bibliography

[Journals](../../examples/demo/wiki/revistes.md) groups works by publication;
[document types](../../examples/demo/wiki/tipus-documents.md) distinguishes
nature, format and consulted material. Both catalogues link to source notes
and do not imply full reading of the papers.

The [Planck addition](../../examples/demo/wiki/fonts/planck-2020.md) supplies a
[comparison matrix](../../examples/demo/wiki/sintesis/tres-vies.md) and
[reading plan](../../examples/demo/wiki/preguntes/pla-lectura.md) for retrieving
sources and organizing checks before writing conclusions.

## Reading the metadata

`sources` and `source_notes` record dependencies. `status: draft` means a draft,
not human review. Tags can group notes; they do not score quality. Graph edges
show links, but reading each note explains whether a relation is an application,
comparison, reference or something else. An index link does not prove a
conceptual relationship.

## Optional graph colours

In Obsidian's graph settings, open **Groups**, add a query and choose its colour.
These groups are included in `examples/demo/.obsidian/graph.json`:

| Group query | Colour | Meaning |
|---|---|---|
| `path:wiki/fonts/` | Blue | Source notes |
| `path:wiki/metodes/` | Green | Methods |
| `path:wiki/preguntes/` | Orange | Questions |
| `path:wiki/sintesis/` | Purple | Syntheses |

Open the complete `examples/demo/` folder as a vault and then the global graph.
Copying only `wiki/` is insufficient: the hidden `.obsidian/` folder holds the
profile. If you had the vault open when the profile was added, close and reopen
it. The demo filters the graph to `wiki/` notes; you can change this filter.

Colours are optional. Change them under Groups or reset them in graph settings.
Do not copy this profile over a personal vault's preferences without reviewing
it. Local graphs can have their own options. No plugins need to be installed.
Only the authored demo profile is distributed, not personal window history or
configuration. Its JSON format has been checked; visual rendering has not been
validated in an Obsidian graphical session for this revision.
[Official graph documentation](https://obsidian.md/help/plugins/graph).
