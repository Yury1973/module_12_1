import unittest

import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walk = runner.Runner('Walker')
        for i in range(10):
            walk.walk()
        self.assertEqual(walk.distance, 50)

    def test_run(self):
        run = runner.Runner('Runner')
        for i in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        walk2 = runner.Runner('Walker_2')
        run2 = runner.Runner('Runner_2')
        for i in range(10):
            walk2.walk()
            run2.run()
        self.assertNotEqual(run2.distance, walk2.distance)


if __name__ == '__main__':
    unittest.main()
