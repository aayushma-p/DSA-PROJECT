import pandas as pd #pandas helps to read the csv file that is arranged in 2D form

class Molecule:
    def __init__(self, name, MW, logp, hbd, hba, psa):
        self.name = str(name)
        self.MW = float(MW)
        self.logp = float(logp)
        self.hbd = int(hbd)
        self.hba = int(hba)
        self.psa = float(psa)
        self.left = None #initializing step
        self.right = None ##initializing step
        root=None


def insert(root, mol): #when we insert a molecule, it first becomes the root
    if root is None:
        return mol

    if mol.name.lower() < root.name.lower(): # we use.lower so everything is in lower case and is easier to compare
        root.left = insert(root.left, mol)
    else:
        root.right = insert(root.right, mol)

    return root


def search(root, name):
    if root is None:
        return None

    if root.name.lower() == name.lower():
        return root

    if name.lower() < root.name.lower():
        return search(root.left, name)
    else:
        return search(root.right, name)


def lipinski(molecule):
    score = 0

    if molecule.MW <= 500:
        score += 1
    if molecule.logp <= 5:
        score += 1
    if molecule.hbd <= 5:
        score += 1
    if molecule.hba <= 10:
        score += 1

    return "Drug-Like" if score >= 3 else "Not Drug-Like"


def admet(molecule):
    absorption = "Good" if molecule.MW < 500 and m.logp < 5 else "Poor"
    distribution = "Good" if molecule.psa < 140 else "Poor"
    metabolism = "Good" if 1 < molecule.logp < 5 else "Poor"
    excretion = "Good" if molecule.MW < 600 else "Poor"
    toxicity = "Safe" if (molecule.hbd + molecule.hba) < 12 else "Risk"

    return absorption, distribution, metabolism, excretion, toxicity



def load_data(filename):
    data = pd.read_csv(filename)
    root = None

    for index, row in data.iterrows():
        mol = Molecule(
            row["Name"],
            row["MW"],
            row["LogP"],
            row["HBD"],
            row["HBA"],
            row["PSA"]
        )
        root = insert(root, mol)

    print("Dataset loaded successfully.")
    return root


file_name = "main.csv"
root = load_data(file_name)  #reads molecules from a csv file

name = input("Enter molecule name: ")
result = search(root, name) #calling our function by assigning a variable 

if result:
    print("Molecule Found")
    print("Name :", result.name)
    print("MW   :", result.MW)
    print("LogP :", result.logp)
    print("HBD  :", result.hbd)
    print("HBA  :", result.hba)
    print("PSA  :", result.psa)

    print("Lipinski Result:", lipinski(result))

    a, d, m, e, t = admet(result)
    print("ADMET Prediction:")
    print("Absorption  :", a)
    print("Distribution:", d)
    print("Metabolism  :", m)
    print("Excretion   :", e)
    print("Toxicity    :", t)

else:
    print("Molecule not found.")
