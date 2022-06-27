^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.17 (2022-06-27)
-------------------
* Merge branch 'nominal-extrinsics-fix' into 'ferrum-devel'
  set nominal extrinsics to true for public sim
  See merge request robots/ari_simulation!28
* change parameter name
* set nominal extrinsics to true for public sim
* Contributors: saikishor, saracooper

0.0.16 (2022-06-09)
-------------------

0.0.15 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  update launch and config files for compatibility with ari-v2
  See merge request robots/ari_simulation!26
* update pal_robot_info with robot_model
* update launch and config files for compatibility with ari-v2
* Contributors: David ter Kuile, davidfernandez

0.0.14 (2022-02-23)
-------------------

0.0.13 (2021-11-02)
-------------------
* Merge branch 'thermal-camera' into 'ferrum-devel'
  add has thermal param
  See merge request robots/ari_simulation!23
* add has thermal param
* Contributors: Sara Cooper, davidfernandez

0.0.12 (2021-08-19)
-------------------
* Merge branch 'separate-spring-cameras' into 'ferrum-devel'
  Separate spring_cameras parameter in two params
  See merge request robots/ari_simulation!22
* Separate spring_cameras parameter in two params
* Contributors: davidfernandez, saikishor

0.0.11 (2021-07-28)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Fixing navigation of the robot in the simulated environment
  See merge request robots/ari_simulation!21
* Rename camera model
* Fixed laser_model set default false
* Contributors: antoniobrandi, davidfernandez, saikishor

0.0.10 (2021-05-20)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Ari laser new
  See merge request robots/ari_simulation!20
* Update ari_gazebo/launch/ari_spawn.launch
* Update ari_gazebo/launch/simulation_ari_bringup.launch
* Rebase
* Added laser_model dependencies
* Rebase
* Change to support sick-571 laser in ari3
* Merge branch 'ferrum-devel' into 'ari_laser_new'
  # Conflicts:
  #   ari_gazebo/launch/ari_gazebo.launch
  #   ari_gazebo/launch/ari_spawn.launch
* Added laser_model dependencies
* Added laser_model dependencies
* Change to support sick-571 laser in ari3
* Contributors: Software Engineer, davidfernandez, sergiomoyano

0.0.9 (2021-04-07)
------------------
* Merge branch 'head-realsense' into 'ferrum-devel'
  Add camera model parameter to set Head Rgb or RGBD camera
  See merge request robots/ari_simulation!18
* change param to camera model
* Add head realsense camera param
* Contributors: Sara Cooper, davidfernandez

0.0.8 (2020-08-31)
------------------
* Add ari_rgbd_sensors dependency
* Merge branch 'spring_cameras' into 'ferrum-devel'
  Add SPRING cameras
  See merge request robots/ari_simulation!16
* Add SPRING cameras
* Contributors: Victor Lopez, davidfernandez, victor

0.0.7 (2020-07-29)
------------------

0.0.6 (2020-06-25)
------------------

0.0.5 (2020-06-02)
------------------
* Merge branch 'slam-toolbox-mapping' into 'ferrum-devel'
  Slam toolbox mapping
  See merge request robots/ari_simulation!13
* Publish rgbd scan or registered color based on public sim
* Correct TF and rgbd_scan publications
* Merge branch 'fake-odom' into 'ferrum-devel'
  Fake odometry publisher for public sim
  See merge request robots/ari_simulation!11
* cosmetic
* Use robot_pose package's fake odom publisher when public_sim is true
* Merge branch 'depth-registered-topic' into 'ferrum-devel'
  Add launch of depth-image-proc
  See merge request robots/ari_simulation!10
* updated call to launch file for depth registration
* Add launch of depth-image-proc
* Contributors: Procópio Stein, Sara Cooper, federiconardi, procopiostein

0.0.4 (2020-03-24)
------------------
* Merge branch 'ari_end_effector' into 'ferrum-devel'
  Ari end effector
  See merge request robots/ari_simulation!7
* Separate hands
* Add param for en_effector
* Contributors: davidfernandez

0.0.3 (2020-03-23)
------------------

0.0.2 (2020-03-13)
------------------
* Merge branch 'cleaned-up-ari-simulation' into 'master'
  Cleaned up ari simulation
  See merge request robots/ari_simulation!6
* cleanup
* Fix topics and localization transform frame values
* Launch rgbd_cloud_laser to enable mapping
* Clean up by removing unecessary parts
* Contributors: Procópio Stein, Sara Cooper, procopiostein, saracooper

0.0.1 (2020-02-10)
------------------
* Merge branch 'remove-pal-throttle' into 'master'
  Remove pal throttle and models/worlds folders
  See merge request robots/ari_simulation!5
* Add pal_throttle package if public_sim:=false
* Remove folders moldels and worlds
* Comment pal_pcl_points_throttle_and_filter
* Merge branch 'realsense_plugin' into 'master'
  Realsense plugin
  See merge request robots/ari_simulation!2
* added realsense gazebo plugin dependency
* Fixed the config files after the adding of the arms in the URDF
* Fixed cameras topics and mobile base config file
* Initial commit
* Contributors: Sai Kishor Kothakota, Victor Lopez, alessandrodifava, saracooper
