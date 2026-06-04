# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice core text-processing skills in Python by working with strings, reading and writing text files, and building reusable text manipulation functions.

## 📝 Tasks

### 🛠️ Build String Utility Functions

#### Description
Create small functions that clean and analyze text. Use string methods to normalize casing, remove extra whitespace, and count useful text metrics.

#### Requirements
Completed program should:

- Implement a function that takes a string and returns a cleaned version (trimmed and lowercase)
- Implement a function that returns the number of words and characters in a string
- Implement a function that replaces a target word or phrase with a new value


### 🛠️ Process a Text File and Save Results

#### Description
Read text from a provided file, apply your string utility functions, and write a short report to an output file.

#### Requirements
Completed program should:

- Read the file `sample-text.txt` using file I/O (`open`, `read`)
- Print a summary that includes line count, word count, and most common word
- Write the transformed text and summary to a new file named `analysis-report.txt`
- Handle missing file errors gracefully (for example, with `try`/`except`)
