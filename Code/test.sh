python -W ignore test_models.py somethingv2 \
    --weights=checkpoint/TSM_somethingv2_RGB_resnet50_shift8_blockres_avg_segment8_e10/ckpt.best.pth \
    --test_segments=8 --batch_size=72 -j 24 --test_crops=1

#Project/temporal-shift-module/checkpoint/TSM_somethingv2_RGB_resnet50_shift8_blockres_avg_segment8_e45.pth

#Project/temporal-shift-module/checkpoint/TSM_somethingv2_RGB_resnet50_shift8_blockres_avg_segment8_e10.pth
#Project/temporal-shift-module/checkpoint/TSM_somethingv2_RGB_resnet50_shift8_blockres_avg_segment8_e10/ckpt.best.pth