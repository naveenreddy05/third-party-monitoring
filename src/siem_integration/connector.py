from datetime import datetime
import json
import os

class SIEMConnector:
    def __init__(self):
        self.alert_levels = {
            'HIGH': 1,
            'MEDIUM': 2,
            'LOW': 3
        }
        self.alerts_file = 'data/alerts.json'
        self._ensure_data_directory()

    def _ensure_data_directory(self):
        """Ensure data directory exists"""
        os.makedirs(os.path.dirname(self.alerts_file), exist_ok=True)

    def get_vendor_data(self, vendor_id):
        """Get vendor SIEM data"""
        return {
            'vendor_id': vendor_id,
            'access_logs': self._get_access_logs(vendor_id),
            'security_events': self._get_security_events(vendor_id),
            'high_risk_indicators': 0,
            'medium_risk_indicators': 1
        }

    def _get_access_logs(self, vendor_id):
        """Get vendor access logs"""
        return []  # Implement actual log retrieval

    def _get_security_events(self, vendor_id):
        """Get vendor security events"""
        return []  # Implement actual event retrieval

    def create_alert(self, vendor_id, alert_type, severity):
        """Create a security alert"""
        alert = {
            'vendor_id': vendor_id,
            'timestamp': datetime.now().isoformat(),
            'alert_type': alert_type,
            'severity': severity,
            'status': 'NEW'
        }
        self.save_alert(alert)
        return alert

    def save_alert(self, alert):
        """Save alert to JSON file"""
        try:
            alerts = self._load_alerts()
            alerts.append(alert)
            with open(self.alerts_file, 'w') as f:
                json.dump(alerts, f, indent=2)
        except Exception as e:
            print(f"Error saving alert: {e}")

    def _load_alerts(self):
        """Load existing alerts"""
        try:
            if os.path.exists(self.alerts_file):
                with open(self.alerts_file, 'r') as f:
                    return json.load(f)
            return []
        except Exception as e:
            print(f"Error loading alerts: {e}")
            return []

    def get_recent_alerts(self, vendor_id, limit=10):
        """Get recent alerts for vendor"""
        alerts = self._load_alerts()
        vendor_alerts = [a for a in alerts if a['vendor_id'] == vendor_id]
        return sorted(vendor_alerts, key=lambda x: x['timestamp'], reverse=True)[:limit]