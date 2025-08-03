import unittest

def max(a, b):
    """تابع مقایسه دو عدد و برگرداندن عدد بزرگتر"""
    if a > b:
        return a
    else:
        return b

class TestMaxFunction(unittest.TestCase):
    """کلاس تست برای تابع max"""
    
    def test_max_with_positive_numbers(self):
        """تست با اعداد مثبت"""
        result = max(5, 3)
        self.assertEqual(result, 5)
        self.assertEqual(max(10, 20), 20)
        self.assertEqual(max(100, 50), 100)
    
    def test_max_with_negative_numbers(self):
        """تست با اعداد منفی"""
        result = max(-5, -10)
        self.assertEqual(result, -5)
        self.assertEqual(max(-20, -15), -15)
    
    def test_max_with_zero(self):
        """تست با صفر"""
        self.assertEqual(max(0, 5), 5)
        self.assertEqual(max(-5, 0), 0)
        self.assertEqual(max(0, 0), 0)  # وقتی هر دو صفر باشند
    
    def test_max_with_equal_numbers(self):
        """تست با اعداد مساوی"""
        self.assertEqual(max(10, 10), 10)
        self.assertEqual(max(-5, -5), -5)
        self.assertEqual(max(0, 0), 0)
    
    def test_max_with_large_numbers(self):
        """تست با اعداد بزرگ"""
        self.assertEqual(max(999999, 1000000), 1000000)
        self.assertEqual(max(-999999, -1000000), -999999)
    
    def test_max_with_decimal_numbers(self):
        """تست با اعداد اعشاری"""
        self.assertEqual(max(3.14, 3.15), 3.15)
        self.assertEqual(max(2.5, 2.5), 2.5)
        self.assertEqual(max(-1.5, -1.6), -1.5)

if __name__ == "__main__":
    unittest.main()
    

    