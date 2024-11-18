from util import mkdir


# directory to store the results
results_dir = './results1/'
mkdir(results_dir)


# # root to the testsets
# dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/ForenSynths'

# # list of synthesis algorithms
# vals = ['progan', 'stylegan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
#         'crn', 'imle', 'seeingdark', 'san', 'deepfake', 'stylegan2', 'whichfaceisreal']
# # indicates if corresponding testset has multiple classes
# multiclass = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]



# root to the testsets
dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/UniversalFakeDetect'

# list of synthesis algorithms
vals = [ 'glide_100_10', 'ldm_200_cfg', 'glide_50_27' ,'ldm_100', 'glide_100_27', 'dalle', 'ldm_200', 'guided']

# indicates if corresponding testset has multiple classes
multiclass = [0, 0, 0, 0, 0, 0, 0, 0]




# root to the testsets
dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/Diffusion1kStep'

# list of synthesis algorithms
vals = [ 'dalle', 'ddpm', 'guided-diffusion' ,'improved-diffusion', 'midjourney']

# indicates if corresponding testset has multiple classes
multiclass = [0, 5, 0, 0, 0]



# model
model_path = 'weights/blur_jpg_prob0.1.pth'
