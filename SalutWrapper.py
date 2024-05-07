import requests
import threading
import time
import uuid

class SalutWrapper:
    def __init__(self, api_key, scope='SALUTE_SPEECH_PERS'):
        self.bearer_token = 0
        self.url = 'https://ngw.devices.sberbank.ru:9443/api/v2/oauth'
        self.speach_url = 'https://smartspeech.sber.ru/rest/v1/speech:recognize'
        self.tts_url = "https://smartspeech.sber.ru/rest/v1/text:synthesize"
        self.scope = scope
        self.api_key = api_key
        self.uuid = self.generate_uuids()



    def start(self):
        task_thread = threading.Thread(target=self.poll_token)
        task_thread.start()
        return task_thread 

    def poll_token(self):
        
        headers = {
            'Authorization': 'Basic ' + self.api_key,
            'RqUID': self.uuid,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Define the data to be sent
        data = {
            'scope': self.scope
        }

        while True:
            print("Starting to get a new bearer token: ")

            self.update_token(headers, data)

            print("Starting to get a new bearer token: ")

            time.sleep(1500)

    def update_token(self, headers, data):
        try:
            response = requests.post(self.url, headers=headers, data=data, verify=False)
            if response.status_code == 200:

                response_data = response.json()
                self.bearer_token = response_data['access_token']

            else:
                print("Access token was not obtained. Please check your api_key")
        except Exception as e:
            print(f"An error occurred: {e}")
            

    def generate_uuids(self):
        random_uuid = str(uuid.uuid4())

        return str(random_uuid)
    
    def check_token(self):
        if self.bearer_token == 0:
            print("No token yet")
            time.sleep(5)

    def audio_to_text(self, audio_file_path, content_type):
        self.check_token()
        speach_headers = {
            'Authorization': 'Bearer ' + str(self.bearer_token),
            'Content-Type': content_type
        }

        try:
            with open(audio_file_path, 'rb') as f:
                response = requests.post(self.speach_url, headers=speach_headers, data=f, verify=False)
                print(response)

                if response.status_code == 200:
                    # Parse the JSON response
                    try:
                        response_data = response.json()
                        print(response_data['result'][0])

                        return response_data['result'][0]
                    except ValueError:
                        print("Error: Received non-JSON response")
                else:
                    print("Failed to get a successful response:", response.status_code)
                    print("Response text:", response.text)

        except ValueError:
            print(f"An error occurred: {e}")

        return "Error occured"
    
    def text_to_audio(self, text, output_path, format='opus', output_format=".ogg", voice='Ost_24000'):
        self.check_token()

        params = {
            'format': format,
            'voice': voice
        }

        # Define the headers
        headers = {
            'Authorization': 'Bearer ' + self.bearer_token,
            'Content-Type': 'application/text'
        }

        try:
            with requests.post(self.tts_url, headers=headers, params=params, data=text.encode('utf-8'), verify=False, stream=True) as response:
                response.raise_for_status()  # Check for HTTP errors
                with open(output_path+'.ogg', 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8096):
                        f.write(chunk)
                print(f"Audio content successfully written to {output_path+output_format}")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Error downloading the audio: {e}")
