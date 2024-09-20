import os
import gzip
import shutil
import pyspark
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Unzip and Store Reviews") \
    .getOrCreate()

# Paths
input_folder = 'E:\\1996-2023\\'  # Folder containing .gz files
temp_folder = 'E:\\temp\\'  # Temporary folder to store unzipped files
output_folder = 'E:\\data\\'  # Folder to save output data

# Step 1: Unzip, process JSONL, store in Parquet, and delete unzipped files
def unzip_process_store(input_folder, temp_folder, output_folder):
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".gz"):
            print(file)
            # gz_file_path = os.path.join(input_folder, file)
            # jsonl_file_path = os.path.join(temp_folder, file[:-3])  # Remove .gz extension

            # # Unzip the .gz file
            # with gzip.open(gz_file_path, 'rb') as f_in:
            #     with open(jsonl_file_path, 'wb') as f_out:
            #         shutil.copyfileobj(f_in, f_out)

            # # Read the unzipped JSONL file
            # df = spark.read.json(jsonl_file_path)
            
            # # Write the DataFrame to Parquet format
            # parquet_output_path = os.path.join(output_folder, file[:-6])  # Remove .jsonl.gz extension
            # df.write.parquet(parquet_output_path)

            # # Delete the unzipped JSONL file
            # os.remove(jsonl_file_path)

# Execute the process
unzip_process_store(input_folder, temp_folder, output_folder)

# Optional: Delete temp folder after processing all files
if os.path.exists(temp_folder) and not os.listdir(temp_folder):
    shutil.rmtree(temp_folder)

# Stop Spark session after processing
spark.stop()
