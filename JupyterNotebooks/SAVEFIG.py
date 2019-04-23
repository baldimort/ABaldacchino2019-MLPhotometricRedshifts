import matplotlib.pyplot as plt
import time,socket

"""
This module was used to simplify saving of figures from matplotlib
If wou wish to use it, comment out the nulled main() function, uncomment
the function below, edit the file path in function to the desired location.

When SAVEFIG.main() is called, the two arguments required are:

message - string, the meassage to be printed to the terminal to 
prompt saving eg. "save astrometry figure? (y/n"

filetag - string, a tag inserted into the filename of the image
eg. "ASTROMETRY_PLOT"

The function will then save the figure most recently called
and save it in desired location with dpi=600 in png format.

"""
'''def main(null1, null2):
    return 0'''


def main(filetag,message='Save figure? (y/n)'):
    devicename = socket.gethostname()
#     print(devicename)
    a = input(message)
    isYes = (a == 'y' or a == 'Y' or a == 'yes' or a == 'Yes')
    file_name = time.strftime("%Y%m%d_%H%M%S_")+filetag+'.png'
    
    if isYes: print("Figure is saved as {}".format(file_name))
    
    if (devicename == 'LaNaranjaDos') and isYes:
          plt.savefig("/mnt/c/Users/Andrew/OneDrive/Uni/L4/ProjectFolder/GitRepo/FinalReport/Figs/"+file_name,\
                                                           dpi=600,format='png')
        
    elif isYes:
          plt.savefig("/mnt/e/Onedrive/Uni/L4/ProjectFolder/GitRepo/FinalReport/Figs/"+file_name,\
                            dpi=600,format='png')
    else: pass

if __name__ == "__main__":
    main('test')