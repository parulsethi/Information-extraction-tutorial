# SciPy 2018 Information Extraction Tutorial

This repository will contain the teaching material and other info associated with the **Information Extraction using Topic Models** tutorial at SciPy US 2018.

## Obtaining the Tutorial Material

If you have a GitHub account, you can clone (or fork) the repository by running:
```
git clone https://github.com/parulsethi/Information-extraction-tutorial.git
```
If you are not familiar with git or don’t have a GitHub account, you can download the repository as a zip file by going to the GitHub repository (https://github.com/parulsethi/Information-extraction-tutorial) in the browser and click the “Download” button on the upper right corner.

Please note that there maybe some updates in the content until shortly before the tutorial session and it is recommended to update your copy of the material one day before the tutorial. If you cloned the repository via git, you can sync your existing local repository with:
```
git pull origin master
```
Or alternatively, re-download the zip file from GitHub.


## Dataset

Download the following datasets for the tutorial: 
- [Kaggle's fake news data](https://www.kaggle.com/mrisdal/fake-news) 
- [NIPS Conference Papers](https://cs.nyu.edu/~roweis/data/nips12raw_str602.tgz)


## Installation Notes

- Install the dependencies using `pip install -r requirements.txt`
- Install the [DTM code](https://github.com/blei-lab/dtm) 
- Excecute `check_env.py` by running:
```
python check_env.py
```
- The tutorial code has been tested for Python 3.6



To run the notebooks, execute:
```
jupyter notebook --NotebookApp.iopub_data_rate_limit=1.0e10
```