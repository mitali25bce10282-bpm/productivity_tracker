#  productivity_tracker
## OVERVIEW
A simple, beginner-friendly, Python-based weekly productivity tracker that helps the user track their productivity by collecting tasks, arranging them in priority order, and providing a weekly report. The report includes feedback and tips for the user, which help them improve and be more productive.
Planning weekly tasks, prioritising work, and being productive at the same time can be hectic, and many face difficulties in doing so. This program gives a simple solution to these problems by giving the following features:
- adds weekly tasks
- sets a deadline
- marks completed tasks
- sorts tasks according to the deadline
- calculates productivity
- gives small tips and motivations to keep going
## OBJECTIVES
- To build a productivity tracker tool using python
- To apply basic concepts learned in the flipped course
- To display a weekly report based on the user's performance
## PROJECT STRUCTURE
productivity_tracker/
│
├── main.py
├── README.md
├── requirements.txt
│
├── src/
│   ├── input.py
│   ├── calculations.py
│   ├── output.py
│   └── storage.py
│
├── screenshots/
└── recordings/

## FEATURES
1) Task input system:
- The user can input the details of their tasks.
- Each task has a task name, deadline and priority.
2) Sorting based on deadline:
- All tasks are sorted automatically using
tasks=sorted(tasks, key=lambda x:x["deadline"])
3) Priority color coding:
   High=Red, Medium=Blue, Low=Magenta
4) Calculation of productivity:
   Productivity is calculated using
   (tasks completed / total tasks)*100
5) Rating system
   Rating and message are displayed with colors based on the user's performance.
6) Tips to improve
7) Weekly report output
   The output includes the user's name, total, completed and remaining tasks, productivity percentage, ratings, a color-coded task list, and timeline.
## HOW TO RUN
1) Open terminal in the folder that contains the project
2) Run: python main.py
## MODULES
- input.py: collects user's details
- calculations.py: calculates productivity, gives ratings and tips
- output.py: gives a final weekly report

## SCREENSHOTS
All related screenshots are stored in /screenshots folder.
