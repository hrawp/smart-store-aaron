# smart-store-aaron
#
Project 4

I had to change file paths to get the dw file in the correct location while still have the etl_to_dw.py in scripts folder.
I had to change the name of the columns.  I'm not sure if that is correct or not, but that worked for me.
I had to update the columns for the additional columns I had made.



Project 3
## Scripts used
```
data_prep.py  This script can be used for data cleaning
```
```
data_scrubber.py  This script holds the indvidual clean methods and called by data_prep.py
```
```
test_data_scrubber.py  This script can be used for testing cleaning programs.
```


# 
Project 2
## How to Install and Run the Project

Create a new repo in Git Hub.  Make sure to include README when creating the new repo.

Clone the new repo to your machine.
```
git clone https://github.com/hrawp/smart-store-aaron
```

Add a .gitignore file with:
# Python virtual environment
'.venv/'

# Visual Studio Code settings and workspace
'.vscode/'

added so .venv files will not be sent up to your repo.

Create a virtual environement by running this command
```
python -m venv .venv
```

Activate the environment by running this command
```
.\.venv\Scripts\activate
```

Update the requirements.txt with libraries that need to be installed.



Run the three Git commands to stange and transmit files to GitHub
```
git add .
```
```
git commit -m "initial commit"
```
```
git push origin main
```


