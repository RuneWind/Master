# CMake generated Testfile for 
# Source directory: /Users/runewind/Documents/GitHub/Master/object detection/opencv-3.4.15/modules/highgui
# Build directory: /Users/runewind/Documents/GitHub/Master/object detection/build_opencv/modules/highgui
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_highgui "/Users/runewind/Documents/GitHub/Master/object detection/build_opencv/bin/opencv_test_highgui" "--gtest_output=xml:opencv_test_highgui.xml")
set_tests_properties(opencv_test_highgui PROPERTIES  LABELS "Main;opencv_highgui;Accuracy" WORKING_DIRECTORY "/Users/runewind/Documents/GitHub/Master/object detection/build_opencv/test-reports/accuracy" _BACKTRACE_TRIPLES "/Users/runewind/Documents/GitHub/Master/object detection/opencv-3.4.15/cmake/OpenCVUtils.cmake;1686;add_test;/Users/runewind/Documents/GitHub/Master/object detection/opencv-3.4.15/cmake/OpenCVModule.cmake;1292;ocv_add_test_from_target;/Users/runewind/Documents/GitHub/Master/object detection/opencv-3.4.15/modules/highgui/CMakeLists.txt;168;ocv_add_accuracy_tests;/Users/runewind/Documents/GitHub/Master/object detection/opencv-3.4.15/modules/highgui/CMakeLists.txt;0;")
