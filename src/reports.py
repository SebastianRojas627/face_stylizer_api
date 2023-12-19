import csv
import io

class Reports:
    def __init__(self):
        self.reports = []

    def add_prediction(self, prediction):
        self.reports.append(prediction)

    def generate_report(self):
        if not self.reports:
            return "No predictions made yet, reports are empty!"
        
        csv_stream = io.StringIO()
        writer = csv.DictWriter(
            csv_stream, 
            fieldnames=["Time and Date of Query", "File Name", "Size (bytes)", "Processing Time (s)", "Model", "Message"],
            quoting=csv.QUOTE_ALL
            )
        writer.writeheader()
        for row in self.reports:
            writer.writerow(row)

        final_report = csv_stream.getvalue()
        return final_report
        