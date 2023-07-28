from matplotlib import pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig('bar.png')
    plt.close()
    
    
def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('/imgs/pie.png')
    plt.close()
    
    
if __name__ == 'main':
    labels = ['a', 'b', 'c']
    values = [100, 200, 80]
# generate_bar_chart(labels, values)

# labels = ['a', 'b', 'c']
# values = [100, 200, 80]

# plt.pie(values, labels=labels)
# plt.show()