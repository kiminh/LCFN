## For latent embedding pre-training
## author@Wenhui Yu  2020.06.02
## email: yuwh16@mails.tsinghua.edu.cn

from p_train_model import *
from p_params import *
from p_print_save import *

GPU_index = "7"
os.environ["CUDA_VISIBLE_DEVICES"] = GPU_index
print('GPU index: ', GPU_index)

if __name__ == '__main__':
    para = [DATASET,MODEL,LR,LAMDA,EMB_DIM, BATCH_SIZE,SAMPLE_RATE,N_EPOCH,TEST_VALIDATION,TOP_K]
    para_name = ['DATASET','MODEL','LR','LAMDA','EMB_DIM','BATCH_SIZE','SAMPLE_RATE','N_EPOCH','TEST_VALIDATION','TOP_K']
    ## print and save model hyperparameters
    print_params(para_name, para)
    ## train the model
    train_model(para)

