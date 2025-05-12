import pandas as pd
from typing import List, Dict, Any
import logging
from pathlib import Path

class CovidDataLoader:
    def __init__(self, data_path: str = 'covid_data.csv'):
        self.data_path = data_path
        self.logger = logging.getLogger(__name__)

    def load_covid_data(self) -> pd.DataFrame:
        """
        Load COVID data from a CSV file into a pandas DataFrame.
        
        Returns:
            pd.DataFrame: DataFrame containing COVID-19 data
        """
        try:
            df = pd.read_csv(self.data_path)
            
            # Convert date column to datetime
            df['date'] = pd.to_datetime(df['date'])
            
            # Convert numeric columns to appropriate types
            numeric_columns = [
                'total_cases', 'new_cases', 'total_deaths', 'new_deaths',
                'reproduction_rate', 'icu_patients', 'hosp_patients',
                'total_tests', 'new_tests', 'total_vaccinations',
                'people_vaccinated', 'people_fully_vaccinated', 'new_vaccinations',
                'population', 'median_age', 'gdp_per_capita', 'life_expectancy',
                'human_development_index'
            ]
            
            for col in numeric_columns:
                if col in df.columns:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
            
            self.logger.info(f"Successfully loaded {len(df)} rows of COVID-19 data")
            return df
            
        except Exception as e:
            self.logger.error(f"Error loading COVID data: {str(e)}")
            raise

def example_data_analysis():
    """
    Example function showing how to use the COVID data loader and perform basic analysis
    """
    # Initialize the data loader
    loader = CovidDataLoader()
    
    try:
        # Load the data
        df = loader.load_covid_data()
        
        print(f"\nLoaded {len(df)} COVID-19 data entries")
        
        # Get unique countries
        countries = df['location'].unique()
        print(f"\nAvailable countries: {', '.join(countries)}")
        
        # Get the latest date in the dataset
        latest_date = df['date'].max()
        print(f"\nData up to: {latest_date.strftime('%Y-%m-%d')}")
        
        # Calculate total cases by country (latest numbers)
        total_cases = df.groupby('location')['total_cases'].last()
        
        print('\nTotal cases by country:')
        for country, cases in total_cases.items():
            print(f"{country}: {cases:,.0f}")
            
        # Additional analysis examples
        print("\nSummary Statistics:")
        print("\nVaccination Progress:")
        latest_data = df.groupby('location').last()
        for country in countries:
            country_data = latest_data.loc[country]
            vaccination_rate = (country_data['people_fully_vaccinated'] / 
                              country_data['population'] * 100)
            print(f"{country}: {vaccination_rate:.1f}% fully vaccinated")
            
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Run example analysis
    example_data_analysis() 