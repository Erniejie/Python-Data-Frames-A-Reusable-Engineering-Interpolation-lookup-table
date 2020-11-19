import  pandas as pd
import numpy as np
pd.get_option("display.max_colwidth",120)

url1 = "http://ouopentextbooks.org/thermodynamics/saturation-properties-temperature-table/"
url2 = "http://ouopentextbooks.org/thermodynamics/superheated-vapor-tables/"

def get_data_from_webpage(url):
    #--this returns a list of dataframes
    #--Should multiple tables available in html,we would need
    #-- if there is one table in html,then we need one only
    
    t_table = pd.read_html(url)
    
    #-- Element 0 is the DataFrame we are looking for

    return t_table

full_df = get_data_from_webpage(url1)
first_df = full_df[0]

def getColumnNamesAsList(df):
    cols = df.columns.tolist()
    return_value = []

    for v in cols:
        return_value.append(v[0] + "" + v[1])
    return return_value

c = getColumnNamesAsList(first_df)

def getValuesAsArray(df):
    vals = df.values.astype(float).T
    return vals

vals = getValuesAsArray(first_df)

temp= 32

print(c[0], ":", temp)

for i in range(1,len(c)):
    print("{0:>22}".format(c[i]), ":", np.interp(temp,vals[0],vals[i]))


## Display of Columns:
cols = first_df.columns
cols
cols[0]

    


    


    
