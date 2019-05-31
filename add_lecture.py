import sys
import shutil
import datetime
import os

try:
    from PyInquirer import prompt, print_json
    import yaml
    from dateutil.parser import parse
except ImportError:
    print(
        "Please install requirements by `pip install PyInquirer pyyaml python-dateutil`"
    )
    sys.exit(1)

CONFIG_PATH = "./_data/lectures.yml"
with open(CONFIG_PATH, "r") as f:
    config = yaml.load(f)

# Find out the closest date
dates = [parse(item["date"]) for item in config]
today = datetime.datetime.now()
dates.append(today)
dates = sorted(dates)
idx = dates.index(today)
lower, upper = idx - 1, idx + 1
if lower < 0:
    lower = 0
if upper >= len(dates):
    upper = len(dates) - 1

intro_section = [
    {
        "type":
        "list",
        "name":
        "lecture_date",
        "message":
        "Please choose the lecture to update",
        "choices": [
            "{date}: {topic}".format(date=config[idx]["date"],
                                     topic=config[idx]["topic"])
            for idx in range(lower, upper + 1)
        ],
    },
    {
        "type": "list",
        "name": "path_or_url",
        "message": "For the slide, are you adding an url or a file?",
        "choices": ["url", "file"],
    },
]

answers = prompt(intro_section)
date_picked = answers['lecture_date'].split(':')[0]
idx = [i for i, item in enumerate(config) if item['date'] == date_picked][0]

if answers['path_or_url'] == 'url':
    url_answer = prompt([{
        'type': 'input',
        'name': 'url',
        'message': 'Enter the url'
    }])
    config[idx]['slides'] = url_answer['url']
else:
    path_answer = prompt([{
        'type': 'input',
        'name': 'path',
        'message': 'Enter the file path to add'
    }])
    path = os.path.expanduser(path_answer['path'])

    if not os.path.exists(path):
        print(
            "File doesn't exist, please make sure you entered the correct path"
        )
        sys.exit(1)
    dst = 'assets/lectures/lec{idx}/{filename}'.format(
        idx=str(idx), filename=os.path.split(path)[-1])
    os.makedirs(os.path.split(dst)[0], exist_ok=True)
    shutil.copyfile(path, dst)
    config[idx]['slides'] = dst

with open(CONFIG_PATH, 'w') as f:
    yaml.dump(config, f, default_flow_style=False)

print("""
=========
All Done! Please use git to add files, commit, and push to the gh-pages branch
========
""")
