# NEREEA: Named Entity Recognition Extensive Error Analysis

Library to compute extensive error analysis for named entity recognition (NER) models. This library is based on the work of [Nejadgholi et al. (2020)](https://aclanthology.org/2020.bionlp-1.19/) extended by [Báez et al. (2021)](https://dl.acm.org/doi/abs/10.1145/3498324) for nested entities.

## Installation

```bash
pip install git+https://github.com/fvillena/nereea.git
```

## Usage

```python
>>> from nereea import ner_report
>>> y_true = [['O', 'O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
>>> y_pred = [['O', 'O', 'B-MISC', 'I-MISC', 'I-MISC', 'I-MISC', 'O'], ['B-PER', 'I-PER', 'O']]
>>> report = ner_report(y_true, y_pred)
>>> print(report)
NerReport(
    correct=1,
    false_positives=0,
    false_negatives=0,
    wrong_label_right_span=0,
    wrong_label_overlapping_span=0,
    right_label_overlapping_span=1,
)
>>> report.asdict()
{
    "correct": [("PER", 8, 9)],
    "false_positives": [],
    "false_negatives": [],
    "wrong_label_right_span": [],
    "wrong_label_overlapping_span": [],
    "right_label_overlapping_span": [(("MISC", 3, 5), ("MISC", 2, 5))],
}
```

