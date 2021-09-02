import os
from os import path
from glob import glob

from tqdm import tqdm

import ipdb

sample_videos_dir = path.join('..', 'demo', 'sample_videos')
sample_videos_output_dir = sample_videos_dir + '_result'
coco_videos_dir = path.join('..', 'demo', 'coco_train_video')
coco_videos_output_dir = coco_videos_dir + '_result'

if not path.exists(sample_videos_output_dir):
    os.makedirs(sample_videos_output_dir)
if not path.exists(coco_videos_output_dir):
    os.makedirs(coco_videos_output_dir)

sample_video_paths = glob(path.join(sample_videos_dir, '*.mp4'))
coco_video_paths = glob(path.join(coco_videos_dir, '*.avi'))
total_video_paths = sample_video_paths + coco_video_paths

sample_video_output_paths = [sample_videos_output_dir for _ in range(len(sample_video_paths))]
coco_video_output_paths = [coco_videos_output_dir for _ in range(len(coco_video_paths))]
total_output_paths = sample_video_output_paths + coco_video_output_paths

yml_raw_path = path.join('configs', 'video.yml')
yml_data = None
with open(yml_raw_path, 'r') as f:
    yml_data = f.readlines()

yml_paths = []
for video_path, output_path in zip(total_video_paths, total_output_paths):
    tmp_yml = yml_data.copy()
    tmp_yml[19] = f' input_video_path: {video_path}\n'
    tmp_yml[20] = f' output_dir: {output_path}\n'

    ext = '.mp4'
    if video_path.find('.avi')!=-1:
        ext = '.avi'
    tmp_yml_path = video_path.replace(ext, '.yml')
    yml_paths.append(tmp_yml_path)
    with open(tmp_yml_path, 'w') as f:
        f.write(''.join(tmp_yml))

for yml_path in tqdm(yml_paths):
    os.system(f'CUDA_VISIBLE_DEVICES=0 python core/test.py --gpu=0 --configs_yml={yml_path}')

print("Finished")
