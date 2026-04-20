# Testing Patterns

**Analysis Date:** 2025-05-14

## Test Framework

**Runner:**
- Not detected (no `pytest`, `unittest`, or `nose` configured).

**Assertion Library:**
- Not detected.

**Run Commands:**
```bash
# No standard test commands found.
```

## Test File Organization

**Location:**
- No dedicated test directory (e.g., `tests/`) or co-located test files (e.g., `*.test.py`) found.

**Naming:**
- N/A.

## Test Structure

**Suite Organization:**
- N/A.

**Patterns:**
- No automated test patterns detected. Testing appears to be manual and verification is done by running the application.

## Mocking

**Framework:**
- N/A.

**What to Mock:**
- External scraper responses (suggested for future implementation).

## Fixtures and Factories

**Test Data:**
- Example NOTAM messages are sometimes included in comments (e.g., in `FNS_NOTAM_SEARCH.py`).

**Location:**
- N/A.

## Coverage

**Requirements:**
- None enforced.

**View Coverage:**
- N/A.

## Test Types

**Unit Tests:**
- None detected. Manual verification of individual helper functions (like `parse_point` in `service/server.py`).

**Integration Tests:**
- None detected. Manual verification by triggering data fetching in the application.

**E2E Tests:**
- None detected. Manual verification of the map UI and export functionality.

## Common Patterns

**Async Testing:**
- N/A.

**Error Testing:**
- N/A.

---

*Testing analysis: 2025-05-14*
