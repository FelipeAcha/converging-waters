# Incident addendum — REV30 rolling-transport sequencing

Parent incident: `INC-CW-WEB-20260825-002`  
Date: 2026-08-25  
Production: NOT_AUTHORIZED / unchanged

## F18 — rolling pointer updated before the fully staged dependency tree existed

**Failure:** while preparing the REV30 Rolling Progress transport, `docs/candidates/progress/current.html` was temporarily updated to a REV30 loader before the new `rev30-hub-*.txt` payload files had been committed to the repository.

**Classification:** `TOOL_CONTRACT_MISMATCH` + `LIFECYCLE_PREREQUISITE_MISSED` + `RESPONSE_BEFORE_EXECUTION`.

**First control failure:** the write sequence violated the Web Workstream Control rule that the complete staged route tree must validate before any repository pointer/ref or active loader is moved.

**Impact:** the rolling review route could have been transiently broken if requested during that interval. Production was never affected.

**Immediate corrective action:** the exact prior REV24 `current.html` blob was restored immediately in commit `4982dcab592e58c306280898a03450b5c6ab77d0`; its blob SHA returned to `71112dad323ad23b4a76a8cbfbb46143af95ff70`. The Rolling Progress route therefore remains intentionally stale at REV24 rather than incorrectly advertising REV30.

**Preventive action:** for connector-based GitHub transport updates, create all new immutable payload resources first, validate them as a complete dependency graph, then update deep-dive loaders, then the hub loader, then the banner/state last. Never update an active loader first merely because its content is ready locally.

**Regression / gate:** `GATE-CW-WEB-REV30-ROLLING-STAGED-TREE` must remain blocked until every REV30 payload exists in GitHub and post-write readback proves the staged route complete. A failed or partial staging attempt must restore the prior active loader before any user-facing completion claim.
