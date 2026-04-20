# STATE: notams

## Project Reference
**Core Value**: A cross-platform tool to fetch and visualize NOTAMs for rocket launch areas.
**Current Focus**: Enabling macOS and Linux support by removing Windows-specific dependencies.

## Current Position
**Phase**: Phase 1 (Core Compatibility)
**Plan**: 01-01-PLAN.md
**Status**: Planning complete, ready to execute
**Progress**: [▓░░░░░░░░░░░░░░░░░░░] 5%

## Performance Metrics
- **Requirement Coverage**: 100% (8/8 v1 requirements mapped)
- **Phase Completion**: 0/3

## Accumulated Context
### Decisions
- Use `pywebview` native APIs for file dialogs to improve cross-platform consistency.
- Standardize on `pathlib` for all file path operations.
- Use `pyperclip` for clipboard operations; fallback to copying file path if image clipboard is not supported.

### Todos
- [ ] Execute Phase 1: Core Compatibility

### Blockers
- None
