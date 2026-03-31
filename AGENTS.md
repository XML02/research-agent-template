# AGENTS.md — Agent Collaboration Guide

## When to use an AI agent
Use an AI agent for:
- Writing Python scripts from specification
- Extracting data from text or tables
- Running repetitive data transformations
- Drafting documentation from code

Do NOT use an agent for:
- Making subjective research decisions
- Interpreting ambiguous results
- Ethical or citation judgments

## Before starting
1. Create a GitHub issue with acceptance criteria
2. Copy issue to `agents/handoff_prompt_template.md`
3. Verify the agent has access to necessary files

## Agent instructions
Always include:
- What to do (specific task)
- What constraints to follow
- How to verify success
- Source citation requirements

## After agent completes
1. Review PR against checklist in `agents/pr_review_checklist.md`
2. Run tests: `pytest -v`
3. Check output format
4. Verify AI disclosure is present
5. Merge or request changes

## AI disclosure requirement
Every file that uses AI-assisted code generation must include:

```python
"""
[Description of what the code does]

AI assistance: [tool name, e.g., Claude, GPT-4]
Human-reviewed by: [your name]
Date: [YYYY-MM-DD]
Source: [paper or method citation]
"""
```

## Commit message convention
For AI-assisted work:
```
[type] [brief description] [AI: tool used]

- What was done
- What was verified
```
Example:
```
analysis: add ESG summary script [AI: Claude 3.5]

- Implements mean ESG calculation per endowment
- 2 pytest tests pass
- Cites Aragon et al. (JFE 2025)
```
