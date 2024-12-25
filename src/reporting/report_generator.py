import csv
from datetime import datetime

class ReportGenerator:
    def __init__(self):
        self.report_types = {
            'risk_summary': self.generate_risk_summary,
            'alerts': self.generate_alerts_report,
            'compliance': self.generate_compliance_report
        }
    
    def generate_report(self, report_type, vendor_id):
        """Generate specified report type"""
        if report_type in self.report_types:
            return self.report_types[report_type](vendor_id)
        raise ValueError(f"Unknown report type: {report_type}")
    
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
        
        # Save report
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
                    value = '; '.join(value)
                writer.writerow([key, value])