def collinearity(x1, y1, x2, y2):
    cross_product = x1 * y2 - y1 * x2
    return cross_product == 0