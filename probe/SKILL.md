---
name: probe
description: Check whether Codex correctly understands the user's request before acting, surface ambiguities that could change the outcome, and ask concise clarifying or follow-up questions. Use when the user explicitly invokes probe, asks to clarify intent, wants the agent to verify its interpretation, or gives a broad, underspecified, high-impact, multi-option, or preference-sensitive request across coding, writing, planning, research, decision-making, or everyday tasks.
---

# Probe

## Overview

Probe the user's request before executing when misunderstanding would waste effort or produce the wrong result. Keep the interaction lightweight: clarify only the details that affect the outcome, then proceed once the intent is sufficiently aligned.

## Core Workflow

1. Restate the understood request.
   - Summarize the user's intent in one or two concise sentences.
   - Name the expected output or action.
   - Include the assumed audience, context, constraints, and success criteria only when they matter.

2. Identify ambiguity.
   Look for missing or conflicting information in:
   - desired outcome or deliverable
   - scope and exclusions
   - audience, tone, format, language, or style
   - inputs, sources, tools, environment, or files
   - constraints such as deadline, budget, length, privacy, risk tolerance, or approval needs
   - success criteria or verification method
   - hidden preferences among several plausible interpretations

3. Decide whether to ask or assume.
   - Ask when the missing detail could change the result, cost, risk, or user satisfaction.
   - Assume when the ambiguity is low-impact, conventional defaults are obvious, or the user asked for speed.
   - State important assumptions briefly before proceeding.
   - Do not ask questions just to be complete.

4. Ask focused questions.
   - Ask at most 1-3 questions at a time.
   - Prefer questions that unblock execution.
   - Use follow-up questions when the user's answer reveals a deeper ambiguity.
   - Provide options only when options reduce effort for the user.
   - Avoid broad "What do you mean?" questions; name the exact uncertainty.

5. Proceed with an aligned interpretation.
   - After the user answers, restate the final interpretation only if it prevents confusion.
   - Then do the requested work using the clarified requirements.

## Question Quality Bar

A useful probing question should satisfy at least one of these:

- It distinguishes between two or more plausible outcomes.
- It determines the shape of the deliverable.
- It sets a boundary that prevents overwork or underwork.
- It reveals a preference the agent cannot infer safely.
- It defines success or verification.
- It reduces risk in a sensitive domain.

Weak questions:

- "Can you provide more details?"
- "What exactly do you want?"
- "Any preferences?"

Better questions:

- "Should the result be a ready-to-send message, a rough outline, or a list of talking points?"
- "Is your priority speed, polish, or maximum accuracy?"
- "Who is the audience: a close friend, a customer, or an internal team?"
- "Should I make the smallest safe change, or is a broader redesign acceptable?"

## Response Patterns

For simple requests with minor ambiguity:

```text
I understand this as: <brief interpretation>. I will assume <assumption> and proceed.
```

For requests where one missing detail matters:

```text
I understand this as: <brief interpretation>.

One detail changes the output: <specific uncertainty>?
```

For broad or high-impact requests:

```text
I understand this as: <brief interpretation>.

Before I proceed, I need to pin down:
1. <question>
2. <question>
3. <question>
```

## Interaction Rules

- Respect explicit urgency. If the user says "just do it," "make a reasonable assumption," or "draft something quickly," ask only about blockers.
- Do not turn every request into a planning session.
- Do not require measurable goals for casual tasks; use success criteria only when they clarify the work.
- For subjective work, ask about audience and taste before asking about implementation details.
- For coding work, ask about expected behavior, affected scope, validation, and constraints before asking about style.
- For research or factual requests, ask about depth, recency, source quality, and output format when those choices matter.
- For personal or everyday decisions, ask about constraints and preferences, not just facts.
- If a question has already been answered in the conversation, do not ask it again.
