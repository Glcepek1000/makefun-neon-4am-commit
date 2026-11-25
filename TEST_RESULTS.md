# Test results

Date: 2026-11-25 (WIB). Python 3.12.3. All commands run for real; outputs
copied verbatim. One failure was found and fixed during testing (see §3).

## 1. Local run

Command:

```sh
OUTPUT_DIR=/tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-out python3 main.py
```

Output:

```text
wrote /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-out/entry.txt: 111 chars, 111 bytes
fix: I wrote this bug at 2am, fixed it at 4am, and filed a restraining order against the version of me from 2am
```

Exit code: 0.

Verification (Python re-read of `entry.txt`):

```text
chars: 111 bytes: 111 newlines: 0 exact match: True
```

- Entry equals the chosen line byte-for-byte (diff clean).
- Gate: 111 chars, within 1–200; single line; not only whitespace. **PASS**
- sha256 of `entry.txt`:
  `65934815245f227a7d148fdc61121aeee2f7261df0f9214ec5831b0bbbc257b1`

## 2. Grader-exact sandbox simulation

Read-only repo copy, clean environment, only the output dir writable,
60 s timeout — the grader's conditions:

```sh
rm -rf /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean-out
cp -r repo /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean
chmod -R a-w /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean
timeout 60 env -i PATH=/usr/bin:/bin TZ=UTC PYTHONHASHSEED=0 OUTPUT_DIR=/tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean-out python3 /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean/main.py
```

Output:

```text
wrote /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean-out/entry.txt: 111 chars, 111 bytes
fix: I wrote this bug at 2am, fixed it at 4am, and filed a restraining order against the version of me from 2am
sim exit=0
65934815245f227a7d148fdc61121aeee2f7261df0f9214ec5831b0bbbc257b1  /tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-clean-out/entry.txt
IDENTICAL to local run
```

- Exit code: 0. `entry.txt` byte-identical to the local run (same sha256).
  **PASS**

## 3. Failure found and fixed during testing

First local run failed with `NameError: name 'os' is not defined` — the
initial `main.py` draft omitted `import os`. Fixed by adding the import;
re-ran the local run (§1) and the grader sim (§2) after the fix — both
pass. No other failures.

## 4. setup.sh one-shot run

Command: `OUTPUT_DIR=/tmp/u-neon-autonomous-the-4am-commit-funniest-agent-bug-195af06d-out sh setup.sh`

Output: `Python 3.12.3`, then the same 111-char write, then
`setup complete: zero errors.` — exit code 0. **PASS**

## 5. zero-fail-qa grep

```sh
grep -rnE "/home/|/Users/|API_KEY|SECRET|TOKEN|PASSWORD|BEGIN.*PRIVATE" repo/
```

Result: no matches — no hardcoded paths, no secrets in the repo. **PASS**

## Summary

| Check | Result |
| --- | --- |
| Local run, exact line, 111 chars | PASS |
| Grader-exact sandbox sim, exit 0, identical sha256 | PASS |
| setup.sh one-shot, zero errors | PASS |
| zero-fail-qa grep (paths/secrets) | PASS |
| Gate (UTF-8, 1–200 chars, single line) | PASS |
