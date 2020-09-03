import pandas as pd

def chunk_d(filename,df,FILE_CHUNK_SIZE):
    row=0
    while len(df) >= row :
        increment_row = FILE_CHUNK_SIZE + row
        row +=1 if row > 0 else row
        df_subset = df[row:increment_row]
        filename= os.path.join(tempfile.tempdir,'{0}-part-{1:0>5}'.format(filename, i) +'.json')
        with open(filename, 'w') as out_json_file:
            df_subset.to_json(path_or_buf=out_json_file, orient="records",lines=True)
        i+=1
        row=increment_row
        z = zipfile.ZipFile(filename+'.zip','w')
        z.write(filename, compress_type=zipfile.ZIP_DEFLATED)
        z.close()


