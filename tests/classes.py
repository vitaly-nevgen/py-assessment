import unittest

from answers import classes

from helpers.stdout_wrap import CapturedOutput

class ClassesTestCase(unittest.TestCase):

    def setUp(self):
        self.captured_output = CapturedOutput()

    def tearDown(self):
        del self.captured_output

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

    def test_operator_overloading(self):
        """
        You need to overload `add` operator to count total pages count
        """

        book1 = classes.Book(pages=100)
        book2 = classes.Book(pages=500)

        self.assertEqual(book1 + book2, 600)

    def test_reverse_operator_overloading(self):
        """
        You need to implement Book class with support of reverse adding
        """

        book1 = classes.Book(pages=400)
        self.assertEqual(5 + book1, 405)
        self.assertEqual(book1 + 10, 410)

    def test_context_manager(self):
        """
        You need to implement context manager, which prints events when it's entered and exited
        """

        with classes.ContextManager():
            pass

        output = self.captured_output.getvalue()
        self.assertEqual(output, 'entered\nexited')

    def test_access_counter(self):
        """
        You need to implement descriptor which counts how many times object was accessed
        read count, write count and total access count
        """

        class DummyClass():
            x = classes.AccessCounter()

        inst = DummyClass()

        dummy = inst.x
        inst.x = 5
        dummy = inst.x
        inst.x = 7
        inst.x = 9
        dummy = inst.x

        # when deleting - must print information about property accesses
        del inst.x

        output = self.captured_output.getvalue()
        self.assertEqual(output, 'read: 3 write: 4\naccess: 7')

