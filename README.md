# Python-cv2-fast-thinning-algorithm
Implementation of a fast thinning algorithm using morphology

Background:
I have been looking for fast thinning algorithms to to use in the determination of fingerprint minutiae, but I didn't find any and OpenCV appers to have none either. I have been working with Zhang Suen, it generates great results, but it is too slow for my usage, so I started developing my own algorithm and want to make it available to the community and hope the community can contribute with hints on how to make the results better and the algorithm even faster. ;)

Current state:
At the current implementation the thinning of the example image is done in less than 1.4s without showing the images and about 1.6s showing the images.

Details of the input image:
1. Image should be binary.
2. I am using the areas of interest as black (value 0) and background as white (value 255), but if needed I can work with the opposite.

Details of the result image:
1. Returns the same image with the edges of the area of interest substituted by background color.

Rules of the result image:
1. Should not break connections.
2. interest areas should be 1 pixel wide.
3. Small branches are undesired.

Download everything and run example.py to try out yourself! (python 2.x and cv2 needed)

Feel free to contact me with questions or sugestions. (lucassilvaennes@gmail.com)

Happy coding! :)
