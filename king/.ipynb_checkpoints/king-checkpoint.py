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

#################################################
#TO UPDATE DATE FOR THE RUN AND DWH BUSINESS DATE
#DHW BUSINESS DATE NEEDS TO BE 1BD BEFORE
#################################################

date =  20240903

# Previous business date compared to date.
dwh_business_date = "2024-09-02 00:00:00"

# 2024-09-02
dwh_business_date_short = dwh_business_date[:10]

# Calling the function.
def call_olympus_trades_for_month_ptt():
  # 
  print(os.getcwd())

  conn = olympusgrpc.pythonclient.connect(properties)

  # Discuss the SQL command during the next session.
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
    JOIN gfolyrep_work.PanelHistory ph ON ph.alert_id like SUBSTRING(uf.source_id,1,36)
    AND ph.dwh_business_date = cast('{dwh_business_date}' as timestamp)
    where uf.item_definition_id IN ('ID-20230906-135243563','ID-20231013-155037324')
    and uf.uno_alert_status = 'new'
    and ph.excpetion_23b='Y'),

    pmc_prices as
    (select smcp,
    MAX(CASE WHEN derived_method = 'BID' THEN metric_value ELSE NULL END) as price_bid,
    MAX(CASE WHEN derived_method = 'ASK' THEN metric_value ELSE NULL END)as price_ask,
    MAX(CASE WHEN derived_method = 'latest' THEN metric_value ELSE NULL END) as price_last
    from (select smcp, derived_method,metric_value
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
    join pmc_prices pp on ad.smcp = pp.smcp

        ;

        """,

        conn,
  )
  print(df)

###########################################################
#TO UPDATE THE PATH TO SAVE SQL OUTPUT IN THE FOLDER NEEDED
###########################################################

output_file_tr = "/home/deniz/Python/King/Test/RegW Final O %s.xlsx" %(date)

writer3 = pd.ExcelWriter(output_file_tr, engine="xlsxwriter")

df.to_excel(writer3,sheet_name="Sheet1", index=false)

writer3.close()

AOMTwithMarketData = df

#make sure format is numerical
AOMTwithMarketData["price_bid"] = pd.to_numeric(
  AOMTwithMarketData["price_bid"],errors="coerce"
)
AOMTwithMarketData["unit_price"] = pd.to_numeric(
  AOMTwithMarketData["trade_unit_price"],errors="coerce"
)
AOMTwithMarketData["price_ask"] = pd.to_numeric(
  AOMTwithMarketData["price_ask"],errors="coerce"
)
AOMTwithMarketData["price_last"] = pd.to_numeric(
  AOMTwithMarketData["price_last"],errors="coerce"
)

# Ratios calc
AOMTwithMarketData["ratioBid"]=(
  AOMTwithMarketData["price_bid"]/AOMTwithMarketData["unit_price"]
)

AOMTwithMarketData["ratioAsk"]=(
  AOMTwithMarketData["price_ask"]/AOMTwithMarketData["unit_price"]
)

AOMTwithMarketData["ratioLast"]=(
  AOMTwithMarketData["price_last"]/AOMTwithMarketData["unit_price"]
)

# populate ratioBasedOnDirection
AOMTwithMarketData["ratioBasedOnDirection"]=[
  AOMTwithMarketData["ratioLast"][i]
  if pd.isna(AOMTwithMarketData["ratioBid"][i])
  or pd.isna(AOMTwithMarketData["ratioAsk"][i])
  else(
      AOMTwithMarketData["ratioBid"][i]
      if AOMTwithMarketData["buy_sell_indicator"][i]=="BUY"
      else AOMTwithMarketData["ratioAsk"][i]
  )
  for i in range(len(AOMTwithMarketData))
]

AOMTwithMarketData["ratioBasedOnDirection"]=pd.to_numeric(
    AOMTwithMarketData["ratioBasedOnDirection"],errors="coerce"
)

#calculation of numbers of rows

AOMTwithMarketData["isNan"]=pd.isna(AOMTwithMarketData["unit_price"])
AOMTwithMarketData["unit_price"].replace("",np.nan,inplace=True)
AOMTwithMarketData["unit_price"].replace(
    "NaN",np.nan,inplace=True
) #if 'Nan' is a string
AOMTwithMarketData["unit_price"].replace("None",np.nan,inplace=True)
AOMTwithMarketData["unit_price"] = AOMTwithMarketData["unit_price"].astype(float)

number_of_rows = len(AOMTwithMarketData)

#to populate Meets 23B Market terms

if number_of_rows == 1:
  if pd.isna(AOMTwithMarketData["unit_price"].iloc[0]):
    AOMTwithMarketData["Manual Check"]="Trade Unit Price is 0"
  else:
    # This checks the condition for the single entry in your DataFrame
    AOMTwithMarketData["Manual Check"] = (
        abs(AOMTwithMarketData["ratioBasedOnDirection"].iloc[0]-1.0)<0.03
    )

if number_of_rows !=1:
  AOMTwithMarketData["Manual Check"]=[
      "Trade Unit Price is 0" if pd.isna(x) or x==0 else (abs(y-1.0)<0.03)
  for x,y in zip(
      AOMTwithMarketData["unit_price"],
      AOMTwithMarketData["ratioBasedOnDirection"],
  )
  ]

AOMTwithMarketData["Meets 23B Market Terms"] = AOMTwithMarketData["Manual Check"]

#to populate Missing Root Order ID
AOMTwithMarketData["Missing Root Order ID"]=AOMTwithMarketData[
    "root_order_id"
].isnull()

#to calculate number of rows
AOMTwithMarketData["concatenated"]=(
    AOMTwithMarketData["Meets 23B Markets Terms"].astype(str)
    + AOMTwithMarketData["Missing Root Order ID"].astype(str)
    + AOMTwithMarketData["uno_alert_id"].astype(str)
)
AOMTwithMarketData["occurences"]=AOMTwithMarketData.groupby("concatenated")[
    "concatenated"
].transform("count")
AOMTwithMarketData["Count of trade ids"]=AOMTwithMarketData["occurences"]

#to sort AOMTwithMarketData
AOMTwithMarketData = AOMTwithMarketData.sort_values(
    by="uno_alert_id",ascending=False
)

# to get the final dataframe for the summary
#
AOMTwithMarketDataSummaryFinal = pd.DataFrame({'dwh_business_date_short':['dwh_business_date_short']}
)

AOMTwithMarketDataSummaryFinal = AOMTwithMarketData[
        [
            "trade_date",
            "segment_description_level_4",
            "uno_alert_id",
            "ppl_product_name",
            "trade_currency",
            "Meets 23B Market Terms",
            "Missing Root Order ID",
            "Count of trade Ids",
        ]
    ]

AOMTwithMarketDataSummaryFinal = AOMTwithMarketDataSummaryFinal.drop_duplicates()
AOMTwithMarketDataSummaryFinal.rename(columns={"trade_date":"dwh business date"})
AOMTwithMarketDataSummaryFinal = AOMTwithMarketDataSummaryFinal.sort_values(
    by="uno_alert_id",ascending=False
)

###############################
#TO UPDATE THE FILE PATH TO GET THE DETAILED FILE WHICH CONTAINS THE SQL OUTPUT ALONG
# WITH THE CALCULATIONS
################################

output_file_tr="C:/Users/IG42629/Documents/Test/RegW Final details O %s.xlsx" %(
  dwh_business_date_short
)

writer5=pd.Excelwriter(output_file_tr,engine="xlsxwriter")
AOMTwithMarketData.to_excel(writer5,sheet_name="Sheet1",index=false)
writer5.close()

#########################
#TO UPDATE THE FILEPATH TO GET THE SUMMARY FILE WHICH CAN BE USED FOR CLOSURE
########################

output_file_tr = "I:\LANDPAGE -I\X\Python - Reg W\Reg W Final O %s.xlsx" %(
  dwh_business_date_short
)

writer6 = pd.ExcelWriter(output_file_tr,engine="xlsxwriter")
AOMTwithMarketDataSummaryFinal.to_excel(writer6,sheet_name="Sheet1",index=False)
writer6.close()

# return df
conn.close()

call_olympus_trades_for_month_ptt()