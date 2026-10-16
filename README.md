# HMM DNA Sequence Analysis

A beginner-friendly Python project that demonstrates how a Hidden Markov Model (HMM) can be used to calculate probabilities for short DNA sequences.

## About the Project

This project uses a simple two-state HMM to analyse DNA sequences.

The hidden states are:
- **C** — Coding region
- **N** — Non-coding region

The observed DNA bases are A, C, G and T.

The program calculates the joint probability of each possible hidden-state path, finds the total probability of an observed sequence, and identifies the highest-probability path.

## Concepts Used

- Python dictionaries
- Functions
- Loops and conditional-free iteration
- Probability calculations
- `itertools.product()`
- Hidden Markov Models
- Initial, transition and emission probabilities

## How It Works

The model uses three types of probabilities:

1. **Initial probabilities:** Probability of starting in each hidden state.
2. **Transition probabilities:** Probability of moving from one hidden state to another.
3. **Emission probabilities:** Probability of observing a DNA base in a given hidden state.

The program evaluates all four possible two-state paths:

- C → C
- C → N
- N → C
- N → N

It then adds their joint probabilities to calculate the total likelihood of the observed sequence.

## Sequences Tested

- A → G
- T → T

## Sample Results

| DNA Sequence | Total Probability | Best Path |
|---|---:|---|
| A → G | 0.0568 | C → C |
| T → T | 0.0832 | N → N |

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python programcode.py
```

## Limitations

This is a small educational example using hypothetical probabilities and sequences of only two bases. It is intended to demonstrate HMM probability calculations, not to perform real-world biological sequence classification.

## Learning Outcome

This project helped me practise Python functions, dictionaries, probability calculations, and the basic working of Hidden Markov Models.
