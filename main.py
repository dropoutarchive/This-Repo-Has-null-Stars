# Idea from: https://github.com/RealPeha/

import os
import sys
import logging
import requests
from time import sleep

logging.basicConfig(level=logging.INFO, format=f"[\x1b[38;5;199mGithub\x1b[0m] \x1b[38;5;199m->\x1b[0m %(message)s")

if sys.platform == "linux":
    clear = lambda: os.system("clear")
else:
    clear = lambda: os.system("cls")

Check_Interval = 1000
Milestone_Step = 500
Repository_ID = "GITHUB_REPO_ID"
Access_Token = "GITHUB_ACCESS_TOKEN"

headers = {
	"Authorization": f"token {Access_Token}"
}

milestones = [
    ":broken_heart:",
    ":heart:",
    ":orange_heart:",
    ":purple_heart:",
    ":yellow_heart:",
    ":heartpulse:",
    ":sparkling_heart:",
    ":gift_heart:",
    ":heartbeat:",
    ":two_hearts:",
    ":revolving_hearts:"
]

def Milestone_Emoji(stars: int):
	Milestone_Index = round(stars / 500)
	return milestones[Milestone_Index]

def Get_Repo_Stars():
	try:
		r = requests.get(f"https://api.github.com/repositories/{Repository_ID}", headers=headers)
		return r.json()["stargazers_count"]
	except:
		return False

def Rename_Repo(json):
	try:
		r = requests.patch(f"https://api.github.com/repositories/{Repository_ID}", headers=headers, json=json)
		if "id" in r.text:
			return True
		else:
			return False
	except:
		return False

def Task():
	logging.info("Started task!")
	while True:
		stars = Get_Repo_Stars()
		if stars != False:
			r = Rename_Repo({
				"name": f"This-Repo-Has-{stars}-Stars",
				"description": f"Yes it's true {Milestone_Emoji(stars)}"
			})
			if r != False:
				logging.info(f"Renamed repo, stars count is now \x1b[38;5;199m@\x1b[0m {stars}")
			else:
				logging.info(f"Failed to rename repo, stars count is now \x1b[38;5;199m@\x1b[0m {stars}")
		else:
			logging.info(f"Failed to fetch stars!")

		logging.info(f"Now waiting {Check_Interval} seconds!")
		sleep(Check_Interval)

if __name__ == "__main__":
	clear()
	Task()
