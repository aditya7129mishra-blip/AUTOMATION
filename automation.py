from apscheduler.schedulers.background import BackgroundScheduler

try:
	from .report_generator import generate_pdf
except ImportError:
	from report_generator import generate_pdf


def start_scheduler() -> BackgroundScheduler:
	scheduler = BackgroundScheduler()
	scheduler.add_job(generate_pdf, "interval", minutes=10)
	scheduler.start()
	print("Automation scheduler started.")
	return scheduler
