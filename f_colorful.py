from gui_ver_tools import *
from f_grey import get_mirage_mat_grey

def get_mirage_mat_colorful(rgb_mat_W, rgb_mat_B):

    # Split RGB into 3 matrices, pair and call mirage_grey() with each pair
    mat_png_R = get_mirage_mat_grey(rgb_mat_W[:,:,0], rgb_mat_B[:,:,0])
    mat_png_G = get_mirage_mat_grey(rgb_mat_W[:,:,1], rgb_mat_B[:,:,1])
    mat_png_B = get_mirage_mat_grey(rgb_mat_W[:,:,2], rgb_mat_B[:,:,2])

    # Merge 3 "LA" matrices into 1 final "RGBA" 3D-Array
    final_png = np.empty((*rgb_mat_W.shape[:2], 4), dtype=float)
    final_png[:,:,0] = mat_png_R[:,:,0]
    final_png[:,:,1] = mat_png_G[:,:,0]
    final_png[:,:,2] = mat_png_B[:,:,0]
    final_png[:,:,3] = (mat_png_R[:,:,1] + mat_png_G[:,:,1] + mat_png_B[:,:,1]) / 3

    # Limit its values within [0, 1], then return it
    np.clip(final_png, 0., 1., out=final_png)
    return final_png


# For module testing
if __name__ == "__main__":

    I_W_path = "./imgs/Tom_surface.jpg"
    I_B_path = "./imgs/Tom_hidden.png"

    # Open in RGB mode
    I_W = Image.open(I_W_path).convert('RGB')
    I_B = Image.open(I_B_path).convert('RGB')

    # Get matrix of image I_W & I_B
    # and remind to cast {0,...,255} to [0,1] first
    mat_W = int2float(np.asarray(I_W))
    mat_B = int2float(np.asarray(I_B))

    # Get result RGBA image in matrix form
    mat_png = get_mirage_mat_colorful(mat_W, mat_B)

    # Trans mat to image in "RGBA" mode, then show it.
    # Notice that we should cast [0,1] to {0,...,255} first
    I_png = Image.fromarray(float2int(mat_png), "RGBA")
    I_png.show()

