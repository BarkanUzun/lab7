import cv2

image = cv2.imread('/Users/barkanuzun/Desktop/IMG_5595.jpeg')
if image is None:
    print("Error: Could not load the image. Please check the file path.")
else:
    # Split the image into BGR color channels
    blue_channel, green_channel, red_channel = cv2.split(image)

    # Show the color channels on the screen
    cv2.imshow('Blue Channel', blue_channel)
    cv2.imshow('Green Channel', green_channel)
    cv2.imshow('Red Channel', red_channel)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Modify the color channels to only have red and blue colors
    green_channel[:] = 0

    # Merge the color channels back together
    modified_image = cv2.merge((blue_channel, green_channel, red_channel))

    # Show the modified image on the screen
    cv2.imshow('Modified Image', modified_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
