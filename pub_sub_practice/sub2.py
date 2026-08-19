import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Sub1(Node):
    
    def __init__(self):
        super().__init__('sub1')
        self.subscription = self.create_subscription(
            Int32,
            'topic',
            self.callback,
            10
        )
        
    def callback(self, msg):
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    sub1 = Sub1()
    rclpy.spin(sub1)
    sub1.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
