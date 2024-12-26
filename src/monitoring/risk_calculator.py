class VendorRiskScore:
    def __init__(self):
        self.weight_security = 0.4
        self.weight_compliance = 0.3
        self.weight_access = 0.3

    def calculate_risk_score(self, vendor_data):
        """Calculate overall risk score"""
        security_score = self._calculate_security_score(vendor_data['security_controls'])
        compliance_score = self._calculate_compliance_score(vendor_data['compliance_data'])
        access_score = self._calculate_access_score(vendor_data['access_logs'])

        return {
            'overall_score': self._weighted_average([
                (security_score, self.weight_security),
                (compliance_score, self.weight_compliance),
                (access_score, self.weight_access)
            ]),
            'security_score': security_score,
            'compliance_score': compliance_score,
            'access_score': access_score
        }

    def _calculate_security_score(self, controls):
        """Calculate security controls score"""
        return 65.0  # Implement actual calculation

    def _calculate_compliance_score(self, compliance_data):
        """Calculate compliance score"""
        return 100.0  # Implement actual calculation

    def _calculate_access_score(self, access_logs):
        """Calculate access control score"""
        return 60.0  # Implement actual calculation

    def _weighted_average(self, scores_and_weights):
        """Calculate weighted average"""
        total = sum(score * weight for score, weight in scores_and_weights)
        return round(total, 1)