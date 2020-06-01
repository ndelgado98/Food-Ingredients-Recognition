def plot_model_sum(hist):
    acc = hist.history['accuracy']
    val_acc = hist.history['val_accuracy']
    loss = hist.history['loss']
    val_loss = hist.history['val_loss']
    epochs = range(len(acc))
    plt.plot(epochs, acc, 'teal', label='Train acc')
    plt.plot(epochs, val_acc, 'firebrick', label='Val acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.figure()
    plt.plot(epochs, loss, 'teal', label='Train loss')
    plt.plot(epochs, val_loss, 'firebrick', label='Val loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()