# Basket-Analysis

### Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Results](#results)
  
### Prorject Overview
This analysis aims to boost sales by gaining a deeper understanding of customer purchasing patterns, enabling the business to enhance cross-selling strategies.

### Data Sources
Online Retail: This is a transnational data set which contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail. [Download here](https://archive.ics.uci.edu/dataset/352/online+retail)

### Tools
 • Python: Data Cleaning and Analysis
 
 • PBI(PowerBi): Visualization

 ### Data Cleaning
 In the initial preperation phase, I perform following tasks:
 1. Load data.
 2. Handle missing data. Since most of the missing values are in Customer_ID, and I only need transactions to perform this analysis, we will leave those missing values untouched.
 3. Inspect data types.

 ### EDA (Explore Data Analysis)
 I have already conducted exploratory data analysis (EDA) on the same dataset, [you can view the analysis here.](https://github.com/Huy24vt/RFM-Segmentation)

 ### Data Analysis
To perform basket analysis, we will need to caculate 3 mains metrics: Support, Confidence and Lift.
1. Support = number of transactions including both products / total number of transactions
   
   This metric indicates the frequency of the product being bought together.
   
2. Confidence:

   Confidence of product 1 = support of basket / support of product 1

   Confidence of product 2 = support of basket / support of product 2

   This metric indicates the direction of cross-selling
   
3. Lift = support of basket / (support of product 1 * support of product 2)

   This metric indicates the strength of the relationship for a basket of two products

I will use Apriori and Association_Rules to caculate these metrics.

### Results
 [You can view the dashboard here](https://app.powerbi.com/view?r=eyJrIjoiMWI4YzYyY2QtZmI2ZC00OTk3LWFmYjUtYTYwMGMyMjkzMDc0IiwidCI6IjJmODVkYzc0LWI2YjQtNDU4NC1iZWVlLWNjZGE3MTQ0NDk3MCIsImMiOjZ9)

<img width="610" alt="image" src="https://github.com/Huy24vt/Basket-Analysis/assets/130732635/d0967207-9f87-4c2b-9926-0adc4838e7c0">

 
In performing basket analysis, businesses gain insights into the relationships between products, enabling them to implement effective cross-selling strategies or create enticing product combos to boost sales revenue. Furthermore, this information empowers businesses to optimize the layout of their stores, strategically placing products for enhanced sales performance.

