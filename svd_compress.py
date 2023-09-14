import matplotlib.pyplot as plt
from numpy import linalg as la
import numpy as np
import matplotlib.image as mpimg

# Author: William Sobolewski

# A user defined class to compress images using Singular Value Decomposition

def compress(img, k, debug=False):
    def compress_method1(img, k, debug):
        # Divide the image array into its components corresponding to colors
        red = img[:, :, 0]
        green = img[:, :, 1]
        blue = img[:, :, 2]

        # Apply SVD to each color component
        U_red, s_red, Vt_red = la.svd(red)
        U_green, s_green, Vt_green = la.svd(green)
        U_blue, s_blue, Vt_blue = la.svd(blue)

        # Truncate the SVD arrays
        U_red = U_red[:, :k]
        s_red = s_red[:k]
        Vt_red = Vt_red[:k, :]

        U_green = U_green[:, :k]
        s_green = s_green[:k]
        Vt_green = Vt_green[:k, :]

        U_blue = U_blue[:, :k]
        s_blue = s_blue[:k]
        Vt_blue = Vt_blue[:k, :]

        # Reconstruct the color components
        red_approx = U_red @ np.diag(s_red) @ Vt_red
        green_approx = U_green @ np.diag(s_green) @ Vt_green
        blue_approx = U_blue @ np.diag(s_blue) @ Vt_blue

        # Combine the approximated color components into an image array
        img_approx = np.stack((red_approx, green_approx, blue_approx), axis=2)

        # Normalize the pixel values
        img_approx = img_approx - img_approx.min()
        img_approx = img_approx / img_approx.max()

        # Debug visualization
        if debug:
            plt.plot(s_red)
            plt.title("Singular Values (Red)")
            plt.show()

            plt.imshow(img_approx)
            plt.title("Approximated Image")
            plt.show()

        return img_approx

    def compress_method2(img, k, debug):
        # Transpose the image array into a suitable shape
        img_transposed = np.transpose(img, (2, 0, 1))

        # Apply SVD to the transposed image array
        U, s, Vt = la.svd(img_transposed)

        # Truncate the SVD arrays
        U = U[:, :k]
        s = s[:k]
        Vt = Vt[:k, :]

        # Reconstruct the image array
        img_approx = U @ np.diag(s) @ Vt
        img_approx = np.transpose(img_approx, (1, 2, 0))

        # Normalize the pixel values
        img_approx = img_approx - img_approx.min()
        img_approx = img_approx / img_approx.max()

        # Debug visualization
        if debug:
            plt.plot(s)
            plt.title("Singular Values")
            plt.show()

            plt.imshow(img_approx)
            plt.title("Approximated Image")
            plt.show()

        return img_approx

    # Read the image file and display the image
    img = mpimg.imread('octopus.jpg')
    plt.imshow(img)
    plt.show()

    # Analyze the image array
    print(img.ndim)
    X, Y, Z = img.shape  # get the image array dimensions
    print(X, Y, Z)
    print(img.dtype)
    print(img.max())
    print(img.min())

    # Compress the image using Method 1
    img_approx = compress_method1(img, k, debug=True)

    return img_approx


if __name__ == '__main__':
    # read the image file and display the image
    img = mpimg.imread('octopus.jpg')
    plt.imshow(img)
    plt.show()

    # analyze the image array
    print(img.ndim)
    X, Y, Z = img.shape                # get the image array dimensions
    print(X, Y, Z)
    print(img.dtype)
    print(img.max())
    print(img.min())

    img_approx = compress(img, 50)
    plt.imshow(img_approx)
    plt.show()
    plt.imsave("octopus_new.jpg", img_approx)
