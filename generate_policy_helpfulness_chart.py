from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

INPUT_FILE = Path("/workspaces/GCAP3226_week2/week2.csv")
OUTPUT_DIR = Path("/workspaces/GCAP3226_week2/plots")
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    df = pd.read_csv(INPUT_FILE)

    candidate_columns = ["policy_helpfulness", "policy_helpfulness_original"]
    target_column = next((col for col in candidate_columns if col in df.columns), None)

    if target_column is None:
        raise ValueError(
            "No policy helpfulness column found. Expected one of: "
            + ", ".join(candidate_columns)
        )

    counts = df[target_column].value_counts().sort_index().reindex(range(1, 6), fill_value=0)
    labels = {
        1: "strongly oppose",
        2: "oppose",
        3: "neutral",
        4: "agree",
        5: "strongly agree",
    }

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar([labels[i] for i in range(1, 6)], [counts.get(i, 0) for i in range(1, 6)], color="steelblue")
    ax.set_title(f"Counts of {target_column}")
    ax.set_xlabel("Response")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    plt.tight_layout()

    output_path = OUTPUT_DIR / "policy_helpfulness_chart.png"
    fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close(fig)

    print(f"Saved chart to: {output_path}")


if __name__ == "__main__":
    main()
