import random
import datetime
import json

# Define the possible values for some fields
t_name_values = ["Begin Shift", "Finish Shift", "Take Temperature"]
t_rp_un_values = ["mihai", "hellen", "anthimos", "georgiana"]
t_type_values = ["begin_prototype", "finish", "take_temperature"]

# Define the date range
start_date = datetime.datetime(2023, 4, 20, 0, 0, 0)
end_date = datetime.datetime(2023, 5, 4, 23, 59, 59)

# Define the business opening hours
opening_hours = [
    {"start": datetime.time(8, 0), "end": datetime.time(14, 0)},
    {"start": datetime.time(17, 0), "end": datetime.time(23, 0)}
]

# Generate a JSON document for each day within the date range
json_docs = []
current_date = start_date
while current_date <= end_date:
    # Determine if the business is open at the current time
    is_open = False
    for hours in opening_hours:
        if current_date.time() >= hours["start"] and current_date.time() <= hours["end"]:
            is_open = True
            break

    # If the business is open, generate JSON documents for the reports
    if is_open:
        # Generate a random number of Take Temperature reports for the current day
        num_take_temp_reports = random.randint(5, 9)

        # Generate a Begin Shift report
        t_name = "Begin Shift"
        t_ts_submit = current_date.replace(hour=8, minute=0, second=0).isoformat() + "Z"
        t_rp_un = random.choice(t_rp_un_values)
        t_type = "begin_prototype"
        t_reports = {"t_1": random.choice(["done", "not done"]), "t_2": random.choice(["done", "not done"]), "t_3": random.choice(["done", "not done"])}
        t_meas_temp = ""
        t_obs = ""
        json_doc = {
            "t_name": t_name,
            "timestamp_type": "ISODate",
            "t_ts_submit": t_ts_submit,
            "t_rp_un": t_rp_un,
            "t_description": "",
            "t_type": t_type,
            "t_reports": t_reports,
            "t_meas_temp": t_meas_temp,
            "t_meas_type": "C",
            "t_obs": t_obs
        }
        json_docs.append(json_doc)

        # Generate a Finish Shift report
        t_name = "Finish Shift"
        t_ts_submit = current_date.replace(hour=22, minute=0, second=0).isoformat() + "Z"
        t_rp_un = random.choice(t_rp_un_values)
        t_type = "finish"
        t_answers = {}
        for i in range(1, 20):
            t_answers[str(i)] = [f"Answer {i}", random.choice(["yes", "no"])]
        t_obs = ""
        json_doc = {
            "t_name": t_name,
            "timestamp_type": "ISODate",
            "t_ts_submit": t_ts_submit,
            "t_rp_un": t_rp_un,
            "answers": t_answers,
            "t_obs": t_obs
        }
        json_docs.append(json_doc)

        # Generate Take Temperature reports
        for i in range(num_take_temp_reports
