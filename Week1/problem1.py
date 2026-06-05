
def linear_search(items, tagret):
    
    flag = False
    for i in range(len(items)):
        if target == items[i]:
            print(i)
            flag = True

    if flag == True:
        print("-1")


if __name__ == "__main__":

    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    linear_search(items, target)

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    linear_search(items, target)
