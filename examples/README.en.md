# Garbell: research questions about dark matter

[English](README.en.md) · [Català](README.md)

This demonstration uses three real publications. Files in `demo/raw/` are
**original summaries of abstracts**, with metadata and links checked between
2026-09-30 and 2026-10-01. They are not full papers or verbatim quotations.
Bibliographic content is real. Vault organization and questions are teaching
proposals, not a thesis or an exhaustive literature review. The demo files
remain in Catalan; these guides explain how to explore them.

## Selected papers

- Douglas Clowe et al. (2006), *A direct empirical proof of the existence of dark matter*.
  [arXiv v1](https://arxiv.org/abs/astro-ph/0608407v1), [publication DOI](https://doi.org/10.1086/508162).
- J. Aalbers et al., LZ Collaboration (2023), *First Dark Matter Search Results from the LUX-ZEPLIN (LZ) Experiment*.
  Initial preprint in 2022, [v4 from 2023](https://arxiv.org/abs/2207.03764v4),
  [publication DOI](https://doi.org/10.1103/PhysRevLett.131.041002).
- Planck Collaboration, N. Aghanim et al., *Planck 2018 results. VI. Cosmological parameters*.
  Published in 2020, [arXiv v4 from 2021](https://arxiv.org/abs/1807.06209v4),
  [DOI](https://doi.org/10.1051/0004-6361/201833910).

This historical selection compares questions and methods. It does not claim
to show the latest results or establish the current state of the field.

## Explore the result

Open **`demo/`** in Obsidian and start at `wiki/index.md`. It contains three
source notes, method and concept notes, collective authorship, comparative
syntheses and questions with a reading plan. Follow synthesis → method → source
note → documentary summary → paper. The [reading guide](../docs/en/demo-guide.md)
explains each piece and how to visualize it. Check `wiki/pendents.md`: reading
the summary does not complete ingestion of the paper.

## Try the skill

Copy `demo/raw/` to a temporary folder and ask:

> Use $garbell to create a dark matter demonstration vault. These files contain
> documentary summaries of abstracts, not full papers. Preserve this limitation,
> prepare source notes with DOI and version, compare the studies' questions and
> identify pending work. Work without Python.

The output may use a different organization. To continue with full papers,
supply them to the temporary copy and request reading with page, table and
figure locators. Do not treat source notes as proof that the papers were read.
The example is not automatically added to any personal library.

## Remove the example

Delete `examples/` when no longer needed. You can also build a package without
examples using `python3 scripts/distribute.py --without-examples`, or copy only
`skills/garbell/`. Publications retain their rights and licences; this project
includes short original summaries with attribution, not copies of the papers.

The hidden `demo/.obsidian/` folder distributed here contains only the demo
graph profile. Preserve it if you want the prepared colours. This visual aid
is optional and is not part of the skill.

The demo also includes `wiki/revistes.md` and `wiki/tipus-documents.md`, grouping
works by journal and document type, with classification explained in source notes.

[Practical walkthrough for querying, comparing and expanding the vault](WALKTHROUGH.en.md).
