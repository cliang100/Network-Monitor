# Network Topology Monitor & Alert System

A network monitoring system that tracks node connectivity, detects failures, and visualizes network topology with real-time alerts.

## Features

- **Network Discovery**: Monitors connectivity to multiple network nodes
- **Failure Detection**: Automatically detects when nodes go offline
- **Topology Visualization**: Shows network layout and connection status
- **Real-time Alerts**: Sends notifications when failures occur
- **Impact Analysis**: Shows which downstream services are affected

## Tech Stack

- **Python**: Monitoring script with ping and metrics collection
- **Prometheus**: Time-series metrics storage
- **Grafana**: Data visualization and alerting
- **Docker Compose**: Container orchestration
- **JSON**: Network topology definition

## Architecture

```
┌─────────────┐
│  Monitor    │  ← Python script that pings nodes
└─────────────┘
       │
       ▼
┌─────────────┐    ┌─────────────┐
│  Prometheus  │───▶│  Grafana     │  ← Visualization & alerts
│  (Metrics)   │    │  (Dashboard)  │
└─────────────┘    └─────────────┘
       │                    ▲
       └────────────────────┘
              Network Topology (JSON)
```

## Quick Start

1. **Start services**:
   ```bash
   docker-compose up -d
   ```

2. **Access Grafana**:
   - Open http://localhost:3000
   - Default: admin/admin

3. **View Prometheus**:
   - Open http://localhost:9090
   - Metrics at http://localhost:9090/metrics

## Network Topology Format

The `topology.json` file defines:

```json
{
  "nodes": [
    {
      "id": "unique-id",
      "name": "Human-readable name",
      "ip": "192.168.1.x",
      "type": "server|router|database",
      "status": "online|offline"
    }
  ],
  "connections": [
    {
      "from": "node-id",
      "to": "node-id", 
      "type": "ethernet|fiber"
    }
  ]
}
```

## Usage Examples

### Adding a new node:
```bash
# Edit topology.json to add:
{
  "nodes": [
    // ... existing nodes ...
    {
      "id": "new-server",
      "name": "New Web Server",
      "ip": "192.168.1.50",
      "type": "server",
      "status": "online"
    }
  ],
  "connections": [
    // ... existing connections ...
    {
      "from": "router-1",
      "to": "new-server",
      "type": "ethernet"
    }
  ]
}
```

### Monitoring commands:
```bash
# Check all nodes
python monitor.py check

# Check specific node
python monitor.py check server-1

# Start continuous monitoring
python monitor.py monitor

# Get affected services
python monitor.py impact server-1
```

## Components

- **topology.json**: Network definition file
- **monitor.py**: Python monitoring script
- **prometheus.yml**: Prometheus configuration
- **docker-compose.yml**: Service orchestration
- **Grafana Dashboard**: Real-time visualization

## Interview Talking Points

**Network Monitoring Concepts:**
- "I built a system that monitors network topology using JSON configuration"
- "Uses Prometheus for metrics collection and Grafana for visualization"
- "Implements ping-based health checks with configurable intervals"
- "Shows downstream impact analysis when nodes fail"

**Technical Implementation:**
- "Python script loads topology from JSON and pings each node"
- "Exposes metrics endpoint for Prometheus scraping"
- "Docker Compose orchestrates the monitoring stack"
- "Grafana dashboard displays real-time network status"

**Learning Outcomes:**
- "Gained experience with Docker and containerization"
- "Learned Prometheus metrics format and Grafana configuration"
- "Practiced network programming concepts and topology analysis"
- "Built end-to-end monitoring solution from scratch"