# DragonOS Robot Control System

A comprehensive robotic control system for automated grain bag loading operations, built on ROS3 and DragonOS SDK.

## System Architecture

The system is organized into five main layers:

1. **Data Service Layer**
   - API Gateway for external system integration
   - Logging system for operation monitoring
   - Task management for loading operations

2. **Safety Layer**
   - Real-time monitoring
   - Vo-DE signal conversion
   - Emergency handling

3. **Decision Layer**
   - Central decision making
   - Path planning
   - Dual-layer simulation

4. **Execution Layer**
   - Mechanical operations control
   - Heterogeneous network management
   - LDAK module for dynamic load adaptation

5. **Hardware Layer**
   - Sensor management
   - RK3588 platform control
   - Driver interfaces

## Prerequisites

- Python 3.10+
- ROS2 environment
- DragonOS SDK
- CUDA-compatible GPU (for vision processing)
- NPU support (for machine learning acceleration)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/DragonOS.git
cd DragonOS
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure ROS3 environment:
```bash
source /opt/ros/humble/setup.bash
```

## Usage

1. Start the robot control system:
```bash
python src/main.py
```

2. Monitor system logs:
```bash
ros2 topic echo /robot_system/logs
```

3. Send commands through API:
```bash
curl -X POST http://localhost:8000/api/v1/tasks -d '{"task_type": "load", "quantity": 10}'
```

## Configuration

System configuration can be modified through YAML files in the `config` directory:
- `hardware_config.yaml`: Sensor and platform settings
- `network_config.yaml`: Communication parameters
- `safety_config.yaml`: Safety thresholds and parameters

## Development

To contribute to the project:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions, please open an issue in the GitHub repository or contact the development team.
