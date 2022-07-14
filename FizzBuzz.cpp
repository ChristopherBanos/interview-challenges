#include <string>
#include <vector>
#include<iostream>

using namespace std;
class Solution {
    public:
        vector<string> fizzBuzz(int n) {
            vector<string> thing;
            for (int i = 1; i <= n; i+=1) {
                if (i % 5 == 0 && i % 3 == 0) {
                    thing.push_back("FizzBuzz");
                }
                else if (i % 5 == 0) {
                    thing.push_back("Buzz");
                }
                else if (i % 3 == 0) {
                    thing.push_back("Fizz");
                }
                else {
                    thing.push_back(to_string(i));
                }
            }
            return thing;
        }
};

int main(int argc, char *argv[])
{
    Solution solution;
    vector<string> answer;
    answer = solution.fizzBuzz(10);
    for (string i: answer)
        cout << i << endl;
}
