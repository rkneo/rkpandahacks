import json
import os
import tempfile
import argparse
import io
from io import StringIO
from datetime import datetime
import pandas as pd
import zipfile

#chunk huge dataframes
def chunk_d(filename,df,FILE_CHUNK_SIZE):
    FILE_CHUNK_SIZE = 10000
    row=0
    while row < len(sales_df):
        sales_df_subset = sales_df[row:row+FILE_CHUNK_SIZE]
        filename= os.path.join(tempfile.tempdir,'{0}-part-{1:0>5}'.format(sales_file, i) +'.json')
        with open(filename, 'w') as out_json_file:
            sales_df_subset.to_json(path_or_buf=out_json_file, orient="records",lines=True)
        i+=1
        row += FILE_CHUNK_SIZE
        z = zipfile.ZipFile(filename+'.zip','w')
        z.write(filename, compress_type=zipfile.ZIP_DEFLATED)
        z.close()

#split Json files        
def split_json(jsontxt,sales_file):
    record_chunks = 10000
    json_obj_list = json.loads(jsontxt.decode("utf-8"))
    json_chunk_list = [json_obj_list[i:i+record_chunks] for i  in range(0, len(json_obj_list), record_chunks)]
    i=0
    filelist =[]
    for json_obj in json_chunk_list:
        filename= os.path.join(tempfile.tempdir,'{0}-part-{1:0>5}'.format(sales_file, i) +'.json')
        filelist.append(filename)
        with open(filename, 'w') as out_json_file:
             json.dump(json_obj, out_json_file,indent=4)
        i= i+1
    return json_chunk_list            


