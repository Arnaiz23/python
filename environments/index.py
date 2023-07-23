import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Data fetched successfully!!")
        print(response.text)
    else:
        print(f"Failed to fetch data. Status code {response.status_code}")

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    fetch_data(url)
