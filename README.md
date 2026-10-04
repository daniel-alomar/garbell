# Garbell

[English](README.md) · [Català](README.ca.md)

Garbell helps build and maintain an Obsidian vault for research or a PhD.
The agent prepares bibliographic notes, connects concepts and methods, and
compares results while preserving authorship, context and limitations.
Claims point to sources and verifiable locators; syntheses distinguish paper
results from your own interpretations and hypotheses. The vault supports
writing, retrieving evidence and identifying gaps or disagreements to revisit.

A **garbell** is a sieve used to separate grain from chaff. The name expresses
a critical approach to reading and organizing information: asking what supports
each conclusion and how far the evidence reaches. Garbell also preserves
negative results, contradictions and uncertainty when relevant to the research.
A useful synthesis should let you retrace how it was reached.

[Garbell repository](https://github.com/daniel-alomar/garbell).

## How the project works

Garbell provides one skill for the AI agent you work with. In normal use, one agent
reads sources, creates and connects notes, and reviews the result in stages.
You do not need to run two agents.

- `agents/` contains optional coordinator and reviewer role guides.
- `skills/garbell/agents/openai.yaml` contains Codex display metadata, not another agent.
- `AGENTS.md` provides contextual instructions for working on the project.

[Operations and step-by-step workflow](docs/en/workflow.md).

## Getting started

Copy `skills/garbell/` into your agent's skills directory, or ask it to read
`skills/garbell/SKILL.md`. The agent needs to read your sources and write files.
In Codex, invoke `$garbell`; the agent performs reading and synthesis.
Use Obsidian to browse and edit the result.

Example request (replace the paths with your own):

> Use $garbell. Organize the papers in `/path/papers` into a vault at
> `/path/research-vault`. Preserve originals and create bibliographic notes
> with verifiable citations. Compare results and methods, distinguish evidence
> from interpretation, and identify pending reading.

Open the whole vault folder in Obsidian: it contains `raw/` and `wiki/`.
Start at `wiki/index.md`. Opening only `wiki/` excludes the sources needed
by the demonstration's links. The skill runs on request; recurring work
requires an agreed schedule and folders.

## Using other AI agents

The core is portable: Markdown instructions, references and local scripts,
with no OpenAI API calls or SDK dependency. It requires an agent with read
and write access to sources and the vault. A chat without file access cannot
maintain the folder directly.

Claude Code supports the same skill format. Copy the whole `skills/garbell/`
folder to `~/.claude/skills/garbell/` and invoke `/garbell`. The `$garbell` syntax
in the examples is for Codex. See the [Claude Code documentation](https://code.claude.com/docs/en/skills).

The skill's `agents/openai.yaml` is Codex-specific metadata and is not part
of the procedure Claude needs. The project-level roles remain optional guides,
not installed Claude subagents. To load project context in Claude Code, ask
it to read `AGENTS.md` or reference it from your existing `CLAUDE.md`, without
replacing that file. [Project context in Claude Code](https://code.claude.com/docs/en/memory).

Format compatibility is documented; these projects have not yet been tested
end to end with Claude Code. Other Claude environments and other providers
may require different installation steps and permissions.

## Python helper

**Python is optional.** You can create, query and maintain the vault with the
agent and Obsidian, provided the agent can read the supplied formats.
To work without Python, add this to your request:

> Work without Python and save `tooling: manual` in `knowledge.yaml`.

The agent interprets this setting. It checks sources and links with available
readers and records what it read. Source notes, citations and connections are
preserved. You lose automatic hash-based detection of duplicates, edited notes
and sources changed during processing; maintenance may require more rereading.
If a format cannot be read without Python, the agent leaves it pending and
explains why.

**Who runs Python?** The agent, if it has command execution and file access.
You request work in natural language; you do not need to copy commands in
normal use. Installing Python is insufficient if the agent cannot run it.
The commands below document maintenance and diagnostics.

| Mode | Benefits | Costs and limitations |
|---|---|---|
| With Python | Repeatable link checks; hash-based change and duplicate detection; protection against sources changing between reading and acceptance | Requires Python 3.10+, `fcntl` and command execution; hashing large corpora takes time; local state must be maintained |
| Without Python | Fewer execution requirements; works with file readers and editors without an interpreter | More rereading and review by the agent; less automatic change and duplicate detection; some formats may remain pending |

In both modes, the agent synthesizes and reviews evidence. Python does not
validate the truth of the content or replace human review. Use `auto` for
normal operation and `manual` when you do not want Python or the environment
cannot run it. “Manual” means the agent uses other tools, not that you must
perform all checks yourself.

By default, `tooling: auto` uses the helper when available. Otherwise, the
agent explains the cause and offers environment setup or work without Python.
It waits for your choice before changing mode. `tooling: python` explicitly
requests automatic checks. [Operational mode reference (Catalan)](skills/garbell/references/tooling.md).

### If Python is unavailable

The agent should explain the problem in plain language and offer:

1. **Help installing or preparing Python**, with instructions for your system
   and the agent's environment. It does not install software automatically.
2. **Continue without Python**, preserving notes, citations, connections and
   queries, with less automatic change and duplicate detection and more review.

It must wait for your decision, and must not ask again on every run after
you choose manual mode. It distinguishes a missing interpreter from an agent
that cannot execute commands: installing Python on your computer does not
necessarily solve a restriction in a remote environment.

### Requirements and libraries

No `pip` packages are required: the utilities use only the **Python 3.10+
standard library**.

| Component | Modules used | Specific requirement |
|---|---|---|
| Inventory, links and acceptance | `argparse`, `collections`, `datetime`, `fcntl`, `hashlib`, `json`, `os`, `pathlib`, `re`, `tempfile` | `fcntl` requires Unix, such as Linux/macOS; the helper does not run under native Windows Python |
| Packaging | `argparse`, `json`, `pathlib`, `zipfile` | ZIP compression needs `zlib`, normally included with Python |
| Tests | `unittest`, `importlib.util` and standard file/hash modules | Import the helper and therefore also require `fcntl` |

On Windows, use a Linux environment such as WSL with Python, or manual mode.
`fcntl` is not a package to install with `pip`. PDF/DOCX readers, OCR and
transcription are not included in these utilities and may need other tools
in the agent's environment. The scripts require no AI library.

## Optional examples

[Demonstration guide](examples/README.en.md): dark matter research based on
three real papers, with DOIs, versions and verifiable references. Includes
source notes, methods, an evidence comparison and research questions. It uses
original summaries of abstracts; reading the full papers remains pending.

Open **`examples/demo/`** as a vault in Obsidian, then open `wiki/index.md`.
The examples are labelled, are not loaded automatically and are not part of
the installed skill. You can remove `examples/` without affecting operation;
the demonstration test is skipped if it is absent. Keep examples separate
from your real sources. The demonstration is one possible organization,
not a mandatory template.

The [practical walkthrough](examples/WALKTHROUGH.en.md) includes prompts,
expected responses and a two-stage addition showing how the vault develops.

## Optional recommendation: graph colours

Colours are an Obsidian navigation aid. The skill works without them and does
not automatically configure personal vault graphs. The demo includes a colour
profile; its [reading and visualization guide](docs/en/demo-guide.md) explains
how to open the graph, interpret the legend and change or remove it.

## Folders

- `skills/garbell/`: instructions, references and optional checker.
- `agents/`: optional role guides, not executable agents.
- `docs/ca/` and `docs/en/`: project guides.
- `context/`: product purpose and decisions.
- `memory/`: optional local summaries, excluded from distribution.
- `examples/`: removable demonstration.
- `scripts/` and `tests/`: distribution tools and project tests.

## Auxiliary vault checks

`skills/garbell/scripts/vault_state.py` requires Python 3.10+ on Linux/macOS
(`fcntl`) and only the standard library. Run these commands from `skills/garbell/`,
usually through the agent:

| Function | Purpose | Effect |
|---|---|---|
| `scan` | Compare sources and notes against saved state; report changes, missing files and duplicates | Read-only |
| `links` | Find missing or ambiguous wikilink destinations | Read-only |
| `accept` | Record a reviewed source and hashes of dependent notes | Writes `.wiki/state.json` |

```sh
python3 scripts/vault_state.py scan /path/to/vault
python3 scripts/vault_state.py links /path/to/vault
```

See the [schema (Catalan)](skills/garbell/references/schema.md) for `accept` syntax
and preconditions. The tool does not summarize documents, validate citations
or knowledge, or check anchors, Markdown links or metadata. Content review
is still necessary. OCR and transcription depend on available readers.

## Testing and preparing a distribution

This section is for people modifying or sharing the project. **You do not
need to run these commands to use the skill or open a vault in Obsidian.**
With Python, from the project root:

```sh
python3 -B -m unittest discover -s tests
python3 scripts/distribute.py
python3 scripts/distribute.py --without-examples
```

The first command checks the utilities, protection of human edits and demo
links. The second creates a ZIP and distributable file manifest in `dist/`.
The third prepares a version without examples; **it does not disable Python**.
Without Python, copy `skills/garbell/` directly and share selected files without
automated packaging. Local memory, personal vaults, conversations and secrets
are excluded from automated distribution. The licence remains undecided.

## Journals and document types

Garbell also organizes sources by journal and document type. The journal list
shows which publications are represented in the vault and links to their works.
The document catalogue helps find research articles, reviews, conference papers,
theses, reports and other materials in the corpus.

Each source note can record editorial format, such as a *Letter*, and the
version consulted: preprint, accepted manuscript or version of record. This
separates what the document is, where it was published and which version was read.

[Journal and document organization (Catalan)](skills/garbell/references/journals.md).

## Related project

[Farcell](https://github.com/daniel-alomar/farcell) organizes documents and information on any topic into connected knowledge, with adaptable profiles for different uses.
