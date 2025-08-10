# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Update this CLAUDE.md file with any new information when developping for fixing features.

## Project Overview

PaceLock is a simracing analytics tool that quantifies driver consistency using statistical analysis of lap times from iRacing race data. The system retrieves race and lap data via the iRacing API, filters out outliers (e.g., out-laps, pit laps, incident laps), and calculates a normalized Consistency Score (0–100 percentile) based on lap time variance and delta stability. Scores can be aggregated over multiple races to produce driver rankings, leaderboards, and trend analysis.

## Architecture

This is a new project. Based on the requirements, the expected architecture will include:

### Core Components
- **API Client**: iRacing API integration using Python with aiohttp/httpx for async requests
- **Data Processing**: Pandas & NumPy for lap time analysis, outlier filtering, and statistical calculations
- **Consistency Scoring**: Python algorithm to calculate normalized consistency scores (0-100 percentile)
- **Data Storage**: SQLite (MVP)
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

### Backend (Python/FastAPI)
```bash
# Development server
uvicorn main:app --reload --port 8000

# Testing
pytest
pytest --cov=src tests/

# Linting and formatting
black src/ tests/
flake8 src/ tests/
mypy src/
```

### Frontend (Svelte/Vite)
```bash
# Development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Linting and formatting
npm run lint
npm run format
```

## Key Implementation Notes

- **iRacing API**: Use aiohttp/httpx for async requests with proper authentication and rate limiting
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

## Frontend
- **Framework:** Svelte — lightweight, compile-time JavaScript framework enabling reactive UI with minimal bundle size (~2KB runtime).  
- **CSS:** Tailwind CSS with PurgeCSS/JIT — utility-first CSS framework optimized to purge unused styles for a minimal CSS footprint.  
- **GraphQL Client:** graphql-request — lightweight GraphQL client for efficient data fetching from the backend.  
- **Build Tool:** Vite — modern, fast build tool optimized for development speed and production bundle size.

## Hosting & Deployment
- **Database & API:** Supabase (PostgreSQL) or local SQLite during MVP phase; hosted on Railway, Render, or similar affordable platforms.  
- **Frontend:** Static hosting on GitHub Pages, Netlify, or similar, serving prebuilt Svelte app with API integration.

# FINAL AGENT INSTRUCTIONS

1. ** ALWAYS ** update this file with each new feature or when a feature changes so that this file reflects how the project works at all time. Make sure to include a depedency graph of all the working pieces and what the purpose of each file is.

2. ** ALWAYS ** update the readme file to include project features, dependencies, developer environment config, commands, etc.

3. ** ALWAYS ** write unit tests using pytest for all the new backend development, and run tests to ensure nothing is broken.