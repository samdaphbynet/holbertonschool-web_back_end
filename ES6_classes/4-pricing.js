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
        this._amount = value;
    }

    get currency() {
        return this._currency;
    }

    set currency(value) {
        this._currency = value;
    }

    displayFullPrice() {
        return `${this.amount} ${this.currency.name} (${this.currency.code})`;
    }

    static convertPrice(amount, conversionRate, targetCurrency) {
        return new Pricing(amount * conversionRate, targetCurrency);
    }
}

export default Pricing;