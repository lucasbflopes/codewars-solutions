def close_compare(a, b, margin=0):
    return (a > b) - (a < b) if abs(a-b) > margin else 0