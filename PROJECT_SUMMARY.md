# KPI Dashboard - Project Summary

## Overview
A production-ready KPI Dashboard built with Apache Spark and Flask for distributed data processing and real-time visualization of key performance indicators.

## Project Statistics
- **Total Lines of Code**: ~495 lines of Python
- **Files Created**: 14 files
- **Test Coverage**: 4 unit tests (all passing)
- **Security Issues**: 0 vulnerabilities
- **Code Review**: Passed with no issues

## Key Features

### 1. Data Processing (Apache Spark)
- Distributed data processing using PySpark
- Support for multiple data formats (CSV, Parquet, JSON)
- Efficient KPI calculation algorithms
- Scalable to large datasets

### 2. Web Dashboard (Flask)
- Responsive HTML/CSS interface
- Real-time KPI display
- Beautiful gradient design with card-based layout
- Mobile-friendly responsive design

### 3. KPI Categories
- **Sales**: Revenue, order values, transaction counts
- **Customers**: Unique customers, retention rates, transaction averages
- **Products**: Product diversity, top products, revenue analysis

### 4. API Endpoints
- `GET /` - Dashboard homepage
- `GET /api/kpis` - JSON API for KPI data
- `GET /api/charts/sales` - Sales chart data
- `GET /api/charts/customers` - Customer chart data

## Project Structure
```
spark_KPI_dashboard/
├── src/
│   ├── kpi_dashboard/        # Main package
│   │   ├── kpi_processor.py  # Spark processing engine (187 lines)
│   │   ├── dashboard.py      # Flask web app (129 lines)
│   │   └── templates/        # HTML templates
│   └── tests/                # Unit tests (73 lines)
├── data/                     # Sample data
├── config/                   # Configuration templates
├── app.py                    # Main entry point (91 lines)
├── Dockerfile                # Docker container config
├── docker-compose.yml        # Docker Compose setup
├── setup.sh                  # Automated setup script
├── requirements.txt          # Python dependencies
├── README.md                 # Full documentation
├── QUICKSTART.md            # Quick start guide
└── LICENSE                   # MIT License
```

## Technology Stack
- **Backend**: Apache Spark (PySpark 3.2.0+), Flask 2.0.0+
- **Data Processing**: Pandas, PySpark SQL
- **Visualization**: Plotly 5.0.0+
- **Testing**: Python unittest
- **Deployment**: Docker, Docker Compose
- **Configuration**: python-dotenv

## Sample Data
- 20 sample transactions
- 10 unique customers
- 5 products
- $33,406.50 total revenue
- 60% customer retention rate

## Getting Started

### Method 1: Automated Setup
```bash
./setup.sh
python app.py
```

### Method 2: Docker
```bash
docker-compose up -d
```

### Method 3: Manual
```bash
pip install -r requirements.txt
python app.py
```

Then visit: http://localhost:5000

## Testing
All tests passing:
```bash
python -m unittest discover src/tests/
# Ran 4 tests in ~18s - OK
```

## Security
- ✅ CodeQL scan: No vulnerabilities found
- ✅ Code review: No issues found
- ✅ Dependencies: All from trusted sources

## Future Enhancements
- Real-time data streaming with Spark Streaming
- Additional visualization charts (time series, heatmaps)
- Export functionality (PDF, Excel)
- User authentication and role-based access
- Database integration (PostgreSQL, MongoDB)
- Advanced analytics and predictive models

## License
MIT License - See LICENSE file

## Author
KPI Dashboard Team
Built with ❤️ using Apache Spark and Flask
