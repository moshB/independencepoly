import numpy as np
from numpy.polynomial import Polynomial


def P():
    P1 = Polynomial([1, 1])
    P2 = Polynomial([1, 3, 1])
    n = 10

    for k in range(2, n, 2):
        P1 = P1 ** k
        P2 = P2 ** (k // 2)
        P1 = P1 * Polynomial([0, 1])
        P = P1 + P2

        # קבלת המקדמים של הפולינום והמרתם לשלמים
        coefficients = [int(c) for c in P.coef]

        # חישוב האיבר הגדול ביותר והמיקום שלו
        max_value = max(coefficients)  # הערך המקסימלי
        max_index = np.argmax(coefficients)  # המיקום של הערך המקסימלי
        array_length = len(coefficients)  # אורך המערך
        relative_position = max_index / array_length  # חישוב היחס

        # הדפסה של הפולינום והיחס
        print(f"P(x), n = {k} = {coefficients}")
        print(
            f"האיבר הגדול ביותר הוא {max_value} והוא ממוקם באינדקס {max_index} מתוך {array_length}, כלומר {relative_position:.2f}")

P()
# if _name_ == '_main_':
#     P()
# חייב שתבדוק את זה....
# הוא כותב לי שעבור n = 10 (קודקודים) האיבר הגדול ביותר יהיה ב0.70 שזה יותר גדול 2/3