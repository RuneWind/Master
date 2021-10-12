#!/bin/zsh
# source /opt/anaconda3/etc/profile.d/conda.sh
# conda activate master
# opencv_version
opencv_traincascade -data trained_classifiers -vec test_data_200.vec -bg bg.txt -numPos 180 -numNeg 1800 -numStages 10 -numThreads 12 -precalcValBufSize 4096 -precalcIdxBufSize 4096 -w 27 -h 27 -acceptanceRatioBreakValue 0.0001 -featureType LBP # -mode ALL