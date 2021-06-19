import tsend
import data_collection
import get_df
import analysis
import numpy as np

df = get_df.get("IBULHSGFIN.NS", "1d", "3mo")    #symbol, period, interval
final = data_collection.processing(df, "Close")  # final[0] is inputs and final[1] is targets
preds = analysis.torch_analysis(50000, final[0], final[1])
#print(final[1])
#print(preds)

#tsend.send("Targets : " + str(final[1]))
#tsend.send(str("Predictions :" + str(preds)))
