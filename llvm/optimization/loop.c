void fun(int y, int z, int n, int* a) {
    int x;
    int i = 0;
    while (i < n) {
        // Loop invariant
        x = y + z;
        a[i] = 6 * i + x * x; // strength reduction possible
        ++i;
    }
}
