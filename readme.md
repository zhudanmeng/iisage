## Instructions

1. Make sure you have "adata_head_S_v1.0.h5ad"
2. To generate the StringDB gene-gene correlations, run gene_gene.py and a numpy file gg_interactions.npy will be generated. This file is 24gb and may take a while to generate. Alternatively you can use a different method for generating the correlations, just replace gene_gene_interactions, adjacency matrix, and edge_index accordingly in new_gnn.ipynb.
3. Run new_gnn.ipynb
