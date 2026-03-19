#Reading files from file.txt
with open("file.txt", "r") as f:
    files = f.readlines()

categorie = {
    "Images": [],
    "Documents": [],
    "Music": [],
    "Video": [],
    "Others": []
}

for file in files:
    file = file.strip()

    if file.endswith(".jpg") or file.endswith(".png"):
        categorie['Images'].append(file)
    elif file.endswith(".pdf") or file.endswith(".txt"):
        categorie['Documents'].append(file)
    elif file.endswith(".mp3"):
        categorie['Music'].append(file)
    elif file.endswith(".mp4"):
        categorie['Video'].append(file)
    else:
        categorie['Others'].append(file)

# Writing the resultat to resultat.txt
with open("resultat.txt", "w") as f:
    for cat, items in categorie.items():
        f.write(cat + ":\n")
        for item in items:
            f.write("  - " + item + "\n")
        f.write("\n")
