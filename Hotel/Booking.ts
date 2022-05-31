import {Room} from "./Room";
import {Guest} from "./Guest";

export class Booking {
    private _room : Room;
    private _people : Array<Guest>;
    private _StartDate : Date;
    private _EndDate : Date;
    
    //Constructor
    constructor(room: Room, people: Array<Guest>, StartDate: Date, EndDate: Date) {
        this._room = room;
        this._people = people;
        this._StartDate = StartDate;
        this._EndDate = EndDate;
    }

    //Getters and setters
    get room(): Room {
        return this._room;
    }

    set room(value: Room) {
        this._room = value;
    }

    get people(): Array<Guest> {
        return this._people;
    }

    set people(value: Array<Guest>) {
        this._people = value;
    }

    get StartDate(): Date {
        return this._StartDate;
    }

    set StartDate(value: Date) {
        this._StartDate = value;
    }

    get EndDate(): Date {
        return this._EndDate;
    }

    set EndDate(value: Date) {
        this._EndDate = value;
    }
}