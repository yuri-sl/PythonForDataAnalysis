import matplotlib.pyplot as plt
year = [1970,1975,1980,1985,1990,2000]

pop = [2.1519,3.692,5.263,6.972,10.32,12.123]

values = [0.0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]

year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
plt.plot(year,pop)
plt.show()
#plt.plot(year,pop)

#plt.scatter(year,pop)

#plt.hist(values,bins=3)
#plt.show()


# Build histogram with 5 bins
#plt.hist(values,5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(values,20)

# Show and clean up again
plt.show()
plt.clf()

#Ticks are made to visually change the name of the markings on each axis
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()



#Colors:
dict = {
    'Asia':'red',
    'Europe':'green',
    'Africa':'blue',
    'Americas':'yellow',
    'Oceania':'black'
}
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c = col,alpha=0.8)
# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call


# Show the plot
plt.show()