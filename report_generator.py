from datetime import datetime
from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table

try:
	from .data_processor import calculate_sales, load_sales_data
except ImportError:
	from data_processor import calculate_sales, load_sales_data

REPORTS_DIR = Path(__file__).parent / "reports"


def generate_pdf():
	data = load_sales_data()
	total_sales = calculate_sales(data)
	generated_at = datetime.now()

	REPORTS_DIR.mkdir(parents=True, exist_ok=True)
	filename = REPORTS_DIR / (
		f"sales_report_{generated_at.strftime('%Y%m%d_%H%M%S')}.pdf"
	)

	pdf = SimpleDocTemplate(str(filename), pagesize=A4)
	styles = getSampleStyleSheet()
	elements = [
		Paragraph("Automated Sales Report", styles["Title"]),
		Paragraph(
			f"Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S')}",
			styles["Normal"],
		),
	]

	table_data = [["Product", "Quantity", "Price", "Total"]]
	for item in data:
		table_data.append(
			[item["product"], item["quantity"], item["price"], item["total"]]
		)
	table_data.append(["", "", "Grand Total", total_sales])

	elements.append(Table(table_data))
	pdf.build(elements)
	return str(filename)
