#!/bin/sh
python lib/utils/batch_videos.py --input=/home/uyoung/human_pose_estimation/ROMP/demo/sample_videos --output=/home/uyoung/human_pose_estimation/ROMP/demo/sample_videos_result --extension mp4 --run_conversion --yaml_template=configs/video-batch.yml
python lib/utils/batch_videos.py --input=/home/uyoung/human_pose_estimation/ROMP/demo/coco_train_video --output=/home/uyoung/human_pose_estimation/ROMP/demo/coco_train_video_result --extension avi --run_conversion --yaml_template=configs/video-batch.yml

