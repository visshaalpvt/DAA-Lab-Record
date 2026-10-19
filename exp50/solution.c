#include <stdio.h>
#define N 4
#define INF 1000000000

int tsp(int d[N][N]) {
    static int dp[1 << N][N];
    for (int m = 0; m < (1 << N); m++)
        for (int i = 0; i < N; i++) dp[m][i] = INF;
    dp[1][0] = 0;
    for (int m = 1; m < (1 << N); m++)
        for (int i = 0; i < N; i++) {
            if (!(m & (1 << i)) || dp[m][i] == INF) continue;
            for (int j = 0; j < N; j++)
                if (!(m & (1 << j)) && dp[m][i] + d[i][j] < dp[m | (1 << j)][j])
                    dp[m | (1 << j)][j] = dp[m][i] + d[i][j];
        }
    int best = INF;
    for (int i = 1; i < N; i++)
        if (dp[(1 << N) - 1][i] + d[i][0] < best) best = dp[(1 << N) - 1][i] + d[i][0];
    return best;
}

int main() {
    int t1[N][N] = {{0,10,15,20},{10,0,35,25},{15,35,0,30},{20,25,30,0}};
    int t2[N][N] = {{0,10,10,10},{10,0,10,10},{10,10,0,10},{10,10,10,0}};
    int t3[N][N] = {{0,1,2,3},{1,0,4,5},{2,4,0,6},{3,5,6,0}};
    printf("Test 1 minimum path distance = %d\n", tsp(t1));
    printf("Test 2 minimum path distance = %d\n", tsp(t2));
    printf("Test 3 minimum path distance = %d\n", tsp(t3));
    return 0;
}
