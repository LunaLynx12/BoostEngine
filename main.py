import webbrowser
import pystray
from PIL import Image
from __init__ import __version__, Logger, Analytics, Config, Donation

# Class instantiation
logger = Logger()
analytics = Analytics()
config = Config()
donation = Donation()

def on_quit_clicked(icon, item):
    if str(item) == "Start":
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

    elif str(item) == "Pause":
        logger.log("Paused BoostEngine...")
        # Add pause functionality here
        logger.log("BoostEngine paused.")

    elif str(item) == "About":
        # open url in web browser
        logger.log("Opening donation page...")
        webbrowser.open("https://github.com/Cathie02/BoostEngine")

    elif str(item) == "Quit":
        icon.stop()

def main():
    image = Image.open("icon.ico")

    # Create the tray icon
    icon = pystray.Icon("BoostEngine Icon", image, menu=pystray.Menu(
        pystray.MenuItem("Start", on_quit_clicked),
        pystray.MenuItem("Pause", on_quit_clicked),
        pystray.MenuItem("About", on_quit_clicked),
        pystray.MenuItem("Quit", on_quit_clicked)
    ), title=f"BoostEngine v{__version__}")

    icon.run()


if __name__ == "__main__":
    main()