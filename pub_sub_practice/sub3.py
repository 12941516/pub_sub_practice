import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Sub3(Node):
    
    def __init__(self):
        super().__init__('sub3')
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
    sub3 = Sub3()
    rclpy.spin(sub3)
    sub3.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
