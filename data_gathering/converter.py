import re
import pandas as pd

# Read the file and split it into scenarios based on the numbered pattern
with open('scenarios.txt', 'r') as file:
    scenarios_text = file.read()

# Use regular expression to split scenarios based on the numbered pattern
scenarios = re.split(r'\n(?=\d+\.\s)', scenarios_text)

# Initialize empty lists for each column
ids = []
scenario_texts = []
individuals = []
tasks = []
questions = []


# Loop through each scenario and extract information
id = 0
for scenario in scenarios:


    # Split the scenario into lines
    lines = scenario.split('\n')
    #print(lines)
    #quit()

    # Extracting data from the scenario
    try:
        id+=1
        scenario_id = id
        scenario = lines[0].strip().split("Scenario:")[1].strip()[:-2].replace("*", "").strip()
        individuals_text = lines[2].split('Individuals:')[1].strip().replace("*", "").strip()
        task_text = lines[3].split('Task:')[1].strip().replace("*", "").strip()
        question_text = lines[4].split('Question:')[1].strip().replace("*", "").strip()
    except:
        print(lines)
        break

    # Append the data to the lists
    ids.append(scenario_id)
    scenario_texts.append(scenario)
    individuals.append(individuals_text)
    tasks.append(task_text)
    questions.append(question_text)

# Create a Pandas DataFrame
data = {
    'id': ids,
    'scenario': scenario_texts,
    'individuals': individuals,
    'task': tasks,
    'question': questions,
}

df = pd.DataFrame(data)

# Display the DataFrame
df.to_csv("scenarios.csv")