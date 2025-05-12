
# COVID-19 Data Dashboard

A data visualization dashboard for COVID-19 statistics, built with React, TypeScript, Tailwind CSS, and recharts.

## Features

- Interactive charts for COVID-19 metrics (cases, deaths, vaccinations)
- Country selection for comparative analysis
- Time range filtering
- Responsive design for desktop and mobile viewing

## Live Demo

Visit the [live demo](https://lovable.dev/projects/e4ecd53d-b3c2-4309-b575-c438b9c0a593)

## Project Setup

### Prerequisites

- Node.js and npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

### Installation

1. Clone the repository:
```sh
git clone https://github.com/yourusername/covid-dashboard.git
cd covid-dashboard
```

2. Install dependencies:
```sh
npm install
```

3. Start the development server:
```sh
npm run dev
```

The application will be available at `http://localhost:5173/`

## Data Source

The project includes a sample COVID-19 dataset in `public/data/covid_data.csv`. This is a simplified dataset for demonstration purposes.

For real-world use, you can replace this file with updated COVID-19 data from:

- [Our World in Data COVID-19 dataset](https://github.com/owid/covid-19-data/tree/master/public/data)
- [Johns Hopkins University CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)

To use your own data, replace the CSV file while maintaining the same column structure, or update the data loader in `src/lib/data-loader.ts` to match your data format.

## Python Data Analysis Script

The repository also includes a Python script (`covid_data_analyzer.py`) that can be used for offline data analysis. This script provides similar functionality to the web dashboard but as a command-line tool.

### Using the Python Script

1. Install required packages:
```sh
pip install pandas numpy matplotlib seaborn
```

2. Run the script:
```sh
python covid_data_analyzer.py
```

3. When prompted, you can either:
   - Press Enter to use the built-in sample data
   - Provide the path to your own COVID-19 data CSV file

## License

MIT