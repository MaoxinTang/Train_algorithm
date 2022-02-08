# -*- coding: utf-8 -*-


class UnionFind:
    '''Represents a data structure that tracks a set of elements partitioned
       into a number of disjoint (non-overlapping) subsets.
    Landau notation: O(α(n)), where α(n) is the inverse Ackermann function.
    See:
    https://www.youtube.com/watch?v=zV3Ul2pA2Fw
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure
    https://atcoder.jp/contests/abc120/submissions/4444942
    '''

    def __init__(self, number_count: int):
        '''
        Args:
            number_count: The size of elements (greater than 2).
        '''
        self.parent_numbers = [-1 for _ in range(number_count)]

    def find_root(self, number: int) -> int:
        '''Follows the chain of parent pointers from number up the tree until
           it reaches a root element, whose parent is itself.
        Args:
            number: The trees id (0-index).
        Returns:
            The index of a root element.
        '''
        if self.parent_numbers[number] < 0:
            return number

        self.parent_numbers[number] = self.find_root(self.parent_numbers[number])
        return self.parent_numbers[number]

    def get_group_size(self, number: int) -> int:
        '''
        Args:
            number: The trees id (0-index).
        Returns:
            The size of group.
        '''
        return -self.parent_numbers[self.find_root(number)]

    def is_same_group(self, number_x: int, number_y: int) -> bool:
        '''Represents the roots of tree number_x and number_y are in the same
           group.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        '''
        return self.find_root(number_x) == self.find_root(number_y)

    def merge_if_needs(self, number_x: int, number_y: int) -> bool:
        '''Uses find_root to determine the roots of the tree number_x and
           number_y belong to. If the roots are distinct, the trees are combined
           by attaching the roots of one to the root of the other.
        Args:
            number_x: The trees x (0-index).
            number_y: The trees y (0-index).
        '''
        x = self.find_root(number_x)
        y = self.find_root(number_y)

        if x == y:
            return False

        if self.get_group_size(x) >= self.get_group_size(y):
            self.parent_numbers[x] += self.parent_numbers[y]
            self.parent_numbers[y] = x
        else:
            self.parent_numbers[y] += self.parent_numbers[x]
            self.parent_numbers[x] = y
        return True


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    degree = [0] * n
    uf = UnionFind(n)

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        # サイクルの検出
        if uf.is_same_group(ai, bi):
            print('No')
            exit()

        uf.merge_if_needs(ai, bi)
        degree[ai] += 1
        degree[bi] += 1
    
    for d in degree:
        if d >= 3:
            print('No')
            exit()

    print('Yes')


if __name__ == "__main__":
    main()



from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)

N,M = map(int, input().split())

uf = UnionFind(N)
x = [0]*N
for i in range(M):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    x[a] += 1
    x[b] += 1
    if x[a]>=3 or x[b]>=3 or uf.same(a,b):
        print("No")
        break
    uf.union(a,b)
else:
    print("Yes")
