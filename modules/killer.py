import os
import psutil

class Killer:
    def __init__(self):
        # Initialization code for the Killer class
        pass

    def kill_process(self, process_id):
        # Kill the process
        try:
            psutil.Process(process_id).terminate()
            print(f"Terminated process with PID: {process_id}")
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            print(f"Access denied to terminate process with PID: {process_id}")
            pass

    def kill_service(self, service_name):
        # Kill the service
        try:
            os.system(f"sc stop {service_name} > nul")
            print(f"Stopped service: {service_name}")
        except Exception as e:
            print(f"Failed to stop service: {service_name}")
            print(e)
            pass
        
