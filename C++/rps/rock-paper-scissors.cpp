#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;


int main() {
   
const int rock = 1;
const int paper = 2;
const int scissors = 3;
int opnum;
int rannum;

srand(time(0));     
rannum = rand() % 3 + 1;


std::cout << "\n\n1. rock 2. paper 3. scissors\n\n";
std::cin >> opnum;

if (opnum == 1) {

if (rannum == 3)
{
   std::cout << "win\n";
} else if (rannum == 2)
{
   std::cout << "lose\n";
} else if (rannum == 1)
{
   std::cout << "tie\n";
}

} else if (opnum == 2) {

if (rannum == 1)
{
   std::cout << "win\n";
} else if (rannum == 3)
{
   std::cout << "lose\n";
} else if (rannum == 2)
{
   std::cout << "tie\n";
}

} else if (opnum == 3)
{
   
if (rannum == 2)
{
   std::cout << "win\n";
} else if (rannum == 1)
{
   std::cout << "lose\n";
} else if (rannum == 3)
{
   std::cout << "tie\n";
}

} else
{
    
std::cout << "invalid\n";

}


if (rannum == 2)
{
   std::cout << "opponent chose paper \n";
} else if (rannum == 1)
{
   std::cout << "opponent chose rock \n";
} else if (rannum == 3)
{
   std::cout << "opponent chose scissors\n";
}














    
}