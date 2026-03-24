# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    
    def test_aged_brie_increases_quality(self):
        items = [Item("Aged Brie", 10, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(11, items[0].quality)

    def test_sulfuras_never_changes(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(80, items[0].quality)

    def test_backstage_pass_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_twice_after_sell_date(self):
        items = [Item("Aged Brie", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(12, items[0].quality)

    def test_normal_item_degrades_twice_after_sell_date(self):
        items = [Item("Normal Item", 0, 10)]
        GildedRose(items).update_quality()
        self.assertEqual(8, items[0].quality)

    def test_quality_never_exceeds_50(self):
        items = [Item("Aged Brie", 10, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(50, items[0].quality)

if __name__ == '__main__':
    unittest.main()
