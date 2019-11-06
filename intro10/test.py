import unittest
from datetime import date


class TestDiffDays(unittest.TestCase):

    # ルール1: 各テストメソッドは、1つのことだけテストする
    def _callFUT(self, from_date, to_date):
        # ルール2: テスト対象のモジュールをテストモジュールのスコープでインポートしない
        # モジュールスコープでインポートエラーになると他のテストメソッドも機能しなくなる可能性
        from sample import diff_days
        return diff_days(from_date, to_date)

    def test_from_date_is_before(self):
        """ from_date が to_date より古い日付 """
        actual = self._callFUT(date(2018, 1, 1), date(2018, 1, 6))
        self.assertEqual(5, actual)

    def test_from_date_is_after(self):
        """ from_date が to_date と同じか新しい日付 """
        actual = self._callFUT(date(2018, 1, 6), date(2018, 1, 1))
        self.assertIsNone(actual)
