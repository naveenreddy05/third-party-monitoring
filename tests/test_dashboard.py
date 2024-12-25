import unittest
from src.dashboard.dashboard import SecurityDashboard

class TestSecurityDashboard(unittest.TestCase):
    def setUp(self):
        self.dashboard = SecurityDashboard()
    
    def test_vendor_summary(self):
        summary = self.dashboard.get_vendor_summary('TEST001')
        self.assertIn('risk_score', summary)
        self.assertIn('alerts', summary)
        self.assertTrue(isinstance(summary['alerts'], list))

if __name__ == '__main__':
    unittest.main()