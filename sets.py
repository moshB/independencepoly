import math

seti = {
    # DONE! with  2 vertics
    2: {1: {1: 1}},
    # dict_keys([1])
    # DONE! with  3 vertics
    # 3 ver: {alfa:{maxindex:num graphs}}
    3: {2: {1: 1}},
    # dict_keys([2])
    # DONE! with  4 vertics
    4: {3: {1: 1}, 2: {1: 1}},
    # dict_keys([3, 2])
    # DONE! with  5 vertics
    5: {4: {2: 1}, 3: {2: 2}},
    # dict_keys([4, 3])
    # DONE! with  6 vertics
    6: {5: {3: 1}, 4: {2: 3}, 3: {2: 2}},
    # dict_keys([5, 4, 3])
    # DONE! with  7 vertics
    7: {6: {3: 1}, 5: {3: 1, 2: 3}, 4: {2: 6}},
    # dict_keys([6, 5, 4])
    # DONE! with  8 vertics
    8: {7: {4: 1}, 6: {3: 5}, 5: {3: 12}, 4: {3: 4, 2: 1}},
    # dict_keys([7, 6, 5, 4])
    # DONE! with  9 vertics
    9: {8: {4: 1}, 7: {4: 2, 3: 4}, 6: {3: 20}, 5: {3: 20}},
    # dict_keys([8, 7, 6, 5])
    # DONE! with  10 vertics
    10: {9: {5: 1}, 8: {4: 7}, 7: {4: 13, 3: 18}, 6: {4: 1, 3: 51}, 5: {3: 15}},
    # dict_keys([9, 8, 7, 6, 5])
    # DONE! with  11 vertics
    11: {10: {5: 1}, 9: {5: 3, 4: 5}, 8: {4: 43}, 7: {4: 88, 3: 19}, 6: {4: 18, 3: 58}},
    # dict_keys([10, 9, 8, 7, 6])
    # DONE! with  12 vertics
    # 12: {11: {6: 1}, 10: {5: 9}, 9: {5: 24, 4: 34}, 8: {5: 1, 4: 191}, 7: {4: 242}, 6: {4: 49}},
    12: {11: {6: 1}, 10: {5: 9}, 9: {5: 24, 4: 34}, 8: {5: 1, 4: 191}, 7: {4: 242}, 6: {4: 49}},
    # dict_keys([11, 10, 9, 8, 7, 6])
    # DONE! with  13 vertics
    13: {12: {6: 1}, 11: {6: 3, 5: 7}, 10: {5: 75}, 9: {5: 158, 4: 155}, 8: {5: 10, 4: 579}, 7: {4: 313}},
    # dict_keys([12, 11, 10, 9, 8, 7])
    # DONE! with  14 vertics
    14: {13: {7: 1}, 12: {6: 11}, 11: {6: 32, 5: 62}, 10: {6: 1, 5: 475}, 9: {5: 983, 4: 240}, 8: {5: 195, 4: 979},
         7: {5: 3, 4: 177}},
    # dict_keys([13, 12, 11, 10, 9, 8, 7])
    # DONE! with  15 vertics
    15: {14: {7: 1}, 13: {7: 3, 6: 9}, 12: {6: 115}, 11: {6: 286, 5: 402}, 10: {6: 22, 5: 2237}, 9: {5: 3304, 4: 1},
         8: {5: 1301, 4: 60}},
    # dict_keys([14, 13, 12, 11, 10, 9, 8])
    # DONE! with  16 vertics
    16: {15: {8: 1}, 14: {7: 13}, 13: {7: 40, 6: 99}, 12: {7: 1, 6: 954}, 11: {6: 2155, 5: 1696}, 10: {6: 287, 5: 7487},
         9: {6: 1, 5: 5885}, 8: {5: 701}},
    # dict_keys([15, 14, 13, 12, 11, 10, 9, 8])
    # DONE! with  17 vertics
    17: {16: {8: 1}, 15: {8: 3, 7: 11}, 14: {7: 164}, 13: {7: 502, 6: 782}, 12: {7: 23, 6: 6134},
         11: {6: 13135, 5: 2955}, 10: {6: 3386, 5: 15372}, 9: {6: 37, 5: 6124}},
    # dict_keys([16, 15, 14, 13, 12, 11, 10, 9])
    # DONE! with  18 vertics
    18: {17: {9: 1}, 16: {8: 15}, 15: {8: 46, 7: 146}, 14: {8: 1, 7: 1679}, 13: {7: 4303, 6: 5073},
         12: {7: 493, 6: 29849}, 11: {7: 1, 6: 48950, 5: 340}, 10: {6: 23626, 5: 6453}, 9: {6: 941, 5: 1950}},
    # dict_keys([17, 16, 15, 14, 13, 12, 11, 10, 9])
    # DONE! with  19 vertics
    19: {18: {9: 1}, 17: {9: 3, 8: 13}, 16: {8: 222}, 15: {8: 815, 7: 1336}, 14: {8: 27, 7: 13682},
         13: {7: 32598, 6: 20639}, 12: {7: 6397, 6: 106460}, 11: {7: 46, 6: 106994}, 10: {6: 28722}},
    # dict_keys([18, 17, 16, 15, 14, 13, 12, 11, 10])
    # DONE! with  20 vertics
    20: {19: {10: 1}, 18: {9: 17}, 17: {9: 52, 8: 202}, 16: {9: 1, 8: 2701}, 15: {8: 8051, 7: 11350},
         14: {8: 645, 7: 87563}, 13: {8: 1, 7: 194124, 6: 39219}, 12: {7: 65121, 6: 245537}, 11: {7: 1137, 6: 154972},
         10: {7: 3, 6: 12368}},
    # dict_keys([19, 18, 17, 16, 15, 14, 13, 12, 11, 10])
    21: {20: {10: 1}, 19: {10: 3, 9: 15}, 18: {9: 288}, 17: {9: 1139, 8: 2202}, 16: {9: 38, 8: 26657},
         15: {8: 70491, 7: 69011}, 14: {8: 12333, 7: 433178}, 13: {8: 80, 7: 766780, 6: 12599},
         12: {7: 419420, 6: 193388}, 11: {7: 23731, 6: 113151}},
    22: {21: {11: 1}, 20: {10: 19}, 19: {10: 58, 9: 267}, 18: {10: 1, 9: 4071}, 17: {9: 13553, 8: 22330},
         16: {9: 892, 8: 211364}, 15: {9: 1, 8: 525516, 7: 272741}, 14: {8: 145485, 7: 1607552},
         13: {8: 1928, 7: 1944368, 6: 1}, 12: {8: 3, 7: 816630, 6: 2411}, 11: {7: 52229, 6: 2335}},

    23: {22: {11: 1}, 21: {11: 3, 10: 17}, 20: {10: 363}, 19: {10: 1490, 9: 3414}, 18: {10: 48, 9: 47202},
         17: {9: 137552, 8: 175023}, 16: {9: 20129, 8: 1337355, 7: 81}, 15: {9: 101, 8: 3065025, 7: 553670},
         14: {8: 1302063, 7: 4006336}, 13: {8: 37993, 7: 3476318}, 12: {8: 82, 7: 663808}},

    24: {23: {12: 1}, 22: {11: 21}, 21: {11: 64, 10: 340}, 20: {11: 1, 10: 5840}, 19: {10: 21446, 9: 39687},
         18: {10: 1248, 9: 446392, 8: 1}, 17: {10: 1, 9: 1216912, 8: 993695}, 16: {9: 297138, 8: 6675048},
         15: {9: 3076, 8: 12600825, 7: 297513}, 14: {9: 3, 8: 7758679, 7: 4361350}, 13: {8: 589482, 7: 3744815},
         12: {8: 2276, 7: 244043}},
    25: {24: {12: 1}, 23: {12: 3, 11: 19}, 22: {11: 447}, 21: {11: 1885, 10: 5007}, 20: {11: 62, 10: 77799},
         19: {10: 243556, 9: 382234}, 18: {10: 32403, 9: 3435831, 8: 1007}, 17: {10: 127, 9: 8842793, 8: 3847625},
         16: {9: 3198852, 8: 25431592}, 15: {9: 75847, 8: 35618162, 7: 4262}, 14: {9: 118, 8: 19722044, 7: 449466},
         13: {8: 2565311, 7: 700437}}

}
eq_set = {2: {1: {1: 0.3333333333333333}},
          3: {2: {1: 0.5}},
          4: {3: {1: 1.0}, 2: {1: 0.5}},
          5: {4: {2: 1.5}, 3: {2: 1.6666666666666667}},
          6: {5: {3: 3.0}, 4: {2: 1.5}, 3: {2: 1.6666666666666667}},
          7: {6: {3: 2.5}, 5: {3: 3.0, 2: 2.0}, 4: {2: 1.5}},
          8: {6: {3: 2.5}, 5: {3: 3.0}, 4: {3: 2.3333333333333335, 2: 1.5}},
          9: {8: {4: 3.5}, 7: {3: 3.0}, 6: {3: 2.5}, 5: {3: 3.0}},
          10: {8: {4: 3.5}, 7: {4: 3.5, 3: 3.0}, 6: {4: 3.6666666666666665, 3: 2.5}, 5: {3: 3.0}},
          11: {10: {5: 4.5}, 9: {4: 4.0}, 8: {4: 3.5}, 7: {4: 3.4545454545454546, 3: 3.0},
               6: {4: 3.6666666666666665, 3: 2.5}},
          12: {10: {5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5}, 7: {4: 3.5}, 6: {4: 3.6666666666666665}},
          13: {12: {6: 5.5}, 11: {6: 5.461538461538462, 5: 5.0}, 10: {5: 4.5}, 9: {5: 4.538461538461538, 4: 4.0},
               8: {5: 5.0, 4: 3.5}, 7: {4: 3.4615384615384617}},
          14: {12: {6: 5.5}, 11: {6: 5.5, 5: 5.0}, 10: {6: 6.0, 5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5},
               7: {5: 4.333333333333333, 4: 3.4285714285714284}},
          15: {14: {7: 6.5}, 13: {7: 6.6, 6: 6.0}, 12: {6: 5.5}, 11: {6: 5.466666666666667, 5: 5.0},
               10: {6: 5.066666666666666, 5: 4.5}, 9: {5: 4.355555555555556, 4: 4.0}, 8: {5: 5.0, 4: 3.5}},
          16: {14: {7: 6.5}, 13: {7: 6.5625, 6: 6.0}, 12: {7: 6.625, 6: 5.5}, 11: {6: 5.5, 5: 5.0},
               10: {6: 5.5, 5: 4.5}, 9: {6: 5.666666666666667, 5: 5.0}, 8: {5: 5.0}},
          17: {16: {8: 7.5}, 15: {8: 7.9411764705882355, 7: 7.0}, 14: {7: 6.5}, 13: {7: 6.529411764705882, 6: 6.0},
               12: {7: 6.529411764705882, 6: 5.5}, 11: {6: 5.0588235294117645, 5: 5.0},
               10: {6: 5.470588235294118, 5: 4.5}, 9: {6: 5.666666666666667, 5: 4.647058823529412}},
          18: {16: {8: 7.5}, 15: {8: 7.055555555555555, 7: 7.0}, 14: {8: 7.055555555555555, 7: 6.5},
               13: {7: 6.5, 6: 6.0}, 12: {7: 6.555555555555555, 6: 5.5}, 11: {7: 7.0, 6: 5.5, 5: 5.0},
               10: {6: 6.0, 5: 4.5}, 9: {6: 5.666666666666667}},
          19: {18: {9: 8.5}, 17: {8: 8.0}, 16: {8: 7.5}, 15: {8: 7.473684210526316, 7: 7.0},
               14: {8: 7.649122807017543, 7: 6.5}, 13: {7: 6.526315789473684, 6: 6.0},
               12: {7: 6.526315789473684, 6: 5.5}, 11: {7: 7.0, 6: 5.473684210526316}, 10: {6: 6.0}},
          20: {18: {9: 8.5}, 17: {9: 8.55, 8: 8.0}, 16: {9: 8.55, 8: 7.5}, 15: {8: 7.5, 7: 7.0},
               14: {8: 7.5, 7: 6.5}, 13: {8: 7.5, 7: 6.5, 6: 6.0}, 12: {7: 6.5, 6: 5.5},
               11: {7: 7.0, 6: 5.5}, 10: {7: 6.333333333333333, 6: 6.0}},
          21: {20: {10: 9.5}, 19: {9: 9.0}, 18: {9: 8.5}, 17: {9: 8.523809523809524, 8: 8.0},
               16: {9: 8.523809523809524, 8: 7.5}, 15: {8: 7.571428571428571, 7: 7.0},
               14: {8: 7.0476190476190474, 7: 6.5}, 13: {8: 7.428571428571429, 7: 6.523809523809524, 6: 6.0},
               12: {7: 6.476190476190476, 6: 5.5}, 11: {7: 7.0, 6: 5.476190476190476}},
          22: {20: {10: 9.5}, 19: {10: 9.727272727272727, 9: 9.0}, 18: {10: 9.181818181818182, 9: 8.5},
               17: {9: 8.5, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {9: 8.181818181818182, 8: 8.0, 7: 7.0},
               14: {8: 7.5, 7: 6.5}, 13: {8: 7.454545454545454, 7: 6.454545454545454, 6: 6.0},
               12: {8: 7.666666666666667, 7: 6.666666666666666, 6: 5.5}, 11: {7: 7.0, 6: 5.818181818181818}},
          23: {22: {11: 10.5}, 21: {10: 10.0}, 20: {10: 9.5}, 19: {10: 10.0, 9: 9.0},
               18: {10: 9.043478260869565, 9: 8.5}, 17: {9: 8.521739130434783, 8: 8.0},
               16: {9: 8.521739130434783, 8: 7.5}, 15: {9: 8.08695652173913, 8: 7.043478260869565, 7: 7.0},
               14: {8: 7.478260869565218, 7: 6.5}, 13: {8: 7.478260869565218, 7: 6.521739130434782},
               12: {8: 7.666666666666667, 7: 6.695652173913044}},
          24: {22: {11: 10.5}, 21: {11: 10.5, 10: 10.0}, 20: {11: 10.375, 10: 9.5}, 19: {10: 9.5, 9: 9.0},
               18: {10: 9.5, 9: 8.5, 8: 8.0}, 17: {10: 10.0, 9: 8.5, 8: 8.0}, 16: {9: 8.5, 8: 7.5},
               15: {9: 9.0, 8: 8.0, 7: 7.0}, 14: {9: 9.0, 8: 7.5, 7: 6.5}, 13: {8: 7.5, 7: 6.5},
               12: {8: 7.666666666666667, 7: 6.5}},
          25: {24: {12: 11.5}, 23: {11: 11.0}, 22: {11: 10.5}, 21: {11: 10.52, 10: 10.0}, 20: {11: 10.52, 10: 9.5},
               19: {10: 9.56, 9: 9.0}, 18: {10: 9.56, 9: 8.5, 8: 8.0}, 17: {10: 9.52, 9: 8.52, 8: 8.0},
               16: {9: 8.52, 8: 7.5}, 15: {9: 8.56, 8: 8.0, 7: 7.0}, 14: {9: 9.0, 8: 7.48, 7: 6.5},
               13: {8: 7.44, 7: 6.48}}}


new = {2: {1: {1: 0.3333333333333333}}, 3: {2: {1: 0.5}}, 4: {3: {1: 1.0}, 2: {1: 0.5}}, 5: {4: {2: 1.5}, 3: {2: 1.6666666666666667}}, 6: {5: {3: 3.0}, 4: {2: 1.5}, 3: {2: 1.6666666666666667}}, 7: {6: {3: 2.5}, 5: {3: 3.0, 2: 2.0}, 4: {2: 1.5}}, 8: {7: {4: 4.0}, 6: {3: 2.5}, 5: {3: 3.0}, 4: {3: 2.3333333333333335, 2: 1.5}}, 9: {8: {4: 3.5}, 7: {4: 4.0, 3: 3.0}, 6: {3: 2.5}, 5: {3: 3.0}}, 10: {9: {5: 5.0}, 8: {4: 3.5}, 7: {4: 4.0, 3: 3.0}, 6: {4: 3.6666666666666665, 3: 2.5}, 5: {3: 3.0}}, 11: {10: {5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {4: 3.5}, 7: {4: 4.0, 3: 3.0}, 6: {4: 3.6666666666666665, 3: 2.5}}, 12: {11: {6: 6.0}, 10: {5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5}, 7: {4: 4.0}, 6: {4: 3.6666666666666665}}, 13: {12: {6: 5.5}, 11: {6: 6.0, 5: 5.0}, 10: {5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5}, 7: {4: 4.0}}, 14: {13: {7: 7.0}, 12: {6: 5.5}, 11: {6: 6.0, 5: 5.0}, 10: {6: 5.5, 5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5}, 7: {5: 4.333333333333333, 4: 4.0}}, 15: {14: {7: 6.5}, 13: {7: 7.0, 6: 6.0}, 12: {6: 5.5}, 11: {6: 6.0, 5: 5.0}, 10: {6: 5.5, 5: 4.5}, 9: {5: 5.0, 4: 4.0}, 8: {5: 5.0, 4: 3.5}}, 16: {15: {8: 8.0}, 14: {7: 6.5}, 13: {7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {6: 6.0, 5: 5.0}, 10: {6: 5.5, 5: 4.5}, 9: {6: 5.666666666666667, 5: 5.0}, 8: {5: 5.0}}, 17: {16: {8: 7.5}, 15: {8: 8.0, 7: 7.0}, 14: {7: 6.5}, 13: {7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {6: 6.0, 5: 5.0}, 10: {6: 5.5, 5: 4.5}, 9: {6: 5.666666666666667, 5: 5.0}}, 18: {17: {9: 9.0}, 16: {8: 7.5}, 15: {8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {7: 7.0, 6: 6.0, 5: 5.0}, 10: {6: 5.5, 5: 4.5}, 9: {6: 5.666666666666667, 5: 5.0}}, 19: {18: {9: 8.5}, 17: {9: 9.0, 8: 8.0}, 16: {8: 7.5}, 15: {8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {7: 7.0, 6: 6.0}, 10: {6: 5.5}}, 20: {19: {10: 10.0}, 18: {9: 8.5}, 17: {9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {8: 8.0, 7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {7: 7.0, 6: 6.0}, 10: {7: 6.333333333333333, 6: 5.5}}, 21: {20: {10: 9.5}, 19: {10: 10.0, 9: 9.0}, 18: {9: 8.5}, 17: {9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {8: 7.0476190476190474, 7: 7.0, 6: 6.0}, 12: {7: 6.5, 6: 5.5}, 11: {7: 7.0, 6: 6.0}}, 22: {21: {11: 11.0}, 20: {10: 9.5}, 19: {10: 10.0, 9: 9.0}, 18: {10: 9.5, 9: 8.5}, 17: {9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {9: 9.0, 8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {8: 8.0, 7: 7.0, 6: 6.0}, 12: {8: 7.666666666666667, 7: 6.5, 6: 5.5}, 11: {7: 7.0, 6: 6.0}}, 23: {22: {11: 10.5}, 21: {11: 11.0, 10: 10.0}, 20: {10: 9.5}, 19: {10: 10.0, 9: 9.0}, 18: {10: 9.5, 9: 8.5}, 17: {9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {9: 8.08695652173913, 8: 8.0, 7: 7.0}, 14: {8: 7.5, 7: 6.5}, 13: {8: 7.043478260869565, 7: 7.0}, 12: {8: 7.666666666666667, 7: 6.5}}, 24: {23: {12: 12.0}, 22: {11: 10.5}, 21: {11: 11.0, 10: 10.0}, 20: {11: 10.5, 10: 9.5}, 19: {10: 10.0, 9: 9.0}, 18: {10: 9.5, 9: 8.5, 8: 8.0}, 17: {10: 10.0, 9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {9: 9.0, 8: 8.0, 7: 7.0}, 14: {9: 9.0, 8: 7.5, 7: 6.5}, 13: {8: 8.0, 7: 7.0}, 12: {8: 7.666666666666667, 7: 6.5}}, 25: {24: {12: 11.5}, 23: {12: 12.0, 11: 11.0}, 22: {11: 10.5}, 21: {11: 11.0, 10: 10.0}, 20: {11: 10.5, 10: 9.5}, 19: {10: 10.0, 9: 9.0}, 18: {10: 9.5, 9: 8.5, 8: 8.0}, 17: {10: 9.04, 9: 9.0, 8: 8.0}, 16: {9: 8.5, 8: 7.5}, 15: {9: 8.96, 8: 8.0, 7: 7.0}, 14: {9: 9.0, 8: 7.5, 7: 6.5}, 13: {8: 8.0, 7: 7.0}}}

No_Match_Cases = [(8, 7, 4), (10, 9, 5), (12, 11, 6), (14, 13, 7), (16, 15, 8), (18, 17, 9), (20, 19, 10), (22, 21, 11),
                  (24, 23, 12)]


# def eqaplusb():
#
#     for i in range(2,21):

def eq1(alpha):
    return (alpha - 1) / 2
def eq3(alpha):
    return (alpha + 1) / 2


def eq2(alpha):
    return (2 * alpha - 1) / 3


# def check_mod_values(data):
#     new_dict = {}
#
#     for n, alpha_dict in data.items():
#         for alpha, mod_dict in alpha_dict.items():
#             for mod, count in mod_dict.items():
#                 if mod == eq1(alpha) or mod == eq2(alpha):
#                     if n not in new_dict:
#                         new_dict[n] = {}
#                     if alpha not in new_dict[n]:
#                         new_dict[n][alpha] = {}
#                     new_dict[n][alpha][mod] = count
#
#     return new_dict
# def check_mod_values(data):
#     new_dict = {}
#
#     for n, alpha_dict in data.items():
#         print(n)
#         for alpha, mod_dict in alpha_dict.items():
#             for mod, count in mod_dict.items():
#                 if mod == math.ceil(eq1(alpha)):
#                     new_dict[n][alpha][mod] = {eq1(alpha)}
#                 elif  mod == math.ceil(eq2(alpha)):
#                     new_dict[n][alpha][mod]  = {eq1(alpha)}
#                 else:
#                     #todo find in new_dict 2 futhers that g1+g2 = g and alph1+alpha2=alpha
#                     if n not in new_dict:
#                         new_dict[n] = {}
#                     if alpha not in new_dict[n]:
#                         new_dict[n][alpha] = {}
#                     new_dict[n][alpha][mod] = count
#
#     return new_dict
# def check_mod_values(data):
#     new_dict = {}
#
#     for n, alpha_dict in data.items():
#         # print(n)
#         if n not in new_dict:
#             new_dict[n] = {}
#         for alpha, mod_dict in alpha_dict.items():
#             for mod, count in mod_dict.items():
#                 if mod == math.ceil(eq1(alpha)):
#                     if alpha not in new_dict[n]:
#                         new_dict[n][alpha] = {}
#                     new_dict[n][alpha][mod] = eq1(alpha)
#                 elif mod == math.ceil(eq2(alpha)):
#                     if alpha not in new_dict[n]:
#                         new_dict[n][alpha] = {}
#                     new_dict[n][alpha][mod] = eq2(alpha)
#                 else:
#                     # חיפוש במילון החדש עבור שני ערכים שמספקים את התנאים
#                     for i in range(2,n//2+1):
#                         g1 = i
#                         g2 = n-i
#                         for alpha1, mods1 in new_dict[g1].items():
#                             alpha2 = alpha-alpha1
#                             if alpha2 in new_dict[g2]:
#                                 for mod1 in mods1:
#                                     for mod2 in new_dict[g2][alpha2].items:
#                                         if mod == math.ceil(2 * (mod1*g1+mod2*g2)/n):
#                                             if alpha not in new_dict[n]:
#                                                 new_dict[n][alpha]={}
#                                             new_dict[n][alpha][mod]=2 * (mod1*g1+mod2*g2)/n
#                                             print(2 * (mod1*g1+mod2*g2)/n)
#
#     return new_dict
import math

import math


def check_mod_values(data):
    new_dict = {}

    for n, alpha_dict in data.items():
        if n not in new_dict:
            new_dict[n] = {}
        for alpha, mod_dict in alpha_dict.items():
            match_found = False  # דגל לבדיקה אם נמצאה התאמה
            for mod, count in mod_dict.items():
                if mod == math.ceil(eq1(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq1(alpha)
                    match_found = True
                elif mod == math.ceil(eq2(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq2(alpha)
                    match_found = True
                elif mod == math.ceil(eq3(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq3(alpha)
                    match_found = True

                else:
                    for i in range(2, n // 2 + 1):
                        g1 = i
                        g2 = n - i
                        if g1 in new_dict and g2 in new_dict:
                            for alpha1, mods1 in new_dict[g1].items():
                                alpha2 = alpha - alpha1
                                if alpha2 in new_dict[g2]:
                                    for mod1 in mods1:
                                        for mod2, value in new_dict[g2][alpha2].items():
                                            if mod == math.ceil(2 * (mod1 * g1 + value * g2) / n):
                                                if alpha not in new_dict[n]:
                                                    new_dict[n][alpha] = {}
                                                new_dict[n][alpha][mod] = 2 * (mod1 * g1 + value * g2) / n
                                                match_found = True
                                                break  # יציאה מהלולאה אם נמצאה התאמה

            if not match_found:
                print(f'לא נמצאה התאמה עבור n={n}, alpha={alpha}, mod={mod}')
    return new_dict


def main():
    d = {}
    # d.keys()
    for i in range(1, 20):
        d[i] = []
    # print(d)
    for v in seti.values():
        for i in range(1, 20):
            if i in v:
                # print(list(v[i].keys()))
                d[i] += list(v[i].keys())
                if i == 3:
                    print(list(v[i]))
    # print(d)
    for i in range(1, 20):
        d[i] = list(set(d[i]))
    # print(d)
    s = set()
    for i in range(1, 20):
        for l in d[i]:
            s.add(l / i)
            if l / i == 0.5294117647058824:
                print('l=', l)
                print('i=', i)
    # print(s)


a = {1: [1], 2: [1], 3: [1, 2], 4: [2, 3], 5: [2, 3], 6: [3, 4], 7: [3, 4, 5], 8: [4, 5], 9: [4, 5, 6], 10: [5, 6, 7],
     11: [5, 6, 7], 12: [6, 7], 13: [8, 6, 7], 14: [8, 7], 15: [8, 7], 16: [8, 9], 17: [8, 9], 18: [9], 19: [10]}
b = {0.5, 1.0, 0.6666666666666666, 0.3333333333333333, 0.75, 0.4, 0.6, 0.42857142857142855, 0.5714285714285714,
     0.7142857142857143, 0.625, 0.5384615384615384, 0.5333333333333333, 0.5625, 0.5294117647058824, 0.5555555555555556,
     0.4666666666666667, 0.5454545454545454, 0.6153846153846154, 0.47058823529411764, 0.7, 0.5263157894736842,
     0.5833333333333334, 0.45454545454545453, 0.6363636363636364, 0.4444444444444444, 0.46153846153846156}


# print('num b', len(b))
def lic():
    d = {}
    for i in range(1, 20):
        d[i] = []
        # print(d)
    for v in seti.values():
        for i in range(1, 20):
            if i in v:
                # print(list(v[i].keys()))
                d[i] += list(v[i].keys())
                # if i == 3:
                # print(list(v[i]))
        # print(d)
    for i in range(1, 20):
        d[i] = list(set(d[i]))
    for bb in b:
        for i in range(1, 20):
            for l in d[i]:
                if l / i == bb:
                    print("start:")
                    print('max=', l, 'alfa=', i)
                    print(bb)


if __name__ == '__main__':
    print(check_mod_values(seti))


def check_mod_values(data):
    new_dict = {}
    no_match_cases = []

    for n, alpha_dict in data.items():
        if n not in new_dict:
            new_dict[n] = {}
        for alpha, mod_dict in alpha_dict.items():
            match_found = False  # דגל לבדיקה אם נמצאה התאמה
            for mod, count in mod_dict.items():
                if mod == math.ceil(eq1(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq1(alpha)
                    match_found = True
                elif mod == math.ceil(eq2(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq2(alpha)
                    match_found = True
                elif mod == math.ceil(eq3(alpha)):
                    if alpha not in new_dict[n]:
                        new_dict[n][alpha] = {}
                    new_dict[n][alpha][mod] = eq3(alpha)
                    match_found = True

                else:
                    for i in range(2, n // 2 + 1):
                        g1 = i
                        g2 = n - i
                        if g1 in new_dict and g2 in new_dict:
                            for alpha1, mods1 in new_dict[g1].items():
                                alpha2 = alpha - alpha1
                                if alpha2 in new_dict[g2]:
                                    for mod1 in mods1:
                                        for mod2, value in new_dict[g2][alpha2].items():
                                            if mod == math.ceil(2 * (mod1 * g1 + value * g2) / n):
                                                if alpha not in new_dict[n]:
                                                    new_dict[n][alpha] = {}
                                                new_dict[n][alpha][mod] = 2 * (mod1 * g1 + value * g2) / n
                                                match_found = True
                                                break  # יציאה מהלולאה הפנימית אם נמצאה התאמה
                                    if match_found:
                                        break  # יציאה מהלולאה אם נמצאה התאמה
                        if match_found:
                            break  # יציאה מהלולאה החיצונית אם נמצאה התאמה

            if not match_found:
                # אם לא נמצאה התאמה, נשמור את המקרה במילון
                no_match_cases.append((n, alpha, mod))

    return new_dict, no_match_cases


new_dict, no_match_cases = check_mod_values(seti)
print("New Dictionary: ", new_dict)
print("No Match Cases: ", no_match_cases)
