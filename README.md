# Interface RSK V1.0.0

Ce projet fournit un processus d'installation et de configuration automatisé pour l'interface RSK (Robot Soccer Kit).

## Prérequis

- Python 3.8 ou supérieur
- Git installé sur votre système
- Connexion Internet

## Démarrage Rapide

1. Téléchargez les fichiers `setup.py` et `start.py`
2. Exécutez le script de démarrage :
```bash
python start.py
```

Le script automatiquement :
- Vérifie si RSK est installé
- Clone le dépôt si nécessaire
- Installe les dépendances manquantes
- Lance l'interface et le contrôleur de jeu

## Installation Manuelle

Vous pouvez aussi utiliser `setup.py` directement avec différentes options :

```bash
python setup.py [options]
```

Options disponibles :
- `--no-clone` : Ignorer le clonage du dépôt
- `--no-install` : Ignorer l'installation de RSK
- `--no-start` : Ignorer le démarrage de l'application
- `--repo URL` : Spécifier une URL de dépôt personnalisée

## Structure du Projet

```
.
├── setup.py    # Script d'installation et de configuration
├── start.py    # Script de lancement principal
└── sourcecode/ # Code source du projet (cloné automatiquement)
```

## Dépannage

Si vous rencontrez des problèmes :
1. Assurez-vous que Python et Git sont correctement installés
2. Vérifiez votre connexion Internet
3. Essayez d'exécuter setup.py avec les privilèges administrateur
4. Vérifiez que le port 5000 est disponible pour l'interface web

## Détails Techniques

Le processus d'installation :
1. Vérifie les prérequis système
2. Clone/met à jour le dépôt
3. Installe RSK via pip
4. Lance l'interface et le contrôleur de jeu
5. Ouvre l'interface web (http://127.0.0.1:5000)