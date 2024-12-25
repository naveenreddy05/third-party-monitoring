class VendorRiskScore:
    def __init__(self):
        self.risk_categories = {
            'security_posture': 0.4,    # 40% weight
            'compliance': 0.3,          # 30% weight
            'access_control': 0.3       # 30% weight
        }
        
    def calculate_security_posture(self, vendor_data):
        """
        Calculate security posture score based on:
        - Security certifications
        - Incident history
        - Security controls
        """
        # Example scoring logic
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