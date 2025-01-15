from google.cloud import bigquery
import json
import os

# Set up BigQuery client
def initialize_bigquery_client():
    #specify your project id here
    return bigquery.Client(project="measurements-220513")

def fetch_top_sites(client, country_code, date):
    # Query to fetch sites with rank < 1000 for the given country
    query = f"""
    SELECT DISTINCT  
        origin,
        experimental.popularity.rank
    FROM 
        `chrome-ux-report.{country_code}.{date}`
    WHERE 
        experimental.popularity.rank <= 1000
    ORDER BY 
        experimental.popularity.rank;
    """
    query_job = client.query(query)
    return query_job.result()

# Save Results to a JSON File
def save_to_json(results, country_code, filename="top_sites_per_country.json"):
    
    cc_upper = country_code.split('_')[-1].upper()

    # Load existing data if the file exists
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = {}

    # Extract origins and add them to a list
    origins = [row[0] for row in results]
    data[cc_upper] = origins
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def list_country_datasets(client):
    datasets = client.list_datasets("chrome-ux-report")  # Specify the project and dataset
    
    # Extract and filter for datasets starting with 'country_'
    country_datasets = [
        dataset.dataset_id
        for dataset in datasets
        if dataset.dataset_id.startswith("country_")
    ]
    return country_datasets


# Main Function
def main():
    try:
        

        client = initialize_bigquery_client()
        print("Fetching data...")

        countries = list_country_datasets(client)
        date=202412
        
        # # country_code = "country_ad"
        for country_code in countries:
            print(f"Processing {country_code}...")
            results = fetch_top_sites(client, country_code,date)
            save_to_json(results, country_code)
            print(f"Results for {country_code} saved to top_sites_by_country.json")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()