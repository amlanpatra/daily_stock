def processing(df,out):
    import numpy as np
    length = len(df.index)
    inputs = np.zeros((length,3))
    x = ["Open","High","Low","Close"]
    x.remove(out)
    y = out
    for i in range(length):
        p = 0
        for j in x:
            inputs[i][p] = (df.iloc[i][j])
            p += 1

    targets = np.zeros(len(df.index))
    for i in range(len(df.index)):
        targets[i] = (df.iloc[i][y])

    inputs = inputs.astype('float32')
    targets = targets.astype('float32')
    final = [inputs,targets]
    return(final)




















