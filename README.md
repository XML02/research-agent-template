# Research Agent Template

A reusable template for AI-assisted research workflows with structured issue-to-PR collaboration.

## Purpose
This repository serves as a template for running structured research projects with AI agents, following a systematic issue → agent → PR workflow. Inspired by the Genskow and Shapiro style guide for reproducible research.

## Quick Start

1. **Use this as a template**: Click "Use this template" on GitHub to create a new project
2. **Clone locally**: `git clone https://github.com/YOUR_USERNAME/your-repo.git`
3. **Create an issue**: Use the issue templates in `.github/ISSUE_TEMPLATE/`
4. **Solve with agent**: Copy issue to agent handoff prompt
5. **Submit PR**: Agent opens PR, human reviews with checklist

## Repository Structure

```
├── .github/
│   └── ISSUE_TEMPLATE/   # Structured issue templates
├── agents/
│   ├── handoff_prompt_template.md  # Agent instructions
│   └── pr_review_checklist.md      # Human review checklist
├── checks/               # Verification scripts
├── data/
│   ├── raw/             # Source data
│   └── output/          # Generated outputs
├── docs/                # Documentation
└── README.md
```

## Issue Workflow

1. Create issue from template
2. Copy issue to `agents/handoff_prompt_template.md`
3. Run agent to solve
4. Agent opens PR
5. Human reviews with `agents/pr_review_checklist.md`
6. Merge or request changes

## Key Principles

- **Reproducibility**: All code includes docstrings and source citations
- **Human oversight**: Every PR is reviewed by a human before merge
- **Transparency**: AI use is disclosed in docstrings and commit messages
- **Structured handoffs**: Every task starts with a written prompt

## Citation

If this template was useful, cite:
> Lei, E. (2026). Research Agent Template. https://github.com/XML02/research-agent-template
