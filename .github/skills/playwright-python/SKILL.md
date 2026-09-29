---
name: playwright-python
description: 'Write, run, and debug browser automation with Playwright for Python. Use when creating or fixing Python Playwright scripts, browser interactions, web UI tests, locator issues, navigation and waiting problems, or browser failures.'
argument-hint: 'Describe the browser task, target page, and expected result'
user-invocable: true
---

# Playwright Python

Create reliable Python browser automation and diagnose it from observed behavior. Prefer the smallest change that meets the requested outcome and fits the current project.

## Workflow

1. **Clarify the behavior.** Identify the target page or application, the action to perform, and an observable success condition. If a key detail is missing, inspect nearby code or ask one focused question rather than guessing selectors or expected results.
2. **Inspect the project.** Read the relevant script and nearby tests/configuration. Preserve the existing Playwright sync or async API, test runner, Python environment, browser setup, and code style. Do not introduce a new framework or change dependency configuration unless necessary.
3. **Check the setup.** Confirm the selected Python environment and whether `playwright` and its browsers are installed. Reuse the project's setup. If setup is missing, explain the smallest required installation steps; do not silently install packages or browsers.
4. **Implement the interaction.** Use Playwright locators and user-visible semantics where practical (`get_by_role`, `get_by_label`, `get_by_text`, or a project-supported test id). Keep locators scoped to the relevant region when that improves uniqueness. Use the existing sync or async API consistently, and follow the surrounding lifecycle and test conventions.
5. **Make it deterministic.** Rely on locator actions and assertions that auto-wait. Wait for a meaningful state such as a URL change, visible element, response, or completed navigation. Avoid fixed sleeps, arbitrary retries, and broad exception suppression. Handle frames, dialogs, downloads, and popups with their dedicated Playwright APIs when the task requires them.
6. **Run the narrowest useful check.** Execute the touched test or script using the project's existing command and environment. Compare the observed result with the success condition. If a live site, credentials, or browser installation is unavailable, state that limitation and validate what can be checked locally.
7. **Diagnose failures from evidence.** Read the full exception and relevant code. Inspect the current URL, locator count/state, and page content as needed. For intermittent or rendering failures, capture a screenshot or trace and use it to identify the cause before changing waits or selectors. Fix the controlling cause, then rerun the same focused check.
8. **Finish cleanly.** Ensure browser, context, and page lifetimes follow the existing pattern and are closed even on failure. Report the files changed, the command and result, and any remaining environment or site-dependent limitation.

## Reliability and Safety

- Prefer stable, accessible locators over brittle CSS/XPath chains or generated class names. If the page has no reliable semantic locator, use the narrowest stable selector supported by the application and explain the assumption.
- Do not use `time.sleep()` to paper over synchronization problems. Wait for the state the next action actually depends on.
- Keep assertions tied to user-visible outcomes; avoid asserting incidental implementation details unless the test specifically covers them.
- Keep credentials, cookies, and other secrets out of source code, logs, screenshots, and committed traces. Use the project's established secret handling and avoid exposing authenticated page data unnecessarily.
- Preserve existing user changes and avoid unrelated refactors.

## Completion Check

Before finishing, verify that the requested action is exercised, its success condition is checked, the focused run has a clear result, and browser resources are cleaned up. Distinguish code defects from missing browsers, unavailable services, or credentials.