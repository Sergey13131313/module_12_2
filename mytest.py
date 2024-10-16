import unittest
import mymodule as my


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def setResult(cls, obj):
        cls.all_results = obj

    def setUp(self):
        runner1 = my.Runner('Усэйн', 10)
        runner2 = my.Runner('Андрей', 9)
        runner3 = my.Runner('Ник', 3)
        return [runner1, runner2, runner3]

    def test_tournament1(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[0], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        aaa = self.all_results[len(self.all_results)]
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')

    def test_tournament2(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[1], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        aaa = self.all_results[len(self.all_results)]
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')

    def test_tournament3(self):
        list_runner = self.setUp()
        obj_t = my.Tournament(90, list_runner[0], list_runner[1], list_runner[2])
        aaa = obj_t.start()
        self.setResult(aaa)
        aaa = self.all_results[len(self.all_results)]
        self.assertEqual(self.all_results[len(self.all_results)], 'Ник')



    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f'{key}: {value.name}')


if __name__ == '__main__':
    unittest.main()
