import unittest
import os
from src.vendor_risk.metrics import VendorRiskScore
from src.siem_integration.connector import SIEMConnector
from src.reporting.report_generator import ReportGenerator

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.risk_calculator = VendorRiskScore()
        self.siem = SIEMConnector()
        self.reporter = ReportGenerator()

    def test_end_to_end_workflow(self):
        # Test complete workflow
        vendor_id = 'TEST_VENDOR_001'
        
        # 1. Calculate risk score
        vendor_data = {
            'has_iso27001': True,
            'has_soc2': True,
            'security_incidents': 0
        }
        risk_score = self.risk_calculator.get_vendor_risk_score(vendor_data)
        
        # 2. Generate SIEM alert
        alert = self.siem.create_alert(vendor_id, 'SECURITY_SCAN', 'MEDIUM')
        
        # 3. Generate reports
        risk_report = self.reporter.generate_risk_summary(vendor_id)
        alerts_report = self.reporter.generate_alerts_report(vendor_id)
        compliance_report = self.reporter.generate_compliance_report(vendor_id)
        
        # Assertions
        self.assertIsNotNone(risk_score)
        self.assertIsNotNone(alert)
        self.assertTrue(os.path.exists(risk_report))
        self.assertTrue(os.path.exists(alerts_report))
        self.assertTrue(os.path.exists(compliance_report))

    def tearDown(self):
        # Clean up generated files
        for file in os.listdir():
            if file.endswith('.csv'):
                os.remove(file)

if __name__ == '__main__':
    unittest.main()