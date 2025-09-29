"""definition d'une fonction qui teste si un nombre est premier"""
from math import sqrt
def isprime(p):
    """fonction qui teste si un nombre est premier"""
    if p<2:
        return False
    for i in range(2,int(sqrt(p)+1)):
        if p%i==0 and p!=i:
            return False
        return True
def main():
    """fonction qui renvoie les nombres premiers inférieurs à 100"""
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
