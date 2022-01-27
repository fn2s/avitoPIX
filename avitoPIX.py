# -*- coding: utf-8 -*-

from os import path, listdir, mkdir
import sys,argparse, cv2, piexif

def pixProcess(fileName, pathIN, pathOUT): 
    sizeY = args['sizeY']   
    label = args['label']
    txt = [label[:6], label[6:10], label[10:]]
    x, y = 18, 32    
    print(fileName, end='')
    img = cv2.imread(path.join(pathIN, fileName))
    size = (int(sizeY/img.shape[0] * img.shape[1]), sizeY)
    iShape = img.shape
    img = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    print('   Resized ', iShape, '---->', img.shape, end='')
    xx = [x, int(size[0]/2) - 42, size[0] - 140] # sublabels X coordinates
    for i in range(len(xx)): # number of sublabels == 3
        c = 255 - (img[y+4, xx[i]+4] + img[y+4, xx[i]+28] + # probing background color
                     img[y+14, xx[i]+4] + img[y+14, xx[i]+28]) / 4
        c = (int(c[0]),int(c[1]), int(c[2]))
        cv2.putText(img, txt[i], (xx[i],y), fontFace= cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=c, thickness=2, lineType=cv2.LINE_AA)
    print('  Labelled', end='')
    fp = path.join(pathOUT, fileName)
    if cv2.imwrite(fp, img):
        piexif.remove(fp)       # removing EXIF metadata
        print('   Written')
    else:
        print('   ERROR ! Cant write !')
        
def dirScan(dirIN, dirOUT):
    if not path.isdir(dirOUT):
        try:
            mkdir(dirOUT)
        except OSError as error:
            print('ERROR! Cannot create output directory !', error)
            sys.exit()    
    for name in listdir(dirIN):
        if path.isdir(path.join(dirIN, name)): # recursively processing subdir
            dirScan(path.join(dirIN, name), path.join(dirOUT, name))
        elif path.splitext(name)[1] in ('.JPG', '.jpg', '.jpeg', '.JPEG'):
            pixProcess(name, dirIN, dirOUT )   

ap = argparse.ArgumentParser(description = """
	Resizing JPG pictures in some directory and it's subdirectories,
    Removing EXIF MetaData
    Adding to them text label (usually phone number) splitted to 3 parts """)
ap.add_argument('-tel', '--label', type = str, default = '8(999)123-45-67',
		help = 'text label to put on pictures')         
ap.add_argument('-in', '--rootIN', type = str, default = 'pixIN',
		help = 'path to input directory (folder with pictures to process)')
ap.add_argument('-out', '--rootOUT', type = str, default = 'pixOUT',
		help = 'path to output directory (folder to write processed pictures)')
ap.add_argument('-y', '--sizeY', type = int, default = 512,
		help = 'vertical resolution of resized picture')
args = vars(ap.parse_args())

def main():
    print('*** Resizing, Clearing MetaData and Labelling Pictures ***')
    if not path.isdir(args['rootIN']):
        print('ERROR! Input directory doesnt exist !')
        sys.exit()    
    dirScan(args['rootIN'], args['rootOUT'])      
    print('*** All Pictures Processed OK ***')    

if __name__ == '__main__':
    main()
