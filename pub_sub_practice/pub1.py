import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Pub1(Node):
    
    def __init__(self):
        super().__init__('pub1')
        self.publisher = self.create_publisher(Int32, 'topic', 10)
        self.initial_value = 0
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
    def timer_callback(self):
        msg = Int32()
        self.initial_value = self.initial_value + 1
        msg.data = self.initial_value
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    pub1 = Pub1()
    rclpy.spin(pub1)
    pub1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
