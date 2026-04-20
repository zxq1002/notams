# ROADMAP: notams

## Phases

- [x] **Phase 1: Core Compatibility** - Remove Windows-specific dependencies and adjust Python versioning.
- [x] **Phase 2: Enhancement** - Improve cross-platform UI interactions and error handling.
- [ ] **Phase 3: Validation** - Verify application stability on target platforms.

## Phase Details

### Phase 1: Core Compatibility
**Goal**: The application can start and perform basic operations on macOS/Linux without Windows-specific errors.
**Depends on**: None
**Requirements**: COMPAT-1.1, COMPAT-1.3, DEPS-2.1, DEPS-2.2, ENHANCE-3.1
**Success Criteria**:
  1. Application starts on macOS/Linux without `ImportError` related to `win32`.
  2. Clipboard functionality (copying images/data) works via a cross-platform method.
  3. `requirements.txt` is updated to remove `pywin32` and specify Python 3.9+.
  4. `pywebview` initializes correctly on non-Windows environments (WebKit/GTK).
  5. All file paths are handled using `pathlib` for OS-agnostic operations.
**Plans**:
- [x] 01-01-PLAN.md — Fix startup dependencies and remove Windows imports.
- [x] 01-02-PLAN.md — Refactor path handling to use pathlib and fix asset paths.
**UI hint**: yes

### Phase 2: Enhancement
**Goal**: Improved cross-platform user experience and robust error handling.
**Depends on**: Phase 1
**Requirements**: COMPAT-1.2, ENHANCE-3.1
**Success Criteria**:
  1. File dialogs use `pywebview` native API instead of `tkinter`.
  2. Network failures during NOTAM scraping are handled gracefully with appropriate user feedback.
  3. UI feedback for scraping failures is improved (no alerts, use notifications).
**Plans**:
- [x] 02-01-PLAN.md — Replace tkinter dialogs with pywebview native APIs and improve UI feedback.
- [x] 02-02-PLAN.md — Implement robust error handling and timeouts in data fetchers.
**UI hint**: yes

### Phase 3: Validation
**Goal**: Verified stability and automated checks across target platforms.
**Depends on**: Phase 2
**Requirements**: VALID-4.1, VALID-4.2
**Success Criteria**:
  1. The application successfully launches, loads maps, and displays NOTAMs on macOS.
  2. A basic test suite verifies core NOTAM parsing and data fetching logic.
  3. Documentation (README) is updated with platform-specific setup instructions.
**Plans**:
- [ ] 03-01-PLAN.md — Establish an automated testing foundation with pytest.
- [ ] 03-02-PLAN.md — Update README.md and perform final manual verification on macOS.
**UI hint**: yes

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Core Compatibility | 2/2 | Completed | 2026-04-20 |
| 2. Enhancement | 2/2 | Completed | 2026-04-20 |
| 3. Validation | 0/2 | Planned | - |
