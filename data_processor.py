import json
from pathlib import Path

SALES_DATA_PATH = Path(__file__).parent / "data" / "sales.json"


def load_sales_data():
	with open(SALES_DATA_PATH, "r", encoding="utf-8") as file:
		return json.load(file)


def calculate_sales(data):
	total = 0

	for item in data:
		item["total"] = item["quantity"] * item["price"]
		total += item["total"]

	return total
