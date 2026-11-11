# Good Software Specification Format (GSSF) #

## Frontmatter ##

| Name | Version | Publication Date | Author(s)                 | Specification Type |
|------|---------|------------------|---------------------------|--------------------|
| GSSF | 0.1.0   | 2026-11-06       | Jack McPherson [jack@jmcph4.dev](mailto:jack@jmcph4.dev)  | `META`             |

## Conformance ##

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 ([RFC 2119](https://www.rfc-editor.org/rfc/rfc2119), [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174)) when, and only when, they appear in all capitals, as shown here.

## Overview ##

This document specifies the Good Software Specification Format (GSSF). GSSF is a format for writing and organising *specification documents* for software.

## Rationale ##

The proliferation of LLM-based agents for software development (so-called agentic programming) has moved the bottleneck for software development upwards in the abstraction stack towards the human operator. Despite the broad and sometimes surprising capabilities of such agents, difficulties in constraining their output still persist. GSSF aims to remedy this by being amenable to ingestion by LLMs and also comfortable for human authors and readers.

## Format ##

### Specification Document ###

A GSSF *specification document* MUST be written in GitHub Flavored Markdown (GFM) [1].

A GSSF *specification document* MUST use the language conventions specified in both RFC 2119 [2] and RFC 8174 [3]. A GSSF *specification document* MUST include all of the following sections:

 1. Frontmatter
 2. Conformance
 3. Rationale
 4. Requirements
 5. Security Considerations
 6. Glossary

These sections MUST appear in the order listed above.

The contents of the "Security Considerations" and "Glossary" sections MAY be empty.

The "Frontmatter" section MUST include a table with the following column names:

 - Name
 - Version
 - Publication Date
 - Author(s)
 - Specification Type

It is RECOMMENDED that each author includes an email address.

GSSF *specification document* versions MUST conform to Semantic Versioning 2.0.0 [4].

The "Conformance" section MUST be the standard conformance boilerplate from RFC 2119 [2] and RFC 8174 [3].

If the "Glossary" section of a GSSF *specification document* is not empty then it MUST contain one or more definitions. Each definition MUST be a subsection of the "Glossary" section. Wherever a term defined in the glossary appears in the *specification document*, it MUST be italicised.

A GSSF *specification document* MAY contain a "Bibliography" section. If the "Bibliography" section is present, it MUST conform to IEEE citation standards [5].

The "Requirements" section MUST specify one or more requirements for the software system being specified, unless the *specification document* is of *specification type* `META`, in which case the "Requirements" section MAY be empty. Each requirement MUST be numbered in the format `REQ-N` where `N` is a natural number. The first requirement MUST be numbered `REQ-1`. Requirements MUST be numbered in an increasing sequence. Requirement numbers MUST be contiguous. These requirements SHOULD represent invariants that the software system being specified can be effectively tested against. Wherever requirements are referenced in the *specification document*, they MUST appear emboldened.

#### Types ####

A GSSF *specification document* MUST have a *specification type*. There are three *specification types*:

 - Bugfix (`BUG`)
 - Feature (`FEAT`)
 - Meta (`META`)

A *specification document* of *specification type* `BUG` MUST include the following sections:

 1. Affected Software
 2. Expected Behaviour
 3. Actual Behaviour
 4. Mitigation

These sections MUST appear in the order listed above. They MUST be placed together, immediately after the "Rationale" section and immediately before the "Requirements" section.

The "Affected Software" section MUST contain the name of the affected software system and MUST contain the affected version(s) of the affected software system.

### Specification Package ###

A GSSF *specification package* is a directory structure that allows for distribution of GSSF specifications and allows for providing any auxiliary files alongside them. A GSSF *specification package* MUST be a directory and MUST be named `[NAME]-gssf`, where `NAME` is the name of the GSSF specification. The directory MUST contain a single *specification document* called `[NAME].md`. This file MUST be in the top level of the directory. A GSSF *specification package* MAY contain one or more auxiliary files next to the *specification document*.

It is implementation-defined how to distribute the *specification package* (for example, as a Tar archive, etc.).

## Requirements ##

N/A

## Security Considerations ##

N/A

## Glossary ##

### Specification document ###

The document, written in GitHub Flavored Markdown, that describes the software system being specified.

### Specification package ###

The directory structure containing the *specification document* and optional auxiliary files.

### Specification type ###

The classification of a *specification document*, which determines the rules that apply to its sections. One of Bugfix (`BUG`), Feature (`FEAT`), or Meta (`META`).

## Bibliography ##

[1] GitHub, San Francisco, CA, USA. *GitHub Flavored Markdown Spec*, Version 0.29-gfm. (2019). Accessed: Nov. 6, 2026. [Online]. Available: https://github.github.com/gfm/

[2] S. Bradner, "Key words for use in RFCs to indicate requirement levels," Internet Engineering Task Force, BCP 14, RFC 2119, Mar. 1997. [Online]. Available: https://www.rfc-editor.org/rfc/rfc2119

[3] B. Leiba, "Ambiguity of uppercase vs lowercase in RFC 2119 key words," Internet Engineering Task Force, BCP 14, RFC 8174, May 2017. [Online]. Available: https://www.rfc-editor.org/rfc/rfc8174

[4] T. Preston-Werner. "Semantic Versioning 2.0.0." Semantic Versioning. Accessed: Nov. 6, 2026. [Online]. Available: https://semver.org/spec/v2.0.0.html

[5] IEEE Publication Operations, Piscataway, NJ, USA. *IEEE Reference Guide*, V 3.28.2025. (2025). Accessed: Nov. 6, 2026. [Online]. Available: https://ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf

