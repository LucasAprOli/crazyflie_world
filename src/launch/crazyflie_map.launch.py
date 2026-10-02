import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('crazyflie_map')
    world_path = os.path.join(pkg_share, 'worlds', 'meu_mapa.world')
    models_path = os.path.join(pkg_share, 'models')

    gazebo_ros_share = get_package_share_directory('gazebo_ros')

    # Configura dinamicamente a variavel GAZEBO_MODEL_PATH
    existing_model_path = os.environ.get('GAZEBO_MODEL_PATH', '')
    if existing_model_path:
        new_model_path = f'{existing_model_path}:{models_path}'
    else:
        new_model_path = models_path

    return LaunchDescription(
        [
            SetEnvironmentVariable('GAZEBO_MODEL_PATH', new_model_path),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(
                        gazebo_ros_share, 'launch', 'gazebo.launch.py'
                    )
                ),
                launch_arguments={'world': world_path}.items(),
            ),
        ]
    )