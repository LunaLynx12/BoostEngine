from __init__ import Logger, Analytics, Config, Donation

# Class instantiation
logger = Logger()
analytics = Analytics()
config = Config()
donation = Donation()


def main():
    logger.log("Starting BoostEngine...")
    config.load()
    analytics.scan()

    for process in analytics.running_processes:
        if process not in config.config.get("whitelisted_processes", []):
            logger.log(f"Killing process: {process}")
            # Kill the process
    
    for service in analytics.running_services:
        if service not in config.config.get("whitelisted_services", []):
            logger.log(f"Killing service: {service}")
            # Kill the service

    logger.log("BoostEngine finished.")


if __name__ == "__main__":
    main()
    donation.display()
    