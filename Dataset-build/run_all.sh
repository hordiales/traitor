#python rotate_img.py $GRAIN_DATASET 270
python 1_process_features.py $GRAIN_DATASET
python 2_read_yolo_tag_and_append.py "${GRAIN_DATASET}_measurements.csv" $GRAIN_DATASET
python 3_filter_csv.py "${GRAIN_DATASET}_measurements_with_YOLO.csv"
