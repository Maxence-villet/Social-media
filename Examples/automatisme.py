import subprocess
import random

# Paramètres pour la génération des graphes
num_graphs = 30  # Nombre de graphes à générer
output_dir = "Examples"  # Répertoire de sortie pour les fichiers générés

# Plages de valeurs pour les paramètres
min_degree_range = (1, 3)
max_degree_range = (4, 6)
num_communities_range = (2, 5)
max_distance_range = (10, 20)
num_vertices_range = (10, 50)

# Fonction pour générer une commande Bash
def generate_command(graph_id):
    oriented = random.choice(["--oriented", "--not_oriented"])
    min_degree = random.randint(*min_degree_range)
    max_degree = random.randint(*max_degree_range)
    num_communities = random.randint(*num_communities_range)
    max_distance = random.randint(*max_distance_range)
    num_vertices = random.randint(*num_vertices_range)
    output_file = f"{output_dir}/graph_{graph_id}.txt"

    command = [
        "python", "main.py", "generate",
        oriented,
        "--min_degree", str(min_degree),
        "--max_degree", str(max_degree),
        "--num_communities", str(num_communities),
        "--max_distance", str(max_distance),
        "--num_vertices", str(num_vertices),
        "--output", output_file
    ]
    return command

# Boucle pour générer plusieurs graphes
for i in range(num_graphs):
    command = generate_command(i)
    print(f"Exécution de la commande: {' '.join(command)}")
    subprocess.run(command)

print(f"{num_graphs} graphes générés avec succès dans le répertoire '{output_dir}'.")