import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

Definitions:

A quarter is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
A recession is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
A recession bottom is the quarter within a recession which had the lowest GDP.
A university town is a city which has a high percentage of university students compared to the total population of the city.
Hypothesis: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (price_ratio=quarter_before_recession/recession_bottom)

The following data files are available for this assignment:

From the Zillow research data site there is housing data for the United States. In particular the datafile for all homes at a city level, City_Zhvi_AllHomes.csv, has median home sale prices at a fine grained level.
From the Wikipedia page on college towns is a list of university towns in the United States which has been copy and pasted into the file university_towns.txt.
From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file gdplev.xls. For this assignment, only look at GDP data from the first quarter of 2000 onward.
Each function in this assignment below is worth 10%, with the exception of run_ttest(), which is worth 50%.

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 
          'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 
          'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 
          'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona',
          'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 
          'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 
          'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida',
          'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 
          'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 
          'VA': 'Virginia'}
*************************************************************************************
def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  ) 

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    
    with open('university_towns.txt') as file:
        data_list = []
        for line in file:               # line is an str
            data_list.append(line[:-1]) #data_list returns a list containing the whole txt seperated by lines
            
    state_town = []
    for line in data_list:
        if line[-6:] == '[edit]': #if the end of the line was '[edit]'
            state = line[:-6]     #then the first of that line is an state
        elif '(' in line:
            town = line[:line.index('(')-1]  #from the beginig of the line until reaching a '(' is the name of a town
            state_town.append([state,town])  
        else:
            town = line
            state_town.append([state,town]) # This is a list of lists, the inner lists each contains two strings: State and Town
            
    df_university_town = pd.DataFrame(state_town,columns = ['State','RegionName']) #creating a DataFrame with 2 columns from a list of lists
    
    return df_university_town
get_list_of_university_towns()

*************************************************************************************
def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    #Load xls file 
    xls_file = pd.ExcelFile('gdplev.xls')
    df_GDP = xls_file.parse(skiprows=7)
    df_GDP = df_GDP[['Unnamed: 4','Unnamed: 5']]
    df_GDP.columns = ['Quarter', 'GDP']
    df_GDP[df_GDP.Quarter == '2000q1'] # find the row of year 2000 where we need for this assignment 
    df_GDP = df_GDP.loc[212:]          # keep the row 212 to the end (year2000 to the end) 
    # recession : starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    recession_start = []
    for i in range(len(df_GDP)-2):
        if (df_GDP.iloc[i][1] > df_GDP.iloc[i+1][1]) & (df_GDP.iloc[i+1][1] > df_GDP.iloc[i+2][1]): 
        #recession : starting with two consecutive quarters of GDP decline
                recession_start.append(df_GDP.iloc[i][0])
    return recession_start[0]
           
get_recession_start()
'2008q3'

*************************************************************************************
def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    #Load xls file 
    xls_file = pd.ExcelFile('gdplev.xls')
    df_GDP = xls_file.parse(skiprows=7)
    df_GDP = df_GDP[['Unnamed: 4','Unnamed: 5']]
    df_GDP.columns = ['Quarter', 'GDP']
    df_GDP[df_GDP.Quarter == '2008q3'] # find the row of year 2008q3 where the ressession (decline) starts 
    df_GDP = df_GDP.loc[246:]          # keep the row 246 to the end (year2008q3/resession_start to the end) 
    # recession : starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
    recession_end = []
    for i in range(len(df_GDP)-2):
        if (df_GDP.iloc[i][1] > df_GDP.iloc[i-1][1]) & (df_GDP.iloc[i-1][1] > df_GDP.iloc[i-2][1]): 
        #recession : ending with two consecutive quarters of GDP growth
                recession_end.append(df_GDP.iloc[i][0])
    return recession_end[0]
get_recession_end()
'2009q4'

*************************************************************************************
def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    #Load xls file 
    xls_file = pd.ExcelFile('gdplev.xls')
    df_GDP = xls_file.parse(skiprows=7)
    df_GDP = df_GDP[['Unnamed: 4','Unnamed: 5']]
    df_GDP.columns = ['Quarter', 'GDP']
    df_GDP[df_GDP.Quarter == '2000q1'] # find the row of year 2000 where we need for this assignment 
    df_GDP = df_GDP.loc[212:]          # keep the row 212 to the end (year2000 to the end) 
    #A recession bottom is the quarter within a recession which had the lowest GDP.
    recession_start = get_recession_start()
    recession_end = get_recession_end()
    df_recession = df_GDP.loc[df_GDP[df_GDP['Quarter'] == recession_start].iloc[0].name : df_GDP[df_GDP['Quarter'] == recession_end].iloc[0].name] 
    df_min_GDP = df_recession[df_recession.GDP == df_recession['GDP'].min()]
    return df_min_GDP.iloc[0][0]

get_recession_bottom()
'2009q2'

*************************************************************************************
def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df_housing_data = pd.read_csv('City_Zhvi_AllHomes.csv') 

    
    df_housing_data.drop(['Metro','CountyName','RegionID','SizeRank'],axis=1,inplace=1)
    #df_housing_data.drop(df.columns[[0, 1, 3]], axis=1) another way to drop columns by their number
    df_housing_data['State'] = df_housing_data['State'].map(states) #Full names of States instead of 2-digit short form
    df_housing_data.set_index(['State','RegionName'],inplace=True)  
    col = list(df_housing_data.columns)
    df_housing_data.drop(list(df_housing_data.columns)[:45],axis=1,inplace=1)
    
        
    def new_col_names():
        #generating the new coloumns names 
        years = list(range(2000,2017))
        quarters = ['q1','q2','q3','q4']
        quar_years = [] 
        for i in years:
            for x in quarters:
                quar_years.append((str(i)+x)) #append two strings and add to the list: quar_years
        return quar_years[:67] # we need columns for 2000q1 through 2016q3, don't want '2016q4' (the last element)
    
    # Q1 is January through March, Q2 is April through June, 
    # Q3 is July through September, Q4 is October through December.
    
    #qs is the quarters of the year
    qs = [list(df_housing_data.columns)[x:x+3] for x in range(0, len(list(df_housing_data.columns)), 3)]
    #creates a list of list, the inner lists are the 3 months of each Q
    # new columns based on quarters not year
    column_names = new_col_names() #changing the name of columns , This is a list, new_col_names() returns a list
    
    # zip(): Iterating through two lists at the same time
    for col,q in zip(column_names,qs):
        df_housing_data[col] = df_housing_data[q].mean(axis=1) #changing the name of columns of df_housing_data
        #creating a new column for df_housing_data: yearQ
    df_housing_data = df_housing_data[column_names]
          
    return df_housing_data


convert_housing_data_to_quarters()
10730 rows × 67 columns

*************************************************************************************
def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    recession_start = get_recession_start()
    recession_bottom = get_recession_bottom()
    df_housing_data = convert_housing_data_to_quarters()
    df_housing_recession = df_housing_data.loc[:,'2008q3':'2009q2']
    df_housing_recession.reset_index(inplace=True)
    s_university_town = get_list_of_university_towns()['RegionName']
    s_university_town = set(s_university_town) #get a list of unique values of univeristy towns
    
    def difference(row):
        return row['2008q3'] - row['2009q2']
        
    df_housing_recession['Difference'] = df_housing_recession.apply(difference, axis=1)
    def is_university_town(row):
        if row['RegionName'] in s_university_town:
            return 1
        else:
            return 0
    df_housing_recession['UniversityTown']=df_housing_recession.apply(is_university_town,axis=1)  
    #create a new column: 'UniversityTown' 
    
    s_housing_uni_town = df_housing_recession[df_housing_recession['UniversityTown'] == 1].loc[:,'Difference'].dropna()
    s_housing_non_uni_town = df_housing_recession[df_housing_recession['UniversityTown'] == 0].loc[:,'Difference'].dropna()
    result = ttest_ind(s_housing_uni_town, s_housing_non_uni_town)
    def test():
        if s_housing_non_uni_town.mean() < s_housing_uni_town.mean():
            return 'non-university town'
        else:
            return 'university town'
    
    p_value = list(result) [1]
    if p_value <0.01:
        difference = True
    else:
        difference = False
    return (difference, p_value, test())
run_ttest()
(True, 7.1245161701732997e-06, 'university town')
