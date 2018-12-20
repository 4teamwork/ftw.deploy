import unittest


class TestCase(unittest.TestCase):

    def deploy(self, *arguments):
        """Run the deploy script with the given arguments.
        """
        return self.script_runner('deploy', *arguments)
