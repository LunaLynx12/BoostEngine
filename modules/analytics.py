import psutil
from .logger import Logger

logger = Logger()

class Analytics:
    def __init__(self):
        self.running_processes = []
        self.running_services = []

    def scan(self):
        # get all running processes
        for process in psutil.process_iter(["name"]):
            self.running_processes.append(process.info["name"])

        # get all running services
        for service in psutil.win_service_iter():
            if service.status() == psutil.STATUS_RUNNING:
                self.running_services.append(service.name())

        logger.log(f"Scanned running processes count: {len(self.running_processes)}")
        logger.log(f"Scanned running services count: {len(self.running_services)}")