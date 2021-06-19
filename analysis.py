import torch


def torch_analysis(limit, inp, tgt):

    inputs = torch.from_numpy(inp)
    targets = torch.from_numpy(tgt)
    w = torch.randn(1, 3, requires_grad=True)
    #b = torch.randn(25,1, requires_grad=True)
    b = torch.randn(len(tgt), 1, requires_grad=True)

    def model(x):
        return (x @ w.t() + b)

    def mse(t1, t2):
        diff = t1 - t2
        return (torch.sum(diff * diff) / diff.numel())

    for i in range(limit):
        preds = model(inputs)
        loss = mse(targets, preds)
        loss.backward()
        with torch.no_grad():
            w -= w.grad * 1e-8
            b -= b.grad * 1e-8
            w.grad.zero_()
            b.grad.zero_()
    result = [preds, w, b]
    return result


# print(preds)
# print(targets)
# print(loss)
