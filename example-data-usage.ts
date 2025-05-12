
import { loadCovidData } from "./lib/data-loader";

// Example function showing how to load and use COVID data
async function exampleDataUsage() {
  // Load data from CSV (with fallback to sample data)
  const data = await loadCovidData();
  
  console.log(`Loaded ${data.length} COVID-19 data entries`);
  
  // Example operations with the data
  const countries = new Set(data.map(entry => entry.location));
  console.log(`Available countries: ${Array.from(countries).join(', ')}`);
  
  // Get the latest date in the dataset
  const latestDate = new Date(Math.max(...data.map(entry => new Date(entry.date).getTime())));
  console.log(`Data up to: ${latestDate.toLocaleDateString()}`);
  
  // Example aggregation - total cases by country
  const totalCasesByCountry = data.reduce((acc, entry) => {
    if (!acc[entry.location]) {
      acc[entry.location] = entry.total_cases;
    } else if (entry.total_cases > acc[entry.location]) {
      acc[entry.location] = entry.total_cases;
    }
    return acc;
  }, {} as Record<string, number>);
  
  console.log('Total cases by country:');
  Object.entries(totalCasesByCountry).forEach(([country, cases]) => {
    console.log(`${country}: ${cases?.toLocaleString() || 'N/A'}`);
  });
}

export { exampleDataUsage };
