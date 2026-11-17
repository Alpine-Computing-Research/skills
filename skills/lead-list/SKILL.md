---
name: lead-list
description: Build an email outreach list of real, researched business leads for a given offer, where every lead has a business name, website URL, email address and status, plus, where they can be found, a contact person's first and last name, a publicly listed business phone number, notes and a location. Use this whenever the user asks for a lead list, an email list, an outreach or prospecting list, a cold email or cold calling list, prospects or leads to email or phone, "who should I contact", "find me businesses in X", "find businesses to pitch X to", or wants to turn a business idea or an ideal customer description into named businesses with contact details, even if they don't say "lead list" explicitly.
argument-hint: <what is being sold, to whom, and where>
---

# Lead list

Produce a list of businesses someone can work through row by row, mainly by
email. The email address is the point of each row; a phone number is
recorded as well when the business publishes one, for whoever prefers to
call. The test for each lead is whether the user could write to it right
now: the business exists, it is the kind of business that buys the offer,
and the contact details are the ones it publishes for itself.

A lead list is only as good as its worst row. An address that bounces or a
business that plainly does not fit costs the user a few minutes and, more
importantly, their trust in the rest of the list. Bounces also damage the
sending domain's reputation, which hurts every later email. So a short list where every
row has been checked is the goal, not a long one.

## Before generating

Work out four things from `$ARGUMENTS` and the conversation:

- **The offer.** What is being sold, and at roughly what price. The price
  decides who is worth contacting: a AUD 300 job and a AUD 30,000 contract
  have different buyers.
- **The buyer.** The kind of business that pays for it. If the offer came
  out of the `business-ideas` skill, its "Who pays" fields are the buyer.
- **The territory.** Where the leads should be: a city, a region, a country,
  or anywhere.
- **Exclusions.** Existing customers, competitors, anyone already contacted.
  If the user has an earlier list or a CRM export, read it and exclude what
  is in it.

If the offer or the buyer is missing, ask one short question covering both
rather than guessing; a list built for the wrong buyer is wasted in full. If
only the territory is missing, infer it from context (the user's location,
the currency they use), say what you assumed, and proceed.

Default to 20 leads unless a number is given. That number is a ceiling, not a
quota: see the filter below.

## Sourcing

Every lead comes from research done in this session, never from memory. This
skill needs a web search or fetch tool. If none is available, say so and
stop after describing the buyer profile and where such buyers are listed; do
not produce a list of businesses and contact details from recall, because
remembered email addresses and phone numbers are often wrong and there is no
way to tell which.

Good places to find leads, roughly in order of usefulness:

- Industry association and chamber of commerce member directories.
- Government and regulator registers of licensed or accredited operators.
- Trade directories, marketplaces and "find a provider" pages for the
  buyer's own industry.
- Map and local business listings for the territory.
- Exhibitor and sponsor lists for the industry's conferences and trade shows.
- Recent news, job advertisements, tenders and funding announcements.

Then, for each candidate, open the business's own website and take the email
address, the contact person, the location and any phone number from there.
A directory tells you the business exists; its own site is the authority on
how to reach it. If the two disagree, use the business's site.

Use only contact details a business publishes for the public to reach it on.
For email, that is a general inbox (`info@`, `office@`) or a named person's
work address shown on a staff or contact page. Never construct an address
from a guessed pattern such as `first.last@domain`; a guess that bounces, or
lands with the wrong person, is worse than a general inbox. For phone, that
is a main line, a branch line, a department line, or a direct line shown on
the business's own pages.

Do not include personal email addresses, personal mobile or home numbers,
details from data-broker or people-search sites, or anything taken from a
leaked or scraped dataset. A sole trader whose published business number is
a mobile is fine; that is their business line.

### Obfuscated email addresses

Many small-business sites hide their email address from scrapers while still
showing it to visitors. A fetch tool that renders pages to text then reports
the address as `[email protected]`, as "not shown", or returns a page with
only a title. That is not the same as the business publishing no address,
and cutting those leads throws away a large share of a small-business list.

When a business's own page yields no readable email address, or shows a
placeholder, run the bundled script on the page before deciding. It reads the
raw HTML and prints every address and `tel:` link it finds:

```
python3 scripts/extract_contacts.py https://example.com/contact
```

The path is relative to this skill's directory. It takes several URLs at
once; try the contact page as well as the home page. It decodes:

- **Cloudflare email protection**, the commonest case: a `data-cfemail`
  attribute or an `/cdn-cgi/l/email-protection#` link holding a hex string.
  The first byte is a key and each following byte is XORed with it.
- **HTML entities and URL encoding** (`&#105;nfo&#64;...`, `info%40...`).
- **Spelled-out addresses** (`name [at] domain [dot] com`).

If the script cannot run, fetch the raw HTML another way and decode by hand
using the rule above.

Treat the output as candidates, not answers. Raw HTML also contains
addresses that are not the business's: font and library licence headers, the
web designer's address, a template's placeholder. Accept an address only
when it is on the business's own domain, or is visibly presented on the page
as how to contact the business (a sole trader's Gmail or Outlook address in
the contact section counts).

This is reading what the site shows any visitor, which is within the rule
above. It stops there: do not work around a contact form, a CAPTCHA, a login
or a "click to reveal" that asks the visitor to prove they are human, and do
not assemble an address the page never contains. If a page holds no address
after decoding, the lead has no published email and is cut.

## Columns

Each lead has exactly these nine columns and no others. Do not add columns
for job titles, sources, scores or scripts; if the user wants more, they
will ask.

| Column | Required | What goes in it |
|---|---|---|
| Business name | yes | Trading name, as the business styles itself |
| Website URL | yes | The business's own site, as a full `https://` URL |
| Email address | yes | An address the business publishes for itself |
| Status | yes | Where the lead stands; `new` on a fresh list |
| First name | no | The contact person's given name |
| Last name | no | The contact person's family name |
| Phone number | no | A published business number, in international format, e.g. `+61 7 3000 0000` |
| Notes | no | Anything the user should know before making contact |
| Location | no | Suburb or city, and state or country |

A lead with any required column missing is not on the list. An optional
column is filled in whenever research supports it and left empty otherwise;
never fill one with a guess.

**Website URL.** The business's own domain, not its page on a directory, a
map listing or a social network. A business with no site of its own is cut.

**Email address.** One address per lead. Prefer the address of whoever
handles the kind of purchase the offer is, when the business's site shows
it; otherwise the general inbox.

**Status.** The user's tracking column. Every lead on a newly generated
list starts as `new`; the user updates it as they work. Use only these
values, so the column can be filtered:

| Status | Meaning |
|---|---|
| `new` | Not yet contacted |
| `contacted` | Emailed or called; no reply yet |
| `follow_up` | Replied or was reached; asked to be contacted again later |
| `interested` | Wants a follow-up, a quote or a meeting |
| `not_interested` | Declined |
| `do_not_contact` | Asked not to be contacted again |
| `invalid` | Email bounced, or the details or business turned out to be wrong or defunct |

When the user supplies an earlier list, read its Status column: everything
on it is excluded from the new list whatever its status, and
`do_not_contact` rows must never reappear on any later list.

**First name and last name.** The contact person is whoever at the business
decides on the kind of purchase the offer is; in a small business that is
usually the owner. Name them only when the business's own site, or another
public professional source, shows them in that role, and the source is
recent enough to trust. A wrong name is worse than no name: an email
addressed to someone who left two years ago is deleted unread. Fill in both columns or
neither, unless the source itself gives only a first name. When the email
address belongs to a named person, the contact person should be that
person. If their role is not obvious, put it in Notes.

**Phone number.** A secondary channel. Fill it in whenever the business
publishes a number and leave it empty when it does not; do not spend extra
searches hunting for one, and never fill the gap with a number from
anywhere other than the business's own pages. Use international format,
except for numbers that have no international form (Australian 13, 1300
and 1800 numbers, for instance), which are written as published.

**Notes.** Short, factual, and useful to someone writing the first email:
the contact person's role, something found in research that makes this
business a good fit (they are hiring for the job the offer replaces, they
just opened a second site), what the business specialises in, "the inbox is
shared across three branches". Leave it empty when there is nothing worth
saying. The user will also write their own notes here as they work the
list.

Include the business's registration and licence numbers wherever they can
be found: in Australia the ABN and ACN, and elsewhere the local equivalent
(NZBN, UK company number, EIN, VAT number), plus any trade licence number
the business displays, such as a QBCC licence. They identify the legal
entity behind a trading name, which lets the user tell two similarly
named businesses apart and look the business up on the public register.
They are usually in the site footer, or on the contact, about or terms
pages; if the site does not show one, look the business up on the public
register (ABN Lookup in Australia) and use the result only when the name
and location match unambiguously. Write them at the start of Notes in a
fixed form, labelled and separated by semicolons, so they can be searched:
`ABN 12 345 678 901; QBCC 1234567; <other notes>`. Copy the digits exactly
as shown, and never infer or reconstruct a number. A lead with no number
found stays on the list.

**Location.** Where the business, or the branch being contacted, is based,
as its own site gives it. Enough to segment the list by area and to know
the time zone; not a street address.

## The filter

Find more candidates than requested, then cut any lead for which one of
these is true:

- **A required column is missing.** No business name, no website of its
  own, or no published email address.
- **The email, or the number if one is given, was not seen on a live page
  this session.**
- **It does not fit the buyer.** Wrong size, wrong sector, wrong territory,
  or obviously unable to afford the offer.
- **It appears to have closed, been acquired, or moved.** Check for signs of
  life: a recent site update, recent reviews, current listings.
- **It is a duplicate.** Branches of one business that share a decision
  maker count as one lead; list the head office or the branch where the
  buyer sits.
- **It is on the user's exclusion list,** or is a direct competitor of the
  user.
- **The only route in is a personal email address,** or a contact form with
  no email address at all. A missing phone number alone does not cut a
  lead.
- **It asks not to be solicited.** Some businesses state "no unsolicited
  email", "no marketing enquiries" or "no sales calls" on their contact
  page. Any of these cuts the lead, whichever channel it names.

Do not rescue a failing lead with a caveat in Notes. Either the user
should contact it or it is not on the list.

If fewer leads survive than were requested, deliver the ones that did and
say in one line how many were found and why the rest fell out, rather than
padding. If the shortfall is large, say which part of the brief is the
constraint (the territory is too small, the buyer too narrow) so the user can
loosen it.

## Output

Do not rank or grade the leads. Sort them by business name.

Write the list to a CSV file, since that is what a mail-merge tool, a CRM
or a spreadsheet will take. Name it `lead-list-<short-slug>-<YYYY-MM-DD>.csv`
in the current working directory unless the user names another place. The
header row is exactly:

```
business_name,website_url,email_address,status,first_name,last_name,phone_number,notes,location
```

Quote every field that contains a comma or a quotation mark, and write the
file as UTF-8. If a file with that name exists, do not overwrite it; add a
numeric suffix.

Then reply in the conversation with:

1. The path to the file, the number of leads, how many have a named
   contact and how many have a phone number.
2. One or two sentences on what the research showed about the market that the
   user should know: where the leads cluster, a segment that turned out to
   publish no contact details.

If the user asks for the list in the conversation rather than as a file, give
it as a Markdown table with the same nine columns.

## Outreach rules

Unsolicited commercial email and telemarketing are regulated nearly
everywhere, and the rules differ by country and by whether the recipient is
a business or a consumer: consent requirements, sender identification, a
working unsubscribe, do-not-call registers and permitted calling hours.
This skill limits the list to contact details a business publishes for
itself and drops businesses that ask not to be solicited, which is the
low-risk end, but that is not consent, nothing is checked against a
do-not-call register, and the list is not legal clearance. Say so in one
line when delivering the list, naming the law or register that applies in
the territory if you know it (in Australia, the Spam Act 2003 and the Do
Not Call Register), and leave it at that; do not lecture.

If the buyer is a consumer rather than a business, do not build the list.
Contacting private individuals using details gathered from the web is the
case those rules exist to stop. Say why, and offer what does work for
consumer offers: the businesses or intermediaries that already reach those
consumers.

## Example

The businesses below are invented to illustrate the format; real rows never
are.

```
business_name,website_url,email_address,status,first_name,last_name,phone_number,notes,location
Harbourline Strata Management,https://harbourline.example,priya.raman@harbourline.example,new,Priya,Raman,+61 2 5550 0142,"ABN 12 345 678 901; senior portfolio manager; advertising for a defects coordinator","Parramatta NSW, Australia"
"Kessler, Wade & Partners Strata",https://kesslerwade.example,enquiries@kesslerwade.example,new,,,,,"Geelong VIC, Australia"
```
