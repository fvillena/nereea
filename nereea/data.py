from typing import List, Tuple
from dataclasses import dataclass

Label = str
Labels = List[Label]
NestedLabels = List[List[Label]]
Annotation = Tuple[Label, int, int]


# {'n_exact_matches': 9,
#  'n_false_positives': 0,
#  'n_false_negatives': 0,
#  'n_wrong_label_right_span': 0,
#  'n_wrong_label_overlapping_span': 0,
#  'n_right_label_overlapping_span': 0,
#  'correct': [('person', 0, 1),
#   ('location', 6, 6),
#   ('organization', 11, 11),
#   ('person', 14, 15),
#   ('location', 21, 24),
#   ('person', 27, 28),
#   ('organization', 33, 33),
#   ('person', 36, 37),
#   ('location', 43, 43)],
#  'false_positives': [],
#  'false_negatives': [],
#  'wrong_label_right_span': [],
#  'wrong_label_overlapping_span': [],
#  'right_label_overlapping_span': []}


@dataclass
class NerReport:
    """Named Entity Recognition Error Analysis Report
    Args:
        correct (List[Tuple[str, int, int]]): List of correct annotations. Each annotation is a tuple of the form (label, start, end).
        false_positives (List[Tuple[str, int, int]]): List of false positives. Each annotation is a tuple of the form (label, start, end).
        false_negatives (List[Tuple[str, int, int]]): List of false negatives. Each annotation is a tuple of the form (label, start, end).
        wrong_label_right_span (List[Tuple[str, int, int]]): List of wrong label right span. Each annotation is a tuple of the form (label, start, end).
        wrong_label_overlapping_span (List[Tuple[str, int, int]]): List of wrong label overlapping span. Each annotation is a tuple of the form (label, start, end).
        right_label_overlapping_span (List[Tuple[str, int, int]]): List of right label overlapping span. Each annotation is a tuple of the form (label, start, end).
    """

    correct: List[Annotation]
    false_positives: List[Annotation]
    false_negatives: List[Annotation]
    wrong_label_right_span: List[Annotation]
    wrong_label_overlapping_span: List[Annotation]
    right_label_overlapping_span: List[Annotation]

    def __repr__(self) -> str:
        return f"""NerReport(
    correct={len(self.correct)},
    false_positives={len(self.false_positives)},
    false_negatives={len(self.false_negatives)},
    wrong_label_right_span={len(self.wrong_label_right_span)},
    wrong_label_overlapping_span={len(self.wrong_label_overlapping_span)},
    right_label_overlapping_span={len(self.right_label_overlapping_span)},
)"""
