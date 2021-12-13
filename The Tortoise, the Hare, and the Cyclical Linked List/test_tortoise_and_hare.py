from unittest import main, TestCase
from list_node import ListNode
from tortoise_and_hare import tortoise_and_hare


class TestTortoiseAndHare(TestCase):

    def test_no_cycle_none(self):
        """
        This test is for None being passed.
        No cycle exists. The algorithm should return None.
        """
        no_cycle_none_root, no_cycle_none_solution = ListNode.generateList(0)
        self.assertEqual(tortoise_and_hare(no_cycle_none_root), no_cycle_none_solution)

    def test_no_cycle_single(self):
        """
        This test is for a single node with None as the next_node being passed in.
        No cycle exists. The algorithm should return None.
        """
        no_cycle_single_root, no_cycle_single_solution = ListNode.generateList(1)
        self.assertEqual(tortoise_and_hare(no_cycle_single_root), no_cycle_single_solution)

    def test_no_cycle_multiple(self):
        """
        This test is for a linked list of length > 1.
        No cycle exists. The algorithm should return None.
        """
        no_cycle_multiple_root, no_cycle_multiple_solution = ListNode.generateList(3)
        self.assertEqual(tortoise_and_hare(no_cycle_multiple_root), no_cycle_multiple_solution)

    def test_start_cycle_single(self):
        """
        This test is for a single node which cycles back to itself.
        A cycle exists. The algorithm should return the node.
        """
        start_cycle_single_root, start_cycle_single_solution = ListNode.generateList(1, 1)
        self.assertEqual(start_cycle_single_root, start_cycle_single_solution)

    def test_start_cycle_multiple(self):
        """
        This test is for a linked list of length > 1 with a cycle back to the start.
        A cycle exists. The algorithm should return the node where the cycle began.
        """
        start_cycle_multiple_root, start_cycle_multiple_solution = ListNode.generateList(3, 1)
        self.assertEqual(tortoise_and_hare(start_cycle_multiple_root), start_cycle_multiple_solution)

    def test_middle_cycle_multiple(self):
        """
        This test is for a linked list of length > 1 with a cycle back to the middle.
        A cycle exists. The algorithm should return the node where the cycle began.
        """
        middle_cycle_multiple_root, middle_cycle_multiple_solution = ListNode.generateList(3, 2)
        self.assertEqual(tortoise_and_hare(middle_cycle_multiple_root), middle_cycle_multiple_solution)

    def test_end_cycle_multiple(self):
        """
        This test is for a linked list of length > 1 with a cycle back to the final node.
        A cycle exists. The algorithm should return the node where the cycle began.
        """
        end_cycle_multiple_root, end_cycle_multiple_solution = ListNode.generateList(3, 3)
        self.assertEqual(tortoise_and_hare(end_cycle_multiple_root), end_cycle_multiple_solution)


if __name__ == "__main__":
    main()
