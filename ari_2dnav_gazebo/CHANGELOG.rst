^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ari_2dnav_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.0.17 (2022-06-27)
-------------------

0.0.16 (2022-06-09)
-------------------

0.0.15 (2022-05-30)
-------------------
* Merge branch 'ari-v2' into 'ferrum-devel'
  update launch and config files for compatibility with ari-v2
  See merge request robots/ari_simulation!26
* update launch and config files for compatibility with ari-v2
* Contributors: David ter Kuile, davidfernandez

0.0.14 (2022-02-23)
-------------------
* Merge branch 'layered_costmap' into 'ferrum-devel'
  Adapting to the new vo_server
  See merge request robots/ari_simulation!24
* Adapting to the new vo_server
* Contributors: antoniobrandi, saikishor

0.0.13 (2021-11-02)
-------------------

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
* Passing down the laser_model param to localization launch files
* Fix typos
* Rename camera model
* Fixing bug when laser_model false
* laser_filters node runned only if laser_model is not false
* fixed small bug
* Fixed laser_model set default false
* Fixing navigation of the robot in the simulated environment
* Contributors: antoniobrandi, davidfernandez, saikishor

0.0.10 (2021-05-20)
-------------------
* Merge branch 'ari_laser_new' into 'ferrum-devel'
  Ari laser new
  See merge request robots/ari_simulation!20
* navigation using laser scanner
* Rebase
* Merge branch 'ferrum-devel' into 'ari_laser_new'
  # Conflicts:
  #   ari_gazebo/launch/ari_gazebo.launch
  #   ari_gazebo/launch/ari_spawn.launch
* Added laser_model dependencies
* Contributors: antoniobrandi, davidfernandez, sergiomoyano

0.0.9 (2021-04-07)
------------------

0.0.8 (2020-08-31)
------------------
* Merge branch 'spring_cameras' into 'ferrum-devel'
  Add SPRING cameras
  See merge request robots/ari_simulation!16
* Add SPRING cameras
* Contributors: davidfernandez, victor

0.0.7 (2020-07-29)
------------------
* Merge branch 'fix_public_sim' into 'ferrum-devel'
  Use non-ORBSLAM for public sim
  See merge request robots/ari_simulation!15
* Use non-ORBSLAM for public sim
* Contributors: davidfernandez, victor

0.0.6 (2020-06-25)
------------------
* changing default world and localization args
* Contributors: Federico Nardi

0.0.5 (2020-06-02)
------------------
* Merge branch 'slam-toolbox-mapping' into 'ferrum-devel'
  Slam toolbox mapping
  See merge request robots/ari_simulation!13
* Fixes
* Cosmetics
* Set fake-odom to publish at 5 Hz
* Remove advanced navigation section
* Use slam_toolbox for public_sim set to true
* Merge branch 'fake-odom' into 'ferrum-devel'
  Fake odometry publisher for public sim
  See merge request robots/ari_simulation!11
* cosmetic
* Use robot_pose package's fake odom publisher when public_sim is true
* Contributors: Procópio Stein, Sara Cooper, procopiostein

0.0.4 (2020-03-24)
------------------

0.0.3 (2020-03-23)
------------------

0.0.2 (2020-03-13)
------------------
* changelog
* Merge branch 'cleaned-up-ari-simulation' into 'master'
  Cleaned up ari simulation
  See merge request robots/ari_simulation!6
* cleanup
* Fix topics and localization transform frame values
* Add transform_tolerance param for localisation and tf_prefix default for navigation.launch
* Added the public sim and removed the other params not needed
* Merge branch 'cleaned-up-ari-simulation' of https://gitlab/robots/ari_simulation into cleaned-up-ari-simulation
* Added some fixing to the 2dnav_gazebo
* ARI gazebo navigation template
* Contributors: Procópio Stein, Sara Cooper, alessandrodifava, procopiostein, saracooper

* Merge branch 'cleaned-up-ari-simulation' into 'master'
  Cleaned up ari simulation
  See merge request robots/ari_simulation!6
* cleanup
* Fix topics and localization transform frame values
* Add transform_tolerance param for localisation and tf_prefix default for navigation.launch
* Added the public sim and removed the other params not needed
* Merge branch 'cleaned-up-ari-simulation' of https://gitlab/robots/ari_simulation into cleaned-up-ari-simulation
* Added some fixing to the 2dnav_gazebo
* ARI gazebo navigation template
* Contributors: Procópio Stein, Sara Cooper, alessandrodifava, procopiostein, saracooper

0.0.1 (2020-02-10)
------------------
