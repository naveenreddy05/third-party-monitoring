class VendorRiskScore:
    def __init__(self):
        self.risk_categories = {
            'security_posture': 0.4,    # 40% weight
            'compliance': 0.3,          # 30% weight
            'access_control': 0.3       # 30% weight
        }
        
    def calculate_security_posture(self, vendor_data):
        """Calculate security posture score"""
        score = 0
        
        # Check for security certifications
        if vendor_data.get('has_iso27001'):
            score += 30
        if vendor_data.get('has_soc2'):
            score += 20
            
        # Check incident history
        incidents = vendor_data.get('security_incidents', 0)
        if incidents == 0:
            score += 30
        elif incidents <= 2:
            score += 15
            
        return min(score, 100)  # Cap at 100

    def calculate_compliance_score(self, vendor_data):
        """Calculate compliance score"""
        score = 0
        
        # Check compliance factors
        if vendor_data.get('has_iso27001'):
            score += 40  # ISO 27001 compliance
            
        if vendor_data.get('has_soc2'):
            score += 30  # SOC 2 compliance
            
        # Add basic compliance score
        score += 30
        
        return min(score, 100)  # Cap at 100

    def calculate_access_score(self, vendor_data):
        """Calculate access control score"""
        score = 70  # Base score
        
        # Reduce score based on security incidents
        incidents = vendor_data.get('security_incidents', 0)
        score -= (incidents * 10)
        
        return max(0, min(score, 100))  # Keep between 0 and 100
    
    def get_vendor_risk_score(self, vendor_data):
        """Calculate overall vendor risk score"""
        scores = {
            'security_posture': self.calculate_security_posture(vendor_data),
            'compliance': self.calculate_compliance_score(vendor_data),
            'access_control': self.calculate_access_score(vendor_data)
        }
        
        # Calculate weighted average
        total_score = 0
        for category, score in scores.items():
            weight = self.risk_categories[category]
            total_score += score * weight
            
        return round(total_score, 2)

    def get_risk_details(self, vendor_data):
        """Get detailed risk breakdown"""
        return {
            'security_posture': {
                'score': self.calculate_security_posture(vendor_data),
                'weight': self.risk_categories['security_posture']
            },
            'compliance': {
                'score': self.calculate_compliance_score(vendor_data),
                'weight': self.risk_categories['compliance']
            },
            'access_control': {
                'score': self.calculate_access_score(vendor_data),
                'weight': self.risk_categories['access_control']
            },
            'overall_score': self.get_vendor_risk_score(vendor_data)
        }