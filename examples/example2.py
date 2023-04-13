import random
import time
from typing import Iterable


class Items:
    def get_items(self) -> Iterable[dict]:
        return [
            {
                "a": (i % 2) == 0,
                "value": random.random(),
            } for i in range(1000000)
        ]


class ItemsProcessor:
    def get_items_to_process(self, item_list: Iterable[dict]) -> Iterable:
        items_to_process = []
        for item in item_list:
            if item["a"]:
                items_to_process.append(item)
        return items_to_process

    def sum_items(self, items_to_process: Iterable) -> float:
        acum_value = 0
        for item in items_to_process:
            acum_value += item["value"]
            time.sleep(0.00001)
        return acum_value

    def process(self, items: Items) -> float:
        items_to_process = self.get_items_to_process(items.get_items())
        return self.sum_items(items_to_process)


def process_items(items: Items) -> float:
    return ItemsProcessor().process(items)


if __name__ == "__main__":
    print(process_items(Items()))
