from crewai import Agent
from tools import yt_tool

# Agent : Senior content researcher

blog_researcher = Agent(
    role = "Blog Researcher from Youtube Videos",
    goal = "get the relevant video content for the topic {topic} from Yt Channel",
    verbose = True,
    memory = True,
    backstory = (
        "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestion"
    ),
    tools = [yt_tool],
    allow_delegation = True
)

## Agent : Senior blog writer agent with YT tool

blog_writer = Agent(
    role="Blog Writer",
    goal = "Narrate compelling tech stories about the video {topic}",
    verbose =True,
    memory = True,
    backstory = (
        "with a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to ligh in an accessible manner."
    ),
    tools = [yt_tool],
    allow_delegation=True
)
