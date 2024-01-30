import unittest
from nereea import ner_report


class TestExtensiveErrorAnalysis(unittest.TestCase):
    def setUp(self):
        self.annotations = [
            # 0
            {
                "sentence": ["el", "paciente", "tiene", "ca", "de", "colon"],
                "true": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Disease", "B-Abbreviation"],
                    ["I-Disease"],
                    ["I-Disease", "B-Body_Part"],
                ],
                "predicted": [
                    ["B-Abbreviation"],
                    ["O"],
                    ["O"],
                    ["B-Disease"],
                    ["O"],
                    ["B-Body_Part"],
                ],
            },
            # 7
            {
                "sentence": [
                    "el",
                    "paciente",
                    "tiene",
                    "ca",
                    "espinocelular",
                    "de",
                    "borde",
                    "de",
                    "lengua",
                ],
                "true": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Disease", "B-Abbreviation"],
                    ["I-Disease"],
                    ["I-Disease"],
                    ["I-Disease", "B-Body_Part"],
                    ["I-Disease", "I-Body_Part"],
                    ["I-Disease", "I-Body_Part"],
                ],
                "predicted": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Disease", "B-Abbreviation"],
                    ["I-Disease"],
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Body_Part"],
                ],
            },
            # 17
            {
                "sentence": ["el", "paciente", "relata", "dolor", "en", "1.3"],
                "true": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom", "B-Body_Part"],
                ],
                "predicted": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Disease"],
                    ["I-Disease"],
                    ["I-Disease", "B-Body_Part"],
                ],
            },
            # 24
            {
                "sentence": ["el", "paciente", "relata", "tinnitus", "en", "od"],
                "true": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom", "B-Body_Part", "B-Abbreviation"],
                ],
                "predicted": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Disease"],
                    ["O"],
                    ["B-Body_Part"],
                ],
            },
            # 31
            {
                "sentence": ["el", "paciente", "presenta", "prúrito", "en", "mi"],
                "true": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom", "B-Body_Part", "B-Abbreviation"],
                ],
                "predicted": [
                    ["O"],
                    ["O"],
                    ["O"],
                    ["B-Sign_or_Symptom"],
                    ["B-Abbreviation", "I-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom", "B-Body_Part"],
                ],
            },
            # 38
            {
                "sentence": ["el", "paciente", "presenta", "cáncer"],
                "true": [["O"], ["O"], ["O"], ["B-Disease"]],
                "predicted": [
                    ["O"],
                    ["B-Sign_or_Symptom"],
                    ["I-Sign_or_Symptom"],
                    ["O"],
                ],
            },
        ]
        self.y_trues = [
            self.annotations[i]["true"] for i in range(len(self.annotations))
        ]
        self.y_predicteds = [
            self.annotations[i]["predicted"] for i in range(len(self.annotations))
        ]
        self.sentences = [
            self.annotations[i]["sentence"] for i in range(len(self.annotations))
        ]
        self.report = ner_report(self.y_trues, self.y_predicteds)

    def test_false_positives(self):
        self.false_positives = [
            # 0
            ("Abbreviation", 0, 0),
            # 7
            # 17
            # 24
            # 31
            ("Abbreviation", 35, 35),
            # 38
            ("Sign_or_Symptom", 39, 40),
        ]
        self.assertCountEqual(self.false_positives, self.report["false_positives"])

    def test_false_negatives(self):
        self.false_negatives = [
            # 0
            ("Abbreviation", 3, 3),
            # 7
            # 17
            # 24
            ("Abbreviation", 29, 29),
            # 31
            ("Abbreviation", 36, 36),
            # 38
            ("Disease", 41, 41),
        ]
        self.assertCountEqual(self.false_negatives, self.report["false_negatives"])

    def test_wrong_label_right_span(self):
        self.wrong_label_right_span = [
            # 0
            # 7
            # 17
            (("Sign_or_Symptom", 20, 22), ("Disease", 20, 22))
            # 24
            # 31
            # 38
        ]
        self.assertCountEqual(
            self.wrong_label_right_span, self.report["wrong_label_right_span"]
        )

    def test_wrong_label_overlapping_span(self):
        self.wrong_label_overlapping_span = [
            # 0
            # 7
            # 17
            # 24
            (("Sign_or_Symptom", 27, 29), ("Disease", 27, 27))
            # 31
            # 38
        ]
        self.assertCountEqual(
            self.wrong_label_overlapping_span,
            self.report["wrong_label_overlapping_span"],
        )

    def test_right_label_overlapping_span(self):
        self.right_label_overlapping_span = [
            # 0
            (("Disease", 3, 5), ("Disease", 3, 3)),
            # 7
            (("Disease", 10, 15), ("Disease", 10, 11)),
            (("Body_Part", 13, 15), ("Body_Part", 15, 15))
            # 17
            # 24
            # 31
            # 38
        ]
        self.assertCountEqual(
            self.right_label_overlapping_span,
            self.report["right_label_overlapping_span"],
        )


if __name__ == "__main__":
    unittest.main()
