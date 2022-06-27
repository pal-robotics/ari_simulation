^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_controller_configuration_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.17 (2022-06-27)
-------------------

0.0.16 (2022-06-09)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  Add params for caster wheel joints in v2
  See merge request robots/ari_simulation!27
* Add params for caster wheel joints in v2
* Contributors: Luca Marchionni, davidfernandez

0.0.15 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  update launch and config files for compatibility with ari-v2
  See merge request robots/ari_simulation!26
* update launch and config files for compatibility with ari-v2
* Contributors: David ter Kuile, davidfernandez

0.0.14 (2022-02-23)
-------------------

0.0.13 (2021-11-02)
-------------------

0.0.12 (2021-08-19)
-------------------

0.0.11 (2021-07-28)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Fixing navigation of the robot in the simulated environment
  See merge request robots/ari_simulation!21
* Fix typos
* Fixed laser_model set default false
* Contributors: antoniobrandi, davidfernandez, saikishor

0.0.10 (2021-05-20)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Ari laser new
  See merge request robots/ari_simulation!20
* Added laser_model dependencies
* Merge branch 'ferrum-devel' into 'ari_laser_new'
  # Conflicts:
  #   ari_gazebo/launch/ari_gazebo.launch
  #   ari_gazebo/launch/ari_spawn.launch
* Added laser_model dependencies
* Contributors: davidfernandez, sergiomoyano

0.0.9 (2021-04-07)
------------------

0.0.8 (2020-08-31)
------------------

0.0.7 (2020-07-29)
------------------

0.0.6 (2020-06-25)
------------------

0.0.5 (2020-06-02)
------------------
* Use robot_pose package's fake odom publisher when public_sim is true
* Fake odometry to base footprint publisher
* Contributors: Sara Cooper

0.0.4 (2020-03-24)
------------------
* Merge branch 'ari_end_effector' into 'ferrum-devel'
  Ari end effector
  See merge request robots/ari_simulation!7
* improve fingers pid values
* Separate hands
* Add param for en_effector
* Contributors: YueErro, davidfernandez

0.0.3 (2020-03-23)
------------------
* Merge branch 'fix-deps' into 'ferrum-devel'
  added playmotion and actionlib deps
  See merge request robots/ari_simulation!9
* added playmotion and actionlib deps
* Contributors: Procópio Stein, procopiostein

0.0.2 (2020-03-13)
------------------
* Merge branch 'cleaned-up-ari-simulation' into 'master'
  Cleaned up ari simulation
  See merge request robots/ari_simulation!6
* cleanup
* Clean up by removing unecessary parts
* Contributors: Procópio Stein, procopiostein, saracooper

0.0.1 (2020-02-10)
------------------
* Merge branch 'actuated_forearm_sim' into 'master'
  Actuated forearm sim
  See merge request robots/ari_simulation!3
* add controllers and pid gain for hand
* Merge branch 'realsense_plugin' into 'master'
  Realsense plugin
  See merge request robots/ari_simulation!2
* fix the issue with the PIDs in simulation
* added play_motion and moveit launch files to simulation
* Fixed the config files after the adding of the arms in the URDF
* Fixed cameras topics and mobile base config file
* Added the extra joints for the caster
* Fixed bugs
* Initial commit
* Contributors: Luca Marchionni, Sai Kishor Kothakota, Victor Lopez, alessandrodifava
