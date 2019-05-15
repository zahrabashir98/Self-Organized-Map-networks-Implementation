# Kohonen (SOM) Implenetation
We want to viualize 3D input (rgb) into 2D using SOM network.

**The program uses two different methods to extract colors:**
* K-means clustering to spit the image in RGB color space to the n_colors clusters. The cluster mean points are selected as colors in the palette.  
* Kohonen Self-Organizing Map (SOM). Random selection of original image pixels are given to the SOM algorithm, which then maps them to a n_colors x n_colors two-dimensional palette. 

I have three files containg `main.py` `processing.py` and `som.py`
you only have to start with `main.py` 
the `som.py` contains the main class of SOM which the logic of SOM networks is implemented there
the `prcessing.py` contains the other details of converting which you can see in the code(the have comments :D)
# Test Results
The results of my program are attached to testcases folder

## How To run:
Start with `main.py` and put your image link in the img_link:
select n_colors which can be any number you want but in this homework it is 40 (40*40 = 1600)
If you wanna give the rgb numbers directly into a list goto `peocessing.py` in the sownload_image function and set this value `no_download = False`
In this way you can give the data manually
## Efficiency
Because it was really boring and took alot of memory I set the `no_download` flag to false and directly convert image to numpy array( not python list which is terrible) and that makes my program efficent

## Dependencies

#### you need to have the follwoing libraries:
* numpy
* pandas
* matplotlib (for visualization)
* sklearn.cluster( for kMean)
* sklearn.utils (for shuffle)
* mpl_toolkits.mplot3d(3D display)
* PIL (pillow for images)
* pickle
* scipy
* multiprocessing (used in som.py)

### Notice:
Run with Python3

