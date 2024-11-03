# Importing the required libraries
from nis import match
import os, random, argparse  # Importing necessary modules
from PIL import Image        # Importing Image module from PIL library
import imghdr               # Importing imghdr module to determine image type
import numpy as np         # Importing numpy for numerical operations

def getAverageRGBOld(image):
    """
    Given PIL Image, return average value of color as (r, g, b)
    """
    # Number of pixels in image
    npixels = image.size[0]*image.size[1]
    # Get colors as [(cnt1, (r1, g1, b1)), ...]
    cols = image.getcolors(npixels)
    # Get [(c1*r1, c1*g1, c1*g2),...]
    sumRGB = [(x[0]*x[1][0], x[0]*x[1][1], x[0]*x[1][2]) for x in cols] 
    # Calculate (sum(ci*ri)/np, sum(ci*gi)/np, sum(ci*bi)/np)
    # The zip gives us [(c1*r1, c2*r2, ..), (c1*g1, c1*g2,...)...]
    avg = tuple([int(sum(x)/npixels) for x in zip(*sumRGB)])
    return avg

def getAverageRGB(image):
    """
    Given PIL Image, return average value of color as (r, g, b)
    """
    # Get image as numpy array
    im = np.array(image)
    # Get shape
    w,h,d = im.shape
    # Get average
    return tuple(np.average(im.reshape(w*h, d), axis=0))

def splitImage(image, size):
    """
    Given Image and dims (rows, cols) returns an m*n list of Images 
    """
    W, H = image.size[0], image.size[1]
    m, n = size
    w, h = int(W/n), int(H/m)
    # Image list
    imgs = []
    # Generate list of dimensions
    for j in range(m):
        for i in range(n):
            # Append cropped image
            imgs.append(image.crop((i*w, j*h, (i+1)*w, (j+1)*h)))
    return imgs

def getImages(imageDir):
    """
    Given a directory of images, return a list of Images
    """
    files = os.listdir(imageDir)
    images = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            # Explicit load so we don't run into resource crunch
            fp = open(filePath, "rb")
            im = Image.open(fp)
            images.append(im)
            # Force loading image data from file
            im.load() 
            # Close the file
            fp.close() 
        except:
            # Skip invalid images
            print("Invalid image: %s" % (filePath,))
    return images

def getImageFilenames(imageDir):
    """
    Given a directory of images, return a list of Image file names
    """
    files = os.listdir(imageDir)
    filenames = []
    for file in files:
        filePath = os.path.abspath(os.path.join(imageDir, file))
        try:
            imgType = imghdr.what(filePath) 
            if imgType:
                filenames.append(filePath)
        except:
            # Skip invalid images
            print("Invalid image: %s" % (filePath,))
    return filenames

def getBestMatchIndex(input_avg, avgs):
    """
    Return index of best Image match based on RGB value distance
    """
    # Input image average
    avg = input_avg
    # Get the closest RGB value to input, based on x/y/z distance
    index = 0
    min_index = 0
    min_dist = float("inf")
    for val in avgs:
        dist = ((val[0] - avg[0])*(val[0] - avg[0]) +
                (val[1] - avg[1])*(val[1] - avg[1]) +
                (val[2] - avg[2])*(val[2] - avg[2]))
        if dist < min_dist:
            min_dist = dist
            min_index = index
        index += 1
    return min_index

def createImageGrid(images, dims):
    """
    Given a list of images and a grid size (m, n), create 
    a grid of images. 
    """
    m, n = dims

    # Sanity check
    assert m*n == len(images)

    # Get max height and width of images
    # i.e., not assuming they are all equal
    width = max([img.size[0] for img in images])
    height = max([img.size[1] for img in images])

    # Create output image
    grid_img = Image.new('RGB', (n*width, m*height))

    # Paste images
    for index in range(len(images)):
        row = int(index/n)
        col = index - n*row
        grid_img.paste(images[index], (col*width, row*height))
    return grid_img

def createPhotomosaic(target_image, input_images, grid_size,
                    reuse_images=True):
    """
    Creates photomosaic given target and input images.
    """
    print('Splitting input image...')
    # Split target image 
    target_images = splitImage(target_image, grid_size)

    print('Finding image matches...')
    # For each target image, pick one from input
    output_images = []
    # For user feedback
    count = 0
    batch_size = int(len(target_images)/10)

    # Calculate input image averages
    avgs = []
    for img in input_images:
        avgs.append(getAverageRGB(img))

    for img in target_images:
        # Target sub-image average
        avg = getAverageRGB(img)
        # Find match index
        match_index = getBestMatchIndex(avg, avgs)
        output_images.append(input_images[match_index])
        # User feedback
        if count > 0 and batch_size > 10 and count % batch_size is 0:
            print('Processed %d of %d...' %(count, len(target_images)))
        count += 1
        # Remove selected image from input if flag set
        if not reuse_images:
            input_images.remove(match)

    print('Creating mosaic...')
    # Draw mosaic to image
    mosaic_image = createImageGrid(output_images, grid_size)

    # Return mosaic
    return mosaic_image

# Gather our code in a main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored

    # Parse arguments
    parser = argparse.ArgumentParser(description='Creates a photomosaic from input images')

    # Add arguments
    parser.add_argument('--target-image', dest='target_image', required=True)
    parser.add_argument('--input-folder', dest='input_folder', required=True)
    parser.add_argument('--grid-size', nargs=2, dest='grid_size', required=True)
    parser.add_argument('--output-file', dest='outfile', required=False)

    args = parser.parse_args()

    ###### INPUTS ######

    # Target image
    target_image = Image.open(args.target_image)

    # Input images
    print('Reading input folder...')
    input_images = getImages(args.input_folder)

    # Check if any valid input images found 
    if input_images == []:
        print('No input images found in %s. Exiting.' % (args.input_folder, ))
        exit()

    # Shuffle list - to get a more varied output?
    random.shuffle(input_images)

    # Size of grid
    grid_size = (int(args.grid_size[0]), int(args.grid_size[1]))

    # Output
    output_filename = 'mosaic.png'
    if args.outfile:
        output_filename = args.outfile

    # Re-use any image in input
    reuse_images = True

    # Resize the input to fit original image size?
    resize_input = True

    ##### END INPUTS #####

    print('Starting photomosaic creation...')

    # If images can't be reused, ensure m*n <= num_of_images 
    if not reuse_images:
        if grid_size[0]*grid_size[1] > len(input_images):
            print('Grid size less than number of images')
            exit()

    # Resizing input
    if resize_input:
        print('Resizing images...')
        # For given grid size, compute max dims w,h of tiles
        dims = (int(target_image.size[0]/grid_size[1]), 
                int(target_image.size[1]/grid_size[0])) 
        print("Max tile dims: %s" % (dims,))
        # Resize
        for img in input_images:
            img.thumbnail(dims)

    # Create photomosaic
    mosaic_image = createPhotomosaic(target_image, input_images, grid_size,
                                    reuse_images)

    # Write out mosaic
    mosaic_image.save(output_filename, 'PNG')

    print("Saved output to %s" % (output_filename,))
    print('Done.')

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
