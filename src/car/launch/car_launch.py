import launch
import launch_ros
from ament_index_python.packages import get_package_share_directory #找目录
import os

def generate_launch_description():
    #获取share路径
    pkg_path = get_package_share_directory('myrobort')
    xacro_path = os.path.join(pkg_path,'urdf','robot.urdf.xacro')
    declare_path = launch.actions.DeclareLaunchArgument(
        name='model',
        default_value = xacro_path,
    )
    default_rviz_config_path = os.path.join(pkg_path, 'config','rviz_config.rviz')

    #获取路径的内容
    path_content = launch.substitutions.Command(['xacro ', launch.substitutions.LaunchConfiguration('model')])
    
    #把内容转换成参数
    robot_description_param = launch_ros.parameter_descriptions.ParameterValue(path_content, value_type=str)

    #启动robot_state_publisher节点 和 joint_state_publisher节点
    action_robot_state_publisher = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description_param}]
    )
    action_joint_state_publisher = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher'
    )

    action_rvisz2 = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', default_rviz_config_path]
        
    )

    return launch.LaunchDescription([
        declare_path,
        action_robot_state_publisher,
        action_joint_state_publisher,
        action_rvisz2
    ])