# Codebase Concerns

**Analysis Date:** 2025-05-14

## Tech Debt

**`service/server.py` Complexity:**
- Issue: Business logic (geometry calculations, time parsing, deduplication) is tightly coupled with Flask route definitions.
- Files: `service/server.py`
- Impact: Harder to test and maintain; logic cannot easily be reused outside the Flask server.
- Fix approach: Refactor utilities and logic into dedicated modules (e.g., `service/utils/geometry.py`).

**Brittle Scraping Logic:**
- Issue: The fetchers rely on manual HTML parsing or specific JSON structures from external sites (FAA, DINS, MSA, MSI).
- Files: `service/fetch/*.py`
- Impact: Frequent breakage when external sites update their UI/API.
- Fix approach: Implement robust error handling (partially done) and possibly transition to official APIs if available.

**Global State in `config.py`:**
- Issue: Configuration is loaded globally and accessed directly, making testing with different configurations difficult.
- Files: `config.py`, `service/server.py`
- Impact: Testing and dependency injection are difficult.
- Fix approach: Use a configuration object or context manager to pass config into functions.

## Known Bugs

**Deduplication Limitations:**
- Symptoms: Potential for false positives or missed duplicates when coordinate or time formats vary between sources.
- Files: `service/server.py` (`should_deduplicate`)
- Trigger: Multiple sources reporting the same event with slightly different precision or formatting.
- Workaround: Manual verification by the user.

## Security Considerations

**API Endpoint Exposure:**
- Risk: The `/logs` and `/config` endpoints expose internal system information.
- Files: `service/server.py`
- Current mitigation: The application is designed to run locally (`127.0.0.1`).
- Recommendations: Ensure documentation explicitly warns against hosting on public interfaces without authentication.

## Performance Bottlenecks

**Concurrent Fetching Overhead:**
- Problem: `ThreadPoolExecutor` is used with a fixed number of workers; many simultaneous network requests might still be slow due to external site rate limits or network latency.
- Files: `service/fetch/FNS_NOTAM_SEARCH.py`
- Cause: Synchronous `requests` blocking threads.
- Improvement path: Migrate to `aiohttp` or `httpx` for true asynchronous I/O.

## Fragile Areas

**Coordinate Regex:**
- Files: `service/server.py` (`parse_point`), `service/fetch/FNS_NOTAM_SEARCH.py` (`extract_coordinate_groups`)
- Why fragile: High reliance on complex regex to extract coordinates from free-form NOTAM messages. Any unexpected format will fail to render on the map.
- Safe modification: Add comprehensive unit tests for various coordinate formats.
- Test coverage: Gaps (None detected).

## Scaling Limits

**Local File Storage:**
- Current capacity: `notam_results.json` grows as more data is fetched.
- Limit: Performance of JSON serialization/deserialization on large files.
- Scaling path: Introduce a lightweight database (e.g., SQLite) if the volume of historical data increases significantly.

## Dependencies at Risk

**`pywin32`:**
- Risk: Ties the project strongly to the Windows operating system.
- Impact: Prevents deployment on Linux or macOS.
- Migration plan: Use cross-platform alternatives for clipboard and file dialogs (e.g., `pyperclip`, `tkinter` as a fallback).

## Missing Critical Features

**Settings UI:**
- Problem: Users must manually edit `config.ini` to change settings.
- Blocks: Non-technical users might find configuration difficult.
- (See `TODOList` point 2)

**Manual Input Unification:**
- Problem: Manual input and auto-fetched data structures are not fully unified.
- Blocks: Features like "edit manual input" are still pending.
- (See `TODOList` point 5)

## Test Coverage Gaps

**Unit Tests for Data Processing:**
- What's not tested: `parse_point`, `point_in_poly`, `should_deduplicate`, `classify_data`.
- Files: `service/server.py`
- Risk: Changes to core logic could break map rendering or deduplication without notice.
- Priority: High.

---

*Concerns audit: 2025-05-14*
