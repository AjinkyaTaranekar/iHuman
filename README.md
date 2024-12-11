# iHuman 🤖💭

## Overview 🌟
iHuman is an AI-driven group chat simulation where various emotions, represented as AI agents, engage in meaningful discussions. By leveraging `pyautogen` and `litellm` libraries, we create a dynamic and interactive chat environment where different emotional perspectives come together to provide rich, multi-faceted responses.

## Features 💫
- 🎭 **Dynamic Agent Creation**
  - Generate AI agents representing different emotions
  - Customize emotion intensity levels
  - Scalable agent architecture

- 👥 **Group Chat Management**
  - Round-robin speaker selection for balanced participation
  - Multi-agent conversation coordination
  - Structured discussion flow

- ⚙️ **Customizable System Messages**
  - Emotion-specific behavior patterns
  - Adjustable emotion intensity percentages
  - Context-aware responses

- 💬 **Interactive Chat Experience**
  - Natural conversation flow
  - Multiple emotional perspectives
  - Insightful strategy generation

## Quick Start 🚀

### Prerequisites
- Python 3.8+
- pip package manager

### Installation 📦
Clone the repository and install the required dependencies:

## Usage 🎮
To start the AI-driven group chat simulation, run:
```
# Run the chat simulation
python main.py
```

## Configuration ⚙️
### LLM Settings: 
Configure the Language Model settings in main.py by updating the llm dictionary.
```python
llm = {
    "config_list": [
        {
            "base_url": "http://0.0.0.0:11434/v1",
            "api_key": "YOUR_API_KEY",
            "model": "llama3.1:8b",
        }
    ],
    "temperature": 0.7,
}
```
### Emotions List: 
Modify the emotions list in main.py to add or adjust emotions and their behavior percentages.
```python
emotions = [
    {"name": "Excited", "behavior_percentage": 20},
    {"name": "Happy", "behavior_percentage": 30},
    # Add more emotions as needed
]
```

### System Messages: 
The generate_system_message function in main.py creates system prompts for each emotion. Adjust this function to change how emotions are represented.

## Dependencies 📦
- pyautogen - For AI agent creation and management
- litellm - For language model integration