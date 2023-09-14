import Currency from './3-currency.js';

class Pricing {
    constructor(amount, currency) {
        this._amount = amount; // Utilisez des variables privées _amount et _currency
        this._currency = currency;
    }

    get amount() {
        return this._amount;
    }

    set amount(value) {
        if (typeof value === 'number') {
            this._amount = value;
        }
    }

    get currency() {
        return this._currency;
    }

    set currency(value) {
        if (currency instanceof Currency) {
            this._currency = value;
        }
    }

    displayFullPrice() {
        return `${this.amount} ${this.currency.name} (${this.currency.code})`;
    }

    static convertPrice(amount, conversionRate) {
        return (amount * conversionRate);
    }
}

export default Pricing;