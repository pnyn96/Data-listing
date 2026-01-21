import pandas as pd
from app.s3_reader import read_json, read_csv
from app.pdf_generator import generate_pdf
from app.excel_generator import generate_excel
from app.salesforce_uploader import upload_to_salesforce

def generate_report(event):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    json_key = event["Records"][0]["s3"]["object"]["key"]

    # Read JSON instructions
    instructions = read_json(bucket, json_key)

    # Read source data
    data = pd.read_csv(
        read_csv("source-data-bucket", "salesforce/data.csv")
    )

    # Apply JSON rules
    if "filter" in instructions:
        data = data.query(instructions["filter"])

    if "columns" in instructions:
        data = data[instructions["columns"]]

    output_type = instructions.get("output", "excel")

    if output_type == "pdf":
        file_path = generate_pdf(data)
    else:
        file_path = generate_excel(data)

    # Upload back to Salesforce
    upload_to_salesforce(file_path)

    return {"status": "SUCCESS"}
