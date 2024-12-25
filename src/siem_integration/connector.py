import datetime
import json

class SIEMConnector:
    def __init__(self):
        self.alert_levels = {
            'HIGH': 1,
            'MEDIUM': 2,
            'LOW': 3
        }
        
    def create_alert(self, vendor_id, alert_type, severity):
        """Create a security alert"""
        alert = {
            'vendor_id': vendor_id,
            'timestamp': datetime.datetime.now().isoformat(),
            'alert_type': alert_type,
            'severity': severity,
            'status': 'NEW'
        }
        
        # Save alert to file (simulating database)
        self.save_alert(alert)
        return alert
    
    def save_alert(self, alert):
        """Save alert to JSON file"""
        try:
            with open('alerts.json', 'a') as f:
                json.dump(alert, f)
                f.write('\n')
        except Exception as e:
            print(f"Error saving alert: {e}")