def generate_html(df):
    file_path = "/tmp/report.html"
    df.to_html(file_path, index=False)
    return file_path
