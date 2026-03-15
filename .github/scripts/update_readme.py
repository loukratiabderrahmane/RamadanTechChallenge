#!/usr/bin/env python3
"""
Auto-update README.md stats based on Day* folders in the repo.
Run by GitHub Actions on every push to main.
"""

import re
from pathlib import Path
from datetime import datetime

# ── CONFIG ──────────────────────────────────────────────────────────────────
TOTAL_DAYS = 30
README_PATH = Path("README.md")

# Map each day to its category
DAY_CATEGORIES = {
    1:  "security",
    2:  "devops", 3: "devops", 4: "devops", 5: "devops",
    6:  "devops", 7: "devops", 8: "devops",
    9:  "orm",
    10: "ia", 11: "ia", 12: "ia", 13: "ia",
    14: "ml",  15: "ml",  16: "ml",  17: "ml",
    18: "dl",  19: "dl",  20: "dl",  21: "dl",  22: "dl",
    23: "dl",  24: "dl",  25: "mlops",
    26: "backend", 27: "security", 28: "backend",
    29: "system", 30: "system",
}

CATEGORY_EMOJI = {
    "security": "🛡️",
    "devops":   "⚙️",
    "orm":      "🗄️",
    "ia":       "🧠",
    "ml":       "📊",
    "dl":       "🔥",
    "mlops":    "🚀",
    "backend":  "🔧",
    "system":   "🌐",
}

# Concepts associés à chaque jour
DAY_CONCEPTS = {
    1:  ("security", "🛡️ Sécurité", [
        "SQL Injection, NoSQL Injection",
        "XSS (Cross-Site Scripting)",
        "CSRF, Brute Force, DDoS",
        "MITM, Broken Authentication",
        "JWT, HTTPS, Rate Limiting",
    ]),
    2:  ("devops", "⚙️ DevOps & Cloud", [
        "Pipeline CI/CD complet (GitHub Actions)",
        "Docker : Images, Containers, Volumes, Networks",
        "Kubernetes : Pods, Deployments, Services, HPA",
        "Architecture Microservices & API Gateway",
        "Apache Kafka : Topics, Partitions, Consumer Groups",
        "IaaS / PaaS / SaaS",
    ]),
    10: ("ia", "🧠 IA & Machine Learning", [
        "Introduction à l'IA — ML, DL, IA Générative",
        "Supervised / Unsupervised / Reinforcement Learning",
        "Logistic Regression, Decision Tree, Random Forest",
        "Confusion Matrix, Accuracy, Precision, Recall, F1 Score",
        "Overfitting / Underfitting, Bias-Variance Tradeoff",
        "Feature Engineering : Scaling, Normalization, Encoding",
        "ML Pipelines avec Scikit-Learn",
    ]),
    18: ("dl", "🔥 Deep Learning & IA Avancée", [
        "Artificial Neural Networks (ANN)",
        "Multilayer Perceptron (MLP), Fonctions d'activation",
        "Backpropagation & Gradient Descent",
        "Convolutional Neural Networks (CNN)",
        "Recurrent Neural Networks (RNN), Vanishing Gradient",
        "Transformer & Attention Mechanism — Self-Attention, BERT, GPT",
        "RAG — Retrieval Augmented Generation",
        "MLOps — Déploiement, FastAPI, Monitoring, Data Drift",
    ]),
}

# ── SCAN REPO ────────────────────────────────────────────────────────────────
def scan_days(root: Path) -> list[int]:
    completed = []
    for folder in root.iterdir():
        if folder.is_dir():
            m = re.match(r"[Dd]ay(\d{1,2})", folder.name)
            if m:
                day_num = int(m.group(1))
                if list(folder.glob("*.md")):
                    completed.append(day_num)
    return sorted(set(completed))


def count_md_files(root: Path) -> int:
    count = 0
    for folder in root.iterdir():
        if folder.is_dir() and re.match(r"[Dd]ay\d+", folder.name):
            count += len(list(folder.glob("*.md")))
    return count


def count_py_files(root: Path) -> int:
    count = 0
    for folder in root.iterdir():
        if folder.is_dir() and re.match(r"[Dd]ay\d+", folder.name):
            count += len(list(folder.glob("*.py")))
    return count


def get_categories(completed_days: list[int]) -> int:
    cats = {DAY_CATEGORIES.get(d) for d in completed_days if DAY_CATEGORIES.get(d)}
    return len(cats)


# ── BUILD PROGRESS BAR ───────────────────────────────────────────────────────
def build_progress_bar(completed: list[int], total: int = 30) -> str:
    filled = len(completed)
    pct = round((filled / total) * 100, 1)
    bar_len = 27
    filled_blocks = round((filled / total) * bar_len)
    bar = "█" * filled_blocks + "░" * (bar_len - filled_blocks)
    return f"```\nProgression  {bar}  {pct}% — Jour {filled}/{total}\n```"


# ── BUILD STATS TABLE ────────────────────────────────────────────────────────
def build_stats_table(completed: list[int], md_count: int, py_count: int) -> str:
    filled = len(completed)
    cats = get_categories(completed)
    pct = round((filled / TOTAL_DAYS) * 100, 1)

    return f"""| Métrique | Valeur |
|---|---|
| 📅 Jours complétés | **{filled} / {TOTAL_DAYS}** |
| 📝 Fichiers Markdown | **{md_count}** |
| 🗂️ Catégories couvertes | **{cats}** |
| 🧠 Concepts techniques | **{filled}** |
| 🐍 Fichiers de code | **{py_count}** |
| 📈 Progression | **{pct}%** |"""


# ── BUILD BADGES ─────────────────────────────────────────────────────────────
def build_badges(completed: list[int]) -> str:
    filled = len(completed)
    color = "7F77DD" if filled < 15 else ("1D9E75" if filled < 25 else "E85D24")
    return f"""[![Days Completed](https://img.shields.io/badge/Jours%20complétés-{filled}%2F{TOTAL_DAYS}-{color}?style=for-the-badge&logo=bookstack&logoColor=white)](.)
[![License](https://img.shields.io/badge/License-MIT-1D9E75?style=for-the-badge)](./LICENSE)
[![Language](https://img.shields.io/badge/Lang-Python%20%7C%20JavaScript-185FA5?style=for-the-badge&logo=python&logoColor=white)](.)
[![Challenge](https://img.shields.io/badge/Ramadan-1447%20H-E85D24?style=for-the-badge)](.)"""


# ── BUILD STRUCTURE ───────────────────────────────────────────────────────────
def build_structure(root: Path) -> str:
    """Auto-generate the project structure tree from actual Day* folders."""
    day_folders = sorted(
        [f for f in root.iterdir() if f.is_dir() and re.match(r"[Dd]ay\d+", f.name)],
        key=lambda f: int(re.search(r"\d+", f.name).group())
    )

    lines = []
    lines.append("```")
    lines.append("RamadanTechChallenge/")
    lines.append("├── .github/")
    lines.append("│   ├── workflows/")
    lines.append("│   │   └── update-readme.yml        ← ⚙️ GitHub Action auto-update")
    lines.append("│   └── scripts/")
    lines.append("│       └── update_readme.py          ← 🐍 Script Python")
    lines.append("│")

    for folder in day_folders:
        md_files = sorted(folder.glob("*.md"))
        py_files = sorted(folder.glob("*.py"))
        all_files = list(md_files) + list(py_files)

        lines.append(f"├── {folder.name}/")
        for i, f in enumerate(all_files):
            connector = "└──" if i == len(all_files) - 1 else "├──"
            label = "    ← 🐍 Code Python" if f.suffix == ".py" else ""
            lines.append(f"│   {connector} {f.name}{label}")

    lines.append("│")
    lines.append("├── README.md                         ← mis à jour automatiquement")
    lines.append("└── LICENSE")
    lines.append("```")

    return "\n".join(lines)


# ── BUILD CONCEPTS CLÉS ───────────────────────────────────────────────────────
def build_concepts(completed: list[int]) -> str:
    """
    Auto-generate 'Concepts clés maîtrisés' section based on completed days.
    Each category appears only if at least one of its days is completed.
    """
    completed_set = set(completed)

    # Define categories in order with their day ranges
    categories = [
        {
            "start_day": 1,
            "category": "security",
            "title": "🛡️ Sécurité",
            "days_range": [1],
            "concepts": [
                "SQL Injection, NoSQL Injection",
                "XSS (Cross-Site Scripting)",
                "CSRF, Brute Force, DDoS",
                "MITM, Broken Authentication",
                "JWT, HTTPS, Rate Limiting",
            ],
        },
        {
            "start_day": 2,
            "category": "devops",
            "title": "⚙️ DevOps & Cloud",
            "days_range": list(range(2, 9)),
            "concepts": [
                "Pipeline CI/CD complet (GitHub Actions)",
                "Docker : Images, Containers, Volumes, Networks",
                "Kubernetes : Pods, Deployments, Services, HPA",
                "Architecture Microservices & API Gateway",
                "Apache Kafka : Topics, Partitions, Consumer Groups",
                "IaaS / PaaS / SaaS",
            ],
        },
        {
            "start_day": 9,
            "category": "orm",
            "title": "🗄️ ORM & Base de données",
            "days_range": [9],
            "concepts": [
                "ORM Advanced — Index, Transactions",
                "N+1 Query Problem & Eager Loading",
                "Optimisation des requêtes SQL",
            ],
        },
        {
            "start_day": 10,
            "category": "ml",
            "title": "📊 Machine Learning",
            "days_range": list(range(10, 18)),
            "concepts": [
                "Introduction à l'IA — ML, DL, IA Générative",
                "Supervised / Unsupervised / Reinforcement Learning",
                "Logistic Regression, Decision Tree, Random Forest",
                "Confusion Matrix, Accuracy, Precision, Recall, F1 Score",
                "Overfitting / Underfitting, Bias-Variance Tradeoff",
                "Feature Engineering : Scaling, Normalization, Encoding",
                "ML Pipelines avec Scikit-Learn",
            ],
        },
        {
            "start_day": 18,
            "category": "dl",
            "title": "🔥 Deep Learning & IA Avancée",
            "days_range": list(range(18, 26)),
            "concepts": [
                "Artificial Neural Networks (ANN)",
                "Multilayer Perceptron (MLP), Fonctions d'activation",
                "Backpropagation & Gradient Descent",
                "Convolutional Neural Networks (CNN)",
                "Recurrent Neural Networks (RNN), Vanishing Gradient",
                "Transformer & Attention Mechanism — Self-Attention, BERT, GPT",
                "RAG — Retrieval Augmented Generation",
                "MLOps — Déploiement, FastAPI, Monitoring, Data Drift",
            ],
        },
    ]

    lines = []
    for cat in categories:
        # Show category only if at least one day in its range is completed
        if any(d in completed_set for d in cat["days_range"]):
            lines.append(f"<details open>")
            lines.append(f"<summary><b>{cat['title']}</b></summary>\n")
            for concept in cat["concepts"]:
                lines.append(f"- {concept}")
            lines.append(f"\n</details>\n")

    return "\n".join(lines)


# ── BUILD ROADMAP ROWS ───────────────────────────────────────────────────────
def build_roadmap_table(completed: list[int]) -> dict[str, str]:
    completed_set = set(completed)

    days_meta = {
        1:  ("🛡️", "Web Security — Types d'attaques backend (SQLi, XSS, CSRF, DDoS...)",
             "Day01_Web_Security", "Day01_Web_Security_Backend_Attacks.md", None),
        2:  ("🚀", "Introduction complète au DevOps",
             "Day02_DevOps", "Day02_DevOps_Introduction.md", None),
        3:  ("🐳", "Docker en profondeur — Images, Containers, Compose",
             "Day03_Docker", "Day03_Docker_Deep_Dive.md", None),
        4:  ("☸️", "Kubernetes — Architecture, Pods, Deployments, HPA",
             "Day04_Kubernetes", "Day04_Kubernetes_Deep_Dive.md", None),
        5:  ("🔄", "CI/CD complet — GitHub Actions + Docker + Kubernetes",
             "Day05_CICD", "Day05_CICD_Docker_GitHub_Kubernetes.md", None),
        6:  ("🏗️", "Architecture Microservices — Patterns, API Gateway",
             "Day06_Microservices", "Day06_Architecture_Microservices.md", None),
        7:  ("🔥", "Apache Kafka — Streaming, Topics, Consumer Groups",
             "Day07_Kafka", "Day07_Apache_Kafka_Deep_Dive.md", None),
        8:  ("☁️", "Cloud Computing — IaaS vs PaaS vs SaaS",
             "Day08_Cloud", "Day08_Cloud_Computing_IaaS_PaaS_SaaS.md", None),
        9:  ("🔗", "ORM Advanced — Index, Transactions, N+1, Eager Loading",
             "Day09_ORM", "Day_09_ORM_Advanced_Concepts.md", None),
        10: ("🤖", "Introduction à l'IA — ML, Deep Learning, IA Générative",
             "Day10_Intro_IA", "Day10_Intro_IA.md", None),
        11: ("📊", "Machine Learning — Types, Pipeline ML, Concepts clés",
             "Day11_ML", "Day11_ML.md", None),
        12: ("🔬", "Premier modèle ML — Logistic Regression en Python",
             "Day12_Modele_ML", "Day12_MLModel.md", "Day12_Modele_ML/Day12_MyModel.py"),
        13: ("🌳", "Classification Algorithms — Logistic, Decision Tree, Random Forest",
             "Day13_Classification_Algorithms", "Day13_Classification_Algorithms.md", None),
        14: ("📈", "Model Evaluation — Confusion Matrix, Accuracy, Precision, F1",
             "Day14_Model_Evaluation", "Day14_Model_Evaluation.md", None),
        15: ("⚖️", "Overfitting vs Underfitting — Bias, Variance, Regularization",
             "Day15_Overfitting_vs_Underfitting", "Day15_Overfitting_vs_Underfitting.md", None),
        16: ("🛠️", "Feature Engineering — Scaling, Normalization, Encoding",
             "Day16_Feature_Engineering", "Day16_Feature_Engineering.md", None),
        17: ("🔧", "ML Pipelines — Scikit-Learn Pipeline, Cross Validation",
             "Day17_ML_Pipeline", "Day17_ML_Pipeline.md", None),
        18: ("🧬", "Introduction au Deep Learning — ANN, Layers, Forward Prop",
             "Day18_Introduction_Deep_Learning", "Day18_Introduction_Deep_Learning.md", None),
        19: ("🧠", "Perceptron Multicouche (MLP) — Architecture, ReLU, Sigmoid",
             "Day19_Perceptron_Multicouche", "Day19_Perceptron_Multicouche.md", None),
        20: ("⬇️", "Backpropagation & Gradient Descent — Loss, Learning Rate",
             "Day20_Backpropagation_Gradient_Descent", "Day20_Backpropagation_Gradient_Descent.md", None),
        21: ("🖼️", "CNN — Convolution, Feature Maps, Pooling, Vision par ordinateur",
             "Day21_CNN_Convolutional_Neural_Networks", "Day21_CNN_Convolutional_Neural_Networks.md", None),
        22: ("🔁", "RNN — Données séquentielles, Vanishing Gradient, LSTM/GRU",
             "Day22_RNN_Recurrent_Neural_Networks", "Day22_RNN_Recurrent_Neural_Networks.md", None),
        23: ("🤗", "Transformers & Attention Mechanism",
             "Day23_transformer_attention", "Day23_transformer_attention.md", None),
        24: ("💬", "RAG — Retrieval Augmented Generation",
             "Day24_Rag", "Day24_Rag.md", None),
        25: ("🚀", "MLOps — Déploiement de modèles ML",
             "Day25_MLops", "Day25_MLops.md", None),
    }

    upcoming = {
        26: ("📡", "APIs REST avancées & GraphQL"),
        27: ("🔒", "Sécurité avancée — OAuth2, JWT, Zero Trust"),
        28: ("🗃️", "Bases de données distribuées"),
        29: ("🌐", "System Design — Architecture à grande échelle"),
        30: ("🏆", "Récapitulatif & mini-projet final"),
    }

    def status(day):
        return "✅" if day in completed_set else "🔜"

    def row(day):
        if day not in days_meta:
            return None
        emoji, title, folder, md_file, extra = days_meta[day]
        link = f"[📄 Day{day:02d}](./{folder}/{md_file})"
        if extra:
            link += f" · [🐍 Code](./{extra})"
        return f"| {status(day)} | {day:02d} | {emoji} {title} | {link} |"

    sec = "| | Jour | Concept | Fichier |\n|---|------|---------|---------|\n"
    sec += row(1) + "\n"

    devops = "| | Jour | Concept | Fichier |\n|---|------|---------|---------|\n"
    for d in range(2, 9):
        devops += row(d) + "\n"

    orm = "| | Jour | Concept | Fichier |\n|---|------|---------|---------|\n"
    orm += row(9) + "\n"

    ia_ml = "| | Jour | Concept | Fichier |\n|---|------|---------|---------|\n"
    for d in range(10, 18):
        ia_ml += row(d) + "\n"

    dl = "| | Jour | Concept | Fichier |\n|---|------|---------|---------|\n"
    for d in range(18, 26):
        dl += row(d) + "\n"

    up_rows = []
    for d in range(26, 31):
        if d not in completed_set:
            emoji, title = upcoming.get(d, ("❓", "À définir"))
            up_rows.append(f"| 🔜 | {d:02d} | {emoji} {title} |")

    upcoming_table = ""
    if up_rows:
        upcoming_table = "| | Jour | Concept prévu |\n|---|------|---------------|\n"
        upcoming_table += "\n".join(up_rows) + "\n"

    return {
        "security": sec,
        "devops": devops,
        "orm": orm,
        "ia_ml": ia_ml,
        "dl": dl,
        "upcoming": upcoming_table,
    }


# ── PATCH README ─────────────────────────────────────────────────────────────
def replace_section(content: str, key: str, new_content: str) -> str:
    pattern = rf"(<!-- AUTO:{key} -->).*?(<!-- /AUTO:{key} -->)"
    replacement = rf"\1\n{new_content}\n\2"
    result, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 0:
        print(f"  ⚠️  Section AUTO:{key} not found in README — skipping")
    return result


def update_readme(root: Path):
    completed = scan_days(root)
    md_count  = count_md_files(root)
    py_count  = count_py_files(root)

    print(f"✅ Days completed : {len(completed)} → {completed}")
    print(f"📄 Markdown files : {md_count}")
    print(f"🐍 Python files   : {py_count}")

    readme = README_PATH.read_text(encoding="utf-8")

    readme = replace_section(readme, "BADGES",           build_badges(completed))
    readme = replace_section(readme, "STATS",            build_stats_table(completed, md_count, py_count))
    readme = replace_section(readme, "PROGRESS",         build_progress_bar(completed))
    readme = replace_section(readme, "STRUCTURE",        build_structure(root))
    readme = replace_section(readme, "CONCEPTS",         build_concepts(completed))

    tables = build_roadmap_table(completed)
    readme = replace_section(readme, "ROADMAP_SECURITY", tables["security"])
    readme = replace_section(readme, "ROADMAP_DEVOPS",   tables["devops"])
    readme = replace_section(readme, "ROADMAP_ORM",      tables["orm"])
    readme = replace_section(readme, "ROADMAP_IAML",     tables["ia_ml"])
    readme = replace_section(readme, "ROADMAP_DL",       tables["dl"])
    readme = replace_section(readme, "ROADMAP_UPCOMING", tables["upcoming"])

    ts = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    readme = replace_section(readme, "UPDATED", f"*Dernière mise à jour automatique : `{ts}`*")

    README_PATH.write_text(readme, encoding="utf-8")
    print(f"✅ README.md updated successfully at {ts}")


if __name__ == "__main__":
    repo_root = Path(".")
    update_readme(repo_root)