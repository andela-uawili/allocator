"""
Custom exceptions used in Allocator related classes.

"""

class AttributeTypeError(TypeError):
   def __init__(self, msg):
      self.msg = msg