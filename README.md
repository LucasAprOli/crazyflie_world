# crazyflie_world
Repositório para implementar mundo em Ros2 para testes com o drone crazyflie 2.1+

rodando no Ubuntu 22
- colcon build
- source install/setup.bash

- export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$PWD/install/meu_mapa_gazebo/share/meu_mapa_gazebo/models
- ros2 launch gazebo_ros gazebo.launch.py "world:=$PWD/install/meu_mapa_gazebo/share/meu_mapa_gazebo/worlds/meu_mapa.world"
