export class Room {
    private _number : number;
    private _numberOfBeds : number;
    private _hasBalcony : boolean;
    private _hasSeaView : boolean;
    private _price : number;

    //Constructor
    constructor(number: number, numberOfBeds: number, hasBalcony: boolean, hasSeaView: boolean, price: number) {
        this._number = number;
        this._numberOfBeds = numberOfBeds;
        this._hasBalcony = hasBalcony;
        this._hasSeaView = hasSeaView;
        this._price = price;
    }

    //Getters and Setters
    get number(): number {
        return this._number;
    }

    set number(value: number) {
        this._number = value;
    }

    get numberOfBeds(): number {
        return this._numberOfBeds;
    }

    set numberOfBeds(value: number) {
        this._numberOfBeds = value;
    }

    get hasBalcony(): boolean {
        return this._hasBalcony;
    }

    set hasBalcony(value: boolean) {
        this._hasBalcony = value;
    }

    get hasSeaView(): boolean {
        return this._hasSeaView;
    }

    set hasSeaView(value: boolean) {
        this._hasSeaView = value;
    }

    get price(): number {
        return this._price;
    }

    set price(value: number) {
        this._price = value;
    }
}