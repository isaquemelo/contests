#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
	int quantityOfCases;

	cin >> quantityOfCases;

	for (int currentCase = 0; currentCase < quantityOfCases; currentCase++) {
		int itensQuantity;
		map<string, float> bucket;

		cin >> itensQuantity;

		for (int itenCounter = 0; itenCounter < itensQuantity; itenCounter++) {
			string productName;
			float productPrice;

			cin >> productName >> productPrice;
			bucket.insert(pair<string, float>(productName, productPrice));
		}

		int itensOrderedQuantity;
		cin >> itensOrderedQuantity;

		float totalPrice = .0f;

		for (int itemOrder = 0; itemOrder < itensOrderedQuantity; itemOrder++) {
			string productName;
			int quantity;

			cin >> productName >> quantity;
			totalPrice += bucket[productName] * quantity;
		}

		printf("R$ %.2f\n", totalPrice);
	}
	
    return 0;
}