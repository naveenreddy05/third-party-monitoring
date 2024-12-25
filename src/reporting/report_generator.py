import csv
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.report_types = {
            'risk_summary': self.generate_risk_summary,
            'alerts': self.generate_alerts_report,
            'compliance': self.generate_compliance_report
        }
    
    def generate_alerts_report(self, vendor_id):
        """Generate alerts report"""
        # Simulate alerts data
        alerts_data = {
            'vendor_id': vendor_id,
            'timestamp': datetime.now(),
            'alerts': [
                {'type': 'Security Breach', 'severity': 'HIGH'},
                {'type': 'Access Violation', 'severity': 'MEDIUM'}
            ]
        }
        
        filename = f"alerts_{vendor_id}_{datetime.now().strftime('%Y%m%d')}.csv"
        self.save_report_to_csv(filename, alerts_data)
        return filename

    def generate_compliance_report(self, vendor_id):
        """Generate compliance report"""
        # Simulate compliance data
        compliance_data = {
            'vendor_id': vendor_id,
            'timestamp': datetime.now(),
            'compliance_status': 'Compliant',
            'frameworks': ['ISO27001', 'SOC2']
        }
        
        filename = f"compliance_{vendor_id}_{datetime.now().strftime('%Y%m%d')}.csv"
        self.save_report_to_csv(filename, compliance_data)
        return filename

    def generate_risk_summary(self, vendor_id):
        """Generate risk summary report"""
        # Simulate report data
        report_data = {
            'vendor_id': vendor_id,
            'timestamp': datetime.now(),
            'risk_score': 85,
            'findings': [
                'Missing security controls',
                'Delayed patch management',
                'Incomplete access logs'
            ]
        }
        
        filename = f"risk_summary_{vendor_id}_{datetime.now().strftime('%Y%m%d')}.csv"
        self.save_report_to_csv(filename, report_data)
        return filename
    
    def save_report_to_csv(self, filename, data):
        """Save report data to CSV file"""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Metric', 'Value'])
            for key, value in data.items():
                if isinstance(value, list):
                    value = '; '.join(map(str, value))
                writer.writerow([key, str(value)])