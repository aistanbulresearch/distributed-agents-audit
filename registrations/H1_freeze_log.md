# H1 freeze log

## prereg-H1-v1

Freeze claim (input to `audit/lib/freeze_check.py`):

| Field | Value |
|---|---|
| Origin | `https://github.com/aistanbulresearch/distributed-agents-audit` |
| Tag | `prereg-H1-v1` (annotated; tag object `d6aa7761b4d4a22eab2e38f5bb5968bcfb459945`) |
| Commit | `7e04da3507c9fa915881d65eb52b2e547f750303` |
| Code commit (in the manifest) | `b2c392f6e2018b2e1a23e87d929be1244ca092f6` |
| Manifest | `registrations/H1_freeze.json` |
| Manifest SHA-256 | `f348e305c44727fb9d1d1395ede8c32771a6c5e68b1c1b76c5ea01a105859356` |
| Reference DE file SHA-256 | `cade64a236e3707e91c289bae32282e8b919276760223e581af2342232bcb969` |
| Upstream pin | `c20445d929f5aedce1d539ef6fbd8843b8c06e25` |

Software Heritage archive:

| Field | Value |
|---|---|
| Save request | 2571075 (requested 2026-10-24T02:10:33Z) |
| Snapshot | `swh:1:snp:b400d491e41692418c7bb586c796bcbb74e2b088` |
| Visit date (freeze date to cite) | 2026-10-24T02:10:40.908Z |
| Tag date | 2026-10-24T02:07:16Z |

Archive check (`verify_archive`, live API, 2026-10-24): the latest complete visit contains the
annotated tag, the tag points to the commit above, the archived manifest has the SHA-256
above, and the visit is not dated before the tag. Receipt:

```json
{
 "snapshot": "b400d491e41692418c7bb586c796bcbb74e2b088",
 "visit_date": "2026-10-24T02:10:40.908000+00:00",
 "release": "d6aa7761b4d4a22eab2e38f5bb5968bcfb459945",
 "commit": "7e04da3507c9fa915881d65eb52b2e547f750303",
 "tag_date": "2026-10-24T05:07:16+03:00"
}
```

Before publication, a fresh clone of the tagged commit (submodule at the pin) reproduced
every annotation artifact byte for byte (`audit/scripts/h1_replay_freeze.py`).

This log is added after the tag; it is not part of the frozen artifacts and does not change
them. No report statistic had been compared with DE values at the time of the freeze.
