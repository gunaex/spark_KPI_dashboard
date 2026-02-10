# Spark KPI Dashboard 📊

A comprehensive Key Performance Indicator (KPI) Dashboard built with Apache Spark and Flask for real-time data processing and visualization.

## Features

- **Apache Spark Integration**: Efficient distributed data processing for large-scale datasets
- **Real-time KPI Calculation**: Automatic calculation of sales, customer, and product metrics
- **Interactive Web Dashboard**: Beautiful, responsive web interface for KPI visualization
- **Flexible Data Import**: Support for CSV, Parquet, and JSON data formats
- **REST API**: RESTful API endpoints for programmatic access to KPIs
- **Sample Data Included**: Ready-to-use sample dataset for testing

## KPI Categories

### 💰 Sales KPIs
- Total Revenue
- Average Order Value
- Total Transactions
- Average Revenue per Transaction
- Max/Min Order Values

### 👥 Customer KPIs
- Unique Customers
- Average Transactions per Customer
- Customer Retention Rate

### 📦 Product KPIs
- Total Products
- Top 10 Products by Revenue
- Average Products per Transaction

## Architecture

```
spark_KPI_dashboard/
├── src/
│   ├── kpi_dashboard/
│   │   ├── __init__.py
│   │   ├── kpi_processor.py    # Spark-based KPI processing
│   │   ├── dashboard.py        # Flask web dashboard
│   │   └── templates/
│   │       └── index.html      # Dashboard UI
│   └── tests/
│       ├── __init__.py
│       └── test_kpi_processor.py
├── data/
│   └── sample_data.csv         # Sample dataset
├── config/
│   └── .env.example            # Configuration template
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
└── README.md
```

## Installation

### Prerequisites
- Python 3.7 or higher
- Java 8 or higher (required for Apache Spark)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/gunaex/spark_KPI_dashboard.git
   cd spark_KPI_dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment (optional)**
   ```bash
   cp config/.env.example .env
   # Edit .env file with your configuration
   ```

## Usage

### Quick Start

Run the dashboard with sample data:

```bash
python app.py
```

The dashboard will be available at `http://localhost:5000`

### Using Your Own Data

```python
from kpi_dashboard import KPIProcessor, Dashboard

# Initialize processor
processor = KPIProcessor(app_name="My_KPI_Dashboard")

# Load your data
df = processor.load_data("path/to/your/data.csv", file_format="csv")

# Calculate KPIs
kpis = processor.calculate_all_kpis(df)

# Start dashboard
dashboard = Dashboard(kpis=kpis)
dashboard.run()
```

### Data Format

Your CSV data should include these columns:
- `transaction_id`: Unique transaction identifier
- `customer_id`: Customer identifier
- `product_id`: Product identifier
- `revenue`: Transaction revenue
- `order_value`: Order value
- `timestamp`: Transaction timestamp (optional)

### API Endpoints

- `GET /` - Main dashboard page
- `GET /api/kpis` - Get all KPIs as JSON
- `GET /api/charts/sales` - Get sales chart data
- `GET /api/charts/customers` - Get customer chart data

## Testing

Run the test suite:

```bash
python -m pytest src/tests/
```

Or using unittest:

```bash
python -m unittest discover src/tests/
```

## Development

### Project Structure

- **kpi_processor.py**: Core Spark processing logic for KPI calculations
- **dashboard.py**: Flask application for web visualization
- **app.py**: Main entry point combining processor and dashboard
- **templates/**: HTML templates for the web interface

### Adding New KPIs

To add custom KPIs, extend the `KPIProcessor` class:

```python
def calculate_custom_kpi(self, df):
    """Calculate custom KPI"""
    # Your calculation logic here
    return kpi_value
```

## Technologies Used

- **Apache Spark**: Distributed data processing
- **PySpark**: Python API for Spark
- **Flask**: Web framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **Python-dotenv**: Configuration management

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues and questions, please open an issue on GitHub.

## Acknowledgments

Built with ❤️ using Apache Spark and Flask