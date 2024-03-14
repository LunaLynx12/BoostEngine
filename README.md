# BoostEngine

BoostEngine is a Python-based optimization tool that utilizes the `psutil` library to optimize system performance by managing processes and services.

## Features

- Optimizes system performance by managing running processes and services.
- Uses a configuration system based on JSON for easy customization.

## Requirements

- Python 3.x
- `psutil` library (install via `pip install psutil`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Cathie02/BoostEngine.git
    ```

2. Install the required dependencies:
    ```bash
    pip install psutil
    ```

## Usage

1. Configure BoostEngine using the `config.json` file.
2. Run main.py to start BoostEngine:
    ```bash
    python main.py
    ```
## Configuration
The configuration of BoostEngine is managed through the `config.json` file. Modify this file to customize the behavior of BoostEngine according to your preferences.

Example configuration (`config.json`):

    ```json
    {
        "whitelisted_processes": [
            "process1.exe",
            "process2.exe"
        ],
        "whitelisted_services": [
            "service1",
            "service2"
        ]
    }
    ```

## Contributing
Contributions to BoostEngine are welcome! Here's how you can contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Create a new Pull Request.

## License
This project is licensed under the GPL-3.0 License - see the [LICENSE](https://raw.githubusercontent.com/Cathie02/BoostEngine/main/LICENSE.md) file for details.
