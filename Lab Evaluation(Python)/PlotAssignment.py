import matplotlib.pyplot as plt

years = dict()
years[2010] = [100,560,200,327,487]
years[2011] = [50,260,170,335,87]
years[2012] = [304,210,455,109,290]
years[2013] = [131,333,270,357,390]
years[2014] = [65,300,225,175,106]

products = ['product1', 'product2', 'product3', 'product4', 'product5']

for k,v in years.items():
    print(k,v)
    plt.pie(v,labels=products, autopct='%1.2f%%')
    plt.title("Year {}".format(k))
    plt.show()
    
plt.stackplot(years.keys(),years[2010],years[2011],years[2012],years[2013],years[2014],labels=products)    
plt.legend(loc='upper right')