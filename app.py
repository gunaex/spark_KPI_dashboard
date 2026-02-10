"""
Example script to run the KPI Dashboard
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from kpi_dashboard import KPIProcessor, Dashboard


def main():
    """Main function to run the KPI dashboard"""
    
    print("=" * 60)
    print("KPI Dashboard - Example Usage")
    print("=" * 60)
    
    # Initialize KPI Processor
    print("\n1. Initializing KPI Processor...")
    processor = KPIProcessor(app_name="KPI_Dashboard_Example")
    
    # Load sample data
    print("\n2. Loading sample data...")
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_data.csv')
    
    if not os.path.exists(data_path):
        print(f"Error: Sample data file not found at {data_path}")
        print("Please ensure the sample_data.csv file exists in the data directory")
        processor.stop()
        return
    
    df = processor.load_data(data_path, file_format='csv', header=True)
    
    # Show sample data
    print("\n3. Sample data preview:")
    df.show(5)
    
    # Calculate KPIs
    print("\n4. Calculating KPIs...")
    kpis = processor.calculate_all_kpis(df)
    
    # Display KPIs
    print("\n" + "=" * 60)
    print("CALCULATED KPIs")
    print("=" * 60)
    
    if 'sales' in kpis:
        print("\n📊 Sales KPIs:")
        for key, value in kpis['sales'].items():
            if isinstance(value, (int, float)):
                print(f"  • {key.replace('_', ' ').title()}: {value:,.2f}")
    
    if 'customers' in kpis:
        print("\n👥 Customer KPIs:")
        for key, value in kpis['customers'].items():
            if isinstance(value, (int, float)):
                print(f"  • {key.replace('_', ' ').title()}: {value:,.2f}")
    
    if 'products' in kpis:
        print("\n📦 Product KPIs:")
        for key, value in kpis['products'].items():
            if isinstance(value, (int, float)):
                print(f"  • {key.replace('_', ' ').title()}: {value:,.2f}")
            elif key == 'top_10_products':
                print(f"  • Top Products:")
                for i, (product_id, revenue) in enumerate(value[:5], 1):
                    print(f"    {i}. {product_id}: ${revenue:,.2f}")
    
    # Initialize and run dashboard
    print("\n" + "=" * 60)
    print("5. Starting Web Dashboard...")
    print("=" * 60)
    print("\nDashboard will be available at: http://localhost:5000")
    print("Press CTRL+C to stop the dashboard\n")
    
    dashboard = Dashboard(kpis=kpis, host='0.0.0.0', port=5000)
    
    try:
        dashboard.run(debug=False)
    except KeyboardInterrupt:
        print("\n\nShutting down dashboard...")
    finally:
        processor.stop()
        print("Dashboard stopped. Goodbye!")


if __name__ == "__main__":
    main()
