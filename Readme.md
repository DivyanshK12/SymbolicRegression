## Directory
* GA2.ipynb is the working of GA's on temperature Data
* GA3.ipynb is the working of GA's on Generated Data
* Hubble.ipynb is Symbolic Regression on Hubble Parameter Data (Refer to Reference Material)
* Supernova.ipynb is Symbolic Regression on Supernova Dataset (Refer to Reference Material)
* Model's folder consists of a text file with model output and correponding plot
* The working has been modified over time, original models required user defined functions, which might no longer be available in the code. The processes can be repeated with newer pipeline to obtain more generic results.

These links also available in Help tab in Jupyter notebook if relevant libraries are installed

## Reference Material
* https://arxiv.org/pdf/2002.12700.pdf : For the overall process for GA2 and GA3 
* https://arxiv.org/pdf/1205.0364.pdf : for error analysis theory
* https://arxiv.org/pdf/2002.12700.pdf : For temperature data
* https://arxiv.org/pdf/1910.01529.pdf : For Supernova and Hubble Data

## TODO
* The GA used is based on loosely typed Symbolic Regression methodology, better results possible from Strongly typed approach
* The optimization function, functions that are used in the main algorithm are basic ones used in relevant documentation, better functions/methods specififc to this problem could exist
* Need to check parallel processing features in Deap library. also test the use of Dask Library (Experiment in the Multiprocessing folder for this)

## Requirements
* deap library for genetic algorithms : https://deap.readthedocs.io/en/master/
* numpy for data generation and storage : https://numpy.org/doc/stable/index.html
* pandas for data manipulation : https://pandas.pydata.org/pandas-docs/stable/?v=20210127140625
* scipy for scientific functions : https://docs.scipy.org/doc/scipy/reference/?v=20210127140625
* plotly for plotting : https://plotly.com/python/

### To view the notebooks without cloning the repo visit https://nbviewer.jupyter.org/ and enter the URL of required jupyter notebook
