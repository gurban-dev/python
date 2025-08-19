######################################
#TO UPDATE USERNAME AND PASSWORD (SSO)
######################################
properties = {
  "username": "",
  "password": "",
  "ENV": "prod",
  "datasource": "STARBURST",
  "queryTimeout": "3600"
}

'''
I had to downgrade my version of numpy to before
2.0 because of an incompatibility issue.
pip install numpy==1.26.4
'''
import numpy as np
# import qpython.qconnection
import pandas as pd
import jaydebeapi
import os
# import olympusgrpc.pythonclient
import datetime

print(os.getcwd())

##################################################
# TO UPDATE DATE FOR THE RUN AND DWH BUSINESS DATE
# DHW BUSINESS DATE NEEDS TO BE 1BD BEFORE
##################################################

date = 20240903

# Demonstrate how to catch invalid input with try catch.
date = int(input('Please input the date:'))

# Previous business date compared to date.
dwh_business_date = "2024-09-02 00:00:00"

# 2024-09-02
dwh_business_date_short = dwh_business_date[:10]

# Calling the function.
def call_olympus_trades_for_month_ptt():
  print(os.getcwd())

  # A connection is being made with the database.
  conn = olympusgrpc.pythonclient.connect(properties)

  '''
  The database schema is the structure of a database.

  pd.read_sql() executes a SQL query and loads
  the results into a Pandas DataFrame, "df".

  "alert_data" is a common table expression or CTE
  which is a variable that stores a temporary result
  set and can be referenced in subsequent SQL statement.
  
  It appear that lines 133 through 143 are columns that
  belong to the "gfolyncr_mis_managed.om_uno_fact uf"
  database table.

  The two characters preceding the . before each column
  name are aliases or alternative names for database tables.

  An INNER JOIN is taking fold. Think of a JOIN as combining
  rows/records from two different tables.

  In this case, rows from tables PanelHistory
  or "ph" and "uf" are being merged.

  PanelHistory is aliased as "ph" and another table.
  
  "uf" is an alias for the om_uno_fact table. 

  The ON keyword specifies the condition for the join. It
  defines how the two tables are related and which columns
  should be compared to find the matching rows.

  The condition states that the alert_id column from the
  PanelHistory table (ph) should match a substring of the
  source_id column from the om_uno_fact (uf) table.

  The LIKE operator is used in a WHERE clause to search
  for a specified pattern in a column.
  
  SUBSTRING(uf.source_id, 1, 36) extracts a portion of the
  string from the source_id column starting at position 1
  (index 0) and continuing for 36 characters. This means
  it will take the first 36 characters of "source_id".

  The next condition further filters the results of the join
  by ensuring that the dwh_business_date column from the
  PanelHistory table matches a specific date, which is
  dynamically provided as {dwh_business_date} and cast to
  the timestamp data type.
  AND ph.dwh_business_date = cast('{dwh_business_date}' as timestamp)

  The cast() function converts the placeholder {dwh_business_date}
  (a string) into a timestamp data type.

  This ensures that the comparison between ph.dwh_business_date
  and {dwh_business_date} is type-consistent.

  E.g. cast('2025-02-23 00:00:00' AS timestamp)

  This ensures that only records corresponding to a
  particular business date are included in the results.

  where uf.item_definition_id IN ('ID-20230906-135243563', 'ID-20231013-155037324')

  The condition checks if item_definition_id is one of two
  specified values ('ID-20230906-135243563' or 'ID-20231013-155037324').

  This limits the results to only those records that match
  these IDs.

  and uf.uno_alert_status = 'new'
  and ph.exception_23b='Y'

  These above conditions filter records to include only
  those where the uno_alert_status column from the uf table
  is equal to 'new' and where the exception column from
  the ph table is equal to 'Y'.
  
  scmp file, is usually known as a schema compare file.
  It stores settings and configurations for comparing
  database schemas.'''
  df = pd.read_sql(
    f"""
    with alert_data as
    (select ph.root_order_id,
      uf.uno_alert_id,
      ph.trade_date,
      ph.pmc_price,
      replace(ph.smcp,'.0',") as smcp,
      ph.buy_sell_indicator,
      ph.trade_unit_price,
      ph.trade_id,
      ph.trade_uit_id,
      ph.segment_description_level_4,
      ph.ppl_product_name,
      ph.trade_currency

    FROM gfolyncr_mis_managed.om_uno_fact uf
    JOIN gfolyrep_work.PanelHistory ph
    ON ph.alert_id like SUBSTRING(uf.source_id,1,36)
    AND ph.dwh_business_date = cast('{dwh_business_date}' as timestamp)
    where uf.item_definition_id IN ('ID-20230906-135243563','ID-20231013-155037324')
    and uf.uno_alert_status = 'new'
    and ph.excpetion_23b='Y'),

    pmc_prices as
    (select smcp,
    MAX(CASE WHEN derived_method = 'BID' THEN metric_value ELSE NULL END) as price_bid,
    MAX(CASE WHEN derived_method = 'ASK' THEN metric_value ELSE NULL END)as price_ask,
    MAX(CASE WHEN derived_method = 'latest' THEN metric_value ELSE NULL END) as price_last
    from (select smcp, derived_method, metric_value
      from
        (
          select
          smcp,
          derived_method,
          metric_value,
          row_number() OVER(PARTITION by SMCP
          ORDER BY lpad(CASE WHEN price_name LIKE 'PMC-PRICE%%' THEN
  REGEXP_REPLACE(price_name,'PMC-PRICE',"") ELSE NULL END,2,'0')ASC) as RN
          from gfolynref_standardization.OM_PMC_RATES_LKP
          where dwh_business_date = {date}
          and policy_code = 'EOD-NAMR'
          and metric_category='PRICE'
          and policy_category='GoldenMetricDerived'
          and upper(contributor) not like '%%CITI%%'
          and derived_method = 'BID'
          )A
          WHERE RN=1
      UNION ALL
          select smcp,derived_method,metric_value
          from
          (
          select
          smcp,
          derived_method,
          metric_value,
          row_number() OVER(PARTITION BY SCMP)
          ORDER BY lpad(CASE WHEN price_name LIKE 'PMC-PRICE%%' THEN
      REGEXP_REPLACE(price_name,'PMC-PRICE',"") ELSE NULL END,2,'0') ASC) as RN
          from gfolynref_standardization.OM_PMC_RATES_LKP
          where dwh_business_date = {date}
          and policy_code = 'EOD-NAMR'
          and metric_category='PRICE'
          and policy_category='GoldenMetricDerived'
          and upper(contributor) not like '%%CITI%%'
          and derived_method = 'ASK'
          )B
      WHERE RN = 1
      UNION ALL

      --SCMPs where BID and ASK prices are not available

      select smcp, derived_method, metric_value
      from
      (
      select
      smcp,
      'latest' as derived_method,
      metric_value,
      row number() OVER(PARTITION BY SMCP)
      ORDER BY lpad(CASE WHEN price_name LIKE 'PMC-PRICE%%' then)
  REGEXP_REPLACE(price_name,'PMC-PRICE',") ELSE NULL END,2,'0')ASC) AS RN
      from gfolynref_standardization.OM_PM_RATES_LKP
      where dwh_business_date={date}
      and policy_code = 'EOD-NAMR'
      and metric_category='PRICE'
      and policy_category='GoldenMetricDerived'
      and upper(contributor) not like '%%CITI%%'
      )C
      WHERE RN=1
    )D
    where smcp in (select DISTINCT smcp FROM alert_data)
    group by smcp
    )

    select distinct ad.*,pp.price_bid,pp.price_ask,pp.price_last
    from alert_data ad
    join pmc_prices pp on ad.smcp = pp.smcp;
    """,
    conn,
  )
  print(df)

############################################################
# TO UPDATE THE PATH TO SAVE SQL OUTPUT IN THE FOLDER NEEDED
############################################################

# output_file_tr = "/home/deniz/Python/King/Test/RegW Final O %s.xlsx" %(date)

output_file_tr = "/home/deniz/Python/King/Test/RegW Final O" + date + ".xlsx"

# Write a pandas DataFrame to an Excel spreadsheet or file.
writer3 = pd.ExcelWriter(output_file_tr, engine="xlsxwriter")

'''
writer3 is an ExcelWriter object.

pandas.DataFrame.to_excel(excel_writer, sheet_name)

writer3 is the excel writer.

"Sheet1" is the sheet_name.

index=false tells pandas not to include the
DataFrame's index as a column in the Excel
file.
'''
df.to_excel(writer3, sheet_name="Sheet1", index=false)

writer3.close()

# Instead of a copy of "df" being made,
# "AOMTwithMarketData" is a reference
# that points to the same memory address/location.
AOMTwithMarketData = df

# Output the memory addresses with id().
print(f"Memory Address of df: {id(df)}\n"
      f"Memory Address of AOMTwithMarketData: {id(AOMTwithMarketData)}")

# Make sure format is numerical.
# If the data cannot be converted to a numeric
# type, we would expect to see "NaN" (not a number)
# for that row in the "price_bid" column.
AOMTwithMarketData["price_bid"] = pd.to_numeric(
  AOMTwithMarketData["price_bid"], errors="coerce"
)

AOMTwithMarketData["unit_price"] = pd.to_numeric(
  AOMTwithMarketData["trade_unit_price"], errors="coerce"
)

AOMTwithMarketData["price_ask"] = pd.to_numeric(
  AOMTwithMarketData["price_ask"],errors="coerce"
)

AOMTwithMarketData["price_last"] = pd.to_numeric(
  AOMTwithMarketData["price_last"],errors="coerce"
)

# Ratios calc
AOMTwithMarketData["ratioBid"] = (
  AOMTwithMarketData["price_bid"] / AOMTwithMarketData["unit_price"]
)

AOMTwithMarketData["ratioAsk"] = (
  AOMTwithMarketData["price_ask"] / AOMTwithMarketData["unit_price"]
)

# Create a new column named "ratioLast".
AOMTwithMarketData["ratioLast"]=(
  AOMTwithMarketData["price_last"] / AOMTwithMarketData["unit_price"]
)

# Populate the new column "ratioBasedOnDirection".
AOMTwithMarketData["ratioBasedOnDirection"]=[
  AOMTwithMarketData["ratioLast"][my_name]

  # Label-based indexing can be can be described as
  # accessing the row at index "my_name" inside the
  # "ratioBid" column of the DataFrame object.
  if pd.isna(AOMTwithMarketData["ratioBid"][my_name])
  or pd.isna(AOMTwithMarketData["ratioAsk"][my_name])
  else(
    AOMTwithMarketData["ratioBid"][my_name]
    if AOMTwithMarketData["buy_sell_indicator"][my_name]=="BUY"
      # What is being executed here?
      # If this if block is entered, the flow of the
      # program wouldn't enter the else block.
    else AOMTwithMarketData["ratioAsk"][my_name]
  )
  for my_name in range(len(AOMTwithMarketData))
]

AOMTwithMarketData["ratioBasedOnDirection"] = pd.to_numeric(
  AOMTwithMarketData["ratioBasedOnDirection"],errors="coerce"
)

# Calculation of numbers of rows

AOMTwithMarketData["isNan"] = pd.isna(AOMTwithMarketData["unit_price"])
AOMTwithMarketData["unit_price"].replace("", np.nan,inplace=True)
AOMTwithMarketData["unit_price"].replace(
  "NaN",np.nan,inplace=True
) #if 'NaN' is a string

AOMTwithMarketData["unit_price"].replace("None", np.nan, inplace=True)

# The astype() method returns a new DataFrame
# where the data types has been changed to the
# specified type.
AOMTwithMarketData["unit_price"] = AOMTwithMarketData["unit_price"].astype(float)

number_of_rows = len(AOMTwithMarketData)

# To populate Meets 23B Market terms

if number_of_rows == 1:
  # isna() evaluates to true when passed None or NaN values.
  # Essentially, this checks to see if there are missing
  # values in the "unit_price" column.
  if pd.isna(AOMTwithMarketData["unit_price"].iloc[0]):
    AOMTwithMarketData["Manual Check"]= "Trade Unit Price is 0"
  else:
    # This checks the condition for the single
    # entry in your DataFrame.

    '''
    Subtract 1.0 from the value in the first row
    of the "ratioBasedOnDirection" column.

    abs() calculates the absolute difference between the
    value and 1.0. Negative values become positive.

    If the absolute difference is less than 0.03, True
    is assigned to the "Manual Check" column. Otherwise,
    False is.
    '''
    AOMTwithMarketData["Manual Check"] = (
      abs(AOMTwithMarketData["ratioBasedOnDirection"].iloc[0] - 1.0) < 0.03
    )

'''
List comprehension syntax:

new_list = [
  expression
  for item in iterable
  if condition
]

expression: The operation you want to perform
            on each item in the iterable.

item: Represents each element in the iterable.

iterable: This can be a list, set, range, or any other
          iterable object.

condition: This is a boolean expression that determines
           whether an item should be included in the new
           list.
'''

if number_of_rows != 1:
  # Create a new column called "Manual Check"
  # in the DataFrame AOMTwithMarketData.
  AOMTwithMarketData["Manual Check"] = [
    '''
    Checks two conditions for each pair of values (x, y)
    from the columns "unit_price" and "ratioBasedOnDirection".

    If x is NaN or None (pd.isna(x)), or equals 0, the
    string "Trade Unit Price is 0" is assigned to it.

    Otherwise, the program checks if the absolute difference
    between y and 1.0 is less than 0.03 (abs(y - 1.0) < 0.03).
    
    If true, True is assigned. Otherwise, False is.'''

    "Trade Unit Price is 0" if pd.isna(x) or x == 0 else (abs(y - 1.0) < 0.03)

    # Send an example of this with two smaller DataFrames.
    for x,y in zip(
      AOMTwithMarketData["unit_price"],
      AOMTwithMarketData["ratioBasedOnDirection"]
    )
  ]

'''
The new column does not create a new copy of the data.

Instead, it references the same underlying data as the
original column. This means that both columns point to
the same memory address/location for their data.

If you wanted to create a new column with its own
independent copy of the data:

df["Meets 23B Market Terms"] = df["Manual Check"].copy()
'''
AOMTwithMarketData["Meets 23B Market Terms"] = AOMTwithMarketData["Manual Check"]

'''
Create a new column named "Missing Root Order ID" in
the DataFrame "AOMTwithMarketData".

This column will contain boolean values indicating
whether the corresponding value in the "root_order_id"
column is missing (NaN or None).

The .isnull() method checks each value in the
"root_order_id" column to see if it is null (NaN
or None). It returns a Series of boolean values
where True indicates a missing value and False
indicates a non-missing value.

A Series is a one-dimensional labeled array.

One of the differences between a Series and a regular
array is that its items/elements can be accessed with
labels that are customisable.
'''

# To populate Missing Root Order ID.
AOMTwithMarketData["Missing Root Order ID"] = AOMTwithMarketData[
  "root_order_id"
].isnull()

'''
The values in columns "Meets 23B Markets Terms",
"Missing Root Order ID", and "uno_alert_id" are
being converted into strings because of astype(str).

This is essential because non-strings cannot be
directly concatenated.

The new column named "concatenated" would contain
records/rows whose values would be a combination of
the values from the three columns being concatenated.

See concatenating_columns.ipynb to visualise this.
'''

# To calculate number of rows.
AOMTwithMarketData["concatenated"] = (
  AOMTwithMarketData["Meets 23B Markets Terms"].astype(str)
  + AOMTwithMarketData["Missing Root Order ID"].astype(str)
  + AOMTwithMarketData["uno_alert_id"].astype(str)
)

'''
The DataFrame "AOMTwithMarketData" is divided into groups
where each group consists of rows that have the same value
in the "concatenated" column.

The ["concatenated"] part is selecting a specific column
from the grouped DataFrame.

This is useful if you want to apply an aggregation function
only to this column.

An aggregation function processes multiple values and
returns a single summary statistic.

.transform("count") counts the number of rows in each group. 
'''
AOMTwithMarketData["occurences"] = AOMTwithMarketData.groupby("concatenated")[
  "concatenated"
].transform("count")

AOMTwithMarketData["Count of trade ids"] = AOMTwithMarketData["occurences"]

'''
sort_values() sorts a DataFrame by one or more columns.

by="uno_alert_id" specifies that the sorting should
be based on the "uno_alert_id" column.

ascending=False indicates that the sorting should be
in descending order.

Sorts the DataFrame "AOMTwithMarketData" in descending
order based on the values in the "uno_alert_id" column.
'''

# To sort AOMTwithMarketData.
AOMTwithMarketData = AOMTwithMarketData.sort_values(
  by="uno_alert_id", ascending=False
)

'''
Create a new pandas DataFrame named "AOMTwithMarketDataSummaryFinal"
with a single column named "dwh_business_date_short".

This column contains a single row with the string value
'dwh_business_date_short'.

See dataframe_with_dictionary.ipynb to visualise this.
'''

# To get the final dataframe for the summary
AOMTwithMarketDataSummaryFinal = pd.DataFrame(
  # {'column_name': ['column_value']}
  {'dwh_business_date_short': ['dwh_business_date_short']}
)

'''
Create a new DataFrame named AOMTwithMarketDataSummaryFinal
by selecting specific columns from the original DataFrame
AOMTwithMarketData.

The list of column names that should be included in the
new DataFrame is specified within the square brackets [].
'''
AOMTwithMarketDataSummaryFinal = AOMTwithMarketData[
  [
    "trade_date",
    "segment_description_level_4",
    "uno_alert_id",
    "ppl_product_name",
    "trade_currency",
    "Meets 23B Market Terms",
    "Missing Root Order ID",
    "Count of trade Ids"
  ]
]

# Remove duplicate rows from the DataFrame.
AOMTwithMarketDataSummaryFinal = AOMTwithMarketDataSummaryFinal.drop_duplicates()

'''
Renames the column "trade_date" to "dwh business date".

Keep in mind that the result of the rename() method is
not assigned back to the DataFrame, so this operation
does not actually change the DataFrame.

To make the change effective, you should assign the
result back to the DataFrame.

See rename_column.ipynb to visualise this.
'''
AOMTwithMarketDataSummaryFinal.rename(columns={"trade_date": "dwh business date"})

# Sort the DataFrame "AOMTwithMarketDataSummaryFinal"
# in descending order based on the values in the
# "uno_alert_id" column.
AOMTwithMarketDataSummaryFinal = AOMTwithMarketDataSummaryFinal.sort_values(
  by="uno_alert_id", ascending=False
)

#############################################
# TO UPDATE THE FILE PATH TO GET THE DETAILED
# FILE WHICH CONTAINS THE SQL OUTPUT ALONG
# WITH THE CALCULATIONS
#############################################

'''
Create a file path by inserting the value of the
"dwh_business_date_short" variable into the
placeholder in the file name.

The placeholder is %s in this case, and represents
a string value.
'''
output_file_tr = "C:/Users/IG42629/Documents/Test/RegW Final details O %s.xlsx" % (
  dwh_business_date_short
)

# Writer object
writer5 = pd.Excelwriter(output_file_tr, engine="xlsxwriter")

# Write the DataFrame to the Excel file.
AOMTwithMarketData.to_excel(writer5, sheet_name="Sheet1", index=false)

writer5.close()

###########################################
# TO UPDATE THE FILEPATH TO GET THE SUMMARY
# FILE WHICH CAN BE USED FOR CLOSURE
###########################################

output_file_tr = "I:\LANDPAGE -I\X\Python - Reg W\Reg W Final O %s.xlsx" %(
  dwh_business_date_short
)

writer6 = pd.ExcelWriter(output_file_tr, engine="xlsxwriter")

AOMTwithMarketDataSummaryFinal.to_excel(writer6, sheet_name="Sheet1", index=False)

writer6.close()

# return df
conn.close()

call_olympus_trades_for_month_ptt()