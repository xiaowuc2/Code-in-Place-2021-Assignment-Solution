### Code in Place 2021 Diagnostic Solution
```
If this repository helped you please give a star ⭐ and encourage me to solve other problems too.
``` 

Video Explanation : https://youtu.be/u8uqTBNZvAY

<p align="center">
  <a href="https://youtu.be/0IURrcpNZmk">
    <img src="https://github.com/xiaowuc2/xiaowuc2/blob/master/source/ranger-1/youtube%20diagnostic.png" alt="Logo">
  </a>

  <h3 align="center">by [@xiaowuc2](https://github.com/xiaowuc2)</h3>

  <p align="center">
  </p>
</p>


- [Code in Place Filter](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/1.%20Astronaut%20Height%20Test.py)
```
  Write a program that asks the user to enter an image file, loads that file and applies the “Code in Place” filter.

Photo of Stanford Main Quad on a nice day.
Same photo as previous but tinted pinkish purple.
To apply the Code in Place filter, you are going to change every pixel to have the following new red, green and blue values, based off the pixels old red, green and blue values:

new red value = old red value * 1.5
new green value = old green value * 0.7
new blue value = old blue value * 1.5
Problem written by Chris Piech. Inspired by image library and examples from Nick Parlante.
```
- [Finding Forest Flames](https://github.com/xiaowuc2/Code-in-Place-2021-Assignment-Solution/blob/main/Diagnostic/2.%20Even%20Odd%20Table.py)
```
We’re going to start by writing a function called find_flames (in the file forest_fire.py) that highlights the areas where a forest fire is active. You’re given a satellite image of Greenland’s 2017 fires (photo credit: Stef Lhermitte, Delft University of Technology). Your job is to detect all of the “sufficiently red” pixels in the image, which are indicative of where fires are burning in the image. As we did in class with the “redscreening” example, we consider a pixel “sufficiently red” if its red value is greater than or equal to the average of the pixel’s three RGB values times a constant INTENSITY_THRESHOLD. 

Recall that the average of a pixel, which has red, green and blue values is:

average = (red + green + blue) / 3
Two side by side photos of smoke plumes from above. The first photo is a normal image, taken from a satellite, and the right image is the same as the previous except it is black and white and the forest fires are highlighted in red.
Original forest fire image on left, and highlighted version of image on right.

When you detect a “sufficiently red” pixel in the original image, you set its red value to 255 and its green and blue values to 0. This will highlight the pixel by making it entirely red. For all other pixels (i.e., those that are not “sufficiently red”), you should convert them to their grayscale equivalent, so that we can more easily see where the fire is originating from. You can grayscale a pixel by summing together its red, green, and blue values and dividing by three (finding the average), and then setting the pixel’s red, green, and blue values to all have this same “average” value. 

Once you highlight the areas that are on fire in the image (and greyscale all the remaining pixels), you should see an image like that shown on the right in the figure. On the left side of the example image, we should the original image for comparison. 

Note: to make this algorithm work on different images of fire, select an appropriate INTENSITY_THRESHOLD value.

```
