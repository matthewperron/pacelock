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
- Python 3.x
- Node.js and npm
- iRacing account and API access

### Development Setup

**Backend**
```bash
# Install dependencies
pip install -r requirements.txt

# Start development server
uvicorn main:app --reload --port 8000

# Run tests
pytest --cov=src tests/
```

**Frontend**
```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## Contributing

This project focuses on providing accurate, unbiased consistency metrics for the simracing community. Contributions should maintain statistical rigor and respect driver data privacy.

## License

MIT
