from pyscript import document

# Club data
clubs = {
    "Robotics Engineering Division": {
        "Description": "Design, build, and program robotic systems.",
        "Meeting Time": "Mondays & Tuesdays & Wednesdays 3:45–5:30 PM",
        "Location": "Engineering Lab",
        "Advisor": "Ms. Carabot, Ms. Caballero",
        "Number of Members": "5",
        "Category": "Academic – Technology"
    },
    "Cybersecurity Taskforce": {
        "Description": "Learn ethical hacking, digital defense, and system security basics.",
        "Meeting Time": "Thursdays & Fridays 4:00–5:15 PM",
        "Location": "ICT Room 2",
        "Advisor": "Ms. Caballero, Ms. Carabot",
        "Number of Members": "14",
        "Category": "Academic – Technology"
    },
    "Wellness & Discipline Club": {
        "Description": "Promotes healthy routines, stress management, and responsible habits.",
        "Meeting Time": "Mondays & Fridays 3:30–4:30 PM",
        "Location": "Room 108",
        "Advisor": "Ms. Solidum, Mr. Calixihan",
        "Number of Members": "22",
        "Category": "Student Development"
    },
    "Campus Logistics Team": {
        "Description": "Organizes school events, manages equipment, and assists with campus operations.",
        "Meeting Time": "Tuesdays & Thursdays 3:00–4:15 PM",
        "Location": "Multipurpose Hall",
        "Advisor": "Mr. De Leon, Mr. Reyes, Mr. Calixihan",
        "Number of Members": "25",
        "Category": "Service & Operations"
    },
}

def show(club_name):
    info_box = document.getElementById("club_info_box")

    if club_name in clubs:
        details = clubs[club_name]
        text = f"Club Name: {club_name}\n"
        for k, v in details.items():
            text += f"{k}: {v}\n"
        info_box.innerText = text
    else:
        info_box.innerText = "No information available."

def RED_Club(e):
    show("Robotics Engineering Division")

def CT_Club(e):
    show("Cybersecurity Taskforce")

def WND_Club(e):
    show("Wellness & Discipline Club")

def CL_Team(e):
    show("Campus Logistics Team")
