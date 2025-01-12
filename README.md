# color_detection
This code detects color based on hue .

**Requirement** :

Numpy

OpenCV-Python

Pillow



Util file has a get_limit function that finds Hue limits for specified color(yellow in my case)

Main file mask the other colors and uses pillow to draw rectangular bounding box sround the yellow objects.
