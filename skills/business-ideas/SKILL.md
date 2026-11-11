---
name: business-ideas
description: Generate potential business ideas in a fixed semi-structured format, where every idea states whether it is a product or a service, who pays (in general and with concrete examples), why they pay, how much they pay, and what the edge is. Use this whenever the user asks for business ideas, startup ideas, side-project or side-hustle ideas, ways to make money from a skill, asset, dataset, tool or codebase, "what could I sell", "how could this be monetised", or wants to brainstorm commercial opportunities in some domain, even if they don't say "business idea" explicitly.
---

# Business ideas

Produce business ideas that someone could actually evaluate, not a list of
themes. The test for each idea is whether a reader could pick up the phone
tomorrow and try to sell it: they know who to call, what to say the price is,
and why the person on the other end would say yes to them rather than to
someone else.

## Before generating

Work out the seed from the conversation: the domain, anything the user owns or
is good at (skills, code, data, access, relationships, location), and any
constraints (capital, time, solo vs team, geography).

The edge field depends on who is running the business, so the user's
background matters. If the conversation or project already tells you enough,
proceed. If you know nothing about the user and they gave no domain, ask one
short question covering both ("what area, and what do you bring to it?")
rather than generating generic ideas. If they want ideas regardless, generate
them and write each edge as "this needs someone who has X".

Default to 5 ideas unless a number is given. That number is a ceiling, not a
quota: see the filter below.

## Format

Use exactly this structure for each idea. The six fields are fixed and always
appear in this order; the prose inside them is free-form but short (one to
three sentences each).

```markdown
## N. <Name>

<One sentence: what it is.>

- **Type:** Product | Service — <what is actually delivered>
- **Who pays (general):** <the category of buyer>
- **Who pays (examples):** <2–4 concrete buyers>
- **Why they pay:** <the cost or pain today, and what they do about it now>
- **How much they pay:** <amount, unit, and the basis for the number>
- **Edge:** <why this business wins and others don't>
```

Nothing else goes in an idea block: no risks section, no next steps, no
scores. If the user wants more, they will ask, and extra fields make the list
harder to scan and compare.

## What each field needs

**Type.** Commit to one of product or service. A product is the same thing
sold to every buyer (software, a dataset, a physical good, a course); a
service is work done per customer. If the idea is genuinely a hybrid, name the
part the customer is charged for and say so in the description after the
dash, for example "Service — monthly audit, delivered through an in-house
tool".

**Who pays (general).** The buyer, which is not always the user. Name the role
that holds the budget ("heads of compliance at mid-sized lenders", not
"lenders"; "parents of year 11–12 students", not "students"). When payer and
user differ, say who the user is.

**Who pays (examples).** Concrete enough that the reader could find them.
Prefer real, named organisations or a tightly specified kind of person ("a
six-vet practice in a regional town with no in-house IT"). Only name real
organisations you are confident exist and fit; an invented company name
presented as real is worse than a precise description. Pick examples that
differ from one another so they show the range of the market.

**Why they pay.** State what the problem costs them now, in money, time, risk
or lost revenue, and what they currently do instead (a spreadsheet, an
overpriced incumbent, a junior employee, nothing). "It saves time" is not an
answer; "their two paralegals spend roughly a day a week on it" is.

**How much they pay.** A number or a range, with a unit (per month, per seat,
per job, per unit, one-off) and a currency. Then say where the number comes
from: a comparable product's price, a fraction of the cost being removed, or
the going rate for the labour replaced. These are estimates and should read
as estimates, but a reasoned figure is far more useful than "pricing varies".
If a web search tool is available and a comparable's price is checkable in a
query or two, check it rather than relying on memory.

**Edge.** Why this business, run by this person, wins against both incumbents
and the next person with the same idea. Real edges are things like
proprietary data, a distribution channel, domain expertise that is slow to
acquire, a cost structure competitors cannot match, regulatory standing, or
an existing relationship with the buyers. "Better UX", "uses AI" and "first
mover" are not edges on their own. Tie the edge to what the user actually
has where possible. If an idea has no edge you can state honestly, drop the
idea rather than inventing one.

## Getting a good set

Generate at least twice as many candidates as requested, then run every one
through the filter below and only output the survivors. The user wants a list
with no nonsense in it: every idea shown should be one a sober, experienced
operator would consider plausible on first read. One silly idea makes the
reader distrust the rest of the list, so the filter matters more than the
count.

### The filter

Cut an idea if any of these is true:

- **Nobody is already spending on the problem.** The buyer should be paying
  today, in money or in staff time, for a worse way of handling it. An idea
  that needs buyers to first discover they have a problem is out.
- **You cannot say who writes the cheque.** If the payer is "users",
  "businesses" or "advertisers, eventually", it is not a business yet.
- **The first dollar needs scale.** Two-sided marketplaces, social networks,
  ad-funded consumer apps and anything else that is worthless until thousands
  of people use it. The idea should be sellable to customer number one.
- **It depends on something that does not exist or is not the user's to
  use.** Technology that does not work reliably yet, a licence or
  accreditation the user lacks, data they have no right to, capital beyond
  their stated means, or a partnership with a large company that has no
  reason to agree.
- **The price does not survive arithmetic.** Multiply the price by a
  realistic number of customers the user could win and serve in a year. If
  that is not worth their time, or the price exceeds what the problem costs
  the buyer, cut it.
- **The edge is generic or missing.** See the edge field above.
- **It is a template, not an idea.** "Uber for X", "AI-powered X", "a
  platform that connects X and Y", a subscription box, a generic agency, a
  course on the thing the user just learned. These are allowed only when the
  specifics make it stand without the label.
- **You would be embarrassed to pitch it to someone in that industry.**
  Imagine saying it to a person who has worked in the buyer's role for ten
  years. If they would laugh or say "we tried that", cut it, unless you can
  say what has changed.

Do not rescue a failing idea by softening its wording or by adding hedges to
the fields; either it passes as stated or it goes.

If fewer ideas survive than were requested, output the ones that did and say
in one line that the rest did not pass, rather than padding the list. Three
solid ideas beat five with two fillers.

### Variety

Among the survivors, prefer a set that varies: mix products and services,
different buyers, different price points and pricing models. Five variants of
the same SaaS for the same buyer is one idea.

Order the ideas by how strong you think they are, strongest first, and after
the list add at most two sentences saying which you would pursue and why.

## Example

```markdown
## 1. Strata defect report triage

Turns the building-inspection PDFs that strata managers receive into a
prioritised, costed defect register.

- **Type:** Service — a register delivered per report within 48 hours, produced with in-house tooling
- **Who pays (general):** Strata management firms, on behalf of owners corporations (the committee members are the readers)
- **Who pays (examples):** A firm managing 80–300 apartment schemes in Sydney or Melbourne; a boutique manager specialising in post-2000 high-rises with active defect claims
- **Why they pay:** Reports run to hundreds of pages and a portfolio manager handling 40+ buildings cannot read them; defects get missed until the statutory warranty window has closed, which shifts the repair cost onto owners
- **How much they pay:** AUD 400–900 per report, passed through to the scheme as a disbursement; anchored against the few hours of a building consultant's time (around AUD 200/h) it replaces
- **Edge:** Needs someone who has both read these reports professionally and can build the extraction pipeline; the buyers are reachable through a handful of state industry associations, so an insider gets distribution cheaply
```
