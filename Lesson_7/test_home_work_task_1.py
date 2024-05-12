
from Home_work_task_1 import sort_asc
from Home_work_task_1 import sort_desc
from Home_work_task_1 import sort_words

random_numbers = (5, 337, 14, 12, 48, 116, 777, 562, 38)
random_words = ('banana', 'boy', 'apple', 'home', 'work')


def test_sort_ask():
    assert sort_asc(random_numbers) == [5, 12, 14, 38, 48, 116, 337, 562, 777]


def test_sort_desc():
    assert sort_desc(random_numbers) == [777, 562, 337, 116, 48, 38, 14, 12, 5]


def test_sort_words():
    assert sort_words(random_words) == ['boy', 'home', 'work', 'apple', 'banana']
