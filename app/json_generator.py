def generate_json(df):
    file_path = "/tmp/report.json"
    df.to_json(file_path, orient="records")
    return file_path
