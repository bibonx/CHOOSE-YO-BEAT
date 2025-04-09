
import os
import json

# Dossiers à scanner
categories = ["beats", "loops", "misc"]

# Dictionnaire pour stocker les fichiers trouvés
index = {}

for category in categories:
    if os.path.exists(category):
        files = [f for f in os.listdir(category) if f.endswith(".mp3")]
        index[category] = files
    else:
        index[category] = []

# Écriture dans le fichier index.json
with open("index.json", "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

print("✅ Fichier index.json généré avec succès !")
