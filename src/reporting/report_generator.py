from fpdf import FPDF


class ReportGenerator:

    def __init__(self):
        self.pdf = FPDF()

    def add_title(self, title):

        self.pdf.set_font("Arial", "B", 16)
        self.pdf.cell(0, 10, title, ln=True)

        self.pdf.ln(5)

    def add_section(self, heading):

        self.pdf.set_font("Arial", "B", 12)
        self.pdf.cell(0, 10, heading, ln=True)

        self.pdf.ln(2)

    def add_text(self, text):

        self.pdf.set_font("Arial", "", 11)
        self.pdf.multi_cell(0, 8, text)

        self.pdf.ln(2)

    def generate_report(
        self,
        dataset_summary,
        quality_report,
        insights,
        output_path="analytics_report.pdf"
    ):

        self.pdf.add_page()

        # Title
        self.add_title("Automated Data Mining & Insight Report")

        # Dataset Overview
        self.add_section("Dataset Overview")

        for key, value in dataset_summary.items():
            self.add_text(f"{key}: {value}")

        # Data Quality
        self.add_section("Dataset Quality Report")

        for key, value in quality_report.items():
            self.add_text(f"{key}: {value}")

        # Insights
        self.add_section("Generated Insights")

        if insights:
            for insight in insights:
                self.add_text(f"- {insight}")
        else:
            self.add_text("No insights generated.")

        # Save file
        self.pdf.output(output_path)

        return output_path