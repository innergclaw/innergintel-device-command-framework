#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

print("InnerG Intel Device Command Map")
print("=" * 36)
print()
print("iPhone       -> Command Deck: approvals, Telegram, capture, mobile QA")
print("MacBook 1    -> Build Studio: code, demos, deploys, creative production")
print("MacBook 2    -> Ops/Review: testing, dashboards, research, second checks")
print("GitHub       -> Source of Truth: repos, deploys, history")
print("Telegram     -> Command Bus: reports, updates, action prompts")
print("Codex        -> Agent Layer: build, verify, summarize, automate")
print()
print(f"Docs: {ROOT / 'docs'}")

