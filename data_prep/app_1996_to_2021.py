import pandas as pd
import zipfile

# 1996 Data to 2021 CTs

# the apportionment table
crosswalk_csv = 'ct_1996_2021.csv'

# the csv with source tract data to apportioned
data_csv = 'data96.csv'

# read in the data
df = pd.read_csv(data_csv, dtype = {"CMA": str, "CT": str})

# create ctuid in data_csv
ctuidcol = "ctuid"
df[ctuidcol] = df["CMA"] + df["CT"]


# names of columns we ewant ot apportion
fields = [
    ["pop96","w_pop",None]
]

# output file name
output_file_name = 'data_from_1996_into_2021_CTs.csv'

# read in crosswalk table
cw = pd.read_csv(crosswalk_csv, dtype = {"source_ctuid": str, "target_ctuid": str})

# joining the two input tables
merge_cw_df = cw.merge(df, how = "inner", left_on = "source_ctuid", right_on = ctuidcol)

print(merge_cw_df)

# loop over each field, multiplying by the apportionment weight
output_fields = []
for f in fields:
	name = f[0]
	weight = f[1]
	mult = f[2]
	print(f)
	if f[2] is None:
		merge_cw_df[name + "_" + weight] = merge_cw_df[weight] * merge_cw_df[name]
		output_fields.append(name + "_" + weight)
	else:
		merge_cw_df[name + "_" + weight] = merge_cw_df[weight] * merge_cw_df[name] * merge_cw_df[mult]
		output_fields.append(name + "_" + weight)
	
# group by the target census tracts, summing by the wanted fields
df_96_in_21 = merge_cw_df.groupby(["target_ctuid"]).sum()
df_96_in_21 = df_96_in_21[output_fields]

for f in fields:
	name = f[0]
	weight = f[1]
	mult = f[2]
	if mult is not None:
		df_96_in_21[name + "_" + weight] = df_96_in_21[name + "_" + weight] / df_96_in_21[mult + "_" + weight]

df_96_in_21["pop96"] = df_96_in_21["pop96_w_pop"].astype(int)
del df_96_in_21["pop96_w_pop"]


print(df_96_in_21)



# 2021 Data from GAF

zf = zipfile.ZipFile("data/stats-can-gaf/2021_92-151_X.zip")
df = pd.read_csv(zf.open("2021_92-151_X.csv"),encoding = "ISO-8859-1", dtype = {"CTUID_SRIDU": str})

df = df[["CTUID_SRIDU","DBPOP2021_IDPOP2021"]]

df = df.round(0).groupby(['CTUID_SRIDU'])['DBPOP2021_IDPOP2021'].sum().reset_index()

df.columns = ["ctuid","pop21"]
df = df.set_index('ctuid')

df = df_96_in_21.join(df)

print(df.sort_values("pop21"))

