# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Update this CLAUDE.md file with any new information when developping for fixing features.

## Project Overview

PaceLock is a simracing analytics tool that quantifies driver consistency using statistical analysis of lap times from iRacing race data. The system retrieves race and lap data via the iRacing API, filters out outliers (e.g., out-laps, pit laps, incident laps), and calculates a normalized Consistency Score (0–100 percentile) based on lap time variance and delta stability. Scores can be aggregated over multiple races to produce driver rankings, leaderboards, and trend analysis.

## Architecture

This is a new project. Based on the requirements, the expected architecture will include:

### Core Components
- **API Client**: iRacing API integration using Python with `iracingdataapi` package for race data retrieval
- **Data Processing**: Pandas & NumPy for lap time analysis, outlier filtering, and statistical calculations
- **Consistency Scoring**: Python algorithm to calculate normalized consistency scores (0-100 percentile)
- **Data Storage**: SQLite (built-in sqlite3 module) for MVP
- **Analytics Engine**: FastAPI backend with Strawberry GraphQL for aggregation and trend analysis
- **User Interface**: Svelte frontend with Tailwind CSS, served as static files

### Key Data Flow
1. Fetch race data from iRacing API
2. Extract and clean lap time data (filter outliers)
3. Calculate lap time variance and delta stability
4. Generate normalized consistency scores
5. Aggregate scores across multiple races
6. Present rankings and trend analysis

## Technology Stack

See [PaceLock Tech Stack Description](#pacelock-tech-stack-description) section below for detailed technology choices.

**Key Technologies:**
- **Backend**: Python 3.x + FastAPI + Strawberry GraphQL + SQLAlchemy
- **Frontend**: Svelte + Vite + Tailwind CSS + graphql-request
- **Database**: SQLite (development - with potential migration to Postgres later)
- **Data Processing**: Pandas + NumPy for statistical analysis
- **Deployment**: Railway/Render (backend) + Netlify/GitHub Pages (frontend)

## Development Commands

### NPM Task Runner (Recommended)
```bash
# One-time setup
npm run setup

# Run backend application
npm run dev

# Run backend API server (when FastAPI is implemented)
npm run dev:server

# Run frontend (when implemented)  
npm run dev:frontend

# Run full stack (backend + frontend)
npm run dev:fullstack

# Testing
npm test
npm run test:coverage

# Code quality
npm run format     # Format with black
npm run lint       # Lint with flake8  
npm run typecheck  # Type check with mypy
npm run quality    # Run all quality checks

# Utilities
npm run clean              # Clean up cache files

# Database
npm run db                 # Open litecli for interactive database access
npm run db:inspect         # Quick database table inspection
```

### Direct Python Commands (Alternative)
```bash
# Run main script
python main.py

# Development server (when FastAPI is implemented)
uvicorn src.api.main:app --reload --port 8000

# Testing
pytest
pytest --cov=src tests/

# Linting and formatting
black src/ tests/
flake8 src/ tests/
mypy src/
```

### Frontend (Future - Svelte/Vite)
```bash
# Development server
npm run dev:frontend

# Build for production
npm run build

# Preview production build
npm run preview
```

## Key Implementation Notes

- **iRacing API**: Use `iracingdataapi` package for seamless API integration with proper authentication and rate limiting (implemented in `iracing_api.py`)
- **Outlier Detection**: Implement statistical algorithms in Pandas to filter invalid laps (pit stops, incidents, out-laps)
- **Consistency Scoring**: Use NumPy for statistically sound variance calculations normalized across track types
- **Caching**: Implement Redis or in-memory caching in FastAPI for frequently accessed race data
- **Data Privacy**: Ensure GDPR compliance and appropriate handling of driver information in database design
- **Database Evolution**: Design SQLAlchemy models for easy migration from SQLite to PostgreSQL
- **GraphQL Schema**: Use Strawberry's type system for clean, type-safe API design
- **Frontend State**: Use Svelte stores for reactive state management with GraphQL data

# PaceLock Tech Stack Description

## Backend
- **Language:** Python 3.x  
- **API Framework:** FastAPI — serves REST and GraphQL endpoints with high performance and async support.  
- **GraphQL:** Strawberry GraphQL — modern, type-hinted GraphQL library integrated into FastAPI for clean API design.  
- **Database:** SQLite (MVP) — lightweight, file-based relational database for local development and prototyping; designed for easy migration to PostgreSQL for scalability.  
- **ORM:** SQLAlchemy — database abstraction layer to enable seamless switching between SQLite and PostgreSQL.  
- **Data Processing:** Pandas & NumPy — for statistical analysis and calculation of driver consistency scores from race telemetry data.
- **iRacing API:** iracingdataapi — Python package for accessing iRacing's web API to retrieve race and session data.
- **Database:** sqlite3 (built-in) — Python's built-in SQLite interface for local data storage during MVP phase.
- **Database CLI:** litecli — Interactive command-line interface for SQLite database inspection and queries.

## Frontend
- **Framework:** Svelte — lightweight, compile-time JavaScript framework enabling reactive UI with minimal bundle size (~2KB runtime).  
- **CSS:** Tailwind CSS with PurgeCSS/JIT — utility-first CSS framework optimized to purge unused styles for a minimal CSS footprint.  
- **GraphQL Client:** graphql-request — lightweight GraphQL client for efficient data fetching from the backend.  
- **Build Tool:** Vite — modern, fast build tool optimized for development speed and production bundle size.

## Hosting & Deployment
- **Database & API:** Supabase (PostgreSQL) or local SQLite during MVP phase; hosted on Railway, Render, or similar affordable platforms.  
- **Frontend:** Static hosting on GitHub Pages, Netlify, or similar, serving prebuilt Svelte app with API integration.

# Project Structure

```
pacelock/
├── main.py                    # Entry point script (runs src/api/main.py)
├── package.json              # NPM configuration and task runner scripts
├── requirements.txt           # Python dependencies
├── .env                      # Environment variables (excluded from git)
├── .gitignore               # Git ignore patterns
├── README.md                # User documentation
├── CLAUDE.md               # Development guidelines
├── pacelock.db             # SQLite database (included in git for now)
├── scripts/
│   ├── setup.sh             # Setup script (creates venv, installs deps)
│   └── dev.sh               # Development script (activates venv, runs app)
└── src/
    ├── __init__.py
    └── api/
        ├── __init__.py
        ├── main.py          # Main application logic and orchestration
        ├── iracing_api.py   # iRacing API integration
        └── database.py      # Database operations and SQLite management
```

## File Dependencies
- **main.py** - Project entry point script
  - Purpose: Adds src/ to Python path and runs src/api/main.py
- **package.json** - NPM configuration and task runner
  - Purpose: Centralized script management for setup, development, testing, and deployment
  - Scripts: setup, dev, test, lint, format, typecheck, clean
- **scripts/setup.sh** - Development environment setup script
  - Purpose: Creates virtual environment and installs Python dependencies
- **scripts/dev.sh** - Development runner script
  - Purpose: Activates virtual environment and runs the main application
- **src/api/main.py** - Main application logic and orchestration
  - Imports: `iracing_api.load_subsession_data()`, `database.initialize_database()`, `database.store_subsession_data()`
  - Purpose: Orchestrate data flow, display session summaries, coordinate API and database operations
- **src/api/iracing_api.py** - iRacing API integration module
  - Dependencies: `iracingdataapi`, `python-dotenv`
  - Purpose: Handle authentication, API calls, and data retrieval from iRacing
  - Functions: `check_environment()`, `get_api_client()`, `load_subsession_data()`, `load_lap_times()`
- **src/api/database.py** - Database operations and SQLite management
  - Dependencies: `sqlite3`, `json`
  - Purpose: Handle database initialization, data storage, and retrieval operations
  - Functions: `initialize_database()`, `store_subsession_data()`, `get_subsession_data()`, `list_stored_subsessions()`, `store_lap_times()`
- **requirements.txt** - Python package dependencies
- **CLAUDE.md** - Project documentation and development guidelines
- **README.md** - User-facing project documentation
- **.env** - Environment variables (credentials, excluded from git)
- **.gitignore** - Git ignore patterns (excludes .env, includes pacelock.db)

# FINAL AGENT INSTRUCTIONS

1. ** ALWAYS ** update this file with each new feature or when a feature changes so that this file reflects how the project works at all time. Make sure to include a depedency graph of all the working pieces and what the purpose of each file is.

2. ** ALWAYS ** update the readme file to include project features, dependencies, developer environment config, commands, etc.

3. ** ALWAYS ** write unit tests using pytest for all the new backend development, and run tests to ensure nothing is broken.