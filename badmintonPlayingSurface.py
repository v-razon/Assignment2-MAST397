from matplotlib import pyplot as plt

# Draws the white lines of the badminton court
def drawLines():
    plt.vlines([0, 2.6, 15.6, 28.4, 41.4, 44],0,20, colors="white", linestyles='solid', linewidths=3.0)
    plt.hlines([0, 1.6, 18.2, 20],0,44, colors="white", linestyles='solid', linewidths=3.0)
    plt.hlines(10, 0, 15.6, colors="white", linestyles='solid', linewidths=3.0)
    plt.hlines(10, 28.4, 41.4, colors="white", linestyles='solid', linewidths=3.0)

# Draws green rectangle surrounding the court
def drawRectangle():
    x_values_green = [-5,-5,49,49]
    y_values_green = [25,-5,-5,25]
    plt.fill(x_values_green,y_values_green, color="green")

# Draws net as a black dotted line
def drawNet():
    plt.vlines(22, -3, 23, colors="black", linestyles='dotted', label='NET', linewidths=3.0)

# Generates the badminton court and saves it as a PNG file
def badmintonCourt():
    drawLines()
    drawRectangle()
    drawNet()
    plt.axis('off')
    plt.savefig("badmintonCourt.png") 
    plt.show()

badmintonCourt()