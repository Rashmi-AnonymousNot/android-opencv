# Android OpenCV

## Description
A demonstration of the OpenCV library, updated to work with Requests. Most other repos I found with this info used the older `urllib`, and made heavy use of deprecaited functions that broke the code when used in python 3.0 and above.

Basically, this is an update to Python 3.x and part 1 of a tutorial on live image recognition using OpenCV and tensorflow in Python. (You will not need tensorflow for this portion of the tutorial.)

## Dependencies

- [Python 3.x](https://www.python.org/) 
- [OpenCV](https://opencv.org/) 
- [Requests](http://docs.python-requests.org/en/master/#),  the only Non-GMO HTTP library for Python, safe for human consumption.
- [IPWebcam Android app](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en)

## Getting Started

0. (Optional) I **strongly** recommend using a virtual enviornment like [Anaconda](https://www.anaconda.com/distribution/) for development. While it is not necessary, it prevents interference with any other python installations, and will be required for the latter portions of this tutorial. Once installed, the enviornment can be created and opened like so:

    ```console
    $ conda create -n androidCV pip python=3.5
    Solving enviornment: done

    $ activate androidCV
    ```

1. Make sure you have Python 3.0 or higher installed on your computer 
    ```console
    $ python -V
    Python 3.5.5 :: Anaconda, Inc.
    ```

2. Install OpenCV version 3.x
    ```console
    $ conda install -c conda-forge opencv
    ```

3. Install Requests
    ```console
    $ conda install -c anaconda requests 
    ```
4. Install IPWebcam on your phone

5. Clone this repository
    ```console
    $ git clone https://github.com/njohnsoncpe/android-opencv.git /path/to/dir/
    ```
6. Make sure that the phone and the computer are on the same Wifi network

## How to Use

Start the webcam server on your phone and take note of the ip address at the bottom of the screen, you will need that to run the program.

The syntax of the program call is as follows:

    ```console
    $ python ipcam.py -ip [ipaddr] -usr [username] -pass [password]
    ```

## Part 2 to follow soon.