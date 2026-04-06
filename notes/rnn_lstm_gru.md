# RNN, LSTM and GRU

## Recurrent Neural Networks (RNNs)

# Weight Matrix Structure

## Vanilla RNN
- **1 weight matrix** (Whh)
- Simple recurrent update: $h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b)$
- Parameters: $d_h \times (d_x + d_h + 1)$

## LSTM (Long Short-Term Memory)
- **4 separate weight matrices** (one per gate):
  - $W_f$ for forget gate
  - $W_i$ for input gate
  - $W_o$ for output gate
  - $W_c$ for cell candidate
- Each has both $W_{hh}$ and $W_{xh}$ components
- Parameters: $4 \times d_h \times (d_x + d_h + 1)$

## GRU (Gated Recurrent Unit)
- **3 separate weight matrices** (one per gate):
  - $W_r$ for reset gate
  - $W_z$ for update gate
  - $W_h$ for candidate hidden state
- Each has both $W_{hh}$ and $W_{xh}$ components
- Parameters: $3 \times d_h \times (d_x + d_h + 1)$

**Key Insight:** GRU is more complex than vanilla RNN (3 matrices vs 1) but simpler than LSTM (3 matrices vs 4), which is why it's faster than LSTM while maintaining comparable performance.

## Comparison Table


| Aspect | RNN (Vanilla) | LSTM | GRU |
|--------|---------------|------|-----|
| Number of gates | None (just tanh activation) | 3 gates + cell candidate (4 total) | 2 gates (Update + Reset) |
| Separate cell state | No – only hidden state $h_t$ | Yes ($C_t$ as memory highway) | No – merged with hidden state |
| Parameters per unit | $d_h \times (d_x + d_h + 1)$ | $4 \times d_h \times (d_x + d_h + 1)$ | $3 \times d_h \times (d_x + d_h + 1)$ |
| Training / Inference speed | Fastest | Slowest | Faster than LSTM (typically 20–30% faster) |
| Memory usage | Lowest | Highest | Lower than LSTM |
| Performance on long sequences | Poor (vanishing gradients) | Best | Very close to LSTM |
| Ease of implementation | Simplest | Most complex | Simpler than LSTM |
| Best when | Short sequences, simplicity, or very low-resource environments | Maximum long-term memory is critical | Speed + efficiency needed (especially on-device/edge) |

# Typical Selection Criteria
- If you need the best performance on long sequences and don't care about training time → **LSTM**
- If you want a good balance of performance and speed → **GRU**
- If you have very short sequences or want the simplest model → **Vanilla RNN**