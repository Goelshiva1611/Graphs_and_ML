import pandas as pd
df_stocks=pd.DataFrame(
    {
    "day":[1,23,34],
    "weather":[1,2,3]
}
)
df_wheather=pd.DataFrame(
    {
    "day":[1,23,34],
    "weather":[1,2,3]
}
)

with pd.ExcelWriter("newexcel.xlsx") as writer:
    df_stocks.to_excel(writer,sheet_name="sheet1_")
    df_wheather.to_excel(writer,sheet_name="sheet2")