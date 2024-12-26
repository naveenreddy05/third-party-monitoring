from flask import Flask, render_template, redirect
from datetime import datetime
from src.dashboard.dashboard import SecurityDashboard
from src.monitoring.threat_detection.detector import ThreatDetector
from src.siem_integration.connector import SIEMConnector

app = Flask(__name__, template_folder='dashboard/templates')

@app.route('/')
def home():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    security_dashboard = SecurityDashboard()
    vendor_id = 'VENDOR001'
    
    # Get comprehensive vendor data
    vendor_summary = security_dashboard.get_vendor_summary(vendor_id)
    
    # Get real-time monitoring data
    siem = SIEMConnector()
    threat_detector = ThreatDetector()
    
    siem_data = siem.get_vendor_data(vendor_id)
    threat_analysis = threat_detector.analyze_vendor_activity(vendor_id, siem_data)
    
    monitoring_data = {
        'real_time_alerts': siem.get_recent_alerts(vendor_id),
        'threat_analysis': threat_analysis,
        'security_posture': {
            'score': vendor_summary['security_posture']['score'],
            'last_updated': datetime.now().isoformat(),
            'findings': [
                {'type': 'Unauthorized Access', 'severity': 'HIGH'},
                {'type': 'Configuration Issue', 'severity': 'MEDIUM'},
                {'type': 'Policy Violation', 'severity': 'LOW'}
            ]
        },
        'compliance_status': vendor_summary['compliance_status']
    }
    
    dashboard_data = {
        'vendor_name': f'Vendor {vendor_id}',
        'last_assessment': datetime.now(),
        'risk_score': vendor_summary['risk_score']['overall_score'],
        'risk_details': {
            'security_posture': {
                'score': vendor_summary['security_posture']['score'],
                'weight': 0.4
            },
            'compliance': {
                'score': vendor_summary['compliance_status']['score'],
                'weight': 0.3
            },
            'access_control': {
                'score': 60.0,
                'weight': 0.3
            }
        },
        'alerts': [
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
        ],
        'monitoring': monitoring_data
    }
    
    return render_template('index.html', data=dashboard_data)

if __name__ == '__main__':
    app.run(debug=True)