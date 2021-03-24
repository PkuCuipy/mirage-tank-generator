from gui_ver_tools import *
from f_colorful import *
from f_grey import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

# Init params
weight_lerp_white_W = 0.0
weight_lerp_grey_W = 0.0
weight_lerp_black_B = 0.0
weight_lerp_grey_B = 0.0

# Axes for showing images
fig = plt.figure(figsize=[7, 7])
I_W_ax = plt.subplot(3,2,1)
I_B_ax = plt.subplot(3,2,2)
Preview_W_ax = plt.subplot(3,2,3)
Preview_B_ax = plt.subplot(3,2,4)

# Create Slider to adjust params
wW_ax = plt.subplot(24,3,61)
gW_ax = plt.subplot(24,3,64)
bB_ax = plt.subplot(24,3,63)
gB_ax = plt.subplot(24,3,66)
wW_slider = Slider(wW_ax, 'lerp white', valmin=0.0, valmax=1.0, valinit=0.0, valstep=0.001)
gW_slider = Slider(gW_ax, 'lerp grey', valmin=0.0, valmax=1.0, valinit=0.0, valstep=0.001)
bB_slider = Slider(bB_ax, 'lerp black', valmin=0.0, valmax=1.0, valinit=0.0, valstep=0.001)
gB_slider = Slider(gB_ax, 'lerp grey', valmin=0.0, valmax=1.0, valinit=0.0, valstep=0.001)

# Open in RGB mode
I_W_path = "./imgs/fast_surface.png"
I_B_path = "./imgs/fast_hidden.png"
I_W = Image.open(I_W_path).convert('RGB')
I_B = Image.open(I_B_path).convert('RGB')

# Get original matrix of image I_W & I_B
original_mat_W = int2float(np.asarray(I_W))
original_mat_B = int2float(np.asarray(I_B))


def draw_4_imgs():
    global weight_lerp_white_W, weight_lerp_grey_W, weight_lerp_black_B, weight_lerp_grey_B

    # Process I_W & I_B with 4 params above
    mat_B = lerp(original_mat_B, weight_lerp_black_B, 'black')
    mat_B = lerp(mat_B, weight_lerp_grey_B, 'grey')
    mat_W = lerp(original_mat_W, weight_lerp_white_W, 'white')
    mat_W = lerp(mat_W, weight_lerp_grey_W, 'grey')

    # Get result RGBA image in matrix form
    mat_png = get_mirage_mat_colorful(mat_W, mat_B)

    # Get preview of this result in BG=white and BG=black
    mat_prevW = get_preview_mat(mat_png, 1)
    mat_prevB = get_preview_mat(mat_png, 0)

    # Get these 4 images
    I_W = Image.fromarray(float2int(mat_W), "RGB")
    I_B = Image.fromarray(float2int(mat_B), "RGB")
    I_prevW = Image.fromarray(float2int(mat_prevW), "RGB")
    I_prevB = Image.fromarray(float2int(mat_prevB), "RGB")

    # Draw these images with plt
    I_W_ax.imshow(I_W)
    I_B_ax.imshow(I_B)
    Preview_W_ax.imshow(I_prevW)
    Preview_B_ax.imshow(I_prevB)


def update_params_and_redraw(val):
    global weight_lerp_white_W, weight_lerp_grey_W, weight_lerp_black_B, weight_lerp_grey_B
    weight_lerp_white_W = wW_slider.val
    weight_lerp_grey_W = gW_slider.val
    weight_lerp_black_B = bB_slider.val
    weight_lerp_grey_B = gB_slider.val
    draw_4_imgs()


# Register func to sliders
wW_slider.on_changed(update_params_and_redraw)
gW_slider.on_changed(update_params_and_redraw)
bB_slider.on_changed(update_params_and_redraw)
gB_slider.on_changed(update_params_and_redraw)


