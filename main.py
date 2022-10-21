#Michael Curran
#I could not figure out how to split the lines, ive tried multiple different times, watch youtube videos its just confusing.
#The program should run fine. 
f = open("nationsPop.txt", "r")
#This loads the text file into python, and reads the file.
print(f.readlines())
#This prints the contents of the file into the output.
import arcade
#this imports the arcade plugin.
arcade.open_window(1200, 900, "Population Bar Graph")
#This opens a window where the bargraph will be.
arcade.start_render()
#this starts to render what we type into the window.
arcade.draw_line(100, 100, 1100, 100, arcade.color.RED)
#This draws the horizontal red line seen in the window.
arcade.draw_line(100, 100, 100, 850, arcade.color.RED)
#This draws the vertical red line seen in the window.
arcade.draw_text("World's Most Populous Countries", 350, 775, arcade.color.RED)
#This draws the red text seen in the window.
arcade.draw_text("China",100, 75, arcade.color.RED, 10)
arcade.draw_text("India",160, 75, arcade.color.RED, 10)
arcade.draw_text("USA",210, 75, arcade.color.RED, 10)
arcade.draw_text("Indonesia",260, 75, arcade.color.RED, 10)
arcade.draw_text("Pakistan",350, 75, arcade.color.RED, 10)
arcade.draw_text("Nigeria",430, 75, arcade.color.RED, 10)
arcade.draw_text("Brazil",500, 75, arcade.color.RED, 10)
arcade.draw_text("Bangladesh",570, 75, arcade.color.RED, 10)
arcade.draw_text("Russia", 660, 75, arcade.color.RED, 10)
arcade.draw_text("Mexico", 725, 75, arcade.color.RED, 10)
arcade.draw_text("Japan", 790, 75, arcade.color.RED, 10)
arcade.draw_text("Ethiopia", 850, 75, arcade.color.RED, 10)
arcade.draw_text("Philippines", 925, 75, arcade.color.RED, 10)
arcade.draw_text("Egypt", 1025, 75, arcade.color.RED, 10)
#These lines of code label the x-axis of the graph.
arcade.draw_text("100M", 25, 100, arcade.color.RED, 10)
arcade.draw_text("200M", 25, 150, arcade.color.RED, 10)
arcade.draw_text("300M", 25, 200, arcade.color.RED, 10)
arcade.draw_text("400M", 25, 250, arcade.color.RED, 10)
arcade.draw_text("500M", 25, 300, arcade.color.RED, 10)
arcade.draw_text("600M", 25, 350, arcade.color.RED, 10)
arcade.draw_text("700M", 25, 400, arcade.color.RED, 10)
arcade.draw_text("800M", 25, 450, arcade.color.RED, 10)
arcade.draw_text("900M", 25, 500, arcade.color.RED, 10)
arcade.draw_text("1B", 25, 550, arcade.color.RED, 10)
arcade.draw_text("1.1B", 25, 600, arcade.color.RED, 10)
arcade.draw_text("1.2B", 25, 650, arcade.color.RED, 10)
arcade.draw_text("1.3B", 25, 700, arcade.color.RED, 10)
arcade.draw_text("1.4B", 25, 750, arcade.color.RED, 10)
arcade.draw_text("1.5B", 25, 800, arcade.color.RED, 10)
#These lines of code label the y-axis of the graph.
arcade.draw_lrtb_rectangle_filled(110, 120, 775, 100, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(170, 180, 769, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(217, 227, 225, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(285, 295, 190, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(365, 375, 165, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(445, 455, 159, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(515, 525, 155, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(590, 600, 140, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(675, 685, 125, 100, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(740, 750, 118, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(805, 815, 115, 100, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(865, 875, 114, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(955, 965, 110, 100, arcade.color.BLUE)
arcade.draw_lrtb_rectangle_filled(1040, 1050, 105, 100, arcade.color.BLUE)
#These lines draw the colored bars that are part of the graph.












arcade.finish_render()
#This finishes the rendering process and closes the window
arcade.run()
#This runs the arcade simulation

