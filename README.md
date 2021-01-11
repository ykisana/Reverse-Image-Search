# Shopify Developer Internship Challenge - Summer 2021
 
Image repository with reverse image search and single/bulk photo additions. Implemented in Python using OpenCV

## How to use
1. Open run.py, this will take you to the proper prompts
2. Select if you would like to add images to the repository, do a search or terminate
3. Enter prompted paths

## Image Addition
The user has the option to add a singular image or bulk images. When a single image is to be added, it simply copies the file to the "images" directory. For  bulk it will copy all images in the specified folder to our "images" folder.

Everytime an image is added, it's feature is calculated and indexed for Image Search use.

## Reverse Image Search
For the reverse Image Search, a feature representing the colour mapping for each image is excracted. All the features are stored in a csv file. When a search is performed, all the features are compared, the closest 10 are displayed. The comparison is done through a chi-squared distance.

All the features are either computed at the first run of a program or when new images are added.

Modified the [pyimagesearch.com](https://www.pyimagesearch.com/2014/12/01/complete-guide-building-image-search-engine-python-opencv/) guide to implement reverse image search.









