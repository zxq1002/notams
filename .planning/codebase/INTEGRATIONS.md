# External Integrations

**Analysis Date:** 2025-05-14

## APIs & External Services

**NOTAM Retrieval:**
- **FAA FNS (Federal NOTAM System):**
  - Used for: Primary source of worldwide NOTAMs (current and historical).
  - SDK/Client: `requests` + `BeautifulSoup4` (scraped/queried via `service/fetch/FNS_NOTAM_SEARCH.py` and `service/fetch/FNS_NOTAM_ARCHIVE_SEARCH.py`).
  - Auth: None (public web interface).
- **US Defense Internet NOTAM Service (DINS):**
  - Used for: Military-specific NOTAM retrieval.
  - SDK/Client: `requests` + `BeautifulSoup4` (via `service/fetch/dinsQueryWeb.py`).
  - Auth: None.

**Maritime Safety Information (MSI):**
- **China MSA (Maritime Safety Administration):**
  - Used for: Maritime navigation warnings for Chinese coastal areas.
  - SDK/Client: `requests` (via `service/fetch/MSA_NAV_SEARCH.py`).
  - Auth: None.
- **US NGA MSI (Maritime Safety Information):**
  - Used for: Global maritime navigation warnings from NGA.
  - SDK/Client: `requests` (via `service/fetch/MSI_NAV_SEARCH.py`).
  - Auth: None.

## Data Storage

**Databases:**
- None. The application uses transient local JSON storage for caching.
  - Client: `json` module.

**File Storage:**
- **Local filesystem only:**
  - Caches NOTAM results in `notam_results.json`.
  - Exports images via Windows file dialog to user-specified paths.

**Caching:**
- **Local JSON Cache:**
  - Used to reduce hits to external NOTAM servers within a specified expiration time (`FETCH_EXPIRE_TIME` in `config.py`).

## Authentication & Identity

**Auth Provider:**
- Custom (None): No user authentication implemented. Local access only.

## Monitoring & Observability

**Error Tracking:**
- Custom: Errors are captured in a `LogCapture` class and exposed via a `/logs` API route (see `service/server.py`).

**Logs:**
- Console output and manual logging via Flask's logger, captured for UI display.

## CI/CD & Deployment

**Hosting:**
- Local execution. No cloud hosting detected.

**CI Pipeline:**
- None.

## Environment Configuration

**Required env vars:**
- None. Uses `config.ini` and `config.py`.

**Secrets location:**
- No secrets (keys, etc.) required for current public scrapers.

## Webhooks & Callbacks

**Incoming:**
- None.

**Outgoing:**
- External scraper requests to FAA, DINS, MSA, and MSI sites.

---

*Integration audit: 2025-05-14*
