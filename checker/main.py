# import requests

# url = "https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/"
# text = input("Enter the text to check for AI-generated content: ")
# payload = { "text": text }
# headers = {
# 	"x-rapidapi-key": "f9c6fdcf34msh47df29fc02a20bcp10e999jsnef5e5b251464",
# 	"x-rapidapi-host": "ai-content-detector-ai-gpt.p.rapidapi.com",
# 	"Content-Type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)


# # print(response.json())

# # import requests

# # url = "https://ai-content-detector-ai-gpt.p.rapidapi.com/api/detectText/"
# # payload = {
# #     "text": "Your sample text here"
# # }
# # headers = {
# #     "Content-Type": "application/json",
# #     "X-RapidAPI-Key": "YOUR_RAPIDAPI_KEY",
# #     "X-RapidAPI-Host": "ai-content-detector-ai-gpt.p.rapidapi.com"
# # }

# # response = requests.post(url, json=payload, headers=headers)

# if response.status_code == 200:
#     print(response.json())
# else:
#     print(f"Error: {response.status_code}, {response.text}")


from copyleaks import Copyleaks
from copyleaks.exceptions import CopyleaksAuthenticationError
import time

# API credentials
API_EMAIL = "YOUR_EMAIL"
API_KEY = 'YOUR_COPYLEAKS_API_KEY'

def check_plagiarism(text_content):
    try:
        # Initialize Copyleaks
        copyleaks = Copyleaks(API_EMAIL, API_KEY)

        # Define the text to check
        submission_data = {
            "base64": False,
            "text": text_content,  # You can also submit a file or URL
        }

        # Submit text for plagiarism check
        process = copyleaks.submit_text(submission_data)

        print(f"Submission success! ID: {process['id']}")

        # Wait for results
        while not copyleaks.is_complete(process['id']):
            print("Waiting for results...")
            time.sleep(10)

        # Fetch plagiarism results
        results = copyleaks.get_result(process['id'])

        if results:
            print("Plagiarism detected!")
            for match in results['scannedDocument']['matches']:
                print(f"Source: {match['url']} - Similarity: {match['percent']}%")
        else:
            print("No plagiarism detected!")

    except CopyleaksAuthenticationError:
        print("Authentication failed. Check your API credentials.")
    except Exception as e:
        print(f"Error: {e}")

# Example text to check for plagiarism
text_to_check = "This is the text content you want to check for plagiarism."
check_plagiarism(text_to_check)

