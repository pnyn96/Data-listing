def generate_excel(df):
    path = "/tmp/report.xlsx"
    df.to_excel(path, index=False)
    return path
