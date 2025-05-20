mport pandas as pd
import umap
import hdbscan
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ==== SETTINGS ====
INPUT_FILE = "synthetic_dataset_1_binary.csv"
OUTPUT_FILE = "synthetic_dataset_1_with_clusters.csv"
CLUSTER_COL = "Cluster"
TRUE_COL = "TrueCluster"

# ==== 1. LOAD DATA ====
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"Dataset not found: {INPUT_FILE}")

df = pd.read_csv(INPUT_FILE)
print(f"✅ Loaded {INPUT_FILE} with {len(df)} rows")

# ==== 2. RUN UMAP ====
X = df.drop(columns=["PatientID", TRUE_COL], errors="ignore")
print("🔄 Running UMAP...")
reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(X)

# ==== 3. RUN HDBSCAN ====
print("🔍 Running HDBSCAN clustering...")
clusterer = hdbscan.HDBSCAN(min_cluster_size=10)
labels = clusterer.fit_predict(embedding)
df[CLUSTER_COL] = labels

# ==== 4. SAVE FILE WITH CLUSTERS ====
df.to_csv(OUTPUT_FILE, index=False)
print(f"💾 Saved clustered dataset to {OUTPUT_FILE}")

# ==== 5. UMAP PLOT ====
print("📊 Plotting UMAP clusters...")
results = pd.DataFrame(embedding, columns=["UMAP1", "UMAP2"])
results["Cluster"] = labels
sns.set(style="whitegrid")

plt.figure(figsize=(10, 8))
palette = sns.color_palette("Spectral", n_colors=len(set(labels)) - (1 if -1 in labels else 0))
sns.scatterplot(data=results, x="UMAP1", y="UMAP2", hue="Cluster", palette=palette, s=40)
plt.title("UMAP Clustering of Symptom Data")
plt.legend(title="Cluster")
plt.tight_layout()
plt.savefig("umap_clusters.png")
plt.show()

# ==== 6. SYMPTOM PREVALENCE HEATMAP ====
print("📋 Generating cluster interpretation heatmap...")
symptom_cols = [col for col in df.columns if col not in ["PatientID", TRUE_COL, CLUSTER_COL]]
cluster_summary = df.groupby(CLUSTER_COL)[symptom_cols].mean().round(2)

plt.figure(figsize=(12, 6))
sns.heatmap(cluster_summary.T, cmap="Blues", annot=True, cbar_kws={'label': 'Proportion with Symptom'})
plt.title("Symptom Prevalence by Cluster")
plt.xlabel("Cluster")
plt.ylabel("Symptom")
plt.tight_layout()
plt.savefig("symptom_heatmap.png")
plt.show()

# ==== 7. BAR PLOT FOR FIRST CLUSTER ====
print("📈 Generating bar plot for one cluster...")
cluster_id = cluster_summary.index[0]
cluster_symptoms = cluster_summary.loc[cluster_id]
cluster_symptoms.sort_values().plot(kind="barh", figsize=(10, 6),
                                    title=f"Top Symptoms in Cluster {cluster_id}")
plt.xlabel("Proportion of Patients with Symptom")
plt.tight_layout()
plt.savefig(f"cluster_{cluster_id}_symptoms.png")
plt.show()

# ==== 8. OPTIONAL: CROSS-TAB WITH TRUE CLUSTERS ====
if TRUE_COL in df.columns:
    print("\n📊 TrueCluster vs. Computed Cluster Crosstab:")
    print(pd.crosstab(df[TRUE_COL], df[CLUSTER_COL]))
else:
    print("ℹ️ TrueCluster column not found. Skipping comparison.")

print("✅ All steps complete. Visualisations saved as PNG files.")
