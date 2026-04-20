# Architecture

**Analysis Date:** 2025-05-14

## Pattern Overview

**Overall:** Client-Server Monolith (Embedded)

**Key Characteristics:**
- **Local-First:** Backend (Python/Flask) and Frontend (JS/Leaflet) run on the same machine.
- **Scraper-Driven:** Primary data acquisition through concurrent web scraping.
- **Hybrid GUI:** Python backend serves as the service layer, while a Web UI (HTML/CSS/JS) provides the interactive mapping interface, wrapped in `pywebview`.

## Layers

**UI Layer (Frontend):**
- Purpose: Renders the map, lists NOTAMs, and provides drawing/exporting tools.
- Location: `web/`
- Contains: `index.html`, Leaflet maps, and JS modules for interaction.
- Depends on: Backend API routes.
- Used by: End user.

**Application Layer (Backend Server):**
- Purpose: Orchestrates data fetching, processing, deduplication, and image exporting.
- Location: `service/server.py`
- Contains: Flask routes, geometry utilities, and business logic for NOTAM classification.
- Depends on: Fetching services and External APIs.
- Used by: UI Layer.

**Service Layer (Data Fetchers):**
- Purpose: Implements specific logic for interacting with various NOTAM and MSI sources.
- Location: `service/fetch/`
- Contains: Scrapers and API clients.
- Depends on: External websites/APIs.
- Used by: Application Layer.

## Data Flow

**NOTAM Fetching Flow:**

1. User clicks "Refresh" in the UI.
2. Frontend calls `/fetch` (API endpoint in `service/server.py`).
3. Backend invokes various fetchers in `service/fetch/` (using `ThreadPoolExecutor` for concurrency).
4. Fetchers query external sites, parse responses, and return standardized data structures.
5. Backend performs deduplication (`should_deduplicate`) and classification (`classify_data`).
6. Backend returns consolidated JSON to the Frontend.
7. Frontend renders NOTAM areas as polygons on the Leaflet map.

**State Management:**
- Local state is managed in the Frontend (JS objects for map layers and NOTAM data).
- Backend maintains a transient cache in `notam_results.json`.

## Key Abstractions

**Fetchers:**
- Purpose: Standardized interface for adding new data sources.
- Examples: `service/fetch/FNS_NOTAM_SEARCH.py`, `service/fetch/MSA_NAV_SEARCH.py`.

**Geometry Utilities:**
- Purpose: Handles coordinate parsing and spatial analysis (point-in-poly, line-segment intersection).
- Pattern: Procedural utility functions in `service/server.py` (`parse_point`, `point_in_poly`).

## Entry Points

**`main.py`:**
- Location: `main.py`
- Triggers: User executing the application.
- Responsibilities: Boots the Flask server thread and initializes the `pywebview` window.

## Error Handling

**Strategy:** Capture and Expose

**Patterns:**
- Try-except blocks around network requests and data parsing.
- `LogCapture` class in `service/server.py` intercepts `stdout/stderr` and Flask logs to display them in the UI's debug panel.

## Cross-Cutting Concerns

**Logging:** Captured via `sys.stdout` redirection and custom `logging.Handler` in `service/server.py`.
**Validation:** Regex-based validation for coordinate strings (`parse_point`).
**Authentication:** Implicitly none; the app is intended for local use.

---

*Architecture analysis: 2025-05-14*
