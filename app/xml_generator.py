import xml.etree.ElementTree as ET

def generate_xml(df):
    root = ET.Element("Report")

    for _, row in df.iterrows():
        record = ET.SubElement(root, "Record")
        for col, val in row.items():
            child = ET.SubElement(record, col)
            child.text = str(val)

    file_path = "/tmp/report.xml"
    ET.ElementTree(root).write(file_path)
    return file_path
