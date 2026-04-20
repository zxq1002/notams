# Technology Stack

**Analysis Date:** 2025-05-14

## Languages

**Primary:**
- Python 3.x - Backend server, data scraping, and geometry processing
- JavaScript (ES6+) - Frontend map interaction and UI logic

**Secondary:**
- HTML5/CSS3 - Frontend structure and styling

## Runtime

**Environment:**
- Python 3.x
- Web Browser (Chromium-based recommended for `pywebview`)

**Package Manager:**
- pip
- Lockfile: missing (only `requirements.txt` present)

## Frameworks

**Core:**
- Flask >=3.1.2 - Web server and API backend
- pywebview >=6.1 - Desktop application wrapper

**Testing:**
- Not detected (no test framework found in `requirements.txt` or codebase)

**Build/Dev:**
- Not detected (no build tools like Webpack or Vite; uses raw scripts and static assets)

## Key Dependencies

**Critical:**
- `leaflet.js` (v1.x) - Interactive map visualization (located in `web/static/leaflet/`)
- `requests` - External API and website scraping
- `beautifulsoup4` - Parsing scraped HTML data
- `shapely` - Geometric operations for NOTAM areas (point-in-poly, etc.)
- `pandas` & `numpy` - Data manipulation and deduplication logic
- `pillow` - Image processing for exporting maps

**Infrastructure:**
- `pywin32` - Windows-specific integrations (clipboard, file dialogs)

## Configuration

**Environment:**
- `config.ini`: Persistent configuration for ICAO codes, server settings, and fetch toggles.
- `config.py`: Python wrapper for loading and accessing `config.ini`.

**Build:**
- No automated build process detected; the project runs directly from source.

## Platform Requirements

**Development:**
- Python 3.x environment with dependencies from `requirements.txt`.
- Windows is the primary target due to `pywin32` usage.

**Production:**
- Standalone execution via `main.py` (requires Python environment).

---

*Stack analysis: 2025-05-14*
