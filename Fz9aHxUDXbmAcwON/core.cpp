#include <bits/stdc++.h>
using namespace std;

long long n, m, d, ans;

int main()
{
    int T;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%lld%lld", &d, &m);
        if (d <= 3)
        {
            printf("%lld\n", (d * 2 - 1 + m) % m);
            continue;
        }
        else
        {
            long long x = 2, i;
            for (i = 4; i <= d; i <<= 1)
            {
                x = x * (i / 2 + 1) % m;
            }
            ans = (x * 2 % m - 1 + m) % m;
            i >>= 1;
            printf("%lld\n", (ans + (d - i) * x % m) % m);
        }
    }
    return 0;
}
