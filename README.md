# KT - Python

This is vinod's new line..

Session that consists of all basic operations.

## Sessions/Topics

- Git
- Python
- Test case - Pytest
- Standards

## How to Document your project
We use pdoc3 library. To install pdoc3,

 ```
 pip install pdoc3
 ```
After pdoc3 is installed, you can just run the below command to generate your document. A folder called 'html' will be generated in which you will have your .html files as documents.
```
pdoc --html .
```

## Sort your imports using isort
Isort package/library is used to sort all your import statements in your projects.
To install isort..
```
pip install isort
```
To run and sort all your imports. Dot (.) represents entire code base.
```
isort [folder/filename.txt] or .
```

## Tune code using black
Black aims for consistency, generality, readability and reducing git diffs.
To install black.
```
pip install black
```
To run black on files.
```
black folder/files
```

## Generate security reports using bandit
Bandit is used to scan files/lines of code in order to check for any security issues in
code base.
To install Bandit.
```
pip install bandit
```
To run bandit on files.
```
bandit {{filename}} or bandit -r {{foldername}}
```
This line is added by Deepak
Another lined added by Deepak
New line added by Ganesh 
