import autogen

llm = {
    "config_list": [
        {
            "base_url": "http://0.0.0.0:11434/v1",
            "api_key": "NULL",
            "model": "llama3.1:8b",
        }
    ],
    "temperature": 0.7,
}


# Optimized function to generate system messages for each emotion
def generate_system_message(emotion_name, behavior_percentage):
    prompt = (
        f"You are an AI assistant embodying the pure emotion of '{emotion_name}'. "
        f"Your responses should consistently reflect a {behavior_percentage}% intensity of this emotion in tone, style, and content. "
        "Engage thoughtfully in the discussion, providing valuable and contextually relevant insights, "
        "while infusing your messages with the essence of this emotion. "
        "Without mentioning or acknowledging that you're portraying an emotion, let it be evident through your language. "
        "Stay focused on the topic introduced by the admin and contribute meaningfully to the conversation."
    )
    return prompt


# Create a user proxy agent
user_proxy = autogen.UserProxyAgent(
    name="Admin",
    system_message="A human admin providing a message to a group of emotions for discussion.",
    human_input_mode="ALWAYS",
    max_consecutive_auto_reply=0,
)

# List of emotions
emotions = [
    {"name": "Excited", "behavior_percentage": 20},
    {"name": "Happy", "behavior_percentage": 30},
    {"name": "Joy", "behavior_percentage": 25},
    {"name": "Content", "behavior_percentage": 40},
    {"name": "Calm", "behavior_percentage": 50},
    {"name": "Relaxed", "behavior_percentage": 35},
    {"name": "Confident", "behavior_percentage": 40},
    {"name": "Pride", "behavior_percentage": 15},
    {"name": "Interest", "behavior_percentage": 60},
    {"name": "Surprise", "behavior_percentage": 10},
    {"name": "Anticipation", "behavior_percentage": 30},
    {"name": "Trust", "behavior_percentage": 50},
    {"name": "Love", "behavior_percentage": 40},
]

# Create agents dynamically
agents = [user_proxy]
for emotion in emotions:
    system_message = generate_system_message(
        emotion["name"], emotion["behavior_percentage"]
    )
    agent = autogen.AssistantAgent(
        name=emotion["name"],
        llm_config=llm,
        system_message=system_message,
    )
    agents.append(agent)

# Create GroupChat
groupchat = autogen.GroupChat(
    agents=agents,
    messages=[],
    max_round=5,
    speaker_selection_method="round_robin",  # Ensure fair participation
)

# Create GroupChatManager
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm)

# Initiate the chat
user_proxy.initiate_chat(
    manager,
    message="I need to participate in a walkathon to win championship this month for my house. What strategies and motivations can you suggest?",
    summary_method="reflection_with_llm",
)
