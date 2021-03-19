import numpy as np
from PIL import Image

def int2float(img_mat):
    return img_mat.astype(float) / 255

def float2int(img_mat):
    return (img_mat * 255).astype('u1')

def get_preview_mat(rgba_mat, bg_color):
    alpha_mat = int2float(rgba_mat[:, :, 3:])
    alpha_mat = np.concatenate((alpha_mat, alpha_mat, alpha_mat), axis=2)
    new_mat = int2float(rgba_mat[:, :, :3])
    new_mat = alpha_mat * new_mat + (1.0 - alpha_mat) * bg_color
    return float2int(new_mat)

def get_grey_mat(img_mat, wR=0.299, wG=0.587, wB=0.114):
    return wR * img_mat[:,:,0] + wG * img_mat[:,:,1] + wB * img_mat[:,:,2]

def lerp(rgb_mat, w_target, target):
    assert 0 <= w_target <= 1, "w_target should be in [0,1]!"
    if target == "grey":
        target_mat = get_grey_mat(rgb_mat).reshape(*rgb_mat.shape[0:2], 1)
        return rgb_mat[:,:,0:3] * (1-w_target) + np.concatenate([target_mat]*3, axis=2) * w_target
    elif target == "white":
        return rgb_mat[:,:,0:3] * (1-w_target) + w_target
    elif target == "black":
        return rgb_mat[:,:,0:3] * (1-w_target)
    else:
        raise TypeError("Unkown type, only support 'grey', 'white' or 'black'")




