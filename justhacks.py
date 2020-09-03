import pandas as pd

#chunk huge dataframes
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


