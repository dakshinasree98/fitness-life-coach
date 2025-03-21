from langgraph.graph import Graph
from workout_planner import generate_workout_plan
from calorie_calculator import calculate_calorie_intake

# Define nodes for the workflow
def generate_plan(state):
    print("State in generate_plan:", state)  # Debug statement
    weight = state["weight"]
    gender = state["gender"]
    workout_goal = state["workout_goal"]
    workout_plan = generate_workout_plan(weight, gender, workout_goal)
    return {**state, "workout_plan": workout_plan}

def calculate_calories(state):
    print("State in calculate_calories:", state)  # Debug statement
    weight = state["weight"]
    gender = state["gender"]
    workout_goal = state["workout_goal"]
    calorie_intake = calculate_calorie_intake(weight, gender, workout_goal)
    return {**state, "calorie_intake": calorie_intake}

def track_progress(state):
    print("State in track_progress:", state)
    feedback = state.get("feedback", "just right")
    if feedback == "hard":
        adjustment = "Reduce intensity for the next week."
    elif feedback == "easy":
        adjustment = "Increase intensity for the next week."
    else:
        adjustment = "Keep the current plan."
    return {**state, "adjustment": adjustment}

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