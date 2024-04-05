import threading, requests, os

def find_even_numbers():
    even_numbers = [num for num in range(30, 50) if num % 2 == 0]
    print("Even numbers:", even_numbers)

def find_odd_numbers():
    odd_numbers = [num for num in range(30, 50) if num % 2 != 0]
    print("Odd numbers:", odd_numbers)

if __name__ == "__main__":
    even_thread = threading.Thread(target=find_even_numbers)
    odd_thread = threading.Thread(target=find_odd_numbers)

    even_thread.start()
    even_thread.join()

    odd_thread.start()
    odd_thread.join()

    
    
    print("Done!")

def download_mp3(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(os.path.dirname(__file__), os.path.basename(url))
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {filename} successfully.")
        else:
            print(f"Failed to download {url}. HTTP Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    mp3_files = [
        "http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3",
        "http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Sevish_-__nbsp_.mp3",
        "http://codeskulptor-demos.commondatastorage.googleapis.com/descent/background%20music.mp3"
    ]

    threads = []

    for url in mp3_files:
        thread = threading.Thread(target=download_mp3, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("All downloads completed.")