b1 >> fuzz([0, 2, 3, 5], dur=1/2, amp=0.8, lpf=linvar([100, 1000], 12), lpr=0.4, oct=3).every(16, "shuffle").every(8, "bubble")
d1 >> play("x o [xx] oxx o [xx] {oO} ", room=0.4).every(16, "shuffle")
d2 >> play("[--]", amp=[1.3, 0.5, 0.5, 0.5], hpf=linvar([6000, 10000], 8), hpr=0.4, spin=4)
p1 >> pasha([0, 2, 3, 5], dur=4, oct=4, amp=0.65, pan=[-0.5, 0.5], striate=16).every(9, "bubble")
m1 >> karp([0, 2, 3, 7, 9], dur=[1/2, 1, 1/2, 1, 1, 1/2]).every(12, "shuffle").every(7, "bubble")
p1.every(4, "stutter", 4)
b1.every(8, "rotate") 