from __init__ import __version__, Logger, Confirmation, Analytics, Config, Donation

# Class instantiation
logger = Logger()
confirmation = Confirmation()
analytics = Analytics()
config = Config()
donation = Donation()


def main():
    logger.log(f"Starting BoostEngine v{__version__} ...")
    confirmation.ask()
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
    