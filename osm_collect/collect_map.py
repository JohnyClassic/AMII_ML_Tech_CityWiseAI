import pandas as pd
import osmnx as ox
import numpy as  np

files_dir = "dataset/"
filename = files_dir + "other_clean_df.csv"
df = pd.read_csv(filename)
df['subway_500'] = None
df['natural_500'] = None
#df['leisure_500'] = None
df["geom"] =  df["latitude"].map(str)  + ',' + df['longitude'].map(str)
distance = 500
tag_subway = {'building': ['train_station']}
tag_natural = {'natural': ['beach', 'park', 'water']}
tag_amenities = {'amenity': ['restaurant', 'pub', 'hotel'],
        'building': ['hotel','transportation','airport'],'store':'mall',
        'tourism': 'hotel'}
#tag_leisure = {
        #'leisure':['park','water-park','amusement-park','theme-park','zoo','stadium']}
batch_list =np.arange(start = 18800, stop = df.shape[0],
           step = 200)

ox.config(log_console=True, use_cache=True) 
          #overpass_endpoint="https://maps.mail.ru/osm/tools/overpass/api/interpreter")
for batch in range(len(batch_list)-1):
        i = batch_list[batch]
        j = batch_list[batch+1]
        for element, row in df.iloc[i:j,:].iterrows():
                ox.config(log_console=True, use_cache=True)
                gdf_amenities = ox.geometries.geometries_from_point((df.iloc[element,:]['latitude'],df.iloc[element,:]['longitude']),dist = distance, tags = tag_amenities) # Boundary to search within
                df.loc[element, 'amenities_500']  = gdf_amenities.shape[0]
                gdf_amenities = ox.geometries.geometries_from_point((df.iloc[element,:]['latitude'],
                                                                     df.iloc[element,:]['longitude']),
                                                                    dist = distance, tags = tag_subway) # Boundary to search within
                df.loc[element, 'subway_500']  = gdf_amenities.shape[0]
                gdf_leisure = ox.geometries.geometries_from_point((df.iloc[element,:]['latitude'],df.iloc[element,:]['longitude']),dist = distance, tags = tag_natural) # Boundary to search within																			dist=distance, tags=tags)
                df.loc[element, 'natural_500']  = gdf_leisure.shape[0]
        #subset_data = df[['id','geom', 'amenities_500', 'leisure_500']].iloc[i:j,:]
        subset_data = df[['id','geom', 'amenities_500', 'subway_500', 'natural_500']].iloc[i:j,:]
        print('Finished Batch: ', batch)
        subset_data.to_csv(f'collected_map_additional/batch-{i}-{j}.csv', index=False)

