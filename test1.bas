10 LET X = 1
20 LET Y = 9
30 LET Z = 0
35 LET Z = Z + 1
40 PRINT Z
50 IF Z < Y GOTO 35
51 LET I = 100000
53 PRINT I
55 LET Y = 0
60 LET Z = Z - 1
70 PRINT Z
80 IF Z > Y GOTO 60
90 GOTO 110
100 PRINT Z
105 PRINT Z
110 LET A = 500
115 PRINT A
120 LET B = A / 2
122 PRINT B
125 LET B = B * 3
127 PRINT B
130 LET C = 25
160 PRINT C
999 STOP