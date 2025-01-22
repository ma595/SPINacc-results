"""Configuration file for the MLacc tasks."""

# Example execution of Trunk
from datetime import datetime
date = datetime.today().strftime('%d-%m-%Y')

from pathlib import Path

def get_active_branch_name():

    head_dir = Path(".") / ".git" / "HEAD"
    with head_dir.open("r") as f: content = f.read().splitlines()

    for line in content:
        if line[0:4] == "ref:":
            return line.partition("refs/heads/")[2]

git_branch = get_active_branch_name()

branch = git_branch

tasks = [
    1,
    2,
    4,
    5
]  # 1=test clustering, 2=clustering, 3=compress forcing, 4=ML, 5=evaluation
reference_dir = "./SPINacc-results/Trunk/"
start_from_scratch = False
kmeans_clusters = 4
max_kmeans_clusters = 9
random_seed = 1000
leave_one_out_cv = False
repro_test_task_1 = False
repro_test_task_2 = False
repro_test_task_3 = False
repro_test_task_4 = False

# TO TEST
take_year_average = True
take_unique = False
smote_bat = True
sel_most_PFTs = False 

parallel = True

algorithms = [
    "bt",
    ]

results_dir = f"./Trunk/{branch}/{algorithms[0]}/{date}/"
logfile = results_dir + "log.MLacc_Trunk"
