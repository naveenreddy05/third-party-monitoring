from datetime import datetime
from ..monitoring.risk_calculator import VendorRiskScore
from ..siem_integration.connector import SIEMConnector
from ..monitoring.siem_cases.use_cases import SIEMUseCases
from ..monitoring.correlation_rules.rules import CorrelationRules
from ..monitoring.threat_detection.detector import ThreatDetector

class SecurityDashboard:
    def __init__(self):
        self.risk_calculator = VendorRiskScore()
        self.siem = SIEMConnector()
        self.siem_cases = SIEMUseCases()
        self.correlation = CorrelationRules()
        self.threat_detector = ThreatDetector()
        self.vendor_data = {}  # Cache for vendor data

    def get_vendor_summary(self, vendor_id):
        """Get comprehensive vendor security summary"""
        vendor_data = self._get_vendor_data(vendor_id)
        siem_data = self.siem.get_vendor_data(vendor_id)
        threat_data = self.threat_detector.analyze_vendor_activity(vendor_id, siem_data)
        
        return {
            'vendor_id': vendor_id,
            'timestamp': datetime.now().isoformat(),
            'risk_score': self._calculate_risk_score(vendor_data),
            'security_posture': self._get_security_posture(vendor_id),
            'alerts': self._get_recent_alerts(vendor_id),
            'compliance_status': self._get_compliance_status(vendor_id),
            'threat_analysis': threat_data
        }

    def _calculate_risk_score(self, vendor_data):
        """Calculate overall risk score"""
        risk_factors = vendor_data['risk_factors']
        weights = {
            'security_posture': 0.4,
            'compliance': 0.3,
            'access_control': 0.3
        }
        
        overall_score = (
            risk_factors['security_posture'] * weights['security_posture'] +
            risk_factors['compliance'] * weights['compliance'] +
            risk_factors['access_control'] * weights['access_control']
        )
        
        return {
            'overall_score': round(overall_score, 1),
            'breakdown': {
                'security_score': risk_factors['security_posture'],
                'compliance_score': risk_factors['compliance'],
                'access_score': risk_factors['access_control']
            }
        }

    def _get_vendor_data(self, vendor_id):
        """Retrieve vendor data from cache or database"""
        if vendor_id not in self.vendor_data:
            # Simulate data fetch and risk calculation
            self.vendor_data[vendor_id] = {
                'name': f'Vendor_{vendor_id}',
                'risk_factors': self._calculate_risk_factors(vendor_id),
                'last_assessment': datetime.now().isoformat()
            }
        return self.vendor_data[vendor_id]

    def _calculate_risk_factors(self, vendor_id):
        """Calculate vendor risk factors"""
        # These values would normally be calculated based on actual vendor data
        return {
            'security_posture': 65.0,  # Example security posture score
            'compliance': 100.0,       # Example compliance score
            'access_control': 60.0     # Example access control score
        }

    def _get_security_posture(self, vendor_id):
        """Get vendor security posture details"""
        siem_findings = self.siem_cases.get_findings(vendor_id)
        correlation_results = self.correlation.analyze_vendor(vendor_id)
        
        return {
            'score': 65.0,
            'weight': 40.0,
            'findings': siem_findings,
            'correlation_analysis': correlation_results,
            'last_updated': datetime.now().isoformat()
        }
    def _get_recent_alerts(self, vendor_id):
        """Get recent security alerts for vendor"""
        # These would normally come from your SIEM system
        return [
            {
                'level': 'HIGH',
                'type': 'Access Violation',
                'timestamp': datetime.now().isoformat(),
                'details': 'Unauthorized access attempt detected'
            },
            {
                'level': 'MEDIUM',
                'type': 'Policy Breach',
                'timestamp': datetime.now().isoformat(),
                'details': 'Non-compliant configuration detected'
            },
            {
                'level': 'LOW',
                'type': 'Failed Login Attempt',
                'timestamp': datetime.now().isoformat(),
                'details': 'Multiple failed login attempts detected'
            }
        ]

    def _get_compliance_status(self, vendor_id):
        """Get vendor compliance status"""
        return {
            'score': 100.0,
            'weight': 30.0,
            'frameworks': ['ISO27001', 'GDPR', 'NIST CSF'],
            'last_audit': datetime.now().isoformat(),
            'findings': self._get_compliance_findings(vendor_id)
        }

    def _get_compliance_findings(self, vendor_id):
        """Get detailed compliance findings"""
        return {
            'total_controls': 100,
            'compliant': 95,
            'non_compliant': 5,
            'critical_findings': 0,
            'last_assessment': datetime.now().isoformat()
        }

    def update_vendor_data(self, vendor_id, new_data):
        """Update vendor data in cache"""
        if vendor_id in self.vendor_data:
            self.vendor_data[vendor_id].update(new_data)
            return True
        return False

    def clear_vendor_cache(self, vendor_id=None):
        """Clear vendor cache for specific vendor or all vendors"""
        if vendor_id:
            self.vendor_data.pop(vendor_id, None)
        else:
            self.vendor_data.clear()