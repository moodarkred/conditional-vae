import utils
import vanilla_train
import vanilla_seq2seq

train_iter, val_iter, test, DE, EN = utils.torchtext_extract()

model_name = "seq2seq_attention_vanilla"

gpu = True

num_layers = 4
embed_size = 500
hidden_size = 750

num_epochs = 50

model = vanilla_seq2seq.Seq2Seq(len(DE.vocab), len(EN.vocab), embed_size, hidden_size, num_layers)
if gpu:
    model.cuda()

vanilla_train.train(model, model_name, train_iter, val_iter, DE, EN, num_epochs, gpu, checkpoint=True)