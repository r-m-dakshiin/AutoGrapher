import pandas as pd
import plotly.express as px
try:
    file_location = input("Enter the location of the csv file with file name and extension : ")
    df = pd.read_csv(file_location)
except:
    print('File does not exist')

x = input("X axis(Enter from the data) : ")
y = input("Y axis(Enter from the data) : ")

type_of_graph = input("Enter the type of graph you would like(Enter only the name) : ").lower()

try:
    if(type_of_graph == "scatter"):
        size = input("Enter relative size from dataset(if you do not want size enter n) : ")
        colour = input("Enter relative color from dataset(if you do not want color enter n) : ")
        if(size == "n" and colour == "n"):
            fig = px.scatter(df, x=x, y=y)
        elif(size == "n"):
            fig = px.scatter(df,x=x,y=y,color=colour)
        elif(colour == "n"):
            fig = px.scatter(df,x=x,y=y,size=size)
        else:
            try:
                fig = px.scatter(df, x=x, y=y, size=size, color=colour)
            except:
                print("Colour or Size not found in the dataset given")
                fig = px.scatter(df, x=x, y=y)
        print("Please wait until graph is being processed.")


    elif(type_of_graph == "bar"):   
        colour = input("Enter color : ")
        try:
            fig = px.bar(df, x=x, y=y, color_discrete_sequence =[colour]*len(df))
        except:
            print("Colour not found, Using default colour")
            fig = px.bar(df, x=x, y=y)
        print("Please wait until graph is being processed.")


    elif(type_of_graph == "line"):
        size = input("Enter relative size(if you do not want size enter n) : ")
        sizeisgiven = False
        colour = input("Enter relative color(if you do not want color enter n) : ")
        colourisgiven = False
        if(size == "n" and colour == "n"):
            sizeisgiven = False
            colourisgiven = False
            fig = px.line(df, x=x, y=y)
        elif(size == "n"):
            fig = px.line(df,x=x,y=y,color=colour)
        elif(colour == "n"):
            fig = px.line(df,x=x,y=y,size=size)
        else:
            try:
                fig = px.line(df, x=x, y=y, size=size, color=colour)
            except:
                print("Colour or Size not found in the dataset given")
                fig = px.line(df, x=x, y=y)
        print("Please wait until graph is being processed.")
    else:
        print("Type does not exist")
except:
    print("x axis, y axis or both are not given properly(Check the spaces,capitalistation,signs)")
print("Processing done. Graph will apear in your default browser.")

fig.show()

