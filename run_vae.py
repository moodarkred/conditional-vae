import utils
import train
import cvae

model_name = "vae_dotattn"

gpu = True
device = 0

num_layers = 2
embed_size = 300
hidden_size = 300
latent_size = 300

lr = 0.002
dpt = 0.3

num_epochs = 50
batch_size = 64

train_iter, val_iter, test, DE, EN = utils.torchtext_extract(d=device, BATCH_SIZE=batch_size)

anneal = utils.kl_anneal_linear

model = cvae.CVAE(len(DE.vocab), len(EN.vocab), embed_size, hidden_size, latent_size, num_layers, dpt)
if gpu:
    model.cuda()

print("Number of parameters: {}".format(utils.count_parameters(model)))

train.train(model, model_name, train_iter, val_iter, DE, EN, anneal, num_epochs, gpu, lr, checkpoint=True)