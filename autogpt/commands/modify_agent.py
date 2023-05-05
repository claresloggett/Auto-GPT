
from autogpt.config.ai_config import AIConfig
from autogpt.config import Config
from autogpt.commands.command import command

CFG = Config()

@command(
    "add_goal",
    "Add Goal",
    '"goal": "<goal>"',
)
def add_goal(goal: str, ai_config: AIConfig):
    """Modify the agent's current list of goals by adding a single new goal.

    Args:
        goal (str): The goal to add
    """

    ai_config.add_goal(goal)
    ai_config.save(CFG.ai_settings_file)
    return "Goal added successfully"

@command(
    "remove_goal",
    "Remove Goal",
    '"goal_number": "<goal_number>"',
)
def remove_goal(goal_number: str, ai_config: AIConfig):
    """Modify the agent's current list of goals by removing a single goal.

    Args:
        goal_number (int): The goal to remove. 
            The goal_number should be 1-indexed and correspond to the list in the prompt.
    """

    try:
        goal_index = int(goal_number)
    except ValueError:
        return "Removing goal failed because goal_number must be a number"

    try:
        ai_config.remove_goal(goal_index)
    except ValueError as e:
        return str(e)
    
    ai_config.save(CFG.ai_settings_file)
    return "Goal removed successfully"