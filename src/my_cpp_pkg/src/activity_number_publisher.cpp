#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/msg/Int64.hpp"

using namespace std::chrono_literals;

class PublisherNode : public rclcpp::Node
{
public:
    PublisherNode() : Node("number_publisher")
    {
        publisher_ = this->create_publisher<example_interfaces::msg::Int64>("number", 10);
        timer_ = this->create_wall_timer(0.5s, std::bind(&PublisherNode::publishNumber, this));
        RCLCPP_INFO(this->get_logger(), "Publisher Node has been activated");
    }
private:
    void publishNumber()
    {
        auto msg = example_interfaces::msg::Int64();
        msg.data = 42; 
        publisher_->publish(msg);
    }
    std::string number;
    rclcpp::publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PublisherNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}