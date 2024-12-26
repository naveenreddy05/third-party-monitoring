import unittest
from datetime import datetime
from src.dashboard.dashboard import SecurityDashboard

class TestSecurityDashboard(unittest.TestCase):
    def setUp(self):
        self.dashboard = SecurityDashboard()
        self.test_vendor_id = 'TEST001'

    def test_vendor_summary(self):
        summary = self.dashboard.get_vendor_summary(self.test_vendor_id)
        
        # Check basic structure
        self.assertIn('risk_score', summary)
        self.assertIn('alerts', summary)
        self.assertIn('compliance_status', summary)
        self.assertIn('threat_analysis', summary)
        
        # Check risk score structure
        self.assertIsInstance(summary['risk_score'], dict)
        self.assertIn('overall_score', summary['risk_score'])
        self.assertIn('breakdown', summary['risk_score'])

    def test_compliance_status(self):
        summary = self.dashboard.get_vendor_summary(self.test_vendor_id)
        compliance = summary['compliance_status']
        
        self.assertIn('score', compliance)
        self.assertIn('weight', compliance)
        self.assertIn('frameworks', compliance)
        self.assertIsInstance(compliance['frameworks'], list)

    def test_security_posture(self):
        summary = self.dashboard.get_vendor_summary(self.test_vendor_id)
        posture = summary['security_posture']
        
        self.assertIn('score', posture)
        self.assertIn('weight', posture)
        self.assertIn('findings', posture)

    def test_alerts(self):
        alerts = self.dashboard._get_recent_alerts(self.test_vendor_id)
        self.assertIsInstance(alerts, list)
        if alerts:
            alert = alerts[0]
            self.assertIn('level', alert)
            self.assertIn('type', alert)
            self.assertIn('timestamp', alert)
            self.assertIn('details', alert)

if __name__ == '__main__':
    unittest.main()