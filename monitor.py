import json
import time
import subprocess
import requests
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class MetricsHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/metrics':
            # Load topology and check nodes
            with open('topology.json', 'r') as f:
                topology = json.load(f)
            
            metrics = []
            for node in topology['nodes']:
                # Ping the node
                try:
                    result = subprocess.run(['ping', '-n', '1', node['ip']], 
                                          capture_output=True, text=True, timeout=5)
                    status = 'online' if result.returncode == 0 else 'offline'
                    
                    # Update node status
                    if status != node.get('status', 'unknown'):
                        node['status'] = status
                        node['lastChecked'] = datetime.now().isoformat()
                    
                    metrics.append(f'node_status{{id="{node["id"]}",status="{status}"}} 1')
                    
                except:
                    metrics.append(f'node_status{{id="{node["id"]}",status="error"}} 1')
            
            # Return Prometheus metrics format
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; version=0.0.4')
            self.end_headers()
            self.wfile.write('\n'.join(metrics).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def main():
    port = 8000
    server = HTTPServer(('0.0.0.0', port), MetricsHandler)
    print(f"Network monitor running on port {port}")
    print("Metrics available at: http://localhost:8000/metrics")
    server.serve_forever()

if __name__ == '__main__':
    main()