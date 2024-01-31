# NEREEA: Named Entity Recognition Extensive Error Analysis

Library to compute extensive error analysis for named entity recognition (NER) models. This library is based on the work of [Nejadgholi et al. (2020)](https://aclanthology.org/2020.bionlp-1.19/) extended by [Báez et al. (2021)](https://dl.acm.org/doi/abs/10.1145/3498324) for nested entities.

## Installation

```bash
pip install git+https://github.com/fvillena/nereea.git
```

## Usage

```python
from nereea import ner_report
y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
ner_report(y_true, y_pred)
```

