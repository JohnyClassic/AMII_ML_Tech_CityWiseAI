#%%
import pandas as pd
import glob, os 

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("collected_map", "*.csv"))))

df.to_csv("merged_map.csv", index=False)
# %%
import pandas as pd
import glob, os 

df = pd.concat(map(pd.read_csv, glob.glob(os.path.join("collected_map_subway", "*.csv"))))

df.to_csv("merged_map_subway.csv", index=False)
# %%
