## gpt4.py
import requests

class GPT4:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.gpt4.com"

    def filter_content(self, content: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "content": content
        }
        response = requests.post(f"{self.base_url}/filter", headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["filtered_content"]
        else:
            raise Exception("Failed to filter content")

    def improve_model(self, feedback: str) -> None:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "feedback": feedback
        }
        response = requests.post(f"{self.base_url}/improve", headers=headers, json=data)
        if response.status_code != 200:
            raise Exception("Failed to improve model")
