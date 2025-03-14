from util import mkdir


# directory to store the results
results_dir = './results1/'
mkdir(results_dir)


# # root to the testsets
# dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/ForenSynths'

dataroot = '/home/ubuntu/jpeg/jpeg75/foren/test'
# # list of synthesis algorithms
vals = ['progan', 'stylegan', 'biggan', 'cyclegan', 'stargan', 'gaugan',
        'deepfake', 'stylegan2']
# # indicates if corresponding testset has multiple classes
# multiclass = [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]

multiclass = [1, 1, 0, 1, 0, 0, 0,1, ]

# # root to the testsets
# dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/UniversalFakeDetect'

# # list of synthesis algorithms
# vals = [ 'glide_100_10', 'ldm_200_cfg', 'glide_50_27' ,'ldm_100', 'glide_100_27', 'dalle', 'ldm_200', 'guided']

# indicates if corresponding testset has multiple classes
# multiclass = [0, 0, 0, 0, 0, 0, 0, 0]




# # root to the testsets
# dataroot = '/home/fanzheming/zm/NPR-DeepfakeDetection/dataset/Diffusion1kStep'

# # list of synthesis algorithms
# vals = [ 'dalle', 'ddpm', 'guided-diffusion' ,'improved-diffusion', 'midjourney']

# # indicates if corresponding testset has multiple classes
# multiclass = [0, 5, 0, 0, 0]

# root to the testsets
# dataroot = '/home/ubuntu/genimagestest/test'

# list of synthesis algorithms
# vals = [ 'wukong', 'VQDM', 'sd14', 'sd15', 'Midjourney', 'glide', 'biggan', 'adm']

# indicates if corresponding testset has multiple classes
# multiclass = [0, 0, 0, 0, 0, 0, 0, 0]

# model
model_path = 'weights/blur_jpg_prob0.1.pth'
