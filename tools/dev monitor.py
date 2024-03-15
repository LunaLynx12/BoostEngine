import psutil
import time
import msvcrt

def get_running_processes():
    processes = set()
    for process in psutil.process_iter():
        try:
            process_name = process.name()
            if process_name.endswith(".exe"):
                processes.add(process_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return processes

def get_running_services():
    services = []
    for service in psutil.win_service_iter():
        try:
            if service.status() == "running":
                services.append(service.name())
        except psutil.NoSuchService:
            pass
    return services

def monitor_processes_and_services():
    print("Monitoring started...")

    old_processes = get_running_processes()
    old_services = get_running_services()

    try:
        while True:
            if msvcrt.kbhit():
                key = ord(msvcrt.getch())
                if key == 27:
                    print("Quitting...")
                    break

            new_processes = get_running_processes()
            for process in new_processes - old_processes:
                print(f"New process detected: {process}")
            
            for process in old_processes - new_processes:
                print(f"Process closed: {process}")

            old_processes = new_processes

            new_services = get_running_services()
            for service in set(new_services) - set(old_services):
                print(f"New service detected: {service}")
            
            for service in set(old_services) - set(new_services):
                print(f"Service stopped: {service}")

            old_services = new_services

            time.sleep(1)
    
    except KeyboardInterrupt:
        print("Quitting due to keyboard interrupt...")

if __name__ == "__main__":
    monitor_processes_and_services()
