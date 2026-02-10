"""
Unit tests for KPI Processor
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from kpi_dashboard import KPIProcessor
from pyspark.sql import Row


class TestKPIProcessor(unittest.TestCase):
    """Test cases for KPI Processor"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures"""
        cls.processor = KPIProcessor(app_name="KPI_Test")
        
        # Create sample data
        data = [
            Row(transaction_id="TXN001", customer_id="CUST001", product_id="PROD001", 
                revenue=1000.0, order_value=1000.0),
            Row(transaction_id="TXN002", customer_id="CUST002", product_id="PROD002", 
                revenue=2000.0, order_value=2000.0),
            Row(transaction_id="TXN003", customer_id="CUST001", product_id="PROD001", 
                revenue=1500.0, order_value=1500.0),
        ]
        cls.test_df = cls.processor.spark.createDataFrame(data)
    
    @classmethod
    def tearDownClass(cls):
        """Tear down test fixtures"""
        cls.processor.stop()
    
    def test_calculate_sales_kpis(self):
        """Test sales KPI calculation"""
        kpis = self.processor.calculate_sales_kpis(self.test_df)
        
        self.assertIn('total_revenue', kpis)
        self.assertIn('total_transactions', kpis)
        self.assertEqual(kpis['total_revenue'], 4500.0)
        self.assertEqual(kpis['total_transactions'], 3)
    
    def test_calculate_customer_kpis(self):
        """Test customer KPI calculation"""
        kpis = self.processor.calculate_customer_kpis(self.test_df)
        
        self.assertIn('unique_customers', kpis)
        self.assertEqual(kpis['unique_customers'], 2)
    
    def test_calculate_product_kpis(self):
        """Test product KPI calculation"""
        kpis = self.processor.calculate_product_kpis(self.test_df)
        
        self.assertIn('total_products', kpis)
        self.assertEqual(kpis['total_products'], 2)
    
    def test_calculate_all_kpis(self):
        """Test calculating all KPIs"""
        kpis = self.processor.calculate_all_kpis(self.test_df)
        
        self.assertIn('sales', kpis)
        self.assertIn('customers', kpis)
        self.assertIn('products', kpis)


if __name__ == '__main__':
    unittest.main()
