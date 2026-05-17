# Ecosystem Command Map

This map defines the four main lanes for the InnerG Intel command dashboard.

## Lanes

| Lane | Purpose | Core Objects | Primary Workflows |
| --- | --- | --- | --- |
| OWNYOURWEB | Website business operations | orders, forms, projects, domains, launches, client updates | live site form, proposal, build, QA, deploy, handoff |
| SHOPNASGFX | Creative design operations | orders, design briefs, assets, drafts, approvals, deliveries | live site booking/contact, asset collection, draft, revision, approval, delivery |
| INNERGINTEL | System and project operations | projects, important details, dates, classes, skills, updates | project planning, class tracking, ops updates, repo logging, automation notes |
| PERSONAL | Non-work life operations | family notes, appointments, investments, bills, private reminders | private intake, human review, reminder, investment watch, follow-up |

## Intake Source Rule

OWNYOURWEB and SHOPNASGFX client memory starts from the live website forms:

- OWNYOURWEB: `https://ownyourweb.xyz/` Project Request form
- SHOPNASGFX: `https://shopnasgfx.com/` Book Now / Contact flow

The dashboard is the command layer after capture. It reviews, organizes, remembers, and turns valid submissions into project cards.

Manual dashboard intake is a fallback for those two lanes. It is normal intake for INNERGINTEL and PERSONAL.

## Shared Object Model

Every lane should eventually support these records:

| Object | Use |
| --- | --- |
| Contact | client, family member, class contact, vendor, or important person |
| Intake | raw request captured from a form, phone, Telegram, email, or conversation |
| Order | paid or requested work that needs fulfillment |
| Project | multi-step work with tasks, due dates, files, and updates |
| Task | one concrete action with owner, status, and priority |
| Date | deadline, appointment, class, review, launch, payment, or reminder |
| File | logo, screenshot, brief, contract, class resource, or private document reference |
| Update | short status note sent to Telegram, a client, or the internal log |
| Approval | human confirmation for sensitive actions |

## Status Flow

Use the same status language across the ecosystem:

1. Capture
2. Review
3. Quote
4. Build
5. Waiting
6. Verify
7. Deliver
8. Closed

Personal items can use a shorter version:

1. Capture
2. Review
3. Do
4. Waiting
5. Done

## Form Requirements

### OWNYOURWEB

Primary source: `https://ownyourweb.xyz/` Project Request form.

- name
- email
- business name
- current website
- website goal
- needed pages
- budget range
- launch target
- notes and links

### SHOPNASGFX

Primary source: `https://shopnasgfx.com/` Book Now / Contact flow.

- name
- email
- design type
- business or brand name
- size/platform
- color/style direction
- text to include
- asset upload link
- deadline

### INNERGINTEL

- project name
- system area
- repo or document link
- due date
- class or update type
- important details
- next action
- approval needed

### PERSONAL

- category
- private note
- important date
- related person
- amount or investment ticker when relevant
- reminder time
- risk level
- approval needed

## Security Rule

Keep personal and sensitive data separate from public dashboards. The dashboard can show categories, statuses, and references, but private notes, credentials, payment data, and investment details need restricted storage and human approval before action.
