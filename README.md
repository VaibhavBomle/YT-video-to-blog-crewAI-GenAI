# YT-video-to-blog-crewAI-GenAI

# CrewAI YouTube to Blog  

This project automates the process of generating blog content from YouTube videos using CrewAI agents. It uses two specialized agents to research and write blogs based on video transcripts from a specified YouTube channel.

## Features
- *YouTube Content Analysis:* Retrieve and summarize video transcripts for blog creation.
- *AI-Powered Agents:* 
  - *Blog Researcher*: Extracts relevant information from YouTube videos.
  - *Blog Writer*: Creates engaging blog posts from the extracted content.
- *Extensible Toolset*: Easily integrate additional tools as needed.

---

## Setup Instructions  

 1. Clone the Repository
    ```bash
       git clone repository-url
 2. Create a Virtual Environment
    ```bash
       python -m venv venv
       source venv/bin/activate  # On Windows: venv\Scripts\activate

 4. Install Requirements
    ```bash
       pip install -r requirements.txt

 5. Environment Variables
Create a .env file in the root directory and add the following keys:
env
OPENAI_API_KEY=<Your OpenAI API Key>

 6. Specify YouTube Channel
Update tools.py with your YouTube channel handle:
   ```bash
      yt_tool = YoutubeChannelSearchTool(youtubeChannelName)


## Steps to Run
Step 1: Define the Topic or Video Name
In crew.py, specify the topic or video name to analyze:
result = crew.kickoff(inputs={'topic': 'Exploring AI in Data Science'})

Step 2: Execute the Process
Run the crew.py file to start the blog creation workflow:
python crew.py

Step 3: Review the Output
The output will be displayed in the console.
A markdown file new-blog-post.md will be created with the blog content.
