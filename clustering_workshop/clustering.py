import pandas as pd
import umap
import hdbscan
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

# Argument parser for selecting dataset from command line
parser = argparse.ArgumentParser(description="Run symptom clustering with UMAP + HDBSCAN")
parser.add_argument('--file', type=str, default='synthetic_dataset_1.csv',
                    help='Path to the CSV dataset (default: synthetic_dataset_1.csv)')
parser.add_argument('--output', type=str, default='cluster_plot.png',
                    help='Filename for the output plot image (default: cluster_plot.png)')
args = parser.parse_args()

# Load dataset
if not os.path.exists(args.file):
    raise FileNotFoundError(f"Dataset file '{args.file}' not found.")

print(f"📥 Loading dataset: {args.file}")
data = pd.read_csv(args.file)

# Dimensionality reduction using UMAP
print("🔄 Running UMAP for dimensionality reduction...")
reducer = umap.UMAP(random_state=42)
embedding = reducer.fit_transform(data)

# Clustering using HDBSCAN
print("🔍 Running HDBSCAN for clustering...")
clusterer = hdbscan.HDBSCAN(min_cluster_size=20)
labels = clusterer.fit_predict(embedding)

# Add results to DataFrame
results = pd.DataFrame(embedding, columns=['UMAP1', 'UMAP2'])
results['Cluster'] = labels

# Plot the clusters
print(f"📊 Plotting results to: {args.output}")
plt.figure(figsize=(10, 8))
palette = sns.color_palette('Spectral', n_colors=len(set(labels)) - (1 if -1 in labels else 0))
sns.scatterplot(data=results, x='UMAP1', y='UMAP2', hue='Cluster', palette=palette, s=30, legend='full')
plt.title('Symptom Clusters Identified by HDBSCAN')
plt.savefig(args.output, dpi=300)
plt.close()

# Summary
num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(f"✅ Done! Found {num_clusters} clusters (excluding noise).\nPlot saved as: {args.output}")
