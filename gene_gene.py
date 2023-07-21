import scanpy
import numpy as np

adata = scanpy.read_h5ad('adata_head_S_v1.0.h5ad')

### Create labelled matrix from StringDB
# Read protein IDs from the first file
with open('7227.protein.info.v11.5.txt', 'r') as file:
    protein_ids = [line.split()[0] for line in file.readlines()[1:]]

# Create a dictionary to store row and column indices
index_dict = {protein_id: index for index, protein_id in enumerate(protein_ids)}

# Read second file and create matrix
matrix = [[0.0] * len(protein_ids) for _ in range(len(protein_ids))]

with open('7227.protein.links.v11.5 2.txt', 'r') as file:
    next(file)  # Skip the first line
    for line in file:
        protein1, protein2, combined_score = line.split()
        row = index_dict[protein1]
        col = index_dict[protein2]
        matrix[row][col] = float(combined_score)
        matrix[col][row] = float(combined_score)  # If the matrix is symmetric

# Create the labeled matrix with protein IDs as row and column labels
labeled_matrix = [[protein_ids[j-1] if i == 0 else matrix[i-1][j-1] for j in range(len(matrix)+1)]
                  for i in range(len(matrix)+1)]
                
# Convert the gene-gene interaction data to a NumPy array
gene_gene_interactions = np.array(labeled_matrix)

with open('gg_interactions.npy', 'wb') as f:
    np.save(f, gene_gene_interactions)