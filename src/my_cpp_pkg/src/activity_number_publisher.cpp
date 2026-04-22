#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/int64.hpp"

using namespace std::chrono_literals;

class NumberPublisherNode : public rclcpp::Node
{
public:
    int number_;
    NumberPublisherNode() : Node("number_publisher"), number_(5)
    {
        number_publisher = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        timer_ = this->create_wall_timer(0.5s, std::bind(&NumberPublisherNode::publishNumber, this));
        RCLCPP_INFO(this->get_logger(), "Publisher Node has been activated");
    
    }
private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = number_; 
        number_publisher->publish(msg);
    }
    int number;
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr number_publisher;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<NumberPublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}