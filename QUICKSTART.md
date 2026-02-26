# Quick Start Guide

## Installation and Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python app.py
   ```

3. **Access the Dashboard**
   - Open your browser and navigate to: http://localhost:5000
   - The dashboard will display KPIs calculated from the sample data

## What You'll See

The dashboard displays three main categories of KPIs:

### 💰 Sales Performance
- Total Revenue
- Average Order Value
- Total Transactions
- Average Revenue per Transaction
- Max/Min Order Values

### 👥 Customer Metrics
- Unique Customers
- Average Transactions per Customer
- Customer Retention Rate

### 📦 Product Analytics
- Total Products
- Top Products by Revenue
- Average Products per Transaction

## Using Your Own Data

To use your own data, replace `data/sample_data.csv` with your file or modify the `app.py` file:

```python
# Change this line in app.py
data_path = "path/to/your/data.csv"
```

Your data should have these columns:
- transaction_id
- customer_id
- product_id
- revenue
- order_value
- timestamp (optional)

## Running Tests

```bash
python -m unittest discover src/tests/
```

## API Endpoints

- `GET /` - Dashboard homepage
- `GET /api/kpis` - Get KPIs as JSON
- `GET /api/charts/sales` - Sales chart data
- `GET /api/charts/customers` - Customer chart data

## Troubleshooting

**Issue**: Java not found
- **Solution**: Install Java 8 or higher (required for Spark)

**Issue**: Module not found errors
- **Solution**: Run `pip install -r requirements.txt` again

**Issue**: Port 5000 already in use
- **Solution**: Modify the port in `app.py` or `config/.env.example`

## Next Steps

1. Customize the KPIs by modifying `src/kpi_dashboard/kpi_processor.py`
2. Update the dashboard layout in `src/kpi_dashboard/templates/index.html`
3. Add your own data sources
4. Deploy to production using a WSGI server like Gunicorn

For more information, see the main [README.md](README.md)
