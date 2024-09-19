import pandas as pd
import json
import requests
from bs4 import BeautifulSoup

# CSV
df = pd.read_csv("RESULTS.csv")

# Web Scraping
def scrape_secteur_info(client_name):
    url = f"https://www.google.com/search?q=site:charika.ma {client_name}"
    url = f"https://www.google.com/search?q=site:telecontact.ma {client_name}"
    url = f"https://www.google.com/search?q=site:linkedin.com {client_name}"
    url = f"https://yandex.com/search/?text={client_name}"
    url = f"https://www.google.com/search?q={client_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.text
    return data

# AI API
def send_to_ai_api(prompt):
    api_url = "https://a.picoapps.xyz/ask-ai"
    response = requests.get(api_url, params={'prompt': prompt})
    return response.json()['response']

n = 0   

df.drop_duplicates(subset='CODE_CLIENT', inplace=True)



# Loop on DataFrame
for index, row in df.iterrows():
    if row['Secteur Activité'] == "Non classifié" or row['Sous-secteur'] == "Non classifié" or row['Sous-sous-secteur'] == "Non classifié":
        # Scraping raw data...
        scraped_data = scrape_secteur_info(row['NOM_CLIENT'])
        # print(scraped_data)
        
        # Prompt
        prompt = f"Please classify the following business information and return for me a json that contain ('secteur-activité','sous-secteur','sous-sous-secteur'); The business informations : {scraped_data}"
        
        # AI API call
        ai_response = send_to_ai_api(prompt)

        try:
            # AI to JSON
            ai_response = json.loads(ai_response)

            try:
                # Extract
                secteur = ai_response['secteur-activité']
                df.at[index, 'Secteur Activité'] = secteur
            except KeyError:
                print(f"{index+2}=> Missing 'secteur-activité' for {row['NOM_CLIENT']}")

            try:
                sous_secteur = ai_response['sous-secteur']
                df.at[index, 'Sous-secteur'] = sous_secteur
            except KeyError:
                print(f"{index+2}=> Missing 'sous-secteur' for {row['NOM_CLIENT']}")

            try:
                sous_sous_secteur = ai_response['sous-sous-secteur']
                df.at[index, 'Sous-sous-secteur'] = sous_sous_secteur
            except KeyError:
                print(f"{index+2}=> Missing 'sous-sous-secteur' for {row['NOM_CLIENT']}")

        except Exception as e:
            print(f"{index+2}=> Error parsing AI response for {row['NOM_CLIENT']}: {e}")
            print("Skipping to the next record...")
            df.to_csv("RESULTS.csv", index=False)
            continue
        

        n += 1    
        df.to_csv("RESULTS.csv", index=False)
        # print(f"{index+2} is done ✅ : {secteur} - {sous_secteur} - {sous_sous_secteur} for {row['NOM_CLIENT']}")

# Save the CSV
df.to_csv("RESULTS.csv", index=False)

print("Processing complete!")
print(f"Total number of rows processed: {n}")
