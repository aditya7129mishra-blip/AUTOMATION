from fastapi import FastAPI

try:
	from .automation import start_scheduler
	from .report_generator import generate_pdf
except ImportError:
	from automation import start_scheduler
	from report_generator import generate_pdf

app = FastAPI(
	title="Enterprise Python Automation",
	version="1.0",
)


@app.get("/")
def home():
	return {"message": "Enterprise Automation API is running"}


@app.get("/generate-report")
def generate_report():
	file = generate_pdf()
	return {
		"message": "Report generated successfully",
		"file": file,
	}


@app.get("/start-automation")
def start_automation():
	scheduler = getattr(app.state, "scheduler", None)
	if scheduler is None or not scheduler.running:
		scheduler = start_scheduler()
		app.state.scheduler = scheduler

	return {"message": "Automatic report generation started"}
