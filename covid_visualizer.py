import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from covid_data_loader import CovidDataLoader

class CovidVisualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        # Set the style for all plots
        plt.style.use('seaborn')
        sns.set_palette("husl")

    def plot_total_cases_trend(self, countries=None):
        """Plot trend of total cases for selected countries"""
        if countries is None:
            countries = self.data['location'].unique()

        plt.figure(figsize=(12, 6))
        for country in countries:
            country_data = self.data[self.data['location'] == country]
            plt.plot(country_data['date'], country_data['total_cases'], label=country)

        plt.title('Total COVID-19 Cases Over Time')
        plt.xlabel('Date')
        plt.ylabel('Total Cases')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt.gcf()

    def plot_vaccination_progress(self, countries=None):
        """Plot vaccination progress for selected countries"""
        if countries is None:
            countries = self.data['location'].unique()

        latest_data = self.data.groupby('location').last()
        vaccination_data = []

        for country in countries:
            country_data = latest_data.loc[country]
            vaccination_data.append({
                'Country': country,
                'Fully Vaccinated': (country_data['people_fully_vaccinated'] / 
                                   country_data['population'] * 100),
                'Partially Vaccinated': ((country_data['people_vaccinated'] - 
                                        country_data['people_fully_vaccinated']) / 
                                       country_data['population'] * 100)
            })

        df_vac = pd.DataFrame(vaccination_data)
        
        plt.figure(figsize=(10, 6))
        df_vac.plot(x='Country', y=['Fully Vaccinated', 'Partially Vaccinated'], 
                    kind='bar', stacked=True)
        plt.title('Vaccination Progress by Country')
        plt.xlabel('Country')
        plt.ylabel('Percentage of Population')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        return plt.gcf()

    def plot_case_fatality_rate(self, countries=None):
        """Plot case fatality rate for selected countries"""
        if countries is None:
            countries = self.data['location'].unique()

        latest_data = self.data.groupby('location').last()
        plt.figure(figsize=(10, 6))
        
        cfr_data = []
        for country in countries:
            country_data = latest_data.loc[country]
            cfr = (country_data['total_deaths'] / country_data['total_cases'] * 100)
            cfr_data.append({'Country': country, 'CFR': cfr})

        df_cfr = pd.DataFrame(cfr_data)
        sns.barplot(data=df_cfr, x='Country', y='CFR')
        plt.title('Case Fatality Rate by Country')
        plt.xlabel('Country')
        plt.ylabel('Case Fatality Rate (%)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        return plt.gcf()

def main():
    # Load the data
    loader = CovidDataLoader()
    data = loader.load_covid_data()
    
    # Create visualizer
    visualizer = CovidVisualizer(data)
    
    # Create and save plots
    plots = [
        (visualizer.plot_total_cases_trend(), 'total_cases_trend.png'),
        (visualizer.plot_vaccination_progress(), 'vaccination_progress.png'),
        (visualizer.plot_case_fatality_rate(), 'case_fatality_rate.png')
    ]
    
    # Save all plots
    for fig, filename in plots:
        fig.savefig(filename)
        plt.close(fig)
        print(f"Saved {filename}")

if __name__ == "__main__":
    main() 