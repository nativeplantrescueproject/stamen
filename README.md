# stamen

## Note on photo extraction recommendations:
- Recommended to use the Google Earth Desktop app to allow for high-res image downloads
- Eye altitude: ca. 600m
- Ideal base image resolution: ca. 2300x1300
- Map layer mode: "Clean" (no labels)
- 3D Building Mode: off

## Manual Collection of Ideal Training Data:
- Using the parameters above, open the image in an editor and crop squares of targeted areas to an image of 256x256 pixels
- Try to crop in a way that excludes artificial markers or anything else that might signal an antipattern 
- Alternatively, you can put the raw photo in 'raw', and let the script take care of it. You might lose control of where it crops though.

## Image folder definitions:
 - **raw**: Initial starting point for newly downloaded photos. From here, they get gridded up and moved to **unseen**
 - **unseen**: staging area for the trained model to iterate over
 - **training_input**: put processed photos that are desirable in 'positive' and not in 'negative'

## TODO:
 - Model doesn't function at the moment :)
 - Need to determine how to properly mark areas of interest -- include confidence on pic?
 - Likely need to track coordinates?