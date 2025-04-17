# Wildlife_Image_Classification

## License

This project is licensed under the [MIT License](https://opensource.org/license/MIT).



## FILE STRUCTURE

Wildlife_Image_Classification
├──analysis
│   └──analysis.ipynb
├──competition_host_files
│   ├──data
│   │   ├──training_features.zip
│   │   │  └──training_images
│   │   ├──test_features.zip
│   │   │ └──test_images
│   │   ├──test_features.csv
│   │   ├──train_features.csv
│   │   └──train_labels.csv
│   └──samples
│       ├──submission_format.csv
│       └──benchmark.ipynb


Wildlife Image Classification

analysisanalysis.ipynb: Jupyter Notebook for data analysis and modeling.competition_host_filesdatatraining_features.zip:  ZIP archive of training image features.training_images/: Directory containing training images.test_features.zip: ZIP archive of test image features.test_images/: Directory containing test images.test_features.csv: CSV file containing test image features.train_features.csv: CSV file containing training image features.train_labels.csv: CSV file containing training labels.samplessubmission_format.csv:  CSV file showing the required submission format.benchmark.ipynb:  Jupyter Notebook providing a benchmark solution.


competition_host_file folder contains all files provided by competion host ie [DRIVENDATA](https://www.drivendata.org/competitions/87/competition-image-classification-wildlife-conservation/)

## GETING STARTED
`conda create -n conda-img python=3.11`
`conda activate conda-img`
`conda install ipykernel`
`python -m ipykernel install --user --name conda-img --display-name "Python(conda-img)"`
