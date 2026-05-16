# Command Map

Use this when deciding where a task belongs.

## Quick Routing

| Task | Device / Service |
| --- | --- |
| New website build | MacBook 1 |
| Update existing website | MacBook 1 |
| Mobile QA | iPhone |
| Desktop QA | MacBook 2 |
| GitHub repo management | MacBook 1 + GitHub |
| Client text/DM | iPhone |
| Long client proposal | MacBook 1 |
| Finance holdings check | MacBook 2 or Codex |
| Telegram report | Telegram |
| Ops update channel | Telegram `-1003997964845` |
| Nightly insight | Codex + Telegram |
| Sensitive approvals | Human on iPhone or active Mac |
| Codex skill development | MacBook 1 |
| Codex skill testing | MacBook 2 |
| Production stack review | Codex + MacBook 2 |
| Security/RLS review | Codex prepares, Nasir approves |
| Error/log review | MacBook 2 + Codex |
| Availability/recovery check | MacBook 2 + GitHub |

## Human Approval Required

These actions require Nasir to approve directly:

- crypto trades
- bank transfers
- sending payment links to clients
- deleting repos
- changing DNS for live domains
- sending client-facing messages that commit price, deadline, or legal terms

Codex can prepare the action, write the command, summarize the risk, and log the result.

## Production Stack Routing

| Layer | Start Here |
| --- | --- |
| Frontend | MacBook 1 + Codex |
| APIs & Backend Logic | MacBook 1 + Codex |
| Database & Storage | GitHub docs + selected backend |
| Auth & Permissions | Codex prepares, human confirms sensitive roles |
| Hosting & Deployment | GitHub + MacBook 1 |
| Cloud & Compute | GitHub decision log + selected provider |
| CI/CD & Version Control | GitHub |
| Security & RLS | Codex review + Nasir approval |
| Rate Limiting | Backend/API layer |
| Caching & CDN | Hosting/CDN layer |
| Load Balancing & Scaling | Cloud/compute layer |
| Error Tracking & Logs | MacBook 2 + hosting tools |
| Availability & Recovery | MacBook 2 + GitHub |
