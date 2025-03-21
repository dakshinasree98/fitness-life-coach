from langgraph.graph import Graph
from workout_planner import generate_workout_plan
from calorie_calculator import calculate_calorie_intake

# Define nodes for the workflow
def generate_plan(state):
    weight = state["weight"]
    gender = state["gender"]
    workout_goal = state["workout_goal"]
    workout_plan = generate_workout_plan(weight, gender, workout_goal)
    return {"workout_plan": workout_plan}

def calculate_calories(state):
    weight = state["weight"]
    gender = state["gender"]
    workout_goal = state["workout_goal"]
    calorie_intake = calculate_calorie_intake(weight, gender, workout_goal)
    return {"calorie_intake": calorie_intake}

def track_progress(state):
    # Simulate progress tracking (e.g., user feedback)
    feedback = state.get("feedback", "just right")
    if feedback == "hard":
        return {"adjustment": "Reduce intensity for the next week."}
    elif feedback == "easy":
        return {"adjustment": "Increase intensity for the next week."}
    else:
        return {"adjustment": "Keep the current plan."}

# Define the workflow
workflow = Graph()
workflow.add_node("generate_plan", generate_plan)
workflow.add_node("calculate_calories", calculate_calories)
workflow.add_node("track_progress", track_progress)

# Define edges
workflow.add_edge("generate_plan", "calculate_calories")
workflow.add_edge("calculate_calories", "track_progress")

# Set entry and end points
workflow.set_entry_point("generate_plan")
workflow.set_finish_point("track_progress")

# Compile the workflow
app = workflow.compile()