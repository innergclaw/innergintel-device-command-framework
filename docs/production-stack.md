# Full-Stack Production Coverage

Use this map to check whether InnerG Intel is covered from idea capture through secure production execution.

## Coverage Layers

| Layer | Owner Lane | Current Coverage | Next Coverage To Add |
| --- | --- | --- | --- |
| Frontend | MacBook 1 + Codex | Static dashboards, client demos, visual QA | Standard UI checklist, mobile screenshot review, accessibility checks |
| APIs & Backend Logic | MacBook 1 + Codex | Planned per product | API route template, input validation, background job pattern |
| Database & Storage | GitHub + project backend | Planned per product | Schema docs, backups, storage rules, migration history |
| Auth & Permissions | Project backend + human approval | Planned per product | Role matrix, session rules, admin-only workflows |
| Hosting & Deployment | GitHub | GitHub Pages lane exists | Deployment checklist per app, domain records, rollback notes |
| Cloud & Compute | GitHub + selected host | Planned per product | Hosting provider decision log, environment variables, secrets map |
| CI/CD & Version Control | GitHub + MacBook 1 | GitHub is source of truth | Branch rules, automated checks, release tags |
| Security & RLS | Codex prepares, Nasir approves sensitive changes | Human approval rules exist | RLS policy checklist, secret scanning, least-privilege review |
| Rate Limiting | Backend/API layer | Planned per product | Per-route limits, abuse rules, webhook protection |
| Caching & CDN | Hosting layer | Planned per product | CDN cache rules, asset versioning, purge process |
| Load Balancing & Scaling | Cloud/compute layer | Future for larger apps | Scale thresholds, queue strategy, provider autoscaling rules |
| Error Tracking & Logs | MacBook 2 + hosting tools | Review lane exists | Error tracker, structured logs, alert routing |
| Availability & Recovery | GitHub + hosting + MacBook 2 | Manual verification lane exists | Uptime checks, backup restore test, incident notes |

## Operating Rule

Do not call a build production-ready until every layer has either:

1. a working implementation,
2. a documented decision that it is not needed yet, or
3. a next action with an owner and approval requirement.

## Codex Role

Codex is responsible for turning each layer into practical work:

- inspect the repo and identify missing layers
- write checklists, config, docs, code, and tests
- prepare secure commands and deployment steps
- summarize risks before sensitive actions
- log what changed after execution

Codex does not provide final human approval for trades, payments, DNS changes, repo deletion, or client-facing commitments.

## Production Readiness Checklist

For each app, create or update a production checklist with:

- repo URL
- live URL
- owner device
- deployment path
- environment variables and secrets location
- auth roles
- database and storage plan
- security/RLS rules
- rate limits
- cache/CDN rules
- logging/error tracker
- backup and recovery process
- current gaps

