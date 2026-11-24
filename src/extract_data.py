import requests
import json
from pathlib import Path
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = "16b652567a3b3409652eb2ad1a7f9bf3"
url = f'https://api.openweathermap.org/data/2.5/weather?q=Sao Paulo,BR&units=metric&lang=pt_br&appid={API_KEY}'

def extract_weather_data(url: str) -> list:
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error("Erro na requisição: %s", response.status_code)
        return []

    if not data:
        logging.warn("Nenhum dado encontrado")
        return []

    output_path = "data/weather_data.json"
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Dados salvos em: {output_path}")
    return data

extract_weather_data(url)
