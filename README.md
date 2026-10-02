# crazyflie_world

Repositório para implementar mundo em ROS 2 para testes com o drone Crazyflie 2.1+.

Rodando no **Ubuntu 22**.

## Passo a Passo

```bash
colcon build
source install/setup.bash
ros2 launch crazyflie_map crazyflie_map.launch.py
