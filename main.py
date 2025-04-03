#include <iostream>
#include <vector>
using namespace std;

class UF {
private:
    vector<int> p;

public:
    UF(int n) : p(n + 1, -1) {}

    int find(int x) {
        if (p[x] < 0)
            return x;

        return p[x] = find(p[x]);
    }

    bool uni(int u, int v) {
        u = find(u);
        v = find(v);

        if (u == v) return false;
        if (p[v] < p[u]) swap(u, v);
        if (p[u] == p[v]) p[u]--;
        p[v] = u;

        return true;
    }
};
