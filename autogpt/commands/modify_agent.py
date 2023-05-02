
from autogpt.config.ai_config import AIConfig
from autogpt.config import Config

CFG = Config()

def add_goal(goal: str, ai_config: AIConfig):
    """Modify the agent's current list of goals by adding a single new goal.

    Args:
        goal (str): The goal to add
    """

    ai_config.add_goal(goal)
    ai_config.save(CFG.ai_settings_file)
    return "Goal added successfully"