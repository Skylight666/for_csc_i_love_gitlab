#include "pch.h"
#include <iostream>


using namespace std;

int main()
{
	setlocale(LC_ALL, "Russian");
	float a, b;
	cout << "Хуйлo ебанное, число ввел быстро:";
	cin >> a;
	if (a < 10000) {
		cout << "Хуйлo ебанное, второе число ввел быстро:";
		cin >> b;
		if (b < 10000) 
		{
			if (a > b) {
				cout << a << ">" << b;
			}
			else if (a < b) {
				cout << a << "<" << b;
			}
			else if (a == b) {
				cout << a << "=" << b;
			}
		}
		else
		{
			cout << "Сказали же, блять, меньше 10000";
			system("pause");
		}

	}
	else {
		cout << "Ну ты тупой пздц";
		system("pause");
	}
}
