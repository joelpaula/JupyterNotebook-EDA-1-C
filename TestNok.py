import unittest
import paramParser


class Tests(unittest.TestCase):

    def testOneIntValue(self):
        result = paramParser.main(["-d C:\\Path\\to\\yourfile\\xxx.m", "-p 'xxxParamName'", "-v 3"])
        self.assertTrue('xxxParamName.Value= 3', result)

    def testMultipleIntValues(self):
        result = paramParser.main(["-d C:\\Path\\to\\yourfile\\xxx.m", "-p 'xxxParamName'", "-v 3"])
        self.assertTrue('[ xxxParamName.Value = [ 1 2 3 ]', result)

    def testTrueBoolean(self):
        result = paramParser.main(["-d C:\\Path\\to\\yourfile\\xxx.m", "-p 'xxxParamName'", "-v true"])
        self.assertTrue('xxxParamName.Value = true', result)

    def testOneValue(self):
        parsed = paramParser.main(["-d", "C:\\Path\\to\\yourfile\\xxx.m", "-p", "xxxParamName", "-v", "3"])
        self.assertEqual(parsed["d"], "C:\\Path\\to\\yourfile\\xxx.m")
        self.assertEqual(parsed["p"], "xxxParamName")
        self.assertEqual(parsed["v"], "3")


if __name__ == '__main__':
    unittest.main()
