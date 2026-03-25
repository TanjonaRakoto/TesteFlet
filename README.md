# 🎲 Lucky Number — Flet App

Un petit jeu de devinette : trouve le nombre secret entre 1 et 100 en 7 tentatives !

## Structure du projet

```
.
├── main.py
├── pyproject.toml
└── .github/
    └── workflows/
        └── build.yml
```

## Tester en local

```bash
pip install flet
python main.py
```

## Générer l'APK sur GitHub

1. Push ce repo sur GitHub (branche `main`)
2. Va dans **Actions** → le workflow `Build Android APK` se lance automatiquement
3. Une fois terminé, clique sur le job → **Artifacts** → télécharge `lucky-number-apk.zip`
4. Extrais le `.apk` et installe-le sur ton Android (active "Sources inconnues")

> Le premier build prend ~10-15 minutes (téléchargement de Flutter + Android SDK).
