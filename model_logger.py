import datetime

def log_prediction(input_data, output):
    with open("prediction_log.txt","a") as f:
        f.write(f"{datetime.datetime.now()} | {input_data} | {output}\n")