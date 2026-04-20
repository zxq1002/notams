# Codebase Structure

**Analysis Date:** 2025-05-14

## Directory Layout

```
notams/
├── .planning/          # GSD planning and codebase map
├── service/            # Backend logic (Python/Flask)
│   ├── fetch/          # Scrapers and API clients for data sources
│   ├── server.py       # Main Flask server and business logic
│   └── notam.py        # NOTAM-related data structures or logic
├── web/                # Frontend assets
│   ├── scripts/        # JavaScript modules for the UI
│   ├── static/         # CSS, images, and Leaflet.js library
│   └── templates/      # HTML templates (Flask/Jinja2)
├── main.py             # Entry point (Starts Flask and pywebview)
├── config.py           # Configuration loader
├── config.ini          # User-editable configuration
├── requirements.txt    # Python dependencies
└── TODOList            # Roadmap and pending tasks
```

## Directory Purposes

**`service/`:**
- Purpose: Contains all server-side logic and integrations.
- Contains: Flask routes, scrapers, data processing utilities.
- Key files: `service/server.py`.

**`service/fetch/`:**
- Purpose: Modules specialized in retrieving data from various sources.
- Contains: Python scrapers using `requests` and `BeautifulSoup4`.
- Key files: `service/fetch/FNS_NOTAM_SEARCH.py`, `service/fetch/MSA_NAV_SEARCH.py`.

**`web/`:**
- Purpose: Frontend code served by Flask.
- Contains: Static assets and templates.
- Key files: `web/templates/index.html`.

**`web/scripts/`:**
- Purpose: JavaScript modules for map and UI interaction.
- Contains: Leaflet map logic, data fetching triggers, sidebar management.
- Key files: `web/scripts/scripts.js`, `web/scripts/notamsDrawer.js`.

## Key File Locations

**Entry Points:**
- `main.py`: Main application entry point.
- `service/server.py`: Flask server entry point (`start_flask`).

**Configuration:**
- `config.ini`: Persistent configuration storage.
- `config.py`: Python interface for configuration.

**Core Logic:**
- `service/server.py`: Contains deduplication, classification, and geometry logic.

**Testing:**
- Not detected.

## Naming Conventions

**Files:**
- Python: `snake_case.py` (e.g., `server.py`). Some fetchers use `UPPER_SNAKE_CASE.py` (e.g., `FNS_NOTAM_SEARCH.py`).
- JavaScript: `camelCase.js` (e.g., `dataFetching.js`).

**Directories:**
- `snake_case` (e.g., `service/fetch`).

## Where to Add New Code

**New Data Source:**
1. Create a new scraper in `service/fetch/`.
2. Update `service/server.py` to import and call the new scraper in the `/fetch` route.
3. Add any necessary toggles to `config.py` and `config.ini`.

**New UI Feature:**
1. Add necessary HTML elements to `web/templates/index.html`.
2. Create or update a module in `web/scripts/`.
3. Add styling in `web/static/styles.css`.

**New Utility:**
- Shared backend helpers: `service/server.py` (or create a new module in `service/`).
- Shared frontend helpers: `web/scripts/scripts.js`.

## Special Directories

**`.planning/`:**
- Purpose: Internal project documentation for the GSD tool.
- Generated: Yes.
- Committed: Yes.

---

*Structure analysis: 2025-05-14*
