#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int a, b, d;
	ifstream cin("linear-trip.in");
	cin»a»b»d;
	cin.close();
	ofstream cout("linear-trip.out");
	if (b >= a + d)
		cout«(a + d)«endl;
	else
	{
		if (a > b && a - d >= b)
			cout«(a - d)«endl;
		else
			cout«b«endl;
	}
	cout.close();
	return 0;
}