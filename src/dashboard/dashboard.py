from flask import Flask, render_template, jsonify
from datetime import datetime
from ..vendor_risk.metrics import VendorRiskScore
from ..siem_integration.connector import SIEMConnector

app = Flask(__name__)

class SecurityDashboard:
    def __init__(self):
        self.risk_calculator = VendorRiskScore()
        self.siem = SIEMConnector()
        
    def get_vendor_summary(self, vendor_id):
        """Get vendor risk summary"""
        # Simulate vendor data
        vendor_data = {
            'vendor_id': vendor_id,
            'has_iso27001': True,
            'has_soc2': True,
            'security_incidents': 1,
            'last_assessment_date': datetime.now()
        }
        
        return {
            'risk_score': self.risk_calculator.get_vendor_risk_score(vendor_data),
            'alerts': self.get_recent_alerts(vendor_id),
            'last_assessment': vendor_data['last_assessment_date']
        }
    
    def get_recent_alerts(self, vendor_id):
        """Get recent security alerts"""
        # Simulate alerts
        return [
            {'type': 'Access Violation', 'severity': 'HIGH'},
            {'type': 'Policy Breach', 'severity': 'MEDIUM'}
        ]

@app.route('/dashboard')
def dashboard():
    dashboard = SecurityDashboard()
    data = dashboard.get_vendor_summary('VENDOR001')
    return render_template('index.html', data=data)

@app.route('/api/metrics/<vendor_id>')
def get_metrics(vendor_id):
    dashboard = SecurityDashboard()
    return jsonify(dashboard.get_vendor_summary(vendor_id))

if __name__== '__main__':
    app.run(debug=True)