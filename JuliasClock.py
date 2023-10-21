## 
#  @package JuliasClock
#  A library for building clocks based on the Julia Sets
#  @todo Implement better file sturucture. Having all the folders for all of the color gradings in the root directory
#  is kind of ugly. The program should be modified so that all the folders containing all of the pictures of all of 
#  julia sets are contained in like a backgrounds directory or something. Clean up the directory structure of the
#  project. 
#  @todo Consolidate all requirements into the requirements.txt file. Should be able to install all requirements
#  seamlessly via pip install -r requirements.txt or the equivalent idea using conda. This will help make the code
#  more productionalized. 
#  @todo Trace out the unit circle once. Store a matrix of value which compromise the length of time which each point
#  had to take to diverge. Map every other color grading onto it. Current POC method of recalculating every julia 
#  set for every color grading is just shit. 


from numpy import absolute
from Julia import *
from WallpaperUpdater import *
import time
from datetime import datetime
from datetime import date
from PIL import Image, ImageDraw
from numpy import genfromtxt
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd



# ##
# #
# class hour_and_minute :
#     def __init__(self, hour, minute):
#         self.hour = hour
#         self.minute = minute




## 
# Julia's Clock is a class defined for creating a clock which in generated from a discrete
# sample of julia sets calculated from points on the unit circle drawn in the complex 
# plane. 
# @note currently is limitted to a linux environment running gnome 
class JuliasClock :


    ## colors is a dictionary of color mappings provided by the matplotlib library. each color maps to a different hour on the clock
    # @details afmhot, autumn, bone, binary, bwr, brg, CMRmap, 
    #   cool, copper, cubehelix, flag, gnuplot, gnuplot2, 
    #   gray, hot, hsv, jet, ocean, pink, prism, rainbow, 
    #   seismic, spring, summer, terrain, winter, 
    #   nipy_spectral, spectral, Accent, Blues, BrBG, 
    #   BuGn, BuPu, Dark2, GnBu, Greens, Greys, Oranges, 
    #   OrRd, Paired, Pastel1, Pastel2, PiYG, PRGn, PuBu, 
    #   PuBuGn, PuOr, PuRd, Purples, RdBu, RdGy, RdPu,  
    #   RdYlBu, RdYlGn, Reds, Set1, Set2, Set3, Spectral, 
    #   YlGn, YlGnBu, YlOrBr, YlOrRd, gist_earth, gist_gray, 
    #  gist_heat, gist_ncar, gist_rainbow, gist_stern, 
    #  gist_yarg, coolwarm, Wistia, afmhot_r, autumn_r, bone_r, 
    #  binary_r, bwr_r, brg_r, CMRmap_r, cool_r, copper_r, 
    #  cubehelix_r, flag_r, gnuplot_r, gnuplot2_r, gray_r, 
    #  hot_r, hsv_r, jet_r, ocean_r, pink_r, prism_r, 
    #  rainbow_r, seismic_r, spring_r, summer_r, terrain_r, 
    #  winter_r, nipy_spectral_r, spectral_r, Accent_r, 
    #  Blues_r, BrBG_r, BuGn_r, BuPu_r, Dark2_r, GnBu_r, 
    #  Greens_r, Greys_r, Oranges_r, OrRd_r, Paired_r, 
    #  Pastel1_r, Pastel2_r, PiYG_r, PRGn_r, PuBu_r, 
    #  PuBuGn_r, PuOr_r, PuRd_r, Purples_r, RdBu_r, RdGy_r, 
    #  RdPu_r, RdYlBu_r, RdYlGn_r, Reds_r, Set1_r, Set2_r, 
    #  Set3_r, Spectral_r, YlGn_r, YlGnBu_r, YlOrBr_r, YlOrRd_r, 
    #  gist_earth_r, gist_gray_r, gist_heat_r, gist_ncar_r, 
    #  gist_rainbow_r, gist_stern_r, gist_yarg_r, coolwarm_r, 
    #  Wistia_r
    # @note this is easily modifiable in order to make it your own
    colors = {
        0 : 'gist_gray_r',
        1 : 'coolwarm_r',
        2 : 'Wistia_r',
        3 : 'gist_gray',
        4 : 'Greys',
        5 : 'prism',
        6 : 'ocean',
        7 : 'Accent',
        8 : 'nipy_spectral_r',
        9 : 'Purples',
        10 : 'Reds',
        11 : 'Oranges',
        12 : 'YlGn_r',
        13 : 'YlOrRd_r',
        14 : 'Greens',
        15 : 'BuGn',
        16 : 'GnBu',
        17 : 'Blues',
        18 : 'gist_stern_r',
        19 : 'gist_yarg_r',
        20 : 'gist_rainbow_r',
        21 : 'gist_earth_r',
        22 : 'Pastel2_r',
        23 : 'winter_r',
    }

    ##
    # Constructor
    def __init__(self, time_steps = 60):
        self._wallpaper_updater = WallpaperUpdater()
        self._time_steps = time_steps
        self.julia = Julia()
    

    ##
    # Check if the jpgs which the clock is created from is
    # already install or if they need to be compiled
    def jpgs_already_exist (self, path):
        return os.path.exists(path + '/winter_r/winter_r0.jpg')
    
   



    ##
    # Useless function but too lazy to delete
    def get_time (self):
        now = datetime.now()
        return now

    ##
    # Start and instance of the clock program
    def start_clock(self):
        path = os.getcwd()
        if (not self.jpgs_already_exist(path)):
            self._compile_sets_of_julia_sets()

        while(True):
            t = self.get_time()
            hour = t.hour
            minute = t.minute
    
            # color gets set by the hour via dictionary of color values
            color = self.colors[hour]

            # create the absolute path for( the 
            current_directory = os.getcwd()
            absolute_path = current_directory + '/' + color + '/' + color + str(minute) + '.jpg'

            self._wallpaper_updater.set_wallpaper(absolute_path)

            time.sleep(60) # sleep for sixty seconds

def exponentially_mapped_and_cyclic_itter(itter):
		return ( ( ( (itter/1080)**2 )*1080) **1.5) % 256
        
    


if __name__ == '__main__':
    jc = JuliasClock()

    julia = Julia()


    os.system(f'rm -rf Output')
    os.system(f'mkdir Output')
    os.system(f'mkdir Output/{date.today()}')
    # print('All ready ran today save or delete data')


    julia.render_unit_circle_sets_to_csv(f"./Output/{date.today()}", 1000, 1080, 1080, 1080)

    print("pic")

    raw_csv_data = np.genfromtxt(f'./Output/{date.today()}/mandelbrot.csv', delimiter= ',')

    raw_colored_array = np.stack(np.vectorize(exponentially_mapped_and_cyclic_itter)(raw_csv_data))


    colored_arr = np.zeros((1080, 1080, 3))

    colored_arr[:, :, 0] = raw_csv_data
    colored_arr[:, :, 1] = raw_colored_array
    colored_arr[:, :, 2] = raw_colored_array 



    img = Image.fromarray(colored_arr.astype('uint8'), 'RGB')

    print(img.getpixel((0, 1)))

    img.save("mandelbrot.png")

    # data = genfromtxt(g, delimiter = ',')
    # matplotlib.image.imsave('mandelbrot.png', data, cmap='gray')
    