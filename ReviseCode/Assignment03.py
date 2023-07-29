Assignment 3 - More Pandas
This assignment requires more individual learning then the last one did - you are encouraged to check out the pandas documentation to find functions or methods you might not have used yet, or ask questions on Stack Overflow and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

Question 1 (20%)
Load the energy data from the file Energy Indicators.xls, which is a list of indicators of energy supply and renewable electricity production from the United Nations for the year 2013, and should be put into a DataFrame with the variable name of energy.

Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:

['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']

Convert Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as np.NaN values.

Rename the following list of countries (for use in later questions):

"Republic of Korea": "South Korea",
"United States of America": "United States",
"United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
"China, Hong Kong Special Administrative Region": "Hong Kong"

There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,

e.g.

'Bolivia (Plurinational State of)' should be 'Bolivia',

'Switzerland17' should be 'Switzerland'.



Next, load the GDP data from the file world_bank.csv, which is a csv containing countries' GDP from 1960 to 2015 from World Bank. Call this DataFrame GDP.

Make sure to skip the header, and rename the following list of countries:

"Korea, Rep.": "South Korea", 
"Iran, Islamic Rep.": "Iran",
"Hong Kong SAR, China": "Hong Kong"



Finally, load the Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.

Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

This function should return a DataFrame with 20 columns and 15 entries.

import pandas as pd
import numpy as np
def answer_one():
    #Load xls file 
    xls_file = pd.ExcelFile('Energy Indicators.xls')
    energy = xls_file.parse(skiprows=17,skip_footer=(38))
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    # Rename the columns
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # Convert "..." to np.NaN
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    #Conevrt Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    #Rename Countries
    energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States",
                                                   "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", 
                                                   "China, Hong Kong Special Administrative Region": "Hong Kong"})
    #Remove parantheses 
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    
    #GDP read_csv & Skip header & only include 10 last years 
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    #Rename Countries
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", 
                                             "Hong Kong SAR, China": "Hong Kong"})
    #Only inlcude 10 last years of GDP 
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    #Load scimagojr-3.xlsx
    ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
    ScimEn_top = ScimEn[:15]
    
    #Join the three DataFrames on Country
    ScimEn_Energy = pd.merge(ScimEn_top, energy, how='inner', left_on='Country', right_on='Country')
    df_joint = pd.merge(ScimEn_Energy, GDP, how='inner', left_on='Country', right_on='Country')
    df_joint = df_joint.set_index('Country')
    return df_joint

answer_one()

Question 2 (6.6%)
The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

This function should return a single number.


%%HTML
<svg width="800" height="300">
  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />
  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />
  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />
  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>
  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>
</svg>
Everything but this!

-
def answer_two():
        #Load xls file 
    xls_file = pd.ExcelFile('Energy Indicators.xls')
    energy = xls_file.parse(skiprows=17,skip_footer=(38))
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    # Rename the columns
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    # Convert "..." to np.NaN
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    #Conevrt Energy Supply to gigajoules (there are 1,000,000 gigajoules in a petajoule)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    #Rename Countries
    energy['Country'] = energy['Country'].replace({"Republic of Korea": "South Korea", "United States of America": "United States",
                                                   "United Kingdom of Great Britain and Northern Ireland": "United Kingdom", 
                                                   "China, Hong Kong Special Administrative Region": "Hong Kong"})
    #Remove parantheses 
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    
    #GDP read_csv & Skip header & only include 10 last years 
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    #Rename Countries
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran", 
                                             "Hong Kong SAR, China": "Hong Kong"})
    #Only inlcude 10 last years of GDP 
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']
    #Load scimagojr-3.xlsx
    ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
        
    #Join the three DataFrames on Country
    ScimEn_Energy = pd.merge(ScimEn, energy, how='inner', left_on='Country', right_on='Country')
    df_joint = pd.merge(ScimEn_Energy, GDP, how='inner', left_on='Country', right_on='Country')
    df_joint = df_joint.set_index('Country')
    df_joint_top = df_joint[:15]
    
    #The Actual answer is this, but (I guess) since the df_joint and df_joint_top were defined in the function answer_one() they 
    # were not defined here so I repeated all the code lines, But I think there should be something like 'global' to use the 
    # variables defined in other functions
    return len(df_joint.index) - len(df_joint_top.index)
answer_two()
147

Question 3 (6.6%)
What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)

This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']].mean(axis=1).rename('avgGDP').sort_values(ascending=False)
    return avgGDP
answer_three()
Country
United States         1.536434e+13
China                 6.348609e+12
Japan                 5.542208e+12
Germany               3.493025e+12
France                2.681725e+12
United Kingdom        2.487907e+12
Brazil                2.189794e+12
Italy                 2.120175e+12
India                 1.769297e+12
Canada                1.660647e+12
Russian Federation    1.565459e+12
Spain                 1.418078e+12
Australia             1.164043e+12
South Korea           1.106715e+12
Iran                  4.441558e+11
Name: avgGDP, dtype: float64


Question 4 (6.6%)
By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?

This function should return a single number.


import pandas as pd
import numpy as np
def answer_four():
    Top15 = answer_one()
    avgGDP = answer_three()
    sixth_avg_GDP = avgGDP[avgGDP == avgGDP[5]]
    sixth_avg_GDP = sixth_avg_GDP.reset_index()
    Sixth_avgGDP_name = sixth_avg_GDP.loc[0][0]
    Top15.reset_index(inplace=True)
    diff = (Top15[Top15['Country'] == Sixth_avgGDP_name]['2015']-Top15[Top15['Country'] == Sixth_avgGDP_name]['2006']).astype(float)
    return diff.loc[3]
answer_four()

import pandas as pd
import numpy as np
def answer_four():
    Top15 = answer_one()
    avgGDP = answer_three()
    sixth_avg_GDP = avgGDP[avgGDP == avgGDP[5]]
    sixth_avg_GDP = sixth_avg_GDP.reset_index()
    Sixth_avgGDP_name = sixth_avg_GDP.loc[0][0]
    Top15.reset_index(inplace=True)
    diff = (Top15[Top15['Country'] == Sixth_avgGDP_name]['2015']-Top15[Top15['Country'] == Sixth_avgGDP_name]['2006']).astype(float)
    return diff.loc[3]
answer_four()
​
246702696075.3999


Question 5 (6.6%)
What is the mean Energy Supply per Capita?

This function should return a single number.


def answer_five():
    Top15 = answer_one()
    mean = Top15["Energy Supply per Capita"].mean()
    return mean
answer_five()
157.6

Question 6 (6.6%)
What country has the maximum % Renewable and what is the percentage?

This function should return a tuple with the name of the country and the percentage.

def answer_six():
    Top15 = answer_one()
    Max_Renewable = Top15[Top15['% Renewable'] == Top15['% Renewable'].max()] 
    return (Max_Renewable.index.tolist()[0],Max_Renewable['% Renewable'].tolist()[0])
answer_six()
('Brazil', 69.64803)

Question 7 (6.6%)
Create a new column that is the ratio of Self-Citations to Total Citations. What is the maximum value for this new column, and what country has the highest ratio?

This function should return a tuple with the name of the country and the ratio.

def answer_seven():
    Top15 = answer_one()
    Top15['Ratio_Self_Citation'] = Top15['Self-citations']/Top15['Citations']
    Max_Ratio_Self_Citation = Top15[Top15['Ratio_Self_Citation'] == Top15['Ratio_Self_Citation'].max()]
    return (Max_Ratio_Self_Citation.index.tolist()[0],Max_Ratio_Self_Citation['Ratio_Self_Citation'].tolist()[0])
answer_seven()
('China', 0.6893126179389422)

Question 8 (6.6%)
Create a column that estimates the population using Energy Supply and Energy Supply per capita. What is the third most populous country according to this estimate?

This function should return a single string value.

def answer_eight():
    Top15 = answer_one()
    Top15['Population_Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    df_Population = Top15['Population_Estimate'].sort_values(ascending=False).reset_index()
    Third_Most_Populous = df_Population['Country'][2]
    return Third_Most_Populous

answer_eight()
'United States'

Question 9 (6.6%)
Create a column that estimates the number of citable documents per person. What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the .corr() method, (Pearson's correlation).

This function should return a single number.

(Optional: Use the built-in function plot9() to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)

def answer_nine():
    Top15 = answer_one()
    Top15['Population_Estimate'] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15['Citable_Docs'] = Top15['Citable documents']/Top15['Population_Estimate']
    #Top15[['Country','Population_Estimate', 'Citable_Docs']]
    correlation = Top15['Citable_Docs'].corr(Top15['Energy Supply per Capita'])
    return correlation
answer_nine()
0.79400104354429424

Question 10 (6.6%)
Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.

This function should return a series named HighRenew whose index is the country name sorted in ascending order of rank.

def answer_ten():
    Top15 = answer_one()
    median = Top15['% Renewable'].median()
    Top15['HighRenew'] = (Top15['% Renewable'] >= median).astype(int)
    Sorted = Top15.sort('Rank')
    return Sorted.HighRenew
answer_ten()
Country
China                 1
United States         0
Japan                 0
United Kingdom        0
Russian Federation    1
Canada                1
Germany               1
India                 0
France                1
South Korea           0
Italy                 1
Spain                 1
Iran                  0
Australia             0
Brazil                1
Name: HighRenew, dtype: int64


Question 11 (6.6%)
Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.

ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
This function should return a DataFrame with index named Continent ['Asia', 'Australia', 'Europe', 'North America', 'South America'] and columns ['size', 'sum', 'mean', 'std']

def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15['Population_Estimate'] = (Top15['Energy Supply']/Top15['Energy Supply per Capita']).astype(float)
    Top15.reset_index(inplace=True)
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    df = Top15.set_index('Continent').groupby(level=0)['Population_Estimate'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
    return df
    
answer_eleven()


Question 12 (6.6%)
Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?

This function should return a Series with a MultiIndex of Continent, then the bins for % Renewable. Do not include groups with no countries.

def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    Top15.reset_index(inplace=True)
    Top15['Continent'] = [ContinentDict[country] for country in Top15['Country']]
    Top15['Renew_bins'] = pd.cut(Top15['% Renewable'],5)
    df = Top15.groupby(['Continent','Renew_bins']).size()
    return df
answer_twelve()

Continent      Renew_bins      
Asia           (2.212, 15.753]     4
               (15.753, 29.227]    1
Australia      (2.212, 15.753]     1
Europe         (2.212, 15.753]     1
               (15.753, 29.227]    3
               (29.227, 42.701]    2
North America  (2.212, 15.753]     1
               (56.174, 69.648]    1
South America  (56.174, 69.648]    1
dtype: int64


Question 13 (6.6%)
Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.

e.g. 317615384.61538464 -> 317,615,384.61538464

This function should return a Series PopEst whose index is the country name and whose values are the population estimate string.

def answer_thirteen():
    Top15 = answer_one()
    Top15['Population_Estimate'] = (Top15['Energy Supply']/Top15['Energy Supply per Capita']).astype(float)
    ans = Top15['Population_Estimate'].apply(lambda x : '{:,}'.format(x))
    return ans
answer_thirteen()
Country
China                 1,367,645,161.2903225
United States          317,615,384.61538464
Japan                  127,409,395.97315437
United Kingdom         63,870,967.741935484
Russian Federation            143,500,000.0
Canada                  35,239,864.86486486
Germany                 80,369,696.96969697
India                 1,276,730,769.2307692
France                  63,837,349.39759036
South Korea            49,805,429.864253394
Italy                  59,908,256.880733944
Spain                    46,443,396.2264151
Iran                    77,075,630.25210084
Australia              23,316,017.316017315
Brazil                 205,915,254.23728815
Name: Population_Estimate, dtype: object


Optional
Use the built in function plot_optional() to see an example visualization.


def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);
​
    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
​
    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")

plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!
This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.
