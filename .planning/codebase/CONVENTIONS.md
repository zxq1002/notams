# Coding Conventions

**Analysis Date:** 2025-05-14

## Naming Patterns

**Files:**
- Python: Primarily `snake_case.py` (e.g., `main.py`, `config.py`), but fetchers often use `UPPER_SNAKE_CASE.py` (e.g., `FNS_NOTAM_SEARCH.py`).
- JavaScript: `camelCase.js` (e.g., `dataFetching.js`).

**Functions:**
- Python: `snake_case` (e.g., `start_flask`, `parse_point`).
- JavaScript: `camelCase` (e.g., `toggleSidebar`, `drawWarning`).

**Variables:**
- Python: `snake_case` for locals, `UPPER_SNAKE_CASE` for globals/constants (e.g., `HOST`, `PORT`, `added_entries`).
- JavaScript: `camelCase` (e.g., `notamList`, `selectedDate`).

**Types:**
- Classes: `PascalCase` (e.g., `LogCapture`, `PrintCapture` in `service/server.py`).

## Code Style

**Formatting:**
- Python: No explicit formatter (like Black) configured, but generally follows PEP 8.
- JavaScript: Standard browser JS style.

**Linting:**
- Not detected.

## Import Organization

**Order:**
1. Standard library imports.
2. Third-party library imports.
3. Local module imports.

**Path Aliases:**
- None.

## Error Handling

**Patterns:**
- Extensive use of `try...except` blocks in the backend to handle network failures and parsing errors.
- Errors are logged to the console and captured via a custom `LogCapture` class for UI display.
- Tracebacks are printed to `stderr` in critical sections.

## Logging

**Framework:**
- `logging` (Python standard library) + custom `LogCapture` / `PrintCapture` to redirect output to the frontend.

**Patterns:**
- `print()` is used frequently for status updates and debugging information.
- Flask request logging is filtered to exclude periodic log-polling requests.

## Comments

**When to Comment:**
- Function docstrings are used for some complex logic (e.g., `coords_to_polygon`).
- Inline comments explain specific regex patterns and business logic decisions.

**JSDoc/TSDoc:**
- Not used.

## Function Design

**Size:**
- Functions in `service/server.py` and `service/fetch/` vary. Some logic (like the `/fetch` route) is quite large (~150 lines).

**Parameters:**
- Uses positional and keyword parameters.

**Return Values:**
- Python: Functions typically return standardized dictionaries or lists for easy JSON serialization.

## Module Design

**Exports:**
- Python: Uses standard imports.
- JavaScript: Uses global scope in the browser via multiple `<script>` tags in `index.html`.

**Barrel Files:**
- None.

---

*Convention analysis: 2025-05-14*
