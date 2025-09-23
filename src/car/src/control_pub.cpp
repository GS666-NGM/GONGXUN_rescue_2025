#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"
#include "chrono"

using namespace std::chrono_literals;

class ContorllNode: public rclcpp::Node
{
private:
rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher;
rclcpp::TimerBase::SharedPtr timer;

public:
    ContorllNode(const std::string& nodename):Node(nodename)
    {
        publisher = this->create_publisher<geometry_msgs::msg::Twist>("/car_cmd", 10);
        timer = this->create_wall_timer(1000ms, std::bind(&ContorllNode::time_callback, this));
    }

    void time_callback(void)
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 1.0;
        msg.angular.z = 0.5;
        publisher->publish(msg);
    }
    
};


int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ContorllNode>("controll_node");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}