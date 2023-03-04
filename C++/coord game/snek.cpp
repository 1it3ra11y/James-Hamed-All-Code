#include <iostream>
#include <vector>
int main() {
    int ded = 0;
    int x = 0;
    int y = 0;
    int w = 0;
    while (ded != 1)
    {
        std::cout <<"x:"<< x <<"y:"<< y <<"\n\n";
        std::cout << "1.left 2.right 3.up or 4.down:";
        std::cin >> w;
        if ( w == 1)
        {
            x--;
        } else if ( w == 2)
        {
            x++;
        } else if ( w == 3)
        {
            y++;
        } else if ( w == 4)
        {
            y--;
        }

        if (x == 10 || x == -10 || y == 10 || y == -10) {
            ded = 1;
            std::cout << "you died\n";
        }





    }

}
