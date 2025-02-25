import torch
from chroma import Chroma, Protein, conditioners, api
device = 'cuda' if torch.cuda.is_available() else 'cpu'
api.register_key("5f98d91c46204cf8a5417ef0118f62d5")

# Initialize the Model
chroma = Chroma()

# Sample a Protein
protein = chroma.sample()

print(protein) # Inspect the sequence of the protein sample
protein.to('chroma_sample.cif') # Save the sample to disk