from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tasks import research_task,write_task


#Initialize crew AI
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process
result=crew.kickoff(inputs={'topic':'Mention_youtube_VIDEO_NAME'})
print(result)