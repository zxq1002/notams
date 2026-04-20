# ROADMAP: notams

## Phases

- [ ] **Phase 1: Core Compatibility** - Remove Windows-specific dependencies and adjust Python versioning.
- [ ] **Phase 2: Enhancement** - Improve cross-platform UI interactions and error handling.
- [ ] **Phase 3: Validation** - Verify application stability on target platforms.

## Phase Details

### Phase 1: Core Compatibility
**Goal**: The application can start and perform basic operations on macOS/Linux without Windows-specific errors.
**Depends on**: None
**Requirements**: COMPAT-1.1, COMPAT-1.3, DEPS-2.1, DEPS-2.2
**Success Criteria**:
  1. Application starts on macOS/Linux without `ImportError` related to `win32`.
  2. Clipboard functionality (copying images/data) works via a cross-platform method.
  3. `requirements.txt` is updated to remove `pywin32` and specify Python 3.9+.
  4. `pywebview` initializes correctly on non-Windows environments (WebKit/GTK).
**Plans**:
- [ ] 01-01-PLAN.md — Fix startup dependencies and remove Windows imports.
**UI hint**: yes

### Phase 2: Enhancement
**Goal**: Improved cross-platform user experience and robust error handling.
**Depends on**: Phase 1
**Requirements**: COMPAT-1.2, ENHANCE-3.1
**Success Criteria**:
  1. File dialogs use `pywebview` native API or another cross-platform solution instead of `tkinter`.
  2. All file and directory paths are handled using `pathlib` for OS-agnostic operations.
  3. Network failures during NOTAM scraping are handled gracefully with appropriate user feedback.
**Plans**: TBD
**UI hint**: yes

### Phase 3: Validation
**Goal**: Verified stability and automated checks across target platforms.
**Depends on**: Phase 2
**Requirements**: VALID-4.1, VALID-4.2
**Success Criteria**:
  1. The application successfully launches, loads maps, and displays NOTAMs on macOS.
  2. A basic test suite verifies core NOTAM parsing and data fetching logic.
  3. Documentation (README) is updated with platform-specific setup instructions.
**Plans**: TBD
**UI hint**: yes

## Progress Table

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Core Compatibility | 0/1 | Not started | - |
| 2. Enhancement | 0/1 | Not started | - |
| 3. Validation | 0/1 | Not started | - |
