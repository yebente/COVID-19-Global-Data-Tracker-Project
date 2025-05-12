# COVID-19 Data Analysis Project

A Python-based data analysis and visualization tool for COVID-19 statistics. This project provides comprehensive analysis and visualization of COVID-19 data, including cases, deaths, vaccination rates, and other key metrics across different countries.

## Features

- Automated data loading and preprocessing using pandas
- Comprehensive data analysis capabilities:
  - Country-wise comparisons
  - Time series analysis
  - Vaccination tracking
  - Mortality rate calculations
- Advanced visualizations using matplotlib and seaborn:
  - Total cases trends over time
  - Vaccination progress by country
  - Case fatality rates
  - Interactive data exploration
- Robust error handling and data validation
- Easy-to-use Python classes for extensible analysis

## Project Structure

```
covid-data-analysis/
│
├── covid_data_loader.py     # Data loading and preprocessing
├── covid_visualizer.py      # Data visualization functions
├── covid_data.csv          # Sample COVID-19 dataset
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

The project requires the following Python packages (specified in requirements.txt):
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0

### Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/covid-data-analysis.git
cd covid-data-analysis
```

2. Create and activate a virtual environment (recommended):
```sh
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```sh
# Make sure you're in the project directory and your virtual environment is activated
pip install -r requirements.txt
```

### Verifying Installation

To verify that everything is installed correctly, you can run:
```sh
python -c "import pandas as pd; import numpy as np; import matplotlib.pyplot as plt; import seaborn as sns; print('All packages installed successfully!')"
```

## Usage

### Basic Analysis

Run the data loader script for basic analysis:
```sh
python covid_data_loader.py
```

This will display:
- Total number of data entries
- List of available countries
- Latest data date
- Total cases by country
- Vaccination progress statistics

### Generating Visualizations

Run the visualizer script to create plots:
```sh
python covid_visualizer.py
```

This generates three visualization files:
- `total_cases_trend.png`: Time series plot of total cases
- `vaccination_progress.png`: Stacked bar chart of vaccination status
- `case_fatality_rate.png`: Bar plot of mortality rates

### Custom Analysis

You can import the classes in your own Python scripts:

```python
from covid_data_loader import CovidDataLoader
from covid_visualizer import CovidVisualizer

# Load and preprocess data
loader = CovidDataLoader()
data = loader.load_covid_data()

# Create custom visualizations
visualizer = CovidVisualizer(data)

# Generate specific plots
visualizer.plot_total_cases_trend(['United States', 'India', 'Kenya'])
visualizer.plot_vaccination_progress()
visualizer.plot_case_fatality_rate()
```

## Data Source

The project uses a CSV file (`covid_data.csv`) containing the following COVID-19 statistics:
- Daily and cumulative case counts
- Death statistics
- Vaccination data
- Healthcare system metrics (ICU patients, hospitalizations)
- Population demographics
- Economic indicators

For real-world use, you can replace this file with updated COVID-19 data from:
- [Our World in Data COVID-19 dataset](https://github.com/owid/covid-19-data/tree/master/public/data)
- [Johns Hopkins University CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)

## Troubleshooting

If you encounter any issues:

1. Make sure your virtual environment is activated
2. Verify Python version: `python --version` (should be 3.8 or higher)
3. Check installed packages: `pip list`
4. If you need to install packages individually:
   ```sh
   pip install pandas>=2.0.0
   pip install numpy>=1.24.0
   pip install matplotlib>=3.7.0
   pip install seaborn>=0.12.0
   ```
5. If matplotlib shows errors, you might need additional system libraries:
   - On Ubuntu/Debian: `sudo apt-get install python3-tk`
   - On CentOS/RHEL: `sudo yum install python3-tkinter`
   - On Windows: Usually comes with Python installation

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT