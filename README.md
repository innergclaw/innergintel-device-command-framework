# InnerG Intel Device Command Framework

A practical operating framework for running the InnerG Intel ecosystem across two MacBooks and an iPhone.

The goal is simple: know where to go for what, which device should own which kind of work, and how Codex, Telegram, GitHub, and local workspaces connect without everything becoming scattered.

## Command OS Lanes

The ecosystem now runs through four dashboard lanes:

| Lane | Owns | Core Need |
| --- | --- | --- |
| **OWNYOURWEB** | website orders, forms, project boards, launches | turn client website requests into delivered web systems |
| **SHOPNASGFX** | design orders, briefs, assets, approvals, deliveries | move creative jobs from request to final files |
| **INNERGINTEL** | projects, important details, dates, classes, ecosystem updates | keep the operating system organized and current |
| **PERSONAL** | life admin, family, reminders, investments, private notes | keep non-work priorities separate but visible |

See [docs/ecosystem-map.md](docs/ecosystem-map.md).

Client intake for OWNYOURWEB and SHOPNASGFX starts on the live sites, then routes into dashboard memory and project management. See [docs/form-intake-memory.md](docs/form-intake-memory.md).

Paid clients use the dedicated [paid client form](docs/paid-client-form.html) for project details, links, assets, deadlines, and notes.

## Core Idea

InnerG Intel runs like a small command network:

- **iPhone** is the command deck.
- **MacBook 1** is the primary build studio.
- **MacBook 2** is the secondary operator and review machine.
- **GitHub** is the source of truth.
- **Telegram** is the mobile command bus.
- **Telegram Ops Update Channel** is `-1003997964845`.
- **Codex** is the agent layer that can move between planning, building, checking, and reporting.

## Device Roles

| Device | Role | Use It For |
| --- | --- | --- |
| iPhone | Command Deck | Telegram approvals, quick prompts, checking updates, client messages, mobile screenshots |
| MacBook 1 | Build Studio | Main coding, websites, client demos, GitHub pushes, creative production |
| MacBook 2 | Ops / Review Node | Testing, second-screen research, admin dashboards, finance checks, remote control |
| GitHub | Source of Truth | Repos, demos, skills, docs, issue history, deploys |
| Telegram | Command Bus | Business updates, finance reports, reminders, quick execution requests |
| Codex | Agent Layer | Build, edit, research, summarize, automate, deploy, report |

## Where To Go For What

| Need | Start Here | Why |
| --- | --- | --- |
| Build a website/demo | MacBook 1 + Codex | Best for file editing, browser checks, GitHub deploys |
| Review a site on mobile | iPhone | Real mobile view, screenshots, client-like experience |
| Send business/finance updates | Telegram | Fastest command and notification layer |
| Send ops updates | Telegram channel `-1003997964845` | Official InnerG Intel ops update lane |
| Manage repos and skills | GitHub | Permanent source of truth |
| Run second checks | MacBook 2 | Keeps primary build flow clean |
| Approve sensitive actions | iPhone or active Mac | Best place for human confirmation |
| Store operating rules | This framework | Prevents confusion across devices |

## Operating Principle

No device should do everything.

Each device gets a lane:

1. **Capture**: iPhone
2. **Build**: MacBook 1
3. **Verify**: MacBook 2 or iPhone
4. **Deploy**: GitHub
5. **Notify**: Telegram
6. **Document**: InnerG Intel framework

## Production Coverage

InnerG Intel should cover the full production stack, not just frontend and backend.

| Area | Coverage Goal |
| --- | --- |
| Frontend | Build and visually verify the user experience |
| APIs & Backend Logic | Handle product behavior, integrations, and validation |
| Database & Storage | Store data safely with documented schemas and backups |
| Auth & Permissions | Control who can access what |
| Hosting & Deployment | Ship live apps with repeatable deploy steps |
| Cloud & Compute | Choose the right runtime for each product |
| CI/CD & Version Control | Keep releases traceable and reversible |
| Security & RLS | Protect data, secrets, and privileged actions |
| Rate Limiting | Prevent abuse and runaway usage |
| Caching & CDN | Keep apps fast and resilient |
| Load Balancing & Scaling | Prepare high-traffic systems when needed |
| Error Tracking & Logs | See failures quickly and debug them |
| Availability & Recovery | Restore service after incidents |

See [docs/production-stack.md](docs/production-stack.md).

## Folder Map

```text
innergintel-device-command-framework/
├── README.md
├── config/
│   ├── devices.yml
│   └── ecosystem.yml
├── docs/
│   ├── command-map.md
│   ├── ecosystem-map.md
│   ├── form-intake-memory.md
│   ├── operating-rules.md
│   ├── production-stack.md
│   └── workflows.md
├── dashboard/
│   ├── index.html
│   └── paid-client-form.html
└── scripts/
    └── print-command-map.py
```

## First Workflows

1. Client website build
2. Telegram finance report
3. Codex skill product build
4. Domain + GitHub Pages deploy
5. Mobile review loop
6. Sensitive action approval loop
7. Ecosystem intake and project routing

See [docs/workflows.md](docs/workflows.md).
