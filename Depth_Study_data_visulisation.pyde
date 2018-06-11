import time
def setup():
    global data_list
    global mapped_list
    fullScreen()
    background(0)
    noStroke()
    maxi = 0
    mini = 9999999999999999#Okay this needs a better, more foolproof logic.
    data_list = []
    mapped_list = []

    data = open("data.txt")
    for value in data:
        value = value.rstrip()
        value = int(float(value))
        data_list.append(value)
        if int(value) > maxi:
            maxi = int(value)
        if int(value) < mini:
            mini = int(value)
    data.close()
    print("maxi", maxi)
    print("mini", mini)
    
    colours = loadImage("Colour mapping scheme2.png")
    image(colours, 0, 0, width, 30)
    
    mapped_data = open("mapped_data.txt", "r+")
    for value in data_list:
        #value = map(value, 0, maxi, 0, width)#Which one is better?
        value = map(value, mini, maxi, 0, width)#Which one is better?
        value = get(int(value)-1, 15)
        mapped_list.append(int(value))
        mapped_data.write(str(value)+"\n")
    
    background(0)
    segment_width = width/len(data_list)
    segment = 0
    for i in range(width/segment_width):
        fill(mapped_list[i])
        rect(segment, 0, segment + segment_width, height)
        segment += segment_width
    filter(BLUR, 30)