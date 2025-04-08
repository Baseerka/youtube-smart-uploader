# YouTube Smart Uploader

**YouTube Smart Uploader** is a Python-based tool designed to automate the process of uploading videos to YouTube. It offers two primary methods for uploading:

1. **YouTube Data API**: Utilizes YouTube's official API for direct uploads.
2. **Selenium WebDriver**: Automates browser interactions to upload videos via YouTube's web interface.

## Features

- **Automated Uploads**: Streamline the video upload process using Python.
- **Dual Upload Methods**: Choose between API-based uploads or browser automation.
- **Configurable Settings**: Customize upload parameters through a `config.json` file.

## Prerequisites

Before using this tool, ensure you have the following:

- **Python 3.x**: The tool is compatible with Python 3.x versions.
- **Google API Credentials**: Necessary for API-based uploads. Obtain them from the [Google Developer Console](https://console.developers.google.com/).
- **Selenium WebDriver**: Required for browser automation. Download it from the [official Selenium website](https://www.selenium.dev/documentation/webdriver/).

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Baseerka/youtube-smart-uploader.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd youtube-smart-uploader
   ```

3. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Set Up `config.json`**:

   Create a `config.json` file in the project directory with the following structure:

   ```json
   {
     "upload_method": "api",
     "video_path": "path/to/your/video.mp4",
     "title": "Your Video Title",
     "description": "Your video description",
     "tags": ["tag1", "tag2"],
     "category": "22",
     "privacy_status": "public",
     "credentials_file": "path/to/credentials.json"
   }
   ```
   - `upload_method`: Choose `"api"` for YouTube Data API or `"selenium"` for Selenium WebDriver.
   - `video_path`: Path to the video file you want to upload.
   - `title`: Title of the video.
   - `description`: Description of the video.
   - `tags`: List of tags associated with the video.
   - `category`: Numeric category ID. Refer to [YouTube API documentation](https://developers.google.com/youtube/v3/docs/videoCategories/list) for valid IDs.
   - `privacy_status`: `"public"`, `"private"`, or `"unlisted"`.
   - `credentials_file`: Required for API method – your Google API credentials file path.

2. **Obtain Google API Credentials** (if using API method):

   - Visit the [Google Developer Console](https://console.developers.google.com/)
   - Create a project or use an existing one.
   - Enable the **YouTube Data API v3**.
   - Create OAuth 2.0 credentials (Desktop App) and download the JSON file.
   - Save it and update the `credentials_file` path in `config.json`.

## Usage

Once configured, run the appropriate script:

### For API-based Upload:

```bash
python upload_with_api.py
