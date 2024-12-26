import csv
from datetime import datetime
from ..vendor_risk.metrics import VendorRiskScore
from ..siem_integration.connector import SIEMConnector
from ..monitoring.siem_cases.use_cases import SIEMUseCases
from ..monitoring.correlation_rules.rules import CorrelationRules
from ..monitoring.threat_detection.detector import ThreatDetector

class ReportGenerator:
    def init(self):
        self.report_types = {
            'risk_summary': self.generate_risk_summary,
            'alerts': self.generate_alerts_report,
            'compliance': self.generate_compliance_report,
            'security_posture': self.generate_security_posture_report  # Added new report type
        }
        self.risk_calculator = VendorRiskScore()
        self.siem_cases = SIEMUseCases()
        self.threat_detector = ThreatDetector()
        self.correlation = CorrelationRules()

    def generate_alerts_report(self, vendor_id):
        """Generate alerts report"""
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
    
    def generate_security_posture_report(self, vendor_id):
        """Generate comprehensive security posture report"""
        report_data = {
            'vendor_id': vendor_id,
            'timestamp': datetime.now(),
            'risk_assessment': self.risk_calculator.get_risk_details(vendor_id),
            'siem_findings': self.siem_cases.get_all_findings(vendor_id),
            'threat_detection': self.threat_detector.get_summary(vendor_id),
            'correlation_analysis': self.correlation.get_analysis(vendor_id)
        }
        
        return self.format_security_posture_report(report_data)

    def save_report_to_csv(self, filename, data):
        """Save report data to CSV file"""
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Metric', 'Value'])
            for key, value in data.items():
                if isinstance(value, list):
                    value = '; '.join(map(str, value))
                writer.writerow([key, str(value)])

    def format_security_posture_report(self, report_data):
        """Format security posture report for better readability"""
        formatted_data = {
            'Vendor ID': report_data['vendor_id'],
            'Timestamp': report_data['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
            'Risk Assessment': report_data['risk_assessment'],
            'SIEM Findings': report_data['siem_findings'],
            'Threat Detection Summary': report_data['threat_detection'],
            'Correlation Analysis': report_data['correlation_analysis']
        }
        filename = f"security_posture_{report_data['vendor_id']}_{datetime.now().strftime('%Y%m%d')}.csv"
        self.save_report_to_csv(filename, formatted_data)
        return filename