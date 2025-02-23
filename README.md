Project Overview
This project is a Python script that allows users to download YouTube videos using the yt-dlp library. It provides features such as customizable video quality, duplicate file handling, and a user-friendly command-line interface. The script is designed to be simple, efficient, and easy to use.

Features
Download YouTube Videos: Download videos in the highest available resolution or a user-specified quality.

Duplicate File Handling: Checks if the file already exists and prompts the user to overwrite or skip.

Customizable Quality: Allows users to choose video quality (e.g., 1080p, 720p, 480p).

Error Handling: Robust error handling to ensure smooth operation.

User-Friendly: Simple command-line interface for ease of use.

Installation Instructions
Follow these steps to set up and run the project:

1. Clone the Repository
Clone the repository to your local machine using the following command:


Copy
git clone https://github.com/your-username/youtube-downloader.git
cd youtube-downloader
2. Install Dependencies
Ensure you have Python 3.8 or higher installed. Then, install the required library:


Copy
pip install yt-dlp




Run the script:
Enter the YouTube video URL when prompted:

Copy
Enter the YouTube URL: https://www.youtube.com/watch?v=example
Choose the video quality (optional):

Copy
Enter video quality (e.g., 1080, 720, 480) or leave blank for best quality: 720
If the file already exists, you will be prompted to overwrite or skip:

Copy
File 'Example Video Title.mp4' already exists. Overwrite? (y/n): n
Download skipped.
Once the download is complete, you will see:

Copy
Download complete.
Code Overview
The script uses the yt-dlp library to fetch and download YouTube videos. Key components include:

User Input Handling: Prompting the user for a YouTube URL and video quality.

Duplicate File Handling: Checking if the file already exists and prompting the user to overwrite or skip.

Video Quality Selection: Allowing the user to specify the desired video quality.

Error Handling: Gracefully handling errors such as invalid URLs or network issues.





