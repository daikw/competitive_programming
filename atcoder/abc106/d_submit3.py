from itertools import accumulate as acc

def LI(): return list(map(int, input().split()))
def LI_(): return list(map(lambda x: int(x) - 1, input().split()))


if __name__ == "__main__":
    N, M, Q = LI()
    LR = [[0]*N for _ in range(N)]
    for i in range(M):
        l, r = LI_()
        LR[l][r] += 1

    # 二次元累積和
    S = [tuple(acc(reversed(s))) for s in zip(*(acc(x) for x in LR))]
    for _ in range(Q):
        p, q = LI()
        # 必ず正方形だから、
        print(S[q-1][N-p])
