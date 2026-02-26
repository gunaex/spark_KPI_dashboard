"""
KPI Processor Module
Handles Spark-based processing and calculation of KPIs
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, max, min, stddev
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, TimestampType
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KPIProcessor:
    """
    KPI Processor for calculating various key performance indicators using Spark
    """
    
    def __init__(self, app_name="KPI_Dashboard"):
        """
        Initialize Spark session and KPI Processor
        
        Args:
            app_name (str): Name of the Spark application
        """
        self.spark = SparkSession.builder \
            .appName(app_name) \
            .config("spark.sql.warehouse.dir", "/tmp/spark-warehouse") \
            .getOrCreate()
        
        logger.info(f"Initialized KPIProcessor with Spark session: {app_name}")
    
    def load_data(self, file_path, file_format="csv", header=True):
        """
        Load data from file into Spark DataFrame
        
        Args:
            file_path (str): Path to the data file
            file_format (str): Format of the file (csv, parquet, json)
            header (bool): Whether the CSV file has a header
            
        Returns:
            DataFrame: Spark DataFrame containing the data
        """
        logger.info(f"Loading data from {file_path}")
        
        if file_format == "csv":
            df = self.spark.read.csv(file_path, header=header, inferSchema=True)
        elif file_format == "parquet":
            df = self.spark.read.parquet(file_path)
        elif file_format == "json":
            df = self.spark.read.json(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_format}")
        
        logger.info(f"Loaded {df.count()} rows")
        return df
    
    def calculate_sales_kpis(self, df):
        """
        Calculate sales-related KPIs
        
        Args:
            df: Spark DataFrame with sales data
            
        Returns:
            dict: Dictionary containing calculated KPIs
        """
        logger.info("Calculating sales KPIs")
        
        kpis = {}
        
        # Total revenue
        if "revenue" in df.columns:
            kpis["total_revenue"] = df.agg(sum("revenue")).collect()[0][0]
        
        # Average order value
        if "order_value" in df.columns:
            kpis["average_order_value"] = df.agg(avg("order_value")).collect()[0][0]
        
        # Total transactions
        kpis["total_transactions"] = df.count()
        
        # Average revenue per transaction
        if "revenue" in df.columns:
            kpis["avg_revenue_per_transaction"] = df.agg(avg("revenue")).collect()[0][0]
        
        # Max and min transaction values
        if "order_value" in df.columns:
            kpis["max_order_value"] = df.agg(max("order_value")).collect()[0][0]
            kpis["min_order_value"] = df.agg(min("order_value")).collect()[0][0]
        
        logger.info(f"Calculated {len(kpis)} sales KPIs")
        return kpis
    
    def calculate_customer_kpis(self, df):
        """
        Calculate customer-related KPIs
        
        Args:
            df: Spark DataFrame with customer data
            
        Returns:
            dict: Dictionary containing calculated KPIs
        """
        logger.info("Calculating customer KPIs")
        
        kpis = {}
        
        # Unique customers
        if "customer_id" in df.columns:
            kpis["unique_customers"] = df.select("customer_id").distinct().count()
        
        # Average transactions per customer
        if "customer_id" in df.columns:
            customer_transactions = df.groupBy("customer_id").count()
            kpis["avg_transactions_per_customer"] = customer_transactions.agg(avg("count")).collect()[0][0]
        
        # Customer retention (repeat customers)
        if "customer_id" in df.columns:
            repeat_customers = df.groupBy("customer_id").count().filter(col("count") > 1).count()
            total_customers = df.select("customer_id").distinct().count()
            kpis["customer_retention_rate"] = (repeat_customers / total_customers * 100) if total_customers > 0 else 0
        
        logger.info(f"Calculated {len(kpis)} customer KPIs")
        return kpis
    
    def calculate_product_kpis(self, df):
        """
        Calculate product-related KPIs
        
        Args:
            df: Spark DataFrame with product data
            
        Returns:
            dict: Dictionary containing calculated KPIs
        """
        logger.info("Calculating product KPIs")
        
        kpis = {}
        
        # Top products by revenue
        if "product_id" in df.columns and "revenue" in df.columns:
            top_products = df.groupBy("product_id") \
                .agg(sum("revenue").alias("total_revenue")) \
                .orderBy(col("total_revenue").desc()) \
                .limit(10)
            kpis["top_10_products"] = [(row.product_id, row.total_revenue) for row in top_products.collect()]
        
        # Product diversity
        if "product_id" in df.columns:
            kpis["total_products"] = df.select("product_id").distinct().count()
        
        # Average products per transaction
        if "transaction_id" in df.columns and "product_id" in df.columns:
            products_per_transaction = df.groupBy("transaction_id").agg(count("product_id").alias("product_count"))
            kpis["avg_products_per_transaction"] = products_per_transaction.agg(avg("product_count")).collect()[0][0]
        
        logger.info(f"Calculated {len(kpis)} product KPIs")
        return kpis
    
    def calculate_all_kpis(self, df):
        """
        Calculate all available KPIs from the dataframe
        
        Args:
            df: Spark DataFrame
            
        Returns:
            dict: Dictionary containing all calculated KPIs
        """
        logger.info("Calculating all KPIs")
        
        all_kpis = {
            "sales": self.calculate_sales_kpis(df),
            "customers": self.calculate_customer_kpis(df),
            "products": self.calculate_product_kpis(df)
        }
        
        logger.info("All KPIs calculated successfully")
        return all_kpis
    
    def stop(self):
        """Stop the Spark session"""
        logger.info("Stopping Spark session")
        self.spark.stop()
