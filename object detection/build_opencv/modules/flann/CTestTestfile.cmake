# CMake generated Testfile for 
# Source directory: /Users/runewind/Documents/GitHub/Master/object detection/opencv/modules/flann
# Build directory: /Users/runewind/Documents/GitHub/Master/object detection/build_opencv/modules/flann
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_flann "/Users/runewind/Documents/GitHub/Master/object detection/build_opencv/bin/opencv_test_flann" "--gtest_output=xml:opencv_test_flann.xml")
set_tests_properties(opencv_test_flann PROPERTIES  LABELS "Main;opencv_flann;Accuracy" WORKING_DIRECTORY "/Users/runewind/Documents/GitHub/Master/object detection/build_opencv/test-reports/accuracy" _BACKTRACE_TRIPLES "/Users/runewind/Documents/GitHub/Master/object detection/opencv/cmake/OpenCVUtils.cmake;1738;add_test;/Users/runewind/Documents/GitHub/Master/object detection/opencv/cmake/OpenCVModule.cmake;1352;ocv_add_test_from_target;/Users/runewind/Documents/GitHub/Master/object detection/opencv/cmake/OpenCVModule.cmake;1110;ocv_add_accuracy_tests;/Users/runewind/Documents/GitHub/Master/object detection/opencv/modules/flann/CMakeLists.txt;2;ocv_define_module;/Users/runewind/Documents/GitHub/Master/object detection/opencv/modules/flann/CMakeLists.txt;0;")