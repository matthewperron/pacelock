# PaceLock

A simracing analytics tool that quantifies driver consistency using statistical analysis of lap times from iRacing race data.

## Vision

PaceLock aims to provide objective, data-driven insights into simracing performance by focusing on consistency rather than raw speed. The system analyzes lap time variance and delta stability to generate normalized consistency scores that help drivers understand their performance patterns and areas for improvement.

## What It Does

- **Retrieves** race and lap data from the iRacing API
- **Filters** outliers including out-laps, pit laps, and incident-affected laps
- **Calculates** normalized Consistency Scores (0–100 percentile) based on lap time variance and delta stability
- **Aggregates** scores across multiple races for comprehensive driver rankings
- **Provides** leaderboards and trend analysis to track consistency improvements over time

## Key Features

### Statistical Analysis
- Advanced outlier detection to ensure accurate lap time analysis
- Variance calculations normalized across different track types
- Percentile-based scoring for fair comparison across drivers

### Data Integration
- Seamless iRacing API integration with proper rate limiting
- Persistent storage of race data and calculated metrics
- Efficient caching for frequently accessed data

### Analytics Dashboard
- Driver rankings and leaderboards
- Trend analysis across multiple races
- Performance metrics visualization

## Technology Stack

**Backend**
- Python 3.x with FastAPI for high-performance async API
- Strawberry GraphQL for modern, type-safe API design
- SQLAlchemy ORM with SQLite (development) and PostgreSQL (production)
- Pandas & NumPy for statistical analysis

**Frontend**
- Svelte with Vite for minimal bundle size and fast builds
- Tailwind CSS for utility-first styling
- graphql-request for efficient data fetching

**Infrastructure**
- Railway/Render for backend hosting
- Netlify/GitHub Pages for frontend deployment
- GitHub Actions for automated workflows

## Getting Started

### Prerequisites
- Node.js 18+ and npm (for task runner)
- Python 3.9+ 
- iRacing account and API access

### Environment Setup

1. **Install Node.js and npm** (required for task runner)

2. **Set up the project:**
   ```bash
   npm run setup
   ```

3. **Set iRacing credentials:**
   ```bash
   export IRACING_USERNAME=your_iracing_username
   export IRACING_PASSWORD=your_iracing_password
   ```
   
   Or create a `.env` file:
   ```
   IRACING_USERNAME=your_iracing_username
   IRACING_PASSWORD=your_iracing_password
   ```

4. **Run the application:**
   ```bash
   npm run dev
   ```

### Development Commands

**NPM Task Runner (Recommended)**
```bash
# One-time setup
npm run setup

# Development
npm run dev                 # Run backend application
npm run dev:server         # Run API server (when implemented)
npm run dev:frontend       # Run frontend (when implemented)
npm run dev:fullstack      # Run both backend and frontend

# Testing
npm test                   # Run tests
npm run test:coverage      # Run tests with coverage

# Code Quality
npm run format             # Format code with black
npm run lint               # Lint code with flake8
npm run typecheck          # Type check with mypy
npm run quality            # Run all quality checks

# Utilities
npm run clean              # Clean up cache files

# Database
npm run db                 # Open litecli for interactive database access
npm run db:inspect         # Quick database table inspection
```

**Direct Python Commands (Alternative)**
```bash
# Install dependencies
pip install -r requirements.txt

# Run main script
python main.py

# Start development server (when implemented)
uvicorn src.api.main:app --reload --port 8000

# Run tests
pytest
pytest --cov=src tests/

# Code quality
black src/ tests/
flake8 src/ tests/
mypy src/
```

## Contributing

This project focuses on providing accurate, unbiased consistency metrics for the simracing community. Contributions should maintain statistical rigor and respect driver data privacy.

## License

MIT
