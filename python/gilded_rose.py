# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class GeneralItemProcessor:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.item.sell_in -= 1
        self.adjust_quality()
        if self.item.sell_in < 0:
            self.adjust_quality()

    def adjust_quality(self):
        self.decrease_quality()

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1

class AgedBrieProcessor(GeneralItemProcessor):
    def adjust_quality(self):
        self.increase_quality()

class SulfurasProcessor(GeneralItemProcessor):
    def update(self):
        pass

class BackstagePassProcessor(GeneralItemProcessor):
    def update(self):
        self.item.sell_in -= 1
        self.increase_quality()
        if self.item.sell_in < 10:
            self.increase_quality()
        if self.item.sell_in < 5:
            self.increase_quality()
        if self.item.sell_in < 0:
            self.item.quality = 0


class GildedRose(object):
    def __init__(self, items):
        self.items = items
       
        self.processor_map = {
            "Aged Brie": AgedBrieProcessor,
            "Sulfuras, Hand of Ragnaros": SulfurasProcessor,
            "Backstage passes to a TAFKAL80ETC concert": BackstagePassProcessor
        }

    def update_quality(self):
        for item in self.items:
            processor_cls = self.processor_map.get(item.name, GeneralItemProcessor)
            processor = processor_cls(item)
            processor.update()
