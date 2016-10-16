# HIV Subtype Classification 
- David Luo, Ravi Mandla

## Background
HIV, or Human Immunodeficiency Virus, commonly occurs in two forms, HIV-1 and HIV-2. While both of these viruses lead to the affliction known as AIDS, HIV-1 acts in much faster rates in comparison to its “less deadly” counterpart. Within this category of HIV-1 lies a variety of subtypes. These subtypes are a direct result of the extensive variation that HIV undergoes due to its error-prone methods of replication, including a lack of proofreading with reverse transcriptase and recombination. HIV-1 consists of three predominant groups: M, N, and O. Within the M group lies 10 recognized subtypes as well as a variety of recombinant hybrids. Amongst these groups, the average genetic variability is 15% for the gag gene and 25% for the env gene. 
Classifying HIV-1 into subtypes is done with the help of nucleotide sequences from many subgenomic regions, including pol, env, and gag. 
These different subtypes are usually heavily concentrated in specific regions of the world. For example the C subtype accounts, based in Southern Africa and India, for 50% of all HIV infections, though little research has actually been done on this subtype of HIV. In North America and Western Europe, the B subtype is the most predominant. Determining what the subtype of a HIV virus is can therefore be used to determine the origin of infection.
Certain studies have also suggested that different subtypes have different risks of transmission and different rates of disease progression. Comparative research has largely been hindered due to a wide range of locations each HIV gene is taken from. 

## Aims
Our primary aim is to predict the subtype of a HIV virus based on its genome alone using machine learning techniques. We hope to create a classifier that when given specific pieces of the HIV genome, will be able to accurately place it in its correct subtype, as well as separate it from different subtypes. Doing so might help us determine the country of origin of infection from any specific strand of HIV. 

We will use Hamming Distances between different subtypes in order to classify them. 

## Timeline
- *Acquiring Data - 10/15*
- *Converting Data into readable files - 10/20*
- Determining features and algorithm to use - 10/30
- Implementing classifier to discern between two different subtypes - 11/8
- Implementing classifier to predict country of origin - 11/14
- Implementing classifier to discern between multiple subtypes - 1/25
- Create neural net to improve accuracy - 12/10

## Convention for data
### Contributing to the Repo
- clone this repository on your local machine (*git clone https://github.com/pimpshark/HIV-Classifier*)
- make your own branch in this new local repo (*git checkout -b name_of_branch*)
- whenever finished making changes to the repo, run *git add -A* and *git commit -m "some message" 
- run *git pull* then run *git push origin name_of_branch*
- to merge your branch, use pull requests on the github website, with the base branch being master and compare branch being your branch
### Naming Data
- name data files as "hiv" + subtype in capitals + "-" + gene name.filetype
- *hivB-gag.csv*
### Converting Data
- run *python conversion.py* followed by the fasta file name and location, as well as the csv file name and location to be created
- *python conversion.py data/hivB-gag.fasta data/hivB-gag.csv*
