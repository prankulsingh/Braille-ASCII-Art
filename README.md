
# Braille ASCII Art

So what this does is convert an image to braille ascii art.

basically, converts this 

![original][original] 

to 

![ok][ok]

pretty cool, huh?

## Dependencies
Python 2.7
pip install opencv-python --user

Run as: ```python img.py <image file name> <scaled size 0-100> <threshold 0-255> <invert image 0 or 1>```

```image file name```: Name of image file to convert

```scaled size```: Large images usually convert to huge chunks of text which are not usable anywhere. If you want to share on reddit/whatsapp/9gag etc, you should scale down the image to the point where converted text's width is less than comment section's width, otherwise a single line will overflow into next line, creating a mess.

![smol][smol]
![ok][ok]
![big][big]

```threshold```: So the image is first converted into a grayscale image. Each pixel has a value between 0-255 (inclusive), 0 being the blackest and 255 being the whitest, with about 2_50 shades of grey_ in between. This value decides upto which value should a single pixel should be considered black, and after which point should it be considered white.

![t1][t1]
![t2][t2]
![ok][ok]
![t3][t3]
![t4][t4]

```invert image```: This is very important. It inverts the flips the black and white dots in braille output. In case you are using light mode (white background) instead of dark mode (black background), you should invert the image for it to look better. Just generate both, with this being set to 0 and 1 and see for yourself which one looks better.

![invert][invert]

_This script is written for python 2.7, because I wrote it a long time ago. Would probably work with python 3 with minimal changes. You can make necessary changes to run in python 3 if you want. I'll make changes and push it in future._

[original]: https://i.imgur.com/JzyWINv.png
[ok]: https://i.imgur.com/82xTjYw.png.png
[t1]: https://i.imgur.com/qgNA9ND.png
[t2]: https://i.imgur.com/0jf6lf9.png
[t3]: https://i.imgur.com/kvYPY5p.png
[t4]: https://i.imgur.com/oDNywuh.png
[smol]: https://i.imgur.com/QPWtFR2.png
[big]: https://i.imgur.com/l0osvun.png
[invert]: https://i.imgur.com/DJ6VHhZ.png
