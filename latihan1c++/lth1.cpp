#include <iostream>
#include <conio.h>
using namespace std;

class lth1
{
public:
    int a, b, c;
    void input()
    {
        cout << "masukkan nilai a: ";
        cin >> a;
        cout << "masukkan nilai b: ";
        cin >> b;
        cout << "masukkan nilai c: ";
        cin >> c;
    }
    void output()
    {
        cout << "nilai a: " << a << endl;
        cout << "nilai b: " << b << endl;
        cout << "nilai c: " << c << endl;
    }
    void lth()
    {
        if (a > b && a > c)
        {
            cout << "nilai terbesar adalah " << a << endl;
        }
        else if (b > a && b > c)
        {
            cout << "nilai terbesar adalah " << b << endl;
        }
        else if (c > a && c > b)
        {
            cout << "nilai terbesar adalah " << c << endl;
        }
        else
        {
            cout << "nilai terbesar adalah " << a << " dan " << b << " dan " << c << endl;
        }
    }
};

int main()
{
    lth1 l;
    l.input();
    l.output();
    l.lth();
    cout << "Hello World!" << endl;
    getch();
    cin.get();
    return 0;
}