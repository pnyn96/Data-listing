from app.report_generator import generate_reports

def handler(event, context):
    return generate_reports(event)
