## Instructions

1. Make sure you have "adata_head_S_v1.0.h5ad"
2. Download 7227.protein.links.v11.5.txt (157 MB) from https://drive.google.com/file/d/1qVZUdHE5hiyS7g2OWJbB_t-m3RkTuxrA/view?usp=sharing
3. To generate the StringDB gene-gene correlations, run gene_gene.py and a numpy file gg_interactions.npy will be generated. This file is 24gb and may take a while to generate. Alternatively you can use a different method for generating the correlations, just replace gene_gene_interactions, adjacency matrix, and edge_index accordingly in new_gnn.ipynb.
4. Run new_gnn.ipynb
