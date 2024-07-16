# GPT-4o Object Detection

## Overview

This project utilizes the GPT-4o model for object detection within images stored in a specified folder. It leverages the advanced capabilities of GPT-4o to analyze images and identify objects, providing detailed insights and classifications. This tool is designed for researchers, developers, and hobbyists interested in exploring object detection capabilities powered by one of the most advanced AI models available.

## Features

- **Batch Processing**: Process multiple images in a specified folder, allowing for efficient analysis of large datasets.
- **Advanced Object Detection**: Utilizes GPT-4o's cutting-edge AI to detect and classify a wide range of objects within images.
- **Customizable Outputs**: Offers options to customize the output format, making it easier to integrate with other applications or for further analysis.
- **Easy to Use**: Simple setup and execution process, designed with a focus on user experience.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed on your system.
- Access to GPT-4o API and the necessary API keys (refer to the [`.env`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FRepositiories%2Fthd-cart-detection%2F.env%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Repositiories\thd-cart-detection\.env") file setup below).
- All required Python packages installed (see the `requirements.txt` file).

## Setup

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.

2. **Install Dependencies**: Navigate to the project directory and install the required Python packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**: Create a `.env` file in the project root with the following variables:

   ```dotenv
   GPT_4o_ENDPOINT=https://example.com/
   GPT_4o_API_KEY=your_api_key_here
   GPT_4o_API_VERSION=your_api_version_here
   GPT_4o_CHAT_DEPLOYMENT_NAME=your_deployment_name_here
   GPT_4o_CHAT_MODEL=your_model_here
   ```

   Replace the placeholder values with your actual GPT-4o API endpoint, API key, API version, deployment name, and model.

## Usage

To use the GPT-4o Object Detection tool, follow these steps:

1. **Prepare Your Images**: Place all the images you want to analyze in the designated image folder.

2. **Run the Script**: Execute the main script ([`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FRepositiories%2Fthd-cart-detection%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "c:\Repositiories\thd-cart-detection\main.py")) from your terminal or command prompt:

   ```bash
   python main.py
   ```

3. **View Results**: The script will process each image and output the detection results. The results can be found in the specified output directory or console, based on your configuration.

## Contributing

Contributions to this project are welcome. Please follow the standard fork-and-pull request workflow. If you plan to introduce a major change, it's best to open an issue first to discuss it.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

This project is made possible by the advanced capabilities of the GPT-4o model and the OpenAI API. Special thanks to the OpenAI team for providing access to such powerful tools.