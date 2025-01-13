class A:
    def a(self):
        print('')


if __name__ == '__main__':
    a = A()
    print(hasattr(a, 'a'))
