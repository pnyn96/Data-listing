from app.report_generator import generate_report

def handler(event, context):
    return generate_report(event)
