
from itertools import chain, combinations

def main():
    filename = input("Enter filename(default mushrooms.csv): ")
    if filename == "":
        filename = "mushrooms.csv"
    
    file_handler = open(filename)
    transactions = []
    items = set()
    for line in file_handler:
        curr_items = line.strip().split(',')
        transactions.append(items)
        for item in curr_items:
            items.add(item)

    min_support = input("Enter min_support: ")
    min_confidence = input("Enter min_confidence: ")
    if min_support ==  "":
        min_support = 0.5
    if min_confidence == "":
        min_confidence = 0.5
    min_support = float(min_support)
    min_confidence = float(min_confidence)



    print( apriori(transactions, items, min_support, min_confidence) )
    
def apriori(transactions, items, min_support, min_confidence):
    f_itemsets = get_f_itemsets(transactions, items, min_support, min_confidence)
    rules = None

    return f_itemsets, rules

def get_f_itemsets(transactions, items, min_support, min_confidence):
    

def subsets(itemset): #non-empty
    return list(map(set, list(chain(*[combinations(itemset, i + 1) for i, a in enumerate(itemset)]) )))



if __name__ == "__main__":
    main()