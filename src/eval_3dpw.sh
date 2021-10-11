# 3DPW Challenge
CUDA_VISIBLE_DEVICES=0 python lib/evaluation/collect_3DPW_results.py --gpu=0 --configs_yml=configs/eval_3dpw_challenge.yml

# 3DPW test
CUDA_VISIBLE_DEVICES=0 python core/benchmarks_evaluation.py --gpu=0 --configs_yml=configs/eval_3dpw_test.yml
