# prt-label-bypass-test

Test repo for evaluating whether `pull_request_target` label-based security guards
can be bypassed via close/modify/reopen sequence.

## Hypothesis

A workflow that removes a "security-reviewed" label only on `synchronize` events
can be bypassed by an external contributor who:
1. Opens a PR with benign content (triggers `opened`)
2. Gets the `security-reviewed` label applied
3. Closes the PR
4. Force-pushes malicious content to their branch
5. Reopens the PR (triggers `reopened`, NOT `synchronize`)

The label persists because the guard only fires on `synchronize`.
