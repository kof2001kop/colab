import tushare as ts
import pandas as pd

stock_code = "600848"

history = ts.get_hist_data(stock_code)

writer = pd.ExcelWriter("storage/dcim/" + stock_code + ".xlsx", engine='xlsxwriter')
    
history.to_excel(writer)

writer.save()
