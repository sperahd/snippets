#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <string>
#include <cstdlib>

void get_all_primes_v0(std::vector <int> &sol, int n)
{
    std::set <int> o_s;
    for (int i = 0; i < n; i++)
    {
        o_s.insert(i);
    }
    for (int i = 2; i < n; i++)
    {
        int j = 0;
        for(j = 0; j < sol.size(); j++)
        {
            if (i % sol[j] == 0)
            {
                break;
            }
        }
        if (j == sol.size())
        {
            sol.push_back(i);
        }
    }
}

void get_all_primes_v1(std::vector <int> &sol, int n)
{
    std::set <int> o_s;
    for (int i = 0; i < n; i++)
    {
        o_s.insert(i);
    }
    for (int i = 2; i < n; i=i+2)
    {
        int j = 0;
        for(j = 0; j < sol.size(); j++)
        {
            if (i % sol[j] == 0)
            {
                break;
            }
        }
        if (j == sol.size())
        {
            sol.push_back(i);
        }
    }
}

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        std::cout << "USAGE: " << argv[0] << " <limit> " << std::endl;
        exit(0);
    }

    std::vector <int> sol;
    get_all_primes(sol, atoi(argv[1]));
    for(int i = 0; i < sol.size(); i++)
    {
        std::cout << "Prime " << i+1 << ": " << sol[i] << std::endl;
    }
}
