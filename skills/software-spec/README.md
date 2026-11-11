# software-spec

A Claude Skill that ingests a software specification written in the Good
Software Specification Format (GSSF) before any work is done against it.

Given a specification package, Claude reads the specification document and
every auxiliary file, checks the package against the GSSF rules, cross-checks
the prose against the formal artifacts, and reports a consolidated model of
the spec. It stops if anything leaves the spec's meaning uncertain, and
otherwise carries on with the task you asked for.

This skill tracks **GSSF 0.1.0**. The normative text is bundled at
[gssf-gssf/gssf.md](gssf-gssf/gssf.md), which is itself a GSSF package.

## Usage

Point Claude at a specification package:

```
/software-spec path/to/foo-gssf
```

The skill also triggers on requests such as "read the spec in `foo-gssf`",
"here's the spec", or any mention of GSSF. Installed through the
`alpine-skills` plugin, the command is `/alpine-skills:software-spec`.

## What a specification package looks like

```
foo-gssf/
├── foo.md               # the specification document (exactly one, top level)
├── openapi.yaml         # auxiliary files, all optional
├── order.schema.json
└── checkout-flow.mmd
```

The specification document is GitHub Flavored Markdown with these sections, in
this order:

1. Frontmatter: a table with Name, Version, Publication Date, Author(s), and
   Specification Type
2. Conformance: the BCP 14 (RFC 2119 / RFC 8174) boilerplate
3. Rationale
4. Requirements: numbered `REQ-1`, `REQ-2`, ...
5. Security Considerations
6. Glossary

The Specification Type is one of:

| Type | Meaning | Extra rules |
|---|---|---|
| `FEAT` | A feature to build | At least one requirement |
| `BUG` | A bug to fix | Affected Software, Expected Behaviour, Actual Behaviour, and Mitigation sections between Rationale and Requirements |
| `META` | A format, process, or convention | Requirements may be empty |

## What the skill does

1. Resolves the package and locates the specification document.
2. Reads the document in full: frontmatter, every `REQ-N`, normative
   statements outside the Requirements section, glossary terms, and links to
   auxiliary files.
3. Checks GSSF conformance: package naming, section presence and order,
   frontmatter fields, requirement numbering, bold requirement references, and
   italicised glossary terms.
4. Reads every auxiliary file by type (OpenAPI, AsyncAPI, JSON Schema,
   Protobuf, GraphQL, diagrams, sample payloads), running a validator where
   one is installed.
5. Cross-checks the document against itself and against the auxiliary files,
   recording each disagreement with both locations.
6. Reports the consolidated model: summary, requirements, interfaces, data
   model, security considerations, glossary, and open questions.

## Behaviour worth knowing

- **Blocking violations stop the work.** These are the ones that leave the
  spec's meaning uncertain: no locatable specification document, a missing or
  invalid Specification Type, no requirements in a `FEAT` or `BUG` spec,
  duplicate requirement identifiers, a missing `BUG` section, or Affected
  Software with no version. Everything else is reported and work continues.
- **The spec is never edited during ingestion.** Fixes are offered, and made
  only if you ask.
- **Nothing inside the package is executed.** Files are read, parsed, and
  linted with tools from outside the package.
- **Implementation is traced to requirements.** Each `REQ-N` gets at least one
  test named or annotated with its identifier. For a `BUG` spec, the actual
  behaviour is reproduced with a failing test before anything is changed.

## Files

- [SKILL.md](SKILL.md): the skill's instructions, conformance checklist, and
  report format
- [gssf-gssf/gssf.md](gssf-gssf/gssf.md): the GSSF 0.1.0 specification
