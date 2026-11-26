"""Directly enumerate binary king boards and compare with the claimed GF."""
def boards(n):
    cells = [(r, c) for r in range(n) for c in range(2)]
    masks = [sum(1 << j for j, (s, d) in enumerate(cells)
                 if 0 < max(abs(r-s), abs(c-d)) <= 1)
             for r, c in cells]
    return sum(all(not (b >> j & 1) or (b & mask).bit_count() in (1, 2)
                   for j, mask in enumerate(masks))
               for b in range(1 << (2*n)))


def coefficients(max_height):
    num = (0, 2, 5, -2, -8)
    den = (1, -3, 1, -6, 8)
    a = []
    for n in range(max_height + 1):
        p = num[n] if n < len(num) else 0
        a.append(p - sum(den[k]*a[n-k] for k in range(1, min(n+1, len(den)))))
    return a


if __name__ == "__main__":
    expected = coefficients(8)
    observed = [boards(n) for n in range(1, 9)]
    if observed != expected[1:]:
        raise SystemExit(f"mismatch: {observed} != {expected[1:]}")
    print("n=1..8:", *observed)
    print("PASS: exhaustive cell-level count equals the GF coefficients")
