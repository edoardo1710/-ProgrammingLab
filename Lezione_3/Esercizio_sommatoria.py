def sum_csv(path_file):
    tot = 0
    with open(path_file, 'r') as my_file:
        for line in my_file:
            elements = line.strip().split(',')
            if elements[0] == 'Date':
                tot += float(elements[1])
    return tot
osso = sum_csv('shampoo_sales.csv')
print(f'{osso}')