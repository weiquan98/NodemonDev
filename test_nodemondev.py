# test_nodemondev.py
"""
Tests for NodemonDev module.
"""

import unittest
from nodemondev import NodemonDev

class TestNodemonDev(unittest.TestCase):
    """Test cases for NodemonDev class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NodemonDev()
        self.assertIsInstance(instance, NodemonDev)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NodemonDev()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
