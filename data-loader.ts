
import { CovidData } from "@/types/covid";
import { sampleCovidData } from "./covid-data";

// Function to load COVID data from a CSV file
export async function loadCovidData(useSampleData: boolean = false): Promise<CovidData[]> {
  if (useSampleData) {
    return Promise.resolve(sampleCovidData);
  }

  try {
    const response = await fetch('/data/covid_data.csv');
    if (!response.ok) {
      console.error('Failed to fetch CSV data:', response.statusText);
      return sampleCovidData; // Fallback to sample data
    }

    const csvText = await response.text();
    return parseCSV(csvText);
  } catch (error) {
    console.error('Error loading COVID data:', error);
    return sampleCovidData; // Fallback to sample data
  }
}

// Parse CSV text into CovidData objects
function parseCSV(csvText: string): CovidData[] {
  const lines = csvText.trim().split('\n');
  const headers = lines[0].split(',');
  
  return lines.slice(1).map(line => {
    const values = line.split(',');
    const entry: Record<string, any> = {};
    
    headers.forEach((header, index) => {
      const value = values[index];
      
      // Convert numeric values
      if (value && !isNaN(Number(value)) && header !== 'iso_code' && header !== 'continent' && header !== 'location' && header !== 'date') {
        entry[header] = Number(value);
      } else {
        entry[header] = value;
      }
    });
    
    return entry as CovidData;
  });
}
