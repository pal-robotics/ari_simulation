^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
