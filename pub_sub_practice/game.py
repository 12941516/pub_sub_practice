import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String

class Game(Node):
    
    def __init__(self):
        super().__init__('game')
        self.subscription = self.create_subscription(
            String,
            'user_item',
            self.callback,
            10
        )
        self.machine_item_list = ['rock', 'paper', 'scissors']
        
    def callback(self, msg):
        user_item = msg.data
        machine_item = random.randint(0, 2)
        self.get_logger().info(f'User item: {user_item}')
        
        if machine_item == 0:   # machine = rock
            self.get_logger().info(f'Machine item: {self.machine_item_list[machine_item]}')
            if user_item == 'rock':     # same
                self.get_logger().info(f'same\n')
            elif user_item == 'paper':  # user win
                self.get_logger().info(f'user win\n')
            else:                       # machine win
                self.get_logger().info(f'machine win\n')
                
        elif machine_item == 1: # machine = paper
            self.get_logger().info(f'Machine item: {self.machine_item_list[machine_item]}')
            if user_item == 'rock':     # machine win
                self.get_logger().info(f'machine win\n')
            elif user_item == 'paper':  # same
                self.get_logger().info(f'same\n')
            else:                       # user win
                self.get_logger().info(f'user\n')
        
        else:                   # machine = scissors
            self.get_logger().info(f'Machine item: {self.machine_item_list[machine_item]}')
            if user_item == 'rock':     # user win
                self.get_logger().info(f'user win\n')
            elif user_item == 'paper':  # machine win
                self.get_logger().info(f'machine win\n')
            else:                       # same
                self.get_logger().info(f'same\n')

def main(args=None):
    rclpy.init(args=args)
    game = Game()
    rclpy.spin(game)
    game.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
