from tools import *

def get_mirage_mat_grey(grey_mat_W, grey_mat_B):
    # Create mat_png as return_val, each pixel has channel L & A (Luminance and Alpha)
    mat_png = np.zeros((*grey_mat_W.shape, 2), dtype=float)
    mat_png[:,:,1] = np.clip(grey_mat_B - grey_mat_W + 1.0, 0, 1) # calc Alpha channel
    mat_png[:,:,0] = grey_mat_B / mat_png[:,:,1]              # calc Luminance channel
    return mat_png



# For module testing
if __name__ == '__main__':

    I_W_path = "./imgs/Tom_surface.jpg"
    I_B_path = "./imgs/Tom_hidden.png"

    # Open I_W and I_B and trans to L type
    I_W = Image.open(I_W_path).convert('L')
    I_B = Image.open(I_B_path).convert('L')

    # Then trans to mat, and remind to cast {0,...,255} to [0,1]
    mat_W = int2float(np.asarray(I_W))
    mat_B = int2float(np.asarray(I_B))

    # Call func in this module, get I_png in mat type
    mat_png = get_mirage_mat_grey(mat_W, mat_B)

    # Trans mat to image in "RGBA" mode,
    # which means Luminance & Alpha, then show it
    I_png = Image.fromarray(float2int(mat_png), "LA")
    I_png.show()

