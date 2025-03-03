#!/usr/bin/env python3
"""
Main entry point for the Robot Control System.
Initializes and coordinates all system layers.
"""

import rclpy
from rclpy.node import Node

from data_service import APIGateway, LoggingSystem, TaskManager
from safety import SafetyMonitor, VoDEConverter
from decision import DecisionCenter
from execution import MechanicalControl, HeterogeneousNetwork
from hardware import SensorManager, RKS58BPlatform

class RobotControlSystem(Node):
    def __init__(self):
        super().__init__('robot_control_system')
        
        # Initialize all layers
        self.api_gateway = APIGateway()
        self.logging_system = LoggingSystem()
        self.task_manager = TaskManager()
        
        self.safety_monitor = SafetyMonitor()
        self.vo_de_converter = VoDEConverter()
        
        self.decision_center = DecisionCenter()
        
        self.mechanical_control = MechanicalControl()
        self.network = HeterogeneousNetwork()
        
        self.sensor_manager = SensorManager()
        self.platform = RKS58BPlatform()
        
        self.get_logger().info('Robot Control System initialized')
        
    def run(self):
        """Main control loop"""
        try:
            while rclpy.ok():
                # Process sensor data
                sensor_data = self.sensor_manager.get_data()
                
                # Safety checks
                if not self.safety_monitor.check_safety(sensor_data):
                    self.handle_emergency()
                    continue
                
                # Process tasks
                tasks = self.task_manager.get_pending_tasks()
                for task in tasks:
                    # Generate decision
                    decision = self.decision_center.process_task(task)
                    
                    # Execute decision
                    self.mechanical_control.execute(decision)
                    
                    # Log execution
                    self.logging_system.log_task_execution(task, decision)
                
                rclpy.spin_once(self)
                
        except Exception as e:
            self.get_logger().error(f'Error in main loop: {str(e)}')
            self.handle_emergency()
    
    def handle_emergency(self):
        """Handle emergency situations"""
        self.mechanical_control.emergency_stop()
        self.logging_system.log_emergency()
        self.api_gateway.notify_emergency()

def main():
    rclpy.init()
    robot_system = RobotControlSystem()
    
    try:
        robot_system.run()
    except KeyboardInterrupt:
        pass
    finally:
        robot_system.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main() 