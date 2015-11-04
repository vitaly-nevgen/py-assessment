import unittest

from answers import classes


class ClassesTestCase(unittest.TestCase):

    def test_get_class_name(self):
        """
        You should get instance's class name
        """

        self.assertEqual(classes.get_instance_class_name(list), 'type')
        self.assertEqual(classes.get_instance_class_name([1, 2, 3]), 'list')

        class SpamEggs():
            pass

        self.assertEqual(classes.get_instance_class_name(SpamEggs()), 'SpamEggs')

    def test_dynamically_create_class(self):
        """
        You should dynamically create class with 'greeting' method
        returning "Hello!" string
        """

        class_name = 'HelloMan'
        instance = classes.dynamically_create_class(class_name)()

        self.assertEqual(classes.get_instance_class_name(instance), class_name)
        self.assertEqual(instance.greeting(), 'Hello!')