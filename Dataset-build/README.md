# Build Seeds Dataset

30 samples from https://github.com/hellodfan/GrainSpace

The GrainSpace dataset is licensed under the Creative Commons BY-NC-SA 4.0 license. Note that All data must not be used for commercial purposes.

Tagging [label-img](https://github.com/HumanSignal/labelImg) using YOLO format

Features calculation

Warning: In this process. It is assumed that there is only one entity per image 

	$ cd Dataset-build

	$ conda activate agro 

	$export GRAIN_DATASET="SojaBinario" 
	$export GRAIN_DATASET="MaizTest" 
	
	(optional) 270 degrees rotate (EXIF Metadata)
	$ python rotate_img.py $GRAIN_DATASET 270 
	
	$ python 1_process_features.py $GRAIN_DATASET

	$ python 2_read_yolo_tag_and_append.py "${GRAIN_DATASET}_measurements.csv" $GRAIN_DATASET

	$ python 3_filter_csv.py "${GRAIN_DATASET}_measurements_with_YOLO.csv" 

Last step takes only one row for each image, taking the most similar bounding box between hand-made tagging and automated one.

# Example Dataset

30 samples extracted from
https://github.com/hellodfan/GrainSpace

The GrainSpace dataset is licensed under the Creative Commons BY-NC-SA 4.0 license. Note that All data must not be used for commercial purposes.

Tagged using [label-img](https://github.com/HumanSignal/labelImg)



# GCP config
	gcloud init

	gcloud auth configure-docker

	gcloud builds submit --tag gcr.io/[]/my-traitor-image . 

After the build:
You can verify this by checking the list of images in GCR:
	gcloud container images list --repository=[gcr.io/[PROJECT_ID]](http://gcr.io/%5BPROJECT_ID%5D)


	gcloud run deploy my-traitor-service [params]

Then:
	gcloud builds submit --config cloudbuild.yaml . # enables layer cache, speeds up docker image building


## Job details

## Minimum requirements

mem: 4GiB ?
cpu: 2 ?


TODO: to be evaluated

## Define env vars on GCP config:

then:
	bucket_name = os.getenv('BUCKET_NAME', 'default-bucket-name')



## Download processed dataset
gsutil -m cp -r \
  "gs://[bucketname]-dataset/output" \
  .
