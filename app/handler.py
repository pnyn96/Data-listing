from app.report_generator import generate_report

def handler(event, context):
    print("Received event:", event)
    return generate_report(event)
