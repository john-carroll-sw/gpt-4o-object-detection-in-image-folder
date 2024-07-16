import base64
import datetime
import json
import os
import sys
import time

from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

# Azure OpenAI client
client = AzureOpenAI(
    azure_deployment=os.getenv("GPT_4o_CHAT_DEPLOYMENT_NAME"),
    azure_endpoint=os.getenv("GPT_4o_ENDPOINT"),
    api_key=os.getenv("GPT_4o_API_KEY"),
    api_version=os.getenv("GPT_4o_API_VERSION")
)

def sort_files_numerically(folder_path):
    files = os.listdir(folder_path)

    # Define a key function that removes '#' from the filename
    def key_func(filename):
        return filename.replace('#', '')
    
    # Sort the files using the key function
    return sorted(files, key=key_func)

def update_progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '#' * int(percent) + '-' * (100 - int(percent))
    sys.stdout.write(f"\r|{bar}| {percent:.2f}%")
    sys.stdout.flush()

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_image(prompt, detail_level, image):
    response = client.chat.completions.create(
        model=os.getenv("GPT_4o_CHAT_MODEL"),
        # max_tokens=100,
        temperature=0,
        top_p=0,
        response_format={ "type": "json_object" },
        messages=[
            {
                "role": "system",
                "content": [
                    {"type": "text", "text": prompt},
                ],
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Image:"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image}",
                            "detail": detail_level
                        }
                    },
                ],
            }
        ],
    )
    
    return response.choices[0].message.content # Extract the processed result from the API response

def process_images(prompt, detail_level, folder_name, images):
    log = []
    times = []

    total_images = len(images)

    for i, image in enumerate(images):
        encoded_image = encode_image_to_base64(image)
    
        start_time = time.time()
        response = process_image(prompt, detail_level, encoded_image)
        end_time = time.time()
        request_time = end_time - start_time
        times.append(end_time - start_time)

        log.append(f"Image: {image}, Request Time: {round(request_time, 4)} seconds, Response: {json.loads(response)}")
        
        # Calculate and Print progress percentage
        update_progress_bar(i, total_images)

    update_progress_bar(len(images), total_images)
    sys.stdout.write("\n")  # Move to the next line after completion

    log.append(f"Image Folder: {folder_name}")
    log.append(f"Average Request Time: {round(sum(times) / len(times), 4)} seconds")
    log.append(f"Minimum request time: {round(min(times), 4)} seconds")
    log.append(f"Maximum request time: {round(max(times), 4)} seconds")

    return log

def handle_logs(log_subfolder_name, foldername, log):
    now = datetime.datetime.now() # Get current date and time
    folder_name = foldername.replace("\\", "_").replace(" ", "_")
    filename = now.strftime(f"{folder_name}_%Y-%m-%d_%I-%M%p_log.txt")

    if not os.path.exists(f'logs/{log_subfolder_name}'):
        os.makedirs(f'logs/{log_subfolder_name}')

    with open(f"logs/{log_subfolder_name}/{filename}", "w") as file:
        for entry in log:
            file.write(entry + "\n")

    for entry in log:
        print(entry)

def main():
    prompt_filename = "SamplePrompt.txt"
    with open(prompt_filename, "r") as file:
        prompt = file.read()

    detail_level = "low"
    # detail_level = "high"
    log_subfolder_name = "test_run_1"
    folder_name = "images"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(current_directory, folder_name)
    sorted_folder_path = sort_files_numerically(folder_path)

    images = []
    for filename in sorted_folder_path:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            images.append(image_path)

    log = process_images(prompt, detail_level, folder_name, images)
    handle_logs(log_subfolder_name, folder_name, log)

if __name__ == "__main__":
    main()