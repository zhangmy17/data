from typing import Iterable, Any

class DeleteItem:
    """
    从列表中删除元素
    """
    def __init__(self, iterable: Iterable[Any]):
        """

        :param iterable: 可迭代对象，在其中删除元素
        """
        self.iterable = list(iterable)

    def delete(self, index_to_delete: int) -> list[Any]:
        """
        在列表中删除元素

        :param index_to_delete: 删除的索引
        """

        #确认删除元素在列表范围内
        length_of_iterable: int = len(self.iterable)
        if index_to_delete < 0 or index_to_delete > length_of_iterable:
            return ['error']

        #从索引处开始，将后一位元素前移
        for i in range(index_to_delete + 1, length_of_iterable):
            self.iterable[i - 1] = self.iterable[i]

        #移除末尾元素
        self.iterable.pop()

        return self.iterable
