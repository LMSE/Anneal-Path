# Anneal-Path

Simulated Annealing-based branched novel biochemical pathway prediction tool

## Introduction

The advancement in the field of synthetic biology has allowed metabolic engineers to construct *de novo* pathways in engineered cells. The promiscuous activities of many enzymes which diversify the natural metabolic pathway network bring lots of possibilities for producing desired non-natural compounds. Although various graph-based computational tools were developed to predict novel pathways and have largely expanded the range of chemicals that can be produced biologically, the chemical repertoire reachable in microorganisms can be further broadened. The main challenge remains in dealing with the combinatorial growth of nodes and branches in the putative reaction network generated when searching the branched pathways. In this paper, a branched novel pathway computation tool that leverages probabilistic methods and machine learning, \textit{Anneal Path}, is presented. It targets chemical diversity and explores a larger theoretically possible chemical space. The pathway network has been modeled through a loop-less directed hypergraph, where a list of starting compounds and a target compound are connected with a series of hyper-edges, each representing a multi-molecular reaction.

This pathway identification program efficiently enumerates chemically possible branched novel biochemical pathways on the basis of (1) multi-molecular reaction hyper-edge rules which identify enzyme's promiscuity on multiple substrates and/or products, (2) simulated annealing-based pruning algorithm that efficiently handle the huge hypergraphic reaction network generated by hyper-edge rules and (3) a decision-tree-based pathway length predictor which accurately estimates the minimum number of enzymatic reaction steps required between two chemical structures. We also show that this \textit{Anneal Path} can identify a large set of branched pathways more efficiently than purely similarity based search methods. Source code for producing Anneal Path and pathway length predictor are available on GitHub at: https://github.com/LMSE/Anneal-Path and https://github.com/LMSE/PathwayLenPred, respectively.










## Sample

A python notebook shows the use of Anneal-Path: 
https://github.com/Zhiqing-Xu/Anneal-Path/blob/main/AP_MAIN/AnnealPath_Main.ipynb




## Quick Installation of Environment

- Clone the repo to your device you would like to run Anneal-Path, (requires git installed)
  ```
  git clone https://github.com/LMSE/Anneal-Path.git
  cd Anneal-Path
  ```


- Create a conda environment for RDkit, 
  ```
  conda create -c rdkit -n rdkit3 rdkit python=3.7
  ```


- Activating the conda environment, and install other required packages using `pip` or `conda`,
  ```
  conda activate rdkit3
  ``` 


- For using RDKit in Jupyter Notebooks, 
  ```
  conda install -n rdkit3 nb_conda_kernels
  ```


- Other packages, 
  ```
  pip install pymysql tqdm
  ```



## Change Path to R in AP_output.py 

Change Path to R in AP_output.py line301 for generating graphical output of the program, 

e.g., `R_path="/bin/R"` or `"C:\\R\\R-4.1.1\\bin\\Rscript.exe"`

