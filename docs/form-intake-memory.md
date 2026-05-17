# Form Intake Memory

OWNYOURWEB and SHOPNASGFX intake should originate from their live site forms, not from manual dashboard entry.

The dashboard is the command view and memory router. The public sites are the capture points.

## Source Rules

| Lane | Primary Source | Memory Route | Dashboard Role |
| --- | --- | --- | --- |
| OWNYOURWEB | `https://ownyourweb.xyz/` Project Request form | website intake memory, build queue, Telegram command center | review, project card, launch tracking |
| SHOPNASGFX | `https://shopnasgfx.com/` Book Now / Contact flow | design intake memory, asset queue, approval trail | review, draft board, delivery tracking |
| INNERGINTEL | dashboard intake, GitHub, Telegram, classes, docs | system memory, dates, project notes, ops updates | source of truth and system routing |
| PERSONAL | dashboard intake, iPhone capture, human-entered private notes | private memory, reminders, investments watchlist | private review and human approval |

## Required Memory Fields

Every imported form submission should be normalized into:

- source site
- lane
- request type
- name
- contact method
- title
- notes
- links
- files or asset references
- priority
- due date or timeline
- consent or approval requirement
- current status
- next action

## OWNYOURWEB Form Memory

Expected fields from the site form:

- first name
- last name
- email
- timeline
- business name
- current website
- project notes

Normalize into:

- lane: OWNYOURWEB
- source: ownyourweb.xyz project request
- object type: website intake
- first status: Capture
- next status: Review

## SHOPNASGFX Form Memory

Expected sources from the site:

- Book Now request
- Contact request
- service/product order details
- asset links or follow-up asset request

Normalize into:

- lane: SHOPNASGFX
- source: shopnasgfx.com book/contact flow
- object type: design intake
- first status: Capture
- next status: Assets Needed or Draft

## Manual Entry Rule

Manual dashboard intake is only for:

- internal INNERGINTEL tasks
- PERSONAL items
- Telegram captures
- correcting or re-entering a form submission
- emergency fallback when the live form is unavailable

Manual entry should not replace the OWNYOURWEB or SHOPNASGFX site forms as the normal source of client intake.

## Paid Client Form

Confirmed paid clients should use `paid-client-form.html`.

That form captures:

- business lane
- payment status
- client name
- email
- phone or contact handle
- service
- project title
- due date
- priority
- paid amount or package
- links and assets
- project notes

On a static GitHub Pages deployment, the form can show a thank-you screen after submission. When a backend is added, this page should post to the production intake database and update the internal dashboard from that source of truth.
