import torch
import torch.nn as nn


class LSTM(nn.Module):

    def __init__(self,
                 vocab_size: int,
                 num_classes: int,
                 embedding_dim: int,
                 hidden_dim: int,
                 dropout: float):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.word_embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=2, batch_first=True, dropout=dropout)
        self.classifier = nn.Linear(hidden_dim, num_classes)

    def forward(self, sentence: torch.Tensor) -> torch.Tensor:
        embeds = self.word_embeddings(sentence)
        out, (hidden, cell)  = self.lstm(embeds)
        y_pred = self.classifier(hidden[-1])
        return y_pred
