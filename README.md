# Data Encoding Detection Utility

Welcome to the Data Encoding Detection Utility repository! This utility helps detect the encoding of text files, which is useful when dealing with data files that may have different character encodings. If you've encountered the "UnicodeDecodeError" while trying to read data into pandas, this utility can help you identify the correct encoding and avoid such errors.

## Introduction

When working with text data, it's essential to know the correct encoding to interpret the characters properly. However, determining the encoding of a text file can be challenging, especially when dealing with files that have unknown or mixed encodings.

This utility provides a simple function to detect the encoding of a text file, making it easier to read the data into pandas or other data processing tools without encountering encoding-related errors.

## Functionality

The `encoding()` function in this utility takes the path to a text file as input and returns a dictionary containing the detected encoding and the language of the text. This information can then be used to read the data into pandas or perform other text processing tasks.

Here's how to use the `encoding()` function:
To use this utility, simply copy the encoding() function into your Python script or import it as a module. Then, call the function with the path to your text file to detect the encoding.

Feel free to customize the function or integrate it into your data processing pipeline as needed.

Special thanks to the charset_normalizer library for providing an easy-to-use solution for detecting text encoding
