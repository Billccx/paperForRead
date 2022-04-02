import torch
import torch.nn as nn
import torch.nn.functional as F

__author__ = "Yu-Hsiang Huang"

class ScaledDotProductAttention(nn.Module):
    ''' Scaled Dot-Product Attention '''

    def __init__(self, temperature, attn_dropout=0.1):
        super().__init__()
        self.temperature = temperature
        self.dropout = nn.Dropout(attn_dropout)

    def forward(self, q, k, v, mask=None):

        # q(batch * heads * n * d)
        # k(batch * heads * d * n)
        # attn(batch * heads * n * n)
        attn = torch.matmul(q / self.temperature, k.transpose(2, 3))

        #将mask为0的地方全部赋值为-1e9
        if mask is not None:
            attn = attn.masked_fill(mask == 0, -1e9)

        # attn(batch * heads * n * n)
        # v(batch * heads * n * dv)
        attn = self.dropout(F.softmax(attn, dim=-1))
        output = torch.matmul(attn, v)
        # output(batch * heads * n * dv)

        return output, attn
