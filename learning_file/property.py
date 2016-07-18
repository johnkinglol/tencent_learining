#!/usr/bin/env python
# coding=utf-8


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError('score must be an Integer')
        if score > 100 or score < 0:
            raise ValueError('the value is between 0 and 100')
        self._score = score


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution
if __name__ == '__main__':
    s = Screen()
    s.width = 1024
    s.height = 768
    print(s.resolution)
    assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution