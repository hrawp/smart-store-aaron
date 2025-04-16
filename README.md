# smart-store-aaron
#
# Project 6 - The Promotion


## Section 1. The Business Goal
The business would like to know how its use of promotional codes and its impact on sales.  They would like to know what codes were used most and what products were purchased.
## Section 2. Data Source
I used my data warehouse that we have been working on in this class.
promotion_code, sale_amount, name, product_name
## Section 3. Tools
I felt I had enough options in PowerBI to complete the assessment.
## Section 4. Workflow & Logic
I needed multiple ways to show the data to the user. Promotion Code was used to show in different charts along with some other data points.  

Here are some examples.

![Overall View](image-5.png)
![Filter on LASTSALE](image-6.png)
![Filter into Quarter 2](image-7.png)
![Fitler on Hoodie](image-8.png)

## Section 5. Results

In Q1 the 16FORLESS promotion code had the highest sales. 
![Q1 16FORLESS](image-9.png)

In Q2 the 16FORLESS promotion code had the highest sales.
![Q2 16FORLESSt](image-11.png)

In Q3 LASTSALE and 16FORLESS promotion codes had almost the same amount of sales at 9K and 8.7 k with KEEP promotion code close with 8k in sales.
![Q3 LASTSALE](image-10.png)

Q4 just had two sales with the 16FORLESS promotion code used once for a 5.6k sale.

Overall the main two promotional codes were LASTSALE and 16FORLESS. LASTSALE then ALLDAY4 were the Promotional codes used the most.

Laptops were the highest sale item with 8 sold under the 16FORLESS Promotion code.
![16FORLESS Laptops](image-12.png)


There were a realtively small amount of orders anaylazed, 94.  But for this sample we can recommend some actions.

Section 6: Suggested Business Action 
I would suggest removing laptops from 16FORLESS promotion code.  The promotion code could still be used on other sales, but I would remove it to keep more profit on those sales.
That may rasie the question what about the other for promotional codes.  I would say limit the precentage discount on laptops or exclude them all together.

Section 7. Challenges
I was somewhat divided whether I should use a python OLAP or POWER BI with OLAP.  I decided to go with PowerBI for P6 since I felt it had all the tools and views necessary.  This includes the slice and dice through the data to help answer the buisness questions I had.




# Project 5

Describe your SQL queries and reports.
I used the SQL from the description.  I had trouble getting it to run in Power Query and Advanced Editor.  CHATGBT helped me find out that I needed to use the Advanced Options when connecting with ODBC.  

Here are the steps/

Open Power BI Desktop

Go to the Home tab at the top

Click Get Data → Select ODBC

In the ODBC window, you’ll see:

🔘 Data source name (DSN) — pick your DSN (e.g., SmartSalesDSN)

✅ Below that, you’ll see a small clickable “Advanced options” link/dropdown.

👉 Click on Advanced options and it will expand the panel.




Explain dashboard design choices.  
I designed my dashboard with the items called out in the instructions, but I did add all the items from seperated sections of the instructions.

Include screenshot of: Power BI Model View / Spark SQL Schema

![Model](image-3.png)

Include screenshot of: Query results

![SQL](image-4.png)

Include screenshot of: Final Dashboard / Charts

![Filtered on South](image.png)

![No Filters](image-1.png)

![Date Slider](image-2.png)

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


