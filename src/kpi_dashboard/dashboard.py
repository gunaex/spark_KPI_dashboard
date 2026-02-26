"""
Dashboard Module
Provides web-based visualization for KPIs using Flask
"""

from flask import Flask, render_template, jsonify
import plotly.graph_objs as go
import plotly.utils
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Dashboard:
    """
    Dashboard class for visualizing KPIs using Flask and Plotly
    """
    
    def __init__(self, kpis=None, host='0.0.0.0', port=5000):
        """
        Initialize Dashboard
        
        Args:
            kpis (dict): Dictionary containing calculated KPIs
            host (str): Host address for the Flask app
            port (int): Port number for the Flask app
        """
        self.app = Flask(__name__, template_folder='templates')
        self.kpis = kpis or {}
        self.host = host
        self.port = port
        
        # Setup routes
        self._setup_routes()
        
        logger.info("Dashboard initialized")
    
    def _setup_routes(self):
        """Setup Flask routes"""
        
        @self.app.route('/')
        def index():
            """Main dashboard page"""
            return render_template('index.html', kpis=self.kpis)
        
        @self.app.route('/api/kpis')
        def get_kpis():
            """API endpoint to get KPIs as JSON"""
            return jsonify(self.kpis)
        
        @self.app.route('/api/charts/sales')
        def sales_chart():
            """Generate sales KPI chart"""
            if 'sales' not in self.kpis:
                return jsonify({"error": "No sales data available"})
            
            sales_kpis = self.kpis['sales']
            
            # Create bar chart for sales metrics
            metrics = []
            values = []
            
            for key, value in sales_kpis.items():
                if isinstance(value, (int, float)):
                    metrics.append(key.replace('_', ' ').title())
                    values.append(value)
            
            fig = go.Figure(data=[
                go.Bar(x=metrics, y=values, marker_color='lightblue')
            ])
            
            fig.update_layout(
                title='Sales KPIs',
                xaxis_title='Metric',
                yaxis_title='Value',
                template='plotly_white'
            )
            
            return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        
        @self.app.route('/api/charts/customers')
        def customer_chart():
            """Generate customer KPI chart"""
            if 'customers' not in self.kpis:
                return jsonify({"error": "No customer data available"})
            
            customer_kpis = self.kpis['customers']
            
            # Create pie chart for customer metrics
            labels = []
            values = []
            
            for key, value in customer_kpis.items():
                if isinstance(value, (int, float)):
                    labels.append(key.replace('_', ' ').title())
                    values.append(value)
            
            fig = go.Figure(data=[
                go.Pie(labels=labels, values=values)
            ])
            
            fig.update_layout(
                title='Customer KPIs',
                template='plotly_white'
            )
            
            return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    def update_kpis(self, kpis):
        """
        Update KPIs in the dashboard
        
        Args:
            kpis (dict): New KPI dictionary
        """
        self.kpis = kpis
        logger.info("KPIs updated in dashboard")
    
    def run(self, debug=False):
        """
        Run the Flask dashboard application
        
        Args:
            debug (bool): Run in debug mode
        """
        logger.info(f"Starting dashboard on {self.host}:{self.port}")
        self.app.run(host=self.host, port=self.port, debug=debug)
