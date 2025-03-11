# AOTL - App On The Line
## Run Apps Without Permanently Downloading Them

This is a project built in python to run EXEs from their github URL.
It is NOT meant for running large applications. Instead, it can be used to run small EXE files that you only need to run once.

Using this to run large applications ( > 200 mb ) can cause problems like really long loading times, and decreased lifespan of your storage device.

## How To Use

To run the program, you need to have a ( .aotl ) file. upload the file to a github repo and copy the link non-raw link.

Open the command line from the directory where you have downloaded the file and write the following command: 'python runner.py ( your link here)' and the program will run.

## The ( .aotl ) File

The ( .aotl ) file is a json file that contains the name, version, author, install link and domain name ( a substitute for the url that is automatically registered once you run the app, you can type just the domain of the app and it will run ).

The format for the ( .aotl ) file is as follows:

    "name : "",

    "version": "",

    "author": "",

    "domain": "",

    "exe": ""


The name, version, author fields are yet to be implemented in the app, and will show up in the CLI in the future. they all are optional.

The domain and exe fields, on the other hand, are necessary for the working of the program.

