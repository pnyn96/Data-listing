import pandas as pd
from app.s3_reader import read_json, read_csv
from app.html_generator import generate_html
from app.json_generator import generate_json
from app.excel_generator import generate_excel
from app.pdf_generator import generate_pdf
from app.xml_generator import generate_xml
from app.salesforce_uploader import upload_to_salesforce

SOURCE_DATA_BUCKET = "source-data-bucket"
SOURCE_DATA_KEY = "salesforce/data.csv"

def generate_reports(event):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    json_key = event["Records"][0]["s3"]["object"]["key"]

    instructions = read_json(bucket, json_key)
    requested_outputs = instructions.get("additional_outputs", [])

    # Read data
    data_bytes = read_csv(SOURCE_DATA_BUCKET, SOURCE_DATA_KEY)
    df = pd.read_csv(pd.io.common.BytesIO(data_bytes))

    # Apply rules
    if "filter" in instructions:
        df = df.query(instructions["filter"])

    if "columns" in instructions:
        df = df[instructions["columns"]]

    generated_files = []

    # 🔹 DEFAULT OUTPUTS (ALWAYS)
    generated_files.append(generate_html(df))
    generated_files.append(generate_json(df))

    # 🔹 OPTIONAL OUTPUTS
    if "excel" in requested_outputs:
        generated_files.append(generate_excel(df))

    if "pdf" in requested_outputs:
        generated_files.append(generate_pdf(df))

    if "xml" in requested_outputs:
        generated_files.append(generate_xml(df))

    # Upload all files
    for file in generated_files:
        upload_to_salesforce(file, instructions["record_id"])

    return {
        "status": "SUCCESS",
        "generated_files": generated_files
    }
