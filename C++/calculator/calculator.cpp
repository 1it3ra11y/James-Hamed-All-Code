#include <iostream>

int main() {
 double num;
 double num2;
 double opnum;
 std::cout << "Give number pls: ";
 std::cin >> num;
 std::cout << "the num you chose was: " << num << " \n";
 std::cout << "give second num: ";
 std::cin >> num2;
 std::cout << "the second num you chose was: " << num2 << " \n";
 std::cout << "choose witch operation you're doing\n\n";
 std::cout << "1.multiply  2.add  3.subtract  4.divide (write num of operation to use)\n\n";
 std::cin >> opnum;
 if (opnum == 1) {
     std::cout << "your answer: " << num * num2 << "\n";
 } else if (opnum == 2) {
     std::cout << "your answer: " << num + num2 << "\n";
 } else if (opnum == 3) {
     std::cout << "your answer: " << num - num2 << "\n";
 } else if (opnum == 4) {
     std::cout << "your answer: " << num / num2 << "\n";
 } else {
     std::cout << "i can't understand sorry, retry\n";
 }










}
