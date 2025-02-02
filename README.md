<div align="center">
    <img height="200px" src="https://github.com/smelnyk/Personal-Productivity-Assistant/blob/main/img/img1.png" alt="Personal Productivity Assistant Tray">
    <img height="600px" src="https://github.com/smelnyk/Personal-Productivity-Assistant/blob/main/img/img2.png" alt="Personal Productivity Assistant Popup">
</div>

<div align="center">
    [MacOS Download](https://github.com/smelnyk/Personal-Productivity-Assistant/raw/refs/heads/main/downloads/MacOS_Personal-Productivity-Assistant.zip?download=true)
</div>

---

# Personal Productivity Assistant  
**Personal Productivity Assistant** is a revolutionary open-source application designed to enhance individual focus and productivity. By utilizing locally hosted Ollama AI models, it provides detailed insights and analytics on work habits. The goal is to empower users to achieve optimal efficiency and performance in their daily tasks.  

Unlike many similar applications that require paid subscriptions and transmit detailed activity data to external servers for storage and analysis, **Personal Productivity Assistant** ensures complete privacy by processing all data locally on your machine. This approach eliminates potential security risks associated with transmitting sensitive information over the internet.  

---

## Features  
- **Privacy & Security**: No information about your activity is sent over the internet, ensuring complete privacy.  
- **Raw Time Log**: The application stores a raw log of your activity in an open format within a designated folder, offering full transparency and user control.  
- **AI Analysis**: An AI model analyzes your long-term activity to uncover hidden patterns and provide actionable insights to enhance productivity.  
- **Classification Customization**: Users can manually adjust AI classifications to better reflect their personal productivity goals.  
- **AI Customization**: Right now the application is using `deepseek-r1:14b` (14 billion params, chain of thoughts). In the future, users will be able to choose from a variety of AI models to suit their specific needs.
- **Browsers Domain Tracking**: The application also tracks the time spent on individual websites within browsers (Chrome, Safari), offering a comprehensive view of online activity.

---

## How It Works  
- **Automatic Time Tracking**: The application automatically tracks the time spent on each application or website in focus.  
- **Application Classification**: Applications/Websites are categorized as "Productive" or "Unproductive," helping you understand how your time is spent.  
- **Time Summarization**: Usage times are aggregated hourly and daily, offering a clear overview of your activity patterns.  
- **AI-Driven Analytics**: AI-powered analytics identify productivity trends and suggest areas for improvement.  
- **Manual Customization**: Users can adjust AI classifications to align with their specific productivity objectives.  

---

## Usage Instructions
- **Classification Customization**: Right-click on the system tray icon to access the menu. Select "Edit Productive Config" to adjust the classification of applications and websites. The same action for "Edit Unproductive Config" will allow you to customize unproductive classifications.

## Installation Instructions  

### Standard Installation  
1. **Download the Application**: Obtain the latest release package for your operating system from the GitHub repository.  
2. **Install Ollama**: Download and install Ollama from its official website.  
3. **Run the Application**: Look for a black circle in the system tray upon launching. During the first run, the application will download the AI model from Ollama (9 GB). Once the download is complete, you can generate productivity reports.  

### Installation from Source  
1. **Clone the Repository**: Download the project files to your local machine using `git clone`.  
2. **Navigate to the Project Directory**: Open the project folder using `$ cd Personal-Productivity-Assistant`.  
3. **Create a Virtual Environment**: Run `$ python3 -m venv .venv` to create a virtual environment, then activate it with `$ source .venv/bin/activate`.  
4. **Install Dependencies**: Install the required packages with `$ pip install -r requirements.txt`.  
5. **Run the Application**: Start the application with `$ python Personal-Productivity-Assistant.py`.  
6. **Begin Usage**: Work as usual. After an hour, you can generate a productivity report from the system tray menu.  

---

## Future Plans  
1. **Cross-Platform Compatibility**: Expand support to include Windows and Linux for seamless integration across various operating systems.  
2. **Custom AI Prompts**: Allow users to tailor AI analysis by creating custom prompts to meet specific productivity needs.  
2. **Trends Report**: Generate detailed reports on productivity trends over time to identify areas for improvement.  

---

## Dependencies  
1. **PyQt5**: Used for creating the system tray application and GUI components.  
2. **Ollama**: Powers AI-based classification and report generation.  

---

## About the Author  
For more information about the author, visit their [LinkedIn profile](https://www.linkedin.com/in/smelnyk/).  
